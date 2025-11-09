from flask import Flask
from datetime import datetime

# Holds name of the current directoy
app = Flask(__name__)

# Stores the current time
current_time = datetime.now()

# sets up the URL path which will call the function output_current_time
@app.route('/')
# Displays a simple message for the webpage
def output_current_time():
    return f'The current time and date is {current_time}'
# Sets the program to listion on all addresses at TCP 5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
