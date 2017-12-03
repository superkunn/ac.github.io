import requests
import os
from bs4 import BeautifulSoup
import re
sum_n = 0
nyist_n = 0
sdut_n = 0
poj_n = 0
hdu_n = 0

# nyist.net
my_id = "hanxukun"
url = "http://acm.nyist.net/JudgeOnline/profile.php?userid=" + my_id
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata,'lxml')
x = soup.select("th")
m = str(x[0])
nyist_n = int(re.sub("\D", "", m))
sum_n = sum_n + nyist_n
print(nyist_n)

# sdutacm.org

my_id = "31567"
url = "http://www.sdutacm.org/onlinejudge2/index.php/Home/User/info/uid/" + my_id
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata,'lxml')
x = soup.select("h4.text-info > small")
m = str(x[1])
sdut_n = int(re.sub("\D", "", m))
sum_n = sum_n + sdut_n
print(sdut_n)

# poj.org

my_id = "hanxukun"
url = "http://poj.org/userstatus?user_id=" + my_id
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata,'lxml')
x = soup.select("a")
pattern = '.*?<a.*?href=".*?user_id=hanxukun">22</a>.*?'
for line in x:
    sline = str(line)
    ret = re.search(pattern, sline)
    if ret:
        b = sline.split('>')
        poj_n = int(re.sub("\D", "", b[1]))
        break
sum_n = sum_n + poj_n
print(poj_n)

# hdu

my_id = "hanxukun"
url = "http://acm.hdu.edu.cn/userstatus.php?user=" + my_id
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata,'lxml')
x = soup.select("td")
pattern = '<td align="center">\d.*?</td>'
i=1
for line in x:
    sline = str(line)
    ret = re.search(pattern, sline)
    if ret:
        if(i==5):
            hdu_n = int(re.sub("\D", "", sline))
            break
        i+=1
sum_n = sum_n + hdu_n
print(hdu_n)





# write
b_text = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>渣渣的题量</title><script type="text/javascript" src="jQuery.js"></script><script type="text/javascript" src="jqplot.js"></script></head><body><div style="text-align:center;clear:both;"><script src="/gg_bd_ad_720x90.js" type="text/javascript"></script><script src="/follow.js" type="text/javascript"></script></div><div id="chart2"></div><script type="text/javascript">var data = [['
m_text = str(sum_n) + ',' + str(nyist_n) + ',' + str(sdut_n) + ',' + str(poj_n) + ',' + str(hdu_n)
e_text = ']];var data_max = 500; var line_title = ["AC题数"]; var y_label = "AC题数"; var x_label = "oj"; var x = ["总量","nyist","sdut","poj","hdu"]; var title = "渣渣的题量";j.jqplot.diagram.base("chart2", data, line_title, "渣渣的题量，自动统计", x, x_label, y_label, data_max, 2);</script></body></html>'
all_the_text = b_text + m_text + e_text
file_object = open('index.html', 'w')
file_object.write(all_the_text)
file_object.close()
