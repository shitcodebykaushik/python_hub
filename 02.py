from ftplib import FTP_TLS

def connect_to_ftps():
    host = "127.0.0.1"
    port = 21
    username = "tutu"
    password = input("Enter your FTP password: ")

    try:
        ftps = FTP_TLS()
        ftps.connect(host, port)
        ftps.auth()  # Secure the control connection
        ftps.prot_p()  # Secure the data connection
        ftps.login(user=username, passwd=password)
        print("Connected securely to the server.")
        return ftps
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    ftps = connect_to_ftps()
    if ftps:
        ftps.retrlines("LIST")
        ftps.quit()