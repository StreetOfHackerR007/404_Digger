import requests
from subprocess import PIPE, Popen


def banner():
    print('+-'*26+'''+-+
  _  _    ___  _  _     ____  _
 | || |  / _ \| || |   |  _ \(_) __ _  __ _  ___ _ __
 | || |_| | | | || |_  | | | | |/ _` |/ _` |/ _ \ '__|
 |__   _| |_| |__   _| | |_| | | (_| | (_| |  __/ |
    |_|  \___/   |_|   |____/|_|\__, |\__, |\___|_|
                                |___/ |___/
                               
    Coded By: Rohit Soni      |   Uday Patel
    Twitter : @streetofhacker |   @_MrBlackstar\n
'''+'+-'*26+'+-+\n')


def check_status(domain):
    domain = domain.strip('\n')
    
    try:
        r = requests.get('http://'+domain, timeout=6)
        if(r.status_code == 404):
            statuscode.append(domain)
            return r.status_code
    except:
        try:
            r = requests.get('https://'+domain, timeout=6)
            if(r.status_code == 404):
                statuscode.append(domain)
                return r.status_code
        except:
            pass


def digger():
    for domain in statuscode:
        cmd = 'dig '+ str(domain) +'| grep CNAME | awk "{print $1 , $5}"'
        output = Popen(args=cmd, stdout=PIPE, shell=True)
        (output, error) = output.communicate()

        output = output.decode('utf-8')
    print("    \\")
    count = 0
    for cname in output.split():
        if(count%2 != 0):
            print('     |-->'+cname)
        count=count+1


if(__name__ == "__main__"):
    banner()
    filename = str(input('[+] Enter filename/path : '))
    statuscode = []
    
    with open(filename,'r') as f:
        domainlst = f.readlines()

    print('\n\n[*] Please wait while i find 404 response code....')
    
    for domain in domainlst:
        if(check_status(domain) != None):
            print("\n\n[~] "+str(domain).strip('\n'))
            digger()

    if(statuscode == []):
        print('\n\n[!] 404 Not Found..!!')
