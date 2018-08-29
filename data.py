class Data:
    def __init__(self):
        self.serial=None
        self.dam_time=None
        self.victim_name=None
        self.bank_name=None
        self.account=None
        self.country=None
        self.ip=None
    
    def cert_data(self):
        fp=open('result\\'+self.ip+'\\signCert.cert','rb')
        crt_data=fp.read()
        self.victim_name=crt_data.split('(')[0].split('=')[1]
        spd=crt_data.split(',')
        self.account=spd[0].split(')')[1]
        self.bank_name=spd[1].split('=')[1]
    
    def ip_country(self):
        import json
        import urllib
        try:
            url ='https://ipinfo.io/'+self.ip+'/json'
            response = urllib.urlopen(url)
            ip_data=json.load(response)
            self.country=ip_data['country']
        except:
            self.country='Unknown'
    def print_csv(self):
        import csv
        fp = open('result\\result.csv','ab')
        wr = csv.writer(fp)
        wr.writerow([self.serial,self.dam_time,self.victim_name,self.bank_name,self.account,self.ip,self.country])
        fp.close()

