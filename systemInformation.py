#/bin/python3
print('*#'*50)
print("\t\t\t[+] Programmed by rKumar ")
print("\t\t\t[+] Commented  by ChatGPT")
print('*#'*50)  
import platform
import os
import socket
import psutil

# Function to convert bytes to GB
def bytes_to_gb(bytes):
    return round(bytes / (1024 ** 3), 2)

# Open the file in "w" mode to create or overwrite the file
try:
	with open("systemInfo.txt", "w") as f:
	    # Get the hostname of the system
	    hostname = socket.gethostname()
	   
	    # Get the operating system name and details
	    system_info = platform.uname()
	    
	    # Get the logged-in username
	    username = os.getlogin()
	    
	    # Get Memory Information
	    memory_usage = psutil.virtual_memory()
	    total_memory_gb = bytes_to_gb(memory_usage.total)
	    available_memory_gb = bytes_to_gb(memory_usage.total)
	    used_memory_gb = bytes_to_gb(memory_usage.used)
	    
	    # Get Disk Information
	    disk_info = psutil.disk_partitions(all=False)
	    
	    # Write the information to the file
	    f.write("[+] Hostname of the system: " + hostname + "\n")
	    f.write("[+] System information : " + str(system_info) + "\n")
	    f.write("[+] Logged-in username : " + username + "\n")
	    f.write("[+] Total Memory : " + str(total_memory_gb) + "\n")  # Convert memory_usage to string
	    f.write("[+] Available Memory : " + str(available_memory_gb) + "\n")
	    f.write("[+] Used Memory : " + str(used_memory_gb) + "\n")
	    f.write("[+] Disk Information : " + str(disk_info) + "\n")  # Convert disk_info to string
	    print("[+] Your System Information has been writen to systemInfo.txt ....")
except:
	print("[+]File already exists " , FileExistsError)

	   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
