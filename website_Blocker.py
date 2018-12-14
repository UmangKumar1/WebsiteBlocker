import time
from datetime import datetime as dt

hosts_path = "/private/etc/hosts"
redirect = "127.0.0.1"
webSiteList = ["www.facebook.com", "www.youtube.com", "www.netflix.com", "www.instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day, 16):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for websites in webSiteList:
                if websites in content:
                    pass
                else:
                    file.write(redirect + " " + websites + "\n")
        print("Working Hours!")

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for lines in content:
                if not any(websites in lines for websites in webSiteList):
                    file.write(lines)
            file.truncate()
            print("Fun time")


    time.sleep(5)
