import sqlite3
import os.path
from typing import Tuple

def ConnectDataBase() -> sqlite3.Connection:
    con = sqlite3.connect("database.db")
    
    return con


def CheckUsersByLogin(username: str, password: str) -> Tuple[bool, str]:
    con = ConnectDataBase()   
    cur = con.cursor()
    
    # res = cur.execute("SELECT title, content FROM posts")   
    # for row in res:
    #     print(f'{row[0]}-{row[1]}')
    
    print("username:", username)
    print("password:", password)
    
    res = cur.execute("SELECT Token FROM Users WHERE UserName=? AND Password=?", [username, password])  
    row = res.fetchone()
    
    if row != None:
        token = row[0]
        con.close()
        return True, token
    else:
        con.close()
        return False, "User not found"