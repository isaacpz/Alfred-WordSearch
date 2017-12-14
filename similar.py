#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow3, web, ICON_WARNING


def main(wf):
    args = wf.args

    def cacheSearch():
        return getSimilar(args[0], args[1])

    words = wf.cached_data(args[0] + "_" + args[1], cacheSearch, max_age=60)

    if not words:
        wf.add_item('No words found', icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    for word in words:
        wf.add_item(title=word['word'], subtitle=word['def'], arg=word['word'], valid=True)

    wf.send_feedback()

def getSimilar(mode, query):
    url = 'https://api.datamuse.com/words'
    params = dict(max=20, md='d')
    params[mode] = query
    
    r = web.get(url, params)

    # throw an error if request failed
    r.raise_for_status()

    words = r.json()
    
    for i, word in enumerate(words):
        definition = ""
        if 'defs' in word and len(word['defs']) != 0:
            definition = word['defs'][0].split("\t")[1]

        words[i]['def'] = definition
    
    return words

    

if __name__ == '__main__':
    wf = Workflow3(update_settings={
        "github_slug": "isaacpz/Alfred-WordSearch"
    })
    if wf.update_available:
        wf.start_update()
    
    sys.exit(wf.run(main))