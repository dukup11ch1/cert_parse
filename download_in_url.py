class Drl:
    def __init__(self, url):
        self.url=url
    
    def download_zip(self,fname):
        import urllib
        import zipfile
        urllib.urlretrieve(self.url+fname,'result\\'+fname)
