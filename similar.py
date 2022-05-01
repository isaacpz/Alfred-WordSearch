#!/usr/bin/python
# encoding: utf-8

import os, sys, json
import urllib.request as urllib2

from workflow import Workflow3, ICON_WARNING

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
    api_url = 'https://api.datamuse.com/words?'+mode+'='+query+'&md=d&max=10'
    dict = urllib2.urlopen(api_url).read()
    words = json.loads(dict)
    
    for i, word in enumerate(words):
        definition = ""
        if 'defs' in word and len(word['defs']) != 0:
            definition = word['defs'][0].split("\t")[1]
        words[i]['def'] = definition
    
    return words
    

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
