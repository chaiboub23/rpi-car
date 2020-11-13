# Remote Control

Controlling the Raspberry Pi wirelessly is done by making a Flask webserver. This is accessed by another Raspberry Pi using lynx as a web browser.

Download Flask using pip.
```
pip3 install flask
```

Next move to the directory with the rest of your code and make a new file called "app.py". This will be the main entry point. You also want to make a directory called "templates" and make a file called "index.html" for your html code.
```bash
cd code
touch app.py
mkdir templates && cd templates
touch index.html
```
