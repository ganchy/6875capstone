# Taken from the full automation.py script, the validation section begins here. This logic prints the newly configured interfaces.
validation = connection.send_command("show ip interface brief")
print(validation)

# This is checking to ensure the loopback interface was correctly configured based on 
# our desired configuration changes above. 
if "10.10.10.1" in validation and not FAIL_MODE:
    print("Validation successful")
else:
    print("Validation failed! Rolling back...")