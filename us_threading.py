###change post address

import threading
import requests

def do_this():
	file = open("notice.log","rb")
	string = file.read()
	
	param = dict(payload = string)
	#print "hi"
	#print string
	ls = string.split("\n")
	#print ls
	list_send= []
	ok = False
	for element in ls:
		hola = element.split("\t")
		if(hola[0]=='#open'):
			param = {}
			param['open'] = hola[1]
			list_send.append(param)
		if(hola[0]=='#close'):
			param = {}
			param['close'] = hola[1]
			list_send.append(param)
		if(hola[0]=='#fields'):
			fields = hola[1:]
		if(ok):
			ans = hola
			ok = False
		if(hola[0]=='#types'):
			ok = True

	for i in range(0,len(fields)):
		param = {}
		param[fields[i]]=ans[i]
		list_send.append(param)
	print list_send

	try :
		print "k"
		response=requests.post('http://example.com',list_send)
		print response
	except :
		print "hi" 
		pass
	


def main():
	main_thread = threading.enumerate()[0]
	#print main_thread.isDaemon()

	our_thread = threading.Thread(target = do_this)
	our_thread.setDaemon(True)
	our_thread.start()

if(__name__ == "__main__"):
	main()