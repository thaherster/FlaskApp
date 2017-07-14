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
				output+= "<html><body>Hola!<a href='/hello'>Back to Hello</a>"
				output+= "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say ?</h2><input name='message' type='text' ><input type='submit' value='Submit'></form>"	
				output+= "</body></html>"
				self.wfile.write(output.encode())
				print (output)
				return
			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()

				output=""
				output+= "<html><body>Hola!<a href='/hello'>Back to Hello</a>"
				output+= "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say ?</h2><input name='message' type='text' ><input type='submit' value='Submit'></form>"	
				output+= "</body></html>"
				self.wfile.write(output.encode())
				print (output)
				return

		except IOError:
			self.send_error(404,"File Not Found %s" % self.path)

	def do_POST(self):
		try:
			self.send_response(301)
			self.send_header('Content-type','text/html')
			self.end_headers()

			ctype, pdict = cgi.parse_header(self.headers.get_all('content-type'))
			if ctype == 'multipart/form-data':
				fields=cgi.parse_multipart(self.rfile,pdict)
				messagecontent = fields.get('message')

				output=""
				output+= "<html><body>"
				output+= "<h2>okay how about this: </h2>"	
				output+= "<h1> %s </h1>" % messagecontent[0]						
				output+= "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say ?</h2><input name='message' type='text' ><input type='submit' value='Submit'></form>"	
				output+= "</body></html>"
				self.wfile.write(output.encode())
				print(output)
				return

		except IOError:
			self.send_error(404,"File Not Found %s" % self.path)


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