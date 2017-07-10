from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
#common gateway interface
class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()

				output=""
				output+= "<html><body>Hello!</body></html>"
				self.wfile.write(output.encode())
				print (output)
				return
			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()

				output=""
				output+= "<html><body>Hola!<a href='/hello'>Back to Hello</a></body></html>"
				self.wfile.write(output.encode())
				print (output)
				return

		except IOError:
			self.send_error(404,"File Not Found %s" % self.path)

	def do_POST:
		try:
			self.send_response(301)
			self.send_headers()

			ctype

		except:


def main():
	try:
		port = 8080
		server = HTTPServer(('',port),webserverHandler)
		print (" Server is runnning on port %s" %port)
		server.serve_forever()


	except KeybordIntercept:
		print ("^C entered , stoppjng web server...")
		server.socket.close()


if __name__ == '__main__':
	main()