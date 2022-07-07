# Word Search
Word Search is an Alfred 4 workflow which exposes powerful word searching utilities. Ultimately, the workflow can be leveraged to widen your vocabulary and make you a better writer.

## Quick Reference
* `syn [word]` - Broadly searches for words related to a word/phrase.
* `dsyn [word]` - Searches for a word’s exact synonyms.
* `ant [word]` - Searches for a word’s antonyms.
* `rhyme [word]` - Searches a word’s rhymes.
* `describing [word]` - Searches for words that describe another word
## Usage
Simply type in a command. Selecting a result will copy that word to your clipboard and automatically paste it in the front most app. 

## Installation
Simply [download the latest .alfredworkflow file](https://github.com/jun6lee/Alfred-WordSearch/releases/latest) and double click it to import it to Alfred.

Word Search will update on its own.

## Demonstration

Searching for synonyms of the word “amazing”
![Demo Image](/screenshots/syn-demo.png)

You can also search for synonyms of phrases, like “ringing in the ears”
![Demo Image](/screenshots/syn-demo-2.png)

Searching for rhymes of the word “strange”
![Demo Image](/screenshots/rhyme-demo.png)

Searching for words that describe “dog”
![Demo Image](/screenshots/describing-demo.png)

## Credits
* [Alfred Workflow](https://github.com/deanishe/alfred-workflow) - the framework that previously wrapped this workflow.
* [Alfred Workflow for Python3](https://github.com/NorthIsUp/alfred-workflow-py3)  - the updated framework for python3 that **now** wraps this workflow.
* [Datamuse](http://datamuse.com) - The dictionary that powers this workflow.
* [jun6lee](https://github.com/jun6lee) - 2.0.1 pieced and ported to make it work with Python3.
* [mtissington](https://github.com/mtissington) - 2.0.2 - fixed spaced (dual words) causing an error.