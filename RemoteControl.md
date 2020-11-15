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

Then you want to insert this code inside "app.py"
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/forward')
def forward():
    forward()
    return 'forward'
@app.route('/backward')
def backward():
    backward()
    return 'backward'
@app.route('/left')
def forward():
    left()
    return 'left'
@app.route('/right)
def forward():
    right()
    return 'right'
```

This code imports Flask and "render_template". Flask runs the webserver and "render_template" returns the HTML file we created to show that file. The reason we put the HTML file in the templates folder was so that you can render the template HTML and use it with Flask. The `@app.route('/')` tells Flask that this function runs at the web address specified, in this case the homepage. The other routes redirect to other pages, which run the functions for the Raspberry Pi car.

```html
<html>
<head>
<title>test</title>
</head>
<body>
<p>Raspberry Pi Robot Car</p>
<a href=forward><button type="button">button</button></a>
<a href=backward><button type="button">button</button></a>
<a href=left><button type="button">button</button></a>
<a href=right><button type="button">button</button></a>
</body>
</html>
```
This is the html file shown at the homepage. It contains all the buttons that redirect to the webpages defined by Flask. This is done by embedding a button element inside an a element, which uses the button 
