import urllib
import zipfile
import parse_url
import download_in_url
import data
import csv


def csv_to_database():
    import csv
    import pymysql


    mydb = pymysql.connect(host='localhost', user='root', passwd='root', db='victim_info')
    cursor = mydb.cursor()
    csv_data = csv.reader(file('result\\result.csv'))
    for row in csv_data[1:]:
        cursor.execute('INSERT INTO result(id, damaged_time, victim_name, bank_name, account, ip, country)' 'VALUES(%s, %s, %s, %s, %s, %s, %s)', row)

    mydb.commit()
    cursor.close()
    print "Imported!"


fp=open('result\\result.csv','wb')
wr=csv.writer(fp)
wr.writerow(["id","damaged_time","victim_name","bank_name","account","ip","country"])
fp.close()
data_list=[]

        
url='http://107.174.85.141/cert/'
url_parser=parse_url.Url(url)
filenames=url_parser.parse_urls()
times = url_parser.parse_time()
#print filenames
serial=0
for filename,time in zip(filenames, times):
    mydata=data.Data()
    mydata.ip=filename.replace('.zip','')
    mydata.dam_time=time
    mydata.serial=serial
    serial=serial+1
    data_list.append(mydata)

down=download_in_url.Drl(url)
for mydata in data_list:
    down.download_zip(mydata.ip+'.zip')
    mydata.cert_data()
    mydata.ip_country()
    mydata.print_csv()

csv_to_database()



