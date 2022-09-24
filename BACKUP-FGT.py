import csv
from netmiko import ConnectHandler
<<<<<<< HEAD
#from getpass import getpass
# Open file and read the data by column  IP, Username, Password, Hostname
=======
from getpass import getpass
# Open the file and read the data by column  IP, Username, Password, Hostname
>>>>>>> 7f0c1ea2837716d684e87ed4131f899c2820892e
def open_file(file_name):
    
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            row_count = len(your_list)
            print("backup up ",row_count," devices")

        for i in your_list:
            try:
                fgt = {
                'device_type': 'fortinet',
                'ip': i[0],
                'username': i[1],
                'password': i[2],
                }
#connect to de firewall by ssh, send show command and print the output to a file with .conf extension          
                print(fgt)
                command = "show"
                with ConnectHandler(**fgt) as net_connect:
                    output = net_connect.send_command(command)
                with open(i[3] + ".conf", "w") as f:
                    f.write(output)
                    f.close()
            except:
                print ("error check firewall configuration :",i[3],i[0])
                pass       

def main():
    file_name = input("Enter the de CSV file name: ")
    open_file(file_name)



if __name__ == '__main__':
    main()


