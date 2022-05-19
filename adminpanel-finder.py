import threading, requests, sys

usage = "Usage: python adminpanel-finder.py <HOST/DOMAIN>"

if len(sys.argv) == 1:
   print("Author:https://facebook.com/hanz.ii.180")
   print(usage)
   print("Example: python adminpanel-finder.py example.com")
   sys.exit()

fw = open('result.txt', 'w')
fa = open('result.txt', 'a')
fr = open('result.txt', 'r')
files = open('admin.txt', 'r')
tco = 20

try:
 for file in files.read().splitlines():
    nt = len(file)
    counter = nt
    def brute():
        try:
          url = sys.argv[1]
          if 'http://' not in url:
            url = 'http://{}/'.format(sys.argv[1])
          rg = requests.get(url + file)
          if rg.status_code == 200:
             print('\033[1;32m' + 'Url:' + rg.url, 'Status-Code:' + str(rg.status_code), 'OK')
             if 'http' in fr.readlines():
                fa.write("Url:{} Status-Code:{}\n".format(rg.url, rg.status_code))
             else:
                fw.write("Url:{} Status-Code:{}\n".format(rg.url, rg.status_code))
          elif rg.status_code == 404:
             print('\033[1;31m' + 'Url:' + rg.url, 'Status-Code:' + str(rg.status_code), 'Not Found')
          elif rg.status_code == 302:
             print('\033[1;33m' + 'Url:' + rg.url, 'Status-Code:' + str(rg.status_code), 'Found')
          elif rg.status_code == 403:
             print('\033[1;34m' + 'Url:' + rg.url, 'Status-Code:' + str(rg.status_code), 'Forbidden')
          else:
             print('\033[1;35m' + 'Url:' + rg.url, 'Status-Code:' + str(rg.status_code))
             if 'http' in fr.readlines():
                fa.write("Url:{} Status-Code:{}\n".format(rg.url, rg.status_code))
             else:
                fw.write("Url:{} Status-Code:{}\n".format(rg.url, rg.status_code))
        except requests.exceptions.ConnectionError:
          print("Please check your connection")
          sys.exit()
    ttl = []
    t = threading.Thread(target=brute)
    ttl.append(t)
    t.start()
    counter -= 1
    while threading.active_count() >= tco:
          ttl = threading.active_count()
 while threading.active_count() != 1:
      ttl = threading.active_count()
 fw.close()
 fa.close()
 fr.close()
except:
 print("Error")
 sys.exit()
