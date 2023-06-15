#!/usr/bin/python3

import sqlite3
import subprocess

def main():
    WARNING = '\033[93m'
    OK = '\033[92m'
    HEADER = '\033[95m'
    RED = '\033[91m'
    END = '\033[0m'

    yndx = 'imap.yandex.ru'
    tmail = 'tmail.tizh.ru'
    exec_bin = '/home/opuser/imapsync/imapsync'

    db = sqlite3.connect('/home/opuser/repos/techno_survey/sqlite/db.sqlite3')
    c = db.cursor()
    c.execute(f"""SELECT id, login, ya_app_pass, tmail_pass
                FROM mail_sync_mails
                WHERE sync IS NULL;""")

    for row in c.fetchall():
        pk = row[0]
        login = row[1]
        ya_pass = row[2]
        tmail_pass = row[3]
        command = [exec_bin, '--host1', yndx, '--user1', login, '--password1', ya_pass, '--host2', tmail, '--user2', login, '--password2', tmail_pass]
        print(f"{HEADER}---------------Try to sync {login}--------------------------{END}")
        try:
            subprocess.run(command, check=True)
            c.execute(f"""UPDATE mail_sync_mails SET sync = {True} WHERE id = {pk}""")
            db.commit()
            print(f"{WARNING}-------------------sync {login} completed without errors--------------------------{END}")
    
        except subprocess.CalledProcessError:
            c.execute(f"""UPDATE mail_sync_mails SET sync = {False} WHERE id = {pk}""")
            db.commit()
            print(f"{RED}-------------------sync {login} completed with errors-----------------------------{END}")

    print(f"{OK}The sync_mail script has been completed.{END}")


if __name__ == "__main__":
    main()

