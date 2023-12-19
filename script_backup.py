import shutil
import time
import os
import schedule
from datetime import datetime

source_dir = '/Users/markaxelus/Documents'
dest_dir = '/Users/markaxelus/Documents/backup_folder'
current_date = datetime.now().strftime("%Y-%m-%d")
os.makedirs(dest_dir, exist_ok=True)

def automatic_backup(source, dest):
    current_date = datetime.now().strftime("%Y-%m-%d")
    backup_folder = os.path.join(dest, f'{current_date}')
    os.makedirs(backup_folder, exist_ok=True)

    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(backup_folder, item)

        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s,d)

schedule.every().day.at("18:00").do(lambda: automatic_backup(source_dir, dest_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
