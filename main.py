import os
from flask import Flask

app = Flask(__name__)
port = int(os.environ["PORT"])
print(port)

@app.route('/')
def callScripts():
    print('Saving to spreadsheet')
    import spreadsheet
    print('Changing html')
    import html_changer
    print('Sending email')
    import email_server
    return 'Sucess'

app.run(port=port, host="0.0.0.0")