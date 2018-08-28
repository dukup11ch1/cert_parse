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
        crt_data=fp.read
        print crt_data