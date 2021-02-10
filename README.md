## Command line driven text search engine


## Install
- Clone the repo into your top level directory
- In the same foler run `python3 search_engine.py`
- To run tests change directoy to the test file and run `python3 -m unittest test_search_engine.py`


## Rules:
- This will read all the text files in the given directory that the script lives
- You can search for single words or phrases
- if no directory is specified or exists it will take the current directory

## Ranking
- Files will be ranked in order of most matched search words

## Input
- You will be prompted for a word or phrase to match 
- Along with a directory which will default to the current directory if none is specified.
- You will be returned all the files names and the number of confirmed matches 


