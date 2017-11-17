from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG']=True
form = """
<!DOCTYPE html> 
<html> 
    <head> 
        <style> 
            form {{
                background-color: #eee; 
                padding: 20px; 
                margin: 0 auto; 
                width: 540px; 
                font: 16px sans-serif; 
                border-radius: 10px; 
            }} 
            textarea {{ 
                margin: 10px 0; 
                width: 540px; 
                height: 120px; 
            }} 
        </style> 
    </head> 
    <body> 
        <!-- create your form here --> 
        <form method='POST'>
        <label for="rot">
                Rotate by:
                <input name="rot" value="0" type="text" />
        </label>
        
        <br>
        
        <textarea type="text" name="text">{0}</textarea>
        
        <br>
        <input type="Submit" />
        </form>

    </body> 
</html> 

"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods = ['POST'])
def encrypt():
    
    encrypt_rot = int(request.form["rot"])
    encrypt_text = str(request.form["text"])
    encrypted_message = rotate_string(encrypt_text, encrypt_rot)
    return form.format(encrypted_message)

app.run()
