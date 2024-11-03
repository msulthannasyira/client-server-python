# Client Server Python Sederhana

## 3SOCKET_TCPECHOSERVER.PY

```python
import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    """ A simple echo server """
    
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Enable reuse address/port  
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the port 
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)
    
    # Listen to clients, backlog argument specifies the max number of queued connections
    sock.listen(backlog)
    
    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()
        
        data = client.recv(data_payload)
        if data:
            print("Data: %s" % data)
            client.send(data)
            print("sent %s bytes back to %s" % (data, address))
        
        # End connection 
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    
    port = given_args.port
    echo_server(port)
```
Kode tersebut berfungsi untuk Membangun server echo sederhana menggunakan Python yang dapat menerima dan mengirim kembali pesan dari klien.

Kode ini mendefinisikan server echo yang menerima data dari klien dan mengirim kembali data yang sama. Server berjalan pada alamat `localhost` dan port yang ditentukan oleh pengguna.

Import Library

•	`socket` untuk membuat dan mengelola koneksi jaringan.

•	`argparse` untuk menangani argumen dari command line.

Fungsi `echo_server(port)`

•	Membuat socket TCP dan mengikatnya ke alamat host dan port yang ditentukan.

•	Mendengarkan koneksi dari klien dan menerima pesan.

•	Mengirim kembali pesan yang diterima ke klien.

•	Menjalankan Server, Menggunakan argumen `--port` untuk menentukan port yang digunakan oleh server.

### Output

Untuk menjalankan server, simpan kode dalam file bernama `echo_server.py` dan eksekusi dari command line sebagai berikut:

```cmd
python echo_server.py --port 12345
```
Setelah menjalankan server, berikut adalah contoh output yang dihasilkan:
```cmd
Starting up echo server on localhost port 12345
Waiting to receive message from client
Data: b'Hello, Server!'
sent 15 bytes back to ('127.0.0.1', 54321)
```
output dari program ini akan keluar setelah kita menjalankan kode untuk client yang akan dijelaskan selanjutnya

## 3SOCKET_TCPECHOCLIENT.PY

```python
import socket
import sys
import argparse

host = '192.168.38.60'

def echo_client(port):
    """ A simple echo client """
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    # Send data 
    try:
        # Send data
        message = "Test message. This will be echoed"
        print("Sending %s" % message)
        sock.sendall(message.encode('utf-8'))
        
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print("Received: %s" % data.decode('utf-8'))
    
    except socket.error as e:
        print("Socket error: %s" % str(e))
    except Exception as e:
        print("Other exception: %s" % str(e))
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    
    port = given_args.port
    echo_client(port)
```
sama seperti sebelumnya kode ini membangun klien echo sederhana menggunakan Python yang dapat mengirim pesan ke server dan menerima kembali pesan yang sama. Kode ini mendefinisikan klien echo yang menghubungkan ke server echo pada alamat IP dan port yang ditentukan, mengirimkan pesan, dan menunggu untuk menerima respons dari server.

Fungsi echo_client(port)

•	Membuat socket TCP/IP dan menghubungkannya ke alamat server yang ditentukan.

•	Mengirimkan pesan ke server dan menunggu untuk menerima respons.

•	Menerima data dari server hingga semua data yang diharapkan diterima.

•	Menjalankan Klien

Menggunakan argumen --port untuk menentukan port yang digunakan untuk menghubungkan ke server.

### Output

Untuk menjalankan klien, simpan kode dalam file bernama `echo_client.py` dan eksekusi dari command line, berikut adalah contoh command nya:

kemudian berikut adalah contoh output yang dihasilkan saat terhubung ke server 
`3SOCKET_TCPECHOSERVER.PY`:

Klien echo sederhana ini berhasil terhubung dengan server, mengirimkan pesan, dan menerima kembali data yang sama, yang dasar yang dapat digunakan untuk memahami konsep komunikasi jaringan antara klien dan server.

## 3SOCKET_UDPECHOSERVER

```python
import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048

def echo_server(port):
    """ A simple echo server """
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)

    while True:
        print("Waiting to receive message from client")
        data, address = sock.recvfrom(data_payload)
        print("Received %s bytes from %s" % (len(data), address))
        print("Data: %s" % data)
        
        if data:
            sent = sock.sendto(data, address)
            print("Sent %s bytes back to %s" % (sent, address))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    
    port = given_args.port
    echo_server(port)
```

Kode tersebut membuat server echo UDP sederhana menggunakan Python yang dapat menerima pesan dari klien dan mengirim kembali pesan yang sama. sistem nya dengan mendefinisikan server echo yang berjalan pada protokol UDP. Server mendengarkan pesan yang dikirim oleh klien dan mengirimkan kembali pesan tersebut ke alamat yang sama.

Fungsi `echo_server(port)`

•	Membuat socket UDP dan mengikatnya ke alamat server dan port yang ditentukan.

•	Menunggu pesan dari klien dengan metode `recvfrom()`.

•	Mencetak informasi tentang data yang diterima, termasuk jumlah byte dan alamat klien.

•	Mengirim kembali data yang diterima ke klien menggunakan metode `sendto()`.

### Output

Untuk menjalankan server, simpan kode dalam file bernama echo_server.py dan buat command dengan contoh seperti berikut:

Setelah menjalankan server, berikut adalah contoh output yang dihasilkan saat menerima pesan dari klien:

Server echo UDP ini berhasil mendengarkan permintaan dari klien, menerima pesan, dan mengirimkannya kembali. Ini adalah implementasi dasar yang berguna untuk memahami konsep komunikasi jaringan berbasis UDP antara klien dan server. untuk membuat client terhubung menggunakan kode yang akan dijelaskan selanjutnya.4

## 3SOCKET_UDPECHOCLIENT
```python
import socket
import sys
import argparse

host = '192.168.38.60'
data_payload = 2048

def echo_client(port):
    """ A simple echo client """
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    
    message = 'This is the message. It will be repeated.'
    
    try:
        # Send data
        print("Sending %s" % message)
        sent = sock.sendto(message.encode('utf-8'), server_address)
        
        # Receive response
        data, server = sock.recvfrom(data_payload)
        print("Received: %s" % data.decode('utf-8'))
    
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    
    port = given_args.port
    echo_client(port)
```
Kode ini mendefinisikan klien echo yang berjalan pada protokol UDP. Klien menghubungkan diri ke server, mengirimkan pesan, dan menerima respons dari server.

Fungsi `echo_client(port)`

•	Membuat socket UDP menggunakan `socket.socket(socket.AF_INET, socket.SOCK_DGRAM).`

•	Mengatur alamat server berdasarkan host yang ditentukan (`192.168.38.60`) dan port yang diberikan.

•	Mencetak informasi tentang koneksi yang sedang dibangun.

•	Mengirim pesan ke server menggunakan `sendto()`.

•	Menerima respons dari server dengan `recvfrom()`, yang akan mengembalikan pesan yang sama.

•	Menutup koneksi setelah selesai.

### Output

Untuk menjalankan klien, simpan kode dalam file bernama `echo_client.py` dan eksekusi dari command line sebagai berikut:

Setelah menjalankan klien, berikut adalah contoh output yang dihasilkan saat mengirim pesan ke server dan menerima respons:

Klien berhasil terhubung dengan mengirim pesan ke server, menerima kembali pesan yang sama, dan menampilkan hasilnya. 

## 3SOCKETFORKIN_SERVER
```python
import os
import socket
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0  # Tells the kernel to pick up a port dynamically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

class ForkedClient:
    """ A client to test forking server """
    
    def __init__(self, ip, port):
        # Create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        self.sock.connect((ip, port))
    
    def run(self):
        """ Client interacting with the server """
        # Send the data to server
        current_process_id = os.getpid()
        print('PID %s Sending echo message to the server: "%s"' % (current_process_id, ECHO_MSG))
        sent_data_length = self.sock.send(bytes(ECHO_MSG, 'utf-8'))
        print("Sent: %d characters, so far..." % sent_data_length)
        
        # Display server response
        response = self.sock.recv(BUF_SIZE)
        print("PID %s received: %s" % (current_process_id, response[5:]))
    
    def shutdown(self):
        """ Cleanup the client socket """
        self.sock.close()

class ForkingServerRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Send the echo back to the client
        data = str(self.request.recv(BUF_SIZE), 'utf-8')
        current_process_id = os.getpid()
        response = '%s: %s' % (current_process_id, data)
        print("Server sending response [current_process_id: data] = [%s]" % response)
        self.request.send(bytes(response, 'utf-8'))

class ForkingServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    """ Nothing to add here, inherited everything necessary from parents """
    pass

def main():
    # Launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address  # Retrieve the port number
    
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)  # Don't hang on exit
    server_thread.start()
    
    print("Server loop running PID: %s" % os.getpid())
     
    # Launch the client(s)
    client1 = ForkedClient(ip, port)
    client1.run()
    print("First client running")

    client2 = ForkedClient(ip, port)
    client2.run()
    print("Second client running")
    
    # Clean them up
    client1.shutdown()
    client2.shutdown()
    server.socket.close()

if __name__ == '__main__':
    main()
```
Kode ini berfungsi untuk membangun server echo yang dapat menangani beberapa klien secara bersamaan menggunakan teknik forking dalam pemrograman socket di Python. perintahnya mencakup implementasi server echo yang menggunakan `socketserver` untuk dapat menangani permintaan dari beberapa klien secara bersamaan dengan menggunakan proses yang terpisah (forking). dengan itu klien akan mengirim pesan ke server dan menerima respons yang sama.

Import Library

•	`os` untuk mendapatkan ID proses.

•	`socket` untuk membuat dan mengelola koneksi jaringan.

•	`threading` untuk menjalankan server dalam thread terpisah.

•	`socketserver` untuk membuat server berbasis socket dengan dukungan untuk multiproses.

Konstanta

•	`SERVER_HOST` alamat server, diatur ke `localhost`.

•	`SERVER_PORT` port yang diatur ke 0 agar kernel memilih port secara dinamis.

•	`BUF_SIZE` ukuran buffer untuk menerima data.

•	`ECHO_MSG` pesan yang akan dikirim ke server.

Kelas `ForkedClient`

•	Inisialisasi membuat socket dan menghubungkan ke server.

•	Metode run yaitu mengirim pesan ke server dan menerima respons, lalu mencetak hasilnya.

•	Metode shutdown dengan menutup koneksi socket.

Kelas `ForkingServerRequestHandler`

•	Mengimplementasikan metode `handle` untuk menerima data dari klien dan mengirimkan kembali respons yang berisi ID proses server dan data yang diterima.

Kelas `ForkingServer`

•	Menggunakan `socketserver.ForkingMixIn` untuk memungkinkan server menangani setiap permintaan dari klien di proses terpisah.

Fungsi `main`

•	Memulai server dan mendapatkan nomor port yang digunakan.

•	Membuat dan menjalankan dua klien yang berinteraksi dengan server.

•	Menutup koneksi klien dan socket server setelah selesai.

### Output

Setelah menjalankan server dan klien, berikut adalah contoh output yang dihasilkan ketika klien mengirim pesan ke server:

Implementasi server dan klien echo ini berhasil menunjukkan penggunaan teknik forking untuk menangani beberapa klien secara bersamaan. Setiap klien berhasil mengirim pesan ke server, dan server mengirimkan kembali pesan tersebut dengan menambahkan ID prosesnya.

## 3SOCKETTHREADING_SERVER

```python
import os
import socket
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0  # Tells the kernel to pick up a port dynamically
BUF_SIZE = 1024

def client(ip, port, message):
    """ A client to test threading mixin server """
    
    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    
    try:
        sock.sendall(bytes(message, 'utf-8'))
        response = sock.recv(BUF_SIZE)
        print("Client received: %s" % response.decode('utf-8'))
    finally:
        sock.close()

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ An example of a threaded TCP request handler """
    
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "%s: %s" % (cur_thread.name, data.decode('utf-8'))
        self.request.sendall(bytes(response, 'utf-8'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ Nothing to add here, inherited everything necessary from parents """
    pass

if __name__ == "__main__":
    # Run server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address  # Retrieve IP address
    
    # Start a thread with the server -- one thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    
    # Exit the server thread when the main thread exits
    server_thread.daemon = True
    server_thread.start()
    
    print("Server loop running on thread: %s" % server_thread.name)
    
    # Run clients
    client(ip, port, "Hello from client 1")
    client(ip, port, "Hello from client 2")
    client(ip, port, "Hello from client 3")
    
    # Server cleanup
    server.shutdown()
```
Kode tersebut memiliki fungsi untuk membuat server TCP yang dapat menangani beberapa klien secara bersamaan menggunakan threading, sehingga setiap klien dapat terhubung dan berkomunikasi dengan server secara independen. Terdiri dari implementasi server TCP multithreaded yang dapat menangani permintaan dari beberapa klien secara bersamaan. Klien akan mengirim pesan ke server, dan server akan mengembalikan pesan tersebut dengan menambahkan informasi tentang thread yang mengolah permintaan.

Import Library

•	`os` untuk menangani operasi sistem (tidak digunakan dalam kode ini, tetapi dapat digunakan untuk keperluan lain).

•	`socket` untuk membuat dan mengelola koneksi jaringan.

•	`threading` untuk mengelola thread dalam program.

•	`socketserver` untuk mempermudah pembuatan server berbasis socket.

Konstanta

•	`SERVER_HOST` yaitu alamat server yang diatur ke localhost.
•	`SERVER_PORT` port diatur ke 0 agar kernel memilih port secara dinamis.
•	`BUF_SIZE` ukuran buffer untuk menerima data (1024 byte).

Fungsi `client`

•	Menciptakan socket klien dan menghubungkan ke server.
•	Mengirimkan pesan ke server dan menerima respons dari server.
•	Mencetak respons yang diterima.

Kelas `ThreadedTCPRequestHandler`

•	Mengimplementasikan metode `handle` yang bertanggung jawab untuk menangani permintaan dari klien.
•	Menerima data dari klien, mendapatkan nama thread saat ini, dan mengirimkan kembali respons yang mencakup nama thread dan data yang diterima.

Kelas `ThreadedTCPServer`

•	Menggunakan `socketserver.ThreadingMixIn` untuk memungkinkan server menangani setiap permintaan dari klien dalam thread terpisah.

Bagian Utama Program

•	Membuat dan menjalankan server.

•	Mengambil alamat IP dan port yang digunakan oleh server.

•	Memulai thread untuk server menggunakan `server.serve_forever()` sehingga dapat menerima permintaan klien.

•	Menjalankan beberapa klien yang mengirimkan pesan ke server.

•	Melakukan pembersihan server setelah klien selesai berkomunikasi.

### Ouput

Untuk menjalankan kode ini, simpan dalam file bernama threaded_echo_server.py dan eksekusi file tersebut melalui command line seperti berikut:

Setelah menjalankan server dan klien, berikut adalah contoh output yang dihasilkan ketika klien mengirim pesan ke server:

Implementasi server dan klien TCP ini menunjukkan penggunaan threading untuk menangani beberapa klien secara bersamaan. Setiap klien dapat mengirim pesan ke server, dan server berhasil mengembalikan respons dengan informasi thread yang memproses permintaan tersebut.

## 3SOCKETTHREADING_SERVER
```python
import select
import socket
import sys
import signal
import pickle
import struct
import argparse

SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'

# Some utilitiesz
def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)

def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error:
        return ''
    
    buf = ""
    while len(buf) < size:
        buf += channel.recv(size - len(buf)).decode('utf-8')
    return pickle.loads(buf)[0]

class ChatServer(object):
    """ An example chat server using select """
    
    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []  # List of output sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print('Server listening to port: %s ...' % port)
        self.server.listen(backlog)
        # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        """ Clean up client outputs """
        print('Shutting down server...')
        # Close existing client sockets
        for output in self.outputs:
            output.close()
        self.server.close()

    def get_client_name(self, client):
        """ Return the name of the client """
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running = True
        
        while running:
            try:
                readable, writeable, exceptional = select.select(inputs, self.outputs, [])
            except select.error:
                break

            for sock in readable:
                if sock == self.server:
                    # Handle the server socket
                    client, address = self.server.accept()
                    print("Chat server: got connection %d from %s" % (client.fileno(), address))
                    # Read the login name
                    cname = receive(client).split('NAME: ')[1]
                    # Compute client name and send back
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)

                    # Send joining information to other clients
                    msg = "\n(Connected: New client (%d) from %s)" % (self.clients, self.get_client_name(client))
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(client)

                elif sock == sys.stdin:
                    # Handle standard input
                    sys.stdin.readline()
                    running = False
                else:
                    # Handle all other sockets
                    try:
                        data = receive(sock)
                        if data:
                            # Send as new client's message...
                            msg = '\n#[' + self.get_client_name(sock) + ']>> ' + data
                            # Send data to all except ourselves
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                        else:
                            print("Chat server: %d hung up" % sock.fileno())
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)

                            # Sending client leaving information to others
                            msg = "\n(Now hung up: Client from %s)" % self.get_client_name(sock)
                            for output in self.outputs:
                                send(output, msg)
                    except socket.error:
                        inputs.remove(sock)
                        self.outputs.remove(sock)
        self.server.close()

class ChatClient(object):
    """ A command line chat client using select """
    
    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        
        # Initial prompt
        self.prompt = '[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        
        # Connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print("Now connected to chat server@ port %d" % self.port)
            self.connected = True
            
            # Send my name...
            send(self.sock, 'NAME: ' + self.name)
            data = receive(self.sock)
            # Contains client address, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
        except socket.error:
            print("Failed to connect to chat server @ port %d" % self.port)
            sys.exit(1)

    def run(self):
        """ Chat client main loop """
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                
                # Wait for input from stdin and socket
                readable, writeable, exceptional = select.select([0, self.sock], [], [])
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data:
                            send(self.sock, data)
                    elif sock == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print('Client shutting down.')
                            self.connected = False
                            break
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print(" Client interrupted.")
                self.sock.close()
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socket Server Example with Select')
    parser.add_argument('--name', action="store", dest="name", required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    name = given_args.name
    
    if name == CHAT_SERVER_NAME:
        server = ChatServer(port)
        server.run()
    else:
        client = ChatClient(name=name, port=port)
        client.run()
```
Kode di atas merupakan implementasi dari sebuah aplikasi chat sederhana yang terdiri dari server dan client menggunakan socket dan modul select untuk menangani komunikasi antara banyak client secara bersamaan.

```python
import select
import socket
import sys
import signal
import pickle
import struct
import argparse
```

Kode ini mengimpor berbagai library yang diperlukan untuk komunikasi jaringan (socket), penanganan sinyal (signal), pengolahan data (pickle, struct), dan pengolahan argumen command line (argparse).

Konstanta
```python
SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'
```
SERVER_HOST mendefinisikan alamat host untuk server. CHAT_SERVER_NAME digunakan untuk membedakan server dari client.

Fungsi ultilitas
```python
def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)

def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error:
        return ''
    
    buf = ""
    while len(buf) < size:
        buf += channel.recv(size - len(buf)).decode('utf-8')
    return pickle.loads(buf)[0]
```
send: Fungsi ini mengirimkan data melalui socket. Data yang dikirim di-serialize menggunakan pickle dan dikirim dalam dua bagian: ukuran dan konten data.

receive: Fungsi ini menerima data dari socket. Ia membaca ukuran data yang diterima dan kemudian menerima data sesuai dengan ukuran tersebut, mendeserialize menggunakan pickle.

Kelas ChatServer
```python
class ChatServer(object):
    """ An example chat server using select """
    
    def __init__(self, port, backlog=5):
        ...
    
    def sighandler(self, signum, frame):
        ...
    
    def get_client_name(self, client):
        ...
    
    def run(self):
        ...
```

init: Konstruktor kelas ChatServer, yang menginisialisasi server socket, menyiapkan penanganan untuk sinyal, dan mendengarkan koneksi dari client.

sighandler: Menangani sinyal untuk menutup server dengan bersih.
get_client_name: Mengembalikan nama client berdasarkan socket yang terhubung.

run: Loop utama yang menggunakan select untuk mendengarkan koneksi baru dan data dari client. Jika ada client baru yang terhubung, server akan menyambut dan menginformasikan semua client lain.

Kelas ChatClient
```python
class ChatClient(object):
    """ A command line chat client using select """
    
    def __init__(self, name, port, host=SERVER_HOST):
        ...
    
    def run(self):
        ...
```
init: Konstruktor kelas ChatClient, yang menginisialisasi koneksi ke server dan mengirimkan nama client.

run: Loop utama untuk client, yang menggunakan select untuk mendeteksi input dari pengguna dan data yang diterima dari server.

Pengaturan Command-Line Interface
```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socket Server Example with Select')
    parser.add_argument('--name', action="store", dest="name", required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    ...
```

Bagian ini mengatur argumen command-line untuk menjalankan server atau client. Server akan dijalankan jika nama yang diberikan sama dengan CHAT_SERVER_NAME, sedangkan client akan dijalankan untuk nama lainnya.

Kode ini mendemonstrasikan cara membangun aplikasi chat berbasis socket menggunakan Python. Server dapat menangani banyak client secara bersamaan dengan menggunakan select, dan client dapat mengirim serta menerima pesan secara real-time. Implementasi ini menekankan penggunaan komunikasi berbasis jaringan yang efektif dan penanganan data dengan baik menggunakan metode serialization.
