# MDtoHTML

### Introduction

This is a small Python library/script i wrote.\
It converts Markdown to HTML using the [Python-Markdown](https://python-markdown.github.io/) Lib.\
After downloading you can install all required modules using
`pip install -r REQ.txt` or `pip install markdown validators`.\
The codehilite existension of Python-Markdown is used to color the code
and the CSS for the code is generated using Pygments.\
There also are a few extras that you can´t do in Markdown normally,\
e.g. Embed Youtube videos. You can see how that works in the test.html file.

### Usage/Examples

`Python mdtohtml(<Markdown>, <title>, <CSS>, <includeCSS>)`

``` Python
from mdtohtml import mdtohtml as mdhtml

with open("index.md", "r") as inp: # open the input file
    with open("index.html", "w+") as out: # open the output file
        out.write(mdhtml(inp.read(), "MyWebSite", dark, False)) # convert with the title 'MyWebSite',
                                                                # dark css and no css in the html itself.
```
