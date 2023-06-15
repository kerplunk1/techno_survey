#!/usr/bin/python3
import sqlite3

def main():
    db = sqlite3.connect('db.sqlite3')
    c = db.cursor()
    c.execute(f"""SELECT * FROM mail_sync_mails;""")
    
    for row in c.fetchall():
        print(row)

if __name__ == "__main__":
    main()
