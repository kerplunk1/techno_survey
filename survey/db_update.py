#!/usr/bin/python3

import sqlite3

def main():

    OK = '\033[92m'
    END = '\033[0m'

    db = sqlite3.connect('/home/opuser/repos/techno_survey/sqlite/db.sqlite3')
    c = db.cursor()
    c.execute(f"""UPDATE mail_sync_mails SET sync = NULL WHERE datetime(time_create) < datetime(time_update) AND sync IS {False}""")  
    db.commit()
    
    print(f"{OK}The database was updated{END}")

if __name__ == "__main__":
    main()

