import time
import platform
from datetime import datetime as dt

hosts_temp = r'/home/rohnak/PythonProjects/04 app3 - website blocker/hosts'
hosts_path_linux_mac = r'/etc/hosts'
hosts_path_windows = r'C:\Windows\System32\drivers\etc\hosts'
redirect_home = '127.0.0.1'
websites = ['www.facebook.com', 'facebook.com']

os = platform.system()

if os == 'Linux' or os == 'Darwin':
    hosts_path = hosts_path_linux_mac
else:
    hosts_path = hosts_path_windows

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Work Hours')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website not in content:
                    file.write('\n' + redirect_home + ' ' + website)
    else:
        print('Fun Hours')
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
