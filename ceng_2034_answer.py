import requests
import os
import os,sys
import multiprocessing
import threading
#Ahmet Oral 180709008

#urls we need to check
"""url_array= ["https://api.github.com","http://bilgisayar.mu.edu.tr/",
            "https://www.python.org/","http://akrepnalan.com/ceng2034",
            "https://github.com/caesarsalad/wow"]"""

#checking the url's
print("200 = Successful, 404 or 505 = Failed\n")	
def requester(url):
	response = requests.get(url)
	print(response.status_code," --> ",url)
	
thread1 = threading.Thread(target = requester,args=("https://api.github.com",))
thread2 = threading.Thread(target = requester,args=("http://bilgisayar.mu.edu.tr/",))
thread3 = threading.Thread(target = requester,args=("https://www.python.org/",))
thread4 = threading.Thread(target = requester,args=("http://akrepnalan.com/ceng2034",))
thread5 = threading.Thread(target = requester,args=("https://github.com/caesarsalad/wow",))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

"""I put rest of the code in while loop because,if code works while threads are working too, output
screen becomes a mess.If want you can always delete while loop and code will keep working anyway."""
while(True):
	if(thread5.is_alive()):
		continue
	
	#printing PID
	print("\nPID value:",os.getpid())		

	#printing nproc
	nproc=multiprocessing.cpu_count()
	print("\nNproc value:",nproc)			

	#printing loadavg
	loadavg=os.getloadavg()
	print("\nLoadavg value",loadavg)
	
	#printing loadavg 5 minutes
	load1,load5,load15 = os.getloadavg()
	print("\nLoadavg 5 minutes:",load5)
	
	#condition of when to end program
	print("\nProgram will end itself if (nproc-5 min loadavg<5)")
	while(True):					
		#print(load5) #if you want to see load5 value changing you can use this code.
		load1,load5,load15 = os.getloadavg()	
		if((nproc-load5)<1):			
			print("5minLoadAvg is too close to nproc...\nProgram Terminated!")
			break
	break				
				
		
		














