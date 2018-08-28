import urllib
import zipfile
import parse_url
import download_in_url

url='http://107.174.85.141/cert/'
url_parser=parse_url.Url(url)
filenames=url_parser.parse_urls()
down=download_in_url.Drl(url)
for filename in filenames:
    down.download_zip(filename)
    
