from mdtohtml import mdtohtml as mh

with open("index.md", "r") as i:
    with open("test.html", "w") as sf:
        sf.write(mh(i, "LoL"))