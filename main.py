
import datetime
from handler.users import User, generate_vcode
from handler import tts
from flask import ( Flask, request,
            session, render_template,
            redirect, url_for,
            send_from_directory, flash,
            send_file, abort
        )
import os


log = print

# create an app's instance and secret key
app = Flask(__name__)
app.secret_key = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8k,9o.0p;/!QAZ@WSX#EDC$RFV%TGB^YHN&UJM*IK<(OL>)P:?"
app.config["CLIENT_MP3"] = "static/audio"



# the index
@app.route('/', methods=['GET', 'POST'])
def root():
    if 'username' in session:
        username = session['username']
        if "message" in session:
            message = session['message']
            session.pop('message', None)
        else:
            message = ""
        if "msgtype" in session:
            msgtype = session['msgtype']
        else:
            msgtype="success"
        return render_template('home/index.html', username = username, message = message, msgtype=msgtype)
    
    return render_template('home/index.html', username = None)




# the favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/logo.ico', mimetype='image/vnd.microsoft.icon')




# the login page and signup page
@app.route('/login/')
def login():
    return render_template('login/login.html')

@app.route('/signup')
def signup():
    return render_template('login/signup.html')




# creates a new user if the username and email are unique
@app.route('/auth/signup', methods=['POST'])
def auth_signup():
    username = request.form.get('username').lower().strip()
    password = request.form.get('password').strip()
    email = request.form.get('email').lower().strip()
    rmail = request.form.get('rmail').lower().strip()
    origin = request.form.get('origin')

    user = User(username, log)
    print(user.usernames)
    if username in user.usernames:
        return {
            "error": True,
            "result": "username",
            "usernames": user.usernames
        }
    
    if email in user.emails:
        return {
            "error": True,
            "result": "email"
        }
    
    user.create_user(password, email, rmail, origin)

    session['username'] = username
    session['email'] = email
    session["message"]="Your Account has been created successfully! Verify your account with a mail sent to you! Don't forget to check your spam and trash'"

    return {
        "error": "",
        "result": "success"
    }




# logs in the user
@app.route('/auth/login', methods=['POST'])
def auth_login():
    username = request.form.get('username').lower().strip()
    password = request.form.get('password')
    email = request.form.get('email').lower().strip()

    user = User(username, log)
    if username not in user.usernames:
        return {
            "error": True,
            "result": "username"
        }
    
    if email != user.get_detail(2):
        return {
            "error": True,
            "result": "email"
        }
    
    if password != user.get_detail(4):
        return {
            "error": True,
            "result": "password"
        }
    
    if user._is_verified():
        session['username'] = username
        session['message'] = "Welcome Back!"
        session.pop('msgtype', None)
        return {
            "error": "",
            "result": "sucess"
        }
        
    else:
        return {
            "error": True,
            "result": "verification"
        }




# verifiy the user from his mail
@app.route('/auth/verify', methods = ['GET'])
def auth_verify():
    username = request.args['username']
    vfcode = request.args['vfcode']

    user = User(username, log)
    if user._is_verified():
        return "You Are Already Verified!"
    
    if vfcode != user.get_vcode():
        return "Wrong Verification Code!"
    
    user.verify_user()

    session['username'] = username
    session['message']="Your account has been verified! You can take a look at your profile, link at the nav bar!"

    return redirect(url_for('root'))




# signouts a user
@app.route('/auth/signout')
def signout():
    if "username" in session:
        session.pop("username", None)
    if "message" in session:
        session.pop("message", None)
    if "msgtype" in session:
        session.pop("msgtype", None)
    if "email" in session:
        session.pop("email", None)
    
    session["message"] = "You Are Succesfully Signed Out!"
    return redirect(url_for('root'))




# the profile page of the user
@app.route('/profile', methods = ["GET", "POST"])
def private_profile():
    if "username" not in session:
        session['message'] = "You should login to view your profile!"
        session['msgtype'] = "danger"
        return redirect(url_for('root'))
    
    username = session['username']
    user = User(username, print)
    if not user._is_verified():
        session['message'] = "Your Acccorunt Is Not Verified! Verify It With A Button Sent To Your Email! Don't Forget To Check Your Spam And Trash Boxes!"
        session['msgtype'] = "danger"
        return redirect(url_for('root'))
    
    details = user.get_details()
    return render_template('profile/profile.html', details = details)




@app.route('/@<username>')
def public_user(username):
    _username = str(username).lower()
    user = User(username, print)

    if not user._in_database():
        return "User Not Found!"
    
    user_dets = user.get_details()
    user_dets[4] = "He Heee!, You will not get it!"

    return render_template('profile/public.html', details = user_dets)




# text to speech root
@app.route('/tts')
def texttospeech():
    if 'username' not in session:
        return render_template('tts/index.html', username="")
    
    username = session['username']
    user = User(username, print)

    # return render_template('tts/index.html', username=username)
    return "<h1>Oops! Your are in a construction site! Take a <a href='/' style='color:#0007;background:#0f78;padding:.3rem 1rem;border: 1px dotted black;border-radius:20px;text-decoration:none;'>step back</a> and come back later.</h1>"

# text to speech post method
@app.route('/fetch/tts', methods=["POST"])
def posttexttospeech():
    text = request.form['text']
    gender = request.form['gender']
    speech_rate = request.form['speechrate']
    path = tts(text, gender, speech_rate)
    return path


# IN DEVELOMPENT :::
@app.route('/fetch/audio/<fname>', methods=["POST", "GET"])
def fetchaudio(fname):
    try:
        return send_from_directory(app.config['CLIENT_MP3'], fname, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route('/file/html/<fname>')
def htmlDisplayer(fname):
    return send_file(fname)
    

# @app.route('/static/<path:path>')
# def send_static(path):
#     return path

if __name__ == "__main__":
    app.run(debug=False, port=7200)
