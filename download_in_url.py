class Drl:
    def __init__(self, url):
        self.url=url
    
    def download_zip(self,fname):
        import urllib
        import zipfile
        import os
        urllib.urlretrieve(self.url+fname,'result\\'+fname)
        myzip=zipfile.ZipFile('result\\'+fname)
        os.system('mkdir result\\'+fname.replace('.zip',''))
        myzip.extractall('result\\'+fname.replace('.zip','')+'\\')
        myzip.close()
        