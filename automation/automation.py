# Initial script requires the student to enter their own
# CSR1000v address. If the current one matches then it will work as is.
# This section will get us our SSH connection to allow configurations.
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}
connection = ConnectHandler(**device)
print("Connected successfully")




# Students then add a method for backing up the router configuration.
# The backup is written to backup.txt in the working directory.
backup = connection.send_command("show running-config")

with open("backup.txt", "w") as f:
f.write(backup)

print("Backup completed")




# This section handles the actual configuration of the network device.
# The FAIL_MODE line functions as an example for dealing with a broken configuration.
# In real implementations, there will be logic in place to properly detect whether
# a change was done correctly or not.
if not FAIL_MODE:          
commands = [               
"interface loopback10",    
"ip address 10.10.10.1 255.255.255.0",
"description AUTOMATION_TEST"
]
else:
commands = [
"interface loopback10",
"ip address 192.168.56.101 255.255.255.0",
"description FAILURE_TEST"
]

output = connection.send_config_set(commands)
print(output)




# Continuing, the validation section begins here. This logic prints the newly configured interfaces.
validation = connection.send_command("show ip interface brief")
print(validation)

# This is checking to ensure the loopback interface was correctly configured based on 
# our desired configuration changes above. 
if "10.10.10.1" in validation and not FAIL_MODE:
    print("Validation successful")
else:
    print("Validation failed! Rolling back...")

