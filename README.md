# Client-Server Python Sederhana

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
Waiting to receive message from client
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

```cmd
Connecting to 127.0.0.1 port 8080
Sending Test message. This will be echoed
Received: Test message. Th
Received: is will be echoe
Received: d
Closing connection to the server
```

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

```cmd
3SOCKET_UDPECHOSERVER.py --port 8080
```

Setelah menjalankan server, berikut adalah contoh output yang dihasilkan saat menerima pesan dari klien:

```cmd
Starting up echo server on 0.0.0.0 port 8080
Waiting to receive message from client
Received 41 bytes from ('127.0.0.1', 50116)
Data: b'This is the message. It will be repeated.'
Sent 41 bytes back to ('127.0.0.1', 50116)
Waiting to receive message from client
```

Server echo UDP ini berhasil mendengarkan permintaan dari klien, menerima pesan, dan mengirimkannya kembali. Ini adalah implementasi dasar yang berguna untuk memahami konsep komunikasi jaringan berbasis UDP antara klien dan server. untuk membuat client terhubung menggunakan kode yang akan dijelaskan selanjutnya.

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

```python
python 3SOCKET_UDPECHOCLIENT.py --port 8080
```

Setelah menjalankan klien, berikut adalah contoh output yang dihasilkan saat mengirim pesan ke server dan menerima respons:

```python
Connecting to 192.168.38.60 port 8080
Sending This is the message. It will be repeated.
Received: This is the message. It will be repeated.
Closing connection to the server
```

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

```cmd
Server loop running PID: 21160
PID 21160 Sending echo message to the server: "Hello echo server!"
Sent: 18 characters, so far...
Server sending response [current_process_id: data] = [21160: Hello echo server!]
PID 21160 received: b': Hello echo server!'
First client running
PID 21160 Sending echo message to the server: "Hello echo server!"
Sent: 18 characters, so far...
Server sending response [current_process_id: data] = [21160: Hello echo server!]
PID 21160 received: b': Hello echo server!'
Second client running
```

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

```cmd
python 3SOCKETTHREADING_SERVER.py
```

Setelah menjalankan server dan klien, berikut adalah contoh output yang dihasilkan ketika klien mengirim pesan ke server:

```cmd
Client received: Thread-2: Hello from client 1
Client received: Thread-3: Hello from client 2
Client received: Thread-4: Hello from client 3
```

Implementasi server dan klien TCP ini menunjukkan penggunaan threading untuk menangani beberapa klien secara bersamaan. Setiap klien dapat mengirim pesan ke server, dan server berhasil mengembalikan respons dengan informasi thread yang memproses permintaan tersebut.
