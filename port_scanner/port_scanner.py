import socket
import time

# Prompt user for target host and port range
target = input("Enter target host (e.g., 127.0.0.1 or scanme.nmap.org): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\n[*] Scanning {target} from port {start_port} to {end_port}...\n")

# Loop through the specified range of ports
for port in range(start_port, end_port + 1):
    try:
        # Create socket and set timeout
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
        s.close()
        time.sleep(0.2)  # polite delay to avoid flooding

    except KeyboardInterrupt:
        print("\n[!] Scan canceled by user")
        break
    except socket.gaierror:
        print("[!] Hostname could not be resolved")
        break
    except socket.error:
        print("[!] Could not connect to server")
        break
