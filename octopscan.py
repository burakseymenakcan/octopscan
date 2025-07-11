import socket

ascii_banner = r"""                                               
               _                               
  ___   ____ _| |_ ___  ____   ___ _____  ____ 
 / _ \ / ___|_   _) _ \|  _ \ /___) ___ |/ ___)
| |_| ( (___  | || |_| | |_| |___ | ____( (___ 
 \___/ \____)  \__)___/|  __/(___/|_____)\____)
                       |_|                     """

print(ascii_banner)

print("\nSelect an option to begin:\n")
print("[1] Port Scanner")
print("[0] Exit\n\n")

choice = input("Enter Your Choice: ")

if choice == "1":
    target = input("Enter target IP address: ")
    print(f"\nScanning target: {target}\n")

    for port in range(1, 10000):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")
                sock.close()
            
            else:
                print(f"[-] Port {port} is CLOSED")
                sock.close()


        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user. Exiting...")
            break

        except socket.gaierror:
            print("[!] Hostname could not be resolved. Exiting...")
            break

        except socket.error:
            print("[!] Couldn't connect to server. Exiting...")
            break

elif choice == "2":
    print("Goodbye!")

else:
    print("Invalid choice. Exiting...")