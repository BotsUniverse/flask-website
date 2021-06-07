import sqlite3

"""
The Rows In The Table ::users::
0. id - id: auto increment: no need to enter
1. username - unique: lower case text: required
2. email - unique: lower case email: required
3. rmail - for-safety: lower case email: required
4. password - for-safety: case sensitive HASHED: required
5. verified - user-check: randomly generated: required
6. createdon - for-details: auto entered: no need to enter
7. roomname - user-choice: case sensitive unique: no need to enter
8. roompassword - for-safety: case sensitive UNHASHED: required if roomname is not None
9. roombuildon - for-details: auto entered: no need to enter if roompassword is not None
10. secretpwd - user-choice: case sensitive unique: required if premium
11. premium - bool: true | false: if user has paid
"""

# creation of usernames table
""" 
db = sqlite3.connect('database/database.db')
cursor = db.cursor()
cursor.execute("\
    CREATE TABLE \
        users (\
            id INTEGER PRIMARY KEY NOT NULL, \
            username TEXT, \
            email TEXT,\
            rmail TEXT, \
            password TEXT, \
            verified TEXT, \
            createdon DATETIME, \
            roomname TEXT, \
            roompassword TEXT, \
            roombuildon DATETIME, \
            secretpwd DATETIME, \
            premium TEXT\
    )"
)
cursor.close()
db.commit()
db.close()
"""

# testing table
""" db = sqlite3.connect('database/database.db')
cursor = db.cursor()
r = cursor.execute("SELECT DISTINCT * FROM test0 where username = 'parvat'")
a = []
for s in r:
    a.append(s)
print(a)
cursor.close()
# db.commit()
db.close() """