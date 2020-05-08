import os
import time
import pyscreenshot
import getpass
import socket
import random
import atexit
import http.server
import socketserver
import multiprocessing

def clean_up():
   os.remove(http_directory + "/screenshot.jpg")
   os.remove(http_directory + "/index.html")
   http_server.socket.close()

atexit.register(clean_up)

user = getpass.getuser()
http_directory = "/home/" + user + "/descatt"
if not os.path.exists(http_directory):
	os.mkdir(http_directory)

index_html = open(http_directory + "/index.html", "w")
index_html.write("""
	<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<style>
				body {
					margin: 0;
					padding: 0;
					background-color: #000000;
				}
				img {
					display: block;
					object-fit: contain;
					margin: 0 auto;
				}
			</style>
		</head>
		<body>
			<img id="screenshot">
			<script>
				var screenshot = document.querySelector("#screenshot");
				screenshot.style.maxWidth = innerWidth + "px";
				screenshot.style.maxHeight = innerHeight + "px";
				setInterval(function() {
					var version = (new Date()).getTime();
					var image = new Image();
					image.addEventListener("load", function() {
						screenshot.src = "/screenshot.jpg?version=" + version;
					});
					image.src = "/screenshot.jpg?version=" + version;
				}, 1000);
			</script>
		</body>
	</html>
""")
index_html.close()

port = random.randint(7425, 7450)

temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
	temp_socket.connect(("10.255.255.255", 1))
	ip = temp_socket.getsockname()[0]
except:
	ip = "127.0.0.1"
finally:
	temp_socket.close()

print("http://" + ip + ":" + str(port) + "/index.html")

def start_screenshotting():
	while True:
		screenshot = pyscreenshot.grab()
		screenshot.save(http_directory + "/screenshot.jpg", quality=50)
		time.sleep(1)

os.chdir(http_directory)
handler = http.server.SimpleHTTPRequestHandler
http_server = socketserver.TCPServer((ip, port), handler)

def start_serving_web_requests():
	http_server.serve_forever()

ss_process = multiprocessing.Process(target=start_screenshotting)
ss_process.start()
sswr_process = multiprocessing.Process(target=start_serving_web_requests)
sswr_process.start()
ss_process.join()
sswr_process.join()
