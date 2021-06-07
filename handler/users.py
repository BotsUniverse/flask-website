import _thread
import datetime
import json
import logging
import os
import random
import shutil
import smtplib, ssl
import sqlite3
import threading
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Union


# a function to generate a randomcode
def generate_vcode(length:int = 200):
    chars = "qwertyuioplkjhgfdsazxcvbnm\
        MNBVCXZASDFGHJKLPOIUYTREWQ1234567890"
    pwd = []
    while len(pwd) < length:
        pwd.append(random.choice(chars))
        random.shuffle(pwd)

    return "".join(pwd).replace(' ', '')


# a class to handle the user
class User:
    """
    A class that can create, edit and delete a user.
    The database is stored at the :database/database.db: in root.
    The current table name is :users: with 12 rows.
    More details are given at :database/handel.py: at line :4:.
    """
    def __init__(self, username:str, log:logging) -> None:
        # the user's name
        self.username = str(username).lower()
        self.log = log

        # some lists that will be filled with database
        self.ids = []
        self.usernames = []
        self.emails = []
        self.rmails = []
        self.passwords = []
        self.verifies = []
        self.createdons = []
        self.roomnames = []
        self.roompasswords = []
        self.roombuildons = []
        self.secretpwds = []
        self.premiums = []

        # a dict to match the column no.
        # with the column name
        self.pairs = {
            0: 'ids',
            1: 'usernames',
            2: 'emails',
            3: 'rmails',
            4: 'passwords',
            5: 'verifies',
            6: 'createdons',
            7: 'roomnames',
            8: 'roompasswords',
            9: 'roombuildons',
            10: 'secretpwds',
            11: 'premiums'
        }

        # the database iteration
        self.db = sqlite3.connect('database/database.db')
        self.cursor = self.db.cursor()
        self.raw_query = self.cursor.execute('SELECT * FROM users')

        # put the details in it respective list
        for (_id, _username,
            _email, _rmail,
            _pwd, _ver, _cdo,
            _rmn, _rmp, _rmb,
            _scp, _prem) in self.raw_query:
            self.ids.append(_id)
            self.usernames.append(_username)
            self.emails.append(_email)
            self.rmails.append(_rmail)
            self.passwords.append(_pwd)
            self.verifies.append(_ver)
            self.createdons.append(_cdo)
            self.roomnames.append(_rmn)
            self.roompasswords.append(_rmp)
            self.roombuildons.append(_rmb)
            self.secretpwds.append(_scp)
            self.premiums.append(_prem)
        
        # close the database
        self.cursor.close()
        self.db.close()


    # function to refresh the values off
    # lists in class instance
    def _refresh_lists(self):
        # some lists that will be filled with database
        self.ids = []
        self.usernames = []
        self.emails = []
        self.rmails = []
        self.passwords = []
        self.verifies = []
        self.createdons = []
        self.roomnames = []
        self.roompasswords = []
        self.roombuildons = []
        self.secretpwds = []
        self.premiums = []

        # the database iteration
        self.db = sqlite3.connect('database/database.db')
        self.cursor = self.db.cursor()
        self.raw_query = self.cursor.execute('SELECT * FROM users')

        # put the details in it respective list
        for (_id, _username,
            _email, _rmail,
            _pwd, _ver, _cdo,
            _rmn, _rmp, _rmb,
            _scp, _prem) in self.raw_query:
            self.ids.append(_id)
            self.usernames.append(_username)
            self.emails.append(_email)
            self.rmails.append(_rmail)
            self.passwords.append(_pwd)
            self.verifies.append(_ver)
            self.createdons.append(_cdo)
            self.roomnames.append(_rmn)
            self.roompasswords.append(_rmp)
            self.roombuildons.append(_rmb)
            self.secretpwds.append(_scp)
            self.premiums.append(_prem)
        
        # close the database
        self.cursor.close()
        self.db.close()

        return self


    # check if the user is in the database,
    # that is, if the user has logged in
    def _in_database(self) -> bool:
        return True if self.username in self.usernames else False


    # get the id of the user with the passed username
    # return int if user is in the database else None
    def _get_id(self) -> int or None:
               return self.usernames.index(self.username) \
            if self._in_database() else None


    # check if the user is verified if the user is in the database
    # return True if verified else False 
    def _is_verified(self) -> bool:
        if self._in_database():
            if self.verifies[self._get_id()] == "verified":
                return True
            else:
                return False
        
        return None


    # check if the user has create a room
    # return True if created else False
    def _has_room(self) -> bool:
        if self._in_database():
            if self.roomnames[self._get_id()] is None:
                return False
            else:
                return True

        return None
    

    # send the user a verification code
    # with a button
    def send_vf_code(self, email, vcode, domain):
        context = ssl.create_default_context()
        port = 465
        # password = 'BillGates2004@'
        # smtp_server = "smtp.zoho.com"
        # sender_email = "no-reply@springreen.me"
        password = 'i_have_an_error'
        smtp_server = "smtp.gmail.com"
        sender_email = "replyerrors.parvat@gmail.com"
        receiver_email = email
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Verify Your Account At SPRINGREEN"
        message["From"] = sender_email
        message["To"] = receiver_email

        html = f"""
        <html>
            <body>
                <h1>Welcome {self.username.capitalize()}!</h1>
                <h2>Click The BUTTON Below To Verify Your Account At SPRINGREEN!</h2>
                <form action="/auth/verify" method="GET">
                    <input type="hidden" name="vfcode" value="{vcode}"></input>
                    <input type="hidden" name="username" value="{self.username}"></input>
                    <input type="submit" value="VERIFY 👍" style="font-size: 20px;">
                </form>
            </body>
        </html>
        """
        part2 = MIMEText(html, "html")
        message.attach(part2)
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()
            
        return f'<a href="{domain}/auth/verify?vcode={vcode}&uname={self.username}">http://127.0.0.1:7000/verify?vcode={vcode}&uname={self.username}</a>'



    # gets the verify column from the user table where
    # username exists
    def get_vcode(self) -> str or None:
        if not self._in_database():
            return None
        
        return self.verifies[self._get_id()]


    # gets requested detail from the db
    # returns none if no detail
    def get_detail(self, req):
        if not self._in_database():
            return None

        # if the req is int
        if type(req) == int:
            req = req % len(self.pairs)
            sol = eval(f"self.{self.pairs[req]}[self._get_id()]")
            return sol

        # if the req is string
        req = req.lower().strip()
        if req not in self.pairs.values():
            return None
        
        sol = eval(f"self.{req}s[_get_id]")
        return sol
    

    # get all details
    def get_details(self):
        if not self._in_database():
            return False
        _id = self._get_id()
        _details = []
        for det in self.pairs:
            _details.append(self.get_detail(det))
        
        return _details
    

    # creates a new user and
    # edits all the values in the class
    def edit_value(self, req:str, val:str):
        if not self._in_database():
            return None
        
        db = sqlite3.connect('database/database.db')
        cursor = db.cursor()
        cursor.execute(
        f'''UPDATE
            users
        SET
            {req.lower()} = {val}
        WHERE
            username = "{self.username.lower()}"
        ''')
        cursor.close()
        db.commit()
        db.close()
        self.log.info(f"<class User>: Changed {req} to {val} where username is {self.username}")
        return True

    # a function to destroy the room within one month
    # this function returns no value and is prossed in thread
    def _start_self_distruct_countdown_for_room(self, roomname, thread_num):
        """
        This threaded function sleeps for 30 days
        and when it wakes up, it deletes the respective room, 
        and the details of the room from the database
        """
        self.log.warning(f"<class User>: Starting self destruct at Thread-{thread_num} for room {roomname}")
        time.sleep(2592000)
        if not self._has_room():
            return False
        shutil.rmtree(f'templates/rooms/{roomname}')
        self.edit_value("roomname", None)
        self.edit_value("roompassword", None)
        self.edit_value("roombuildon", None)
        self.log.critical(f"<class User>: Destroyed The room {roomname} By thread Thread-{thread_num}")
        self._refresh_lists()


    # create a room for the user
    # and also create some files
    def create_room(self, roomname:str, roompassword:str):
        if self._has_room():
            return False
        
        # CREATE FILES
        # 1. read the template
        with open('templates/room/template.html', "r") as template:
            html_template = template.read()
            template.close()

        # 2. create a base path variable
        base_path = f'templates/rooms/{roomname}'
        # 3. create directory, html file, json file, database file
        os.mkdir(base_path)
        with open(base_path + "/index.html", 'w') as html_file:
            html_file.write(html_template)
            html_file.close()
        
        json_dets = {
            "roomname": roomname,
            "roompassword": roompassword,
            "roombuildon": str(datetime.datetime.now()),
            "roomowner": self.username,
            "ispremium": self.premiums[self._get_id()],
            "secretpwd": self.secretpwds[self._get_id()],
            "maxmembers": 16,
            "admins": [
                
            ],
            "members": [
                
            ]
        }
        with open(base_path + '/index.json', 'w') as json_:
            json.dump(json_dets, json_, indent = 4)
            json_.close()
        
        db = sqlite3.connect(base_path + '/index.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE room (id INTEGER PRIMARY KEY, username TEXT, message TEXT, dom DATETIME)")
        cursor.close()
        db.commit()
        db.close()
        thread_num = threading.active_count() + 1
        _thread.start_new_thread(self._start_self_distruct_countdown_for_room, (roomname, thread_num))
        self.log.info(f"<class User>: Created Room For {self.username} Names {roomname}")

        # add details in database
        db = sqlite3.connect('database/database.db')
        cursor = db.cursor()
        cursor.execute(f'''
        UPDATE 
            users 
        SET 
            roomname = "{roomname.lower().strip()}" 
            and 
            roompassword = "{roompassword.strip()}" 
            and 
            roombuildon = "{datetime.datetime.now()}"
        WHERE
            username = "{self.username}"
        ''')
        cursor.close()
        db.commit()
        db.close()


        return True
    

    # creates a new user and sends a verification code
    # to his mail
    # returns True if created else False
    def create_user(self, password, email, rmail, domain_origin):
        if self._in_database():
            return False
        
        vcode = generate_vcode(160)
        username = self.username
        db = sqlite3.connect('database/database.db')
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO \
            users (username, email, rmail,\
                    password, verified, createdon)\
            VALUES ('{username}', '{email}', '{rmail}', '{password}',\
                    '{vcode}', '{datetime.datetime.now()}') \
            "
        )
        cursor.close()
        db.commit()
        db.close()
        domain_origin = domain_origin if domain_origin[-1] != '/' else domain_origin[:-1]

        _thread.start_new_thread(self.send_vf_code, (email, vcode, domain_origin))

        return True
    

    # verify the user
    # return true if if verified now else False if already verified
    def verify_user(self):
        if self._is_verified():
            return False
        
        db = sqlite3.connect('database/database.db')
        cursor = db.cursor()
        cursor.execute(f"UPDATE users SET verified = 'verified' WHERE username = '{self.username.lower()}'")
        cursor.close()
        db.commit()
        db.close()

        # self._refresh_lists()
        return True

    # remove a user from the db
    # return True if removed else False
    def remove_user(self):
        if not self._in_database():
            return False

        # delete the room if there is one
        if self._has_room():
            def delete_room(roomname):
                shutil.rmtree(f'templates/rooms/{roomname}')
            _thread.start_new_thread(delete_room, (self.roomnames[self._get_id()],))

        # remove the user from the database
        username = self.username
        db = sqlite3.connect('database/database.db')
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM users WHERE username = '{username}'")
        cursor.close()
        db.commit()
        db.close()

        # refresh the list
        self._refresh_lists() 
        # task complete
        return True
    

    # clear all database, rooms
    @staticmethod
    def clean_all():
        db = sqlite3.connect('database/database.db')
        cursor = db.cursor()
        cursor.execute("DELETE FROM users")
        cursor.close()
        db.commit()
        db.close()

        shutil.rmtree('templates/rooms')
        os.mkdir("templates/rooms")

        return True

