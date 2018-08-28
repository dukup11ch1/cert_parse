class Url:
    def __init__(self,target_url):
        self.target_url=target_url
    
    def parse_urls(self):
        import requests
        import re
        res=requests.get(self.target_url)
        data=res.text
        regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.zip")
        exname=regex.findall(data)
        return exname
        

