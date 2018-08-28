import urllib
import zipfile
import parse_url
import download_in_url
import data

data_list=[]

url='http://107.174.85.141/cert/'
url_parser=parse_url.Url(url)
filenames=url_parser.parse_urls()
times = url_parser.parse_time()
for filename,time in zip(filenames, times):
    mydata=data.Data()
    mydata.ip=filename.replace('.zip','')
    mydata.dam_time=time
    data_list.append(mydata)

down=download_in_url.Drl(url)
for mydata in data_list:
    down.download_zip(mydata.ip+'.zip')
    mydata.cert_data()



