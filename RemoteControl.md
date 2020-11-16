# Remote Control

Controlling the Raspberry Pi wirelessly is done by making a Flask webserver. This is accessed by another Raspberry Pi using lynx as a web browser.

Download Flask using pip.
```
pip3 install flask
```

Next move to the directory with the rest of your code and make a new file called app.py. This will be the main entry point. You also want to make a directory called templates and make a file called index.html for your html code.
```bash
cd code
touch app.py
mkdir templates && cd templates
touch index.html
```

Then you want to insert this code inside app.py.
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
app.run(host='ip address')
```

This code imports Flask and "render_template". Flask runs the webserver and "render_template" returns the HTML file we created to show that file. The reason we put the HTML file in the templates folder was so that you can render the template HTML and use it with Flask. The `@app.route('/')` tells Flask that this function runs at the web address specified, in this case the homepage. The other routes redirect to other pages, which run the functions for the Raspberry Pi car. The `app.run(host='ip address')` function is used to run the web server. Replace `'ip address'` with a static ip address of the Raspberry Pi.

To have a static ip address, you want to edit the file located at `$HOME/etc/dhcpcd.conf`.
```bash
nano $HOME/etc/dhcpcd.conf
```
Then you want to add the following lines to the file.
```
interface eth0
static ip_address=192.168.0.4/24    
static routers=192.168.0.254
static domain_name_servers=192.168.0.254 8.8.8.8
```
You will now have a static ip address, which removes the burden of having to change the app.py file everytime you restart the Raspberry Pi.

```html
<html>
<head>
<title>test</title>
</head>
<body>
<p>Raspberry Pi Robot Car</p>
<a href=forward><button type="button">forward</button></a>
<a href=backward><button type="button">backward</button></a>
<a href=left><button type="button">left</button></a>
<a href=right><button type="button">right</button></a>
</body>
</html>
```
This is the HTML file shown at the homepage. It contains all the buttons that redirect to the webpages defined by Flask. This is done by embedding a button element inside an a element, which uses the button to redirect to one of the webpages.

```html
<html>
    <head>
        <title>forward</title>
    </head>
    <body>
        <p>Moving forwards...</p>
        <a href=/><button type="button">back home</button></a>
    </body>
</html>
```

This is an example of a page that runs the functions that move the Raspberry Pi car. They contain a button to redirect back home.
