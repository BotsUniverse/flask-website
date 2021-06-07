import sqlite3
import _thread
import datetime
import json
import os
from handler.users import User

class Room:
    def __init__(self, username:str, roomname:str):
        self.roomname = str(roomname).lower()
        self.roomnames = User('', print).roomnames
    
    def _room_exists(self):
        ...