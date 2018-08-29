class Url:
    def __init__(self,target_url):
        import requests
        self.target_url=target_url
        res=requests.get(self.target_url)
        self.data=res.text
    def parse_urls(self):
        import re
        regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.zip")
        exname=list(set(regex.findall(self.data)))
        return exname
    
    def parse_time(self):
        import re
        regex = re.compile("\d{4}-\d{2}-\d{2} \d{2}:\d{2}")
        times=regex.findall(self.data)
        return times

