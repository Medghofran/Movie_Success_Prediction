import SocketServer
import SimpleHTTPServer
import re
import json

PORT = 9090

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if None != re.search('/api/square/*', self.path):
            num = float(self.path.split('/')[-1])
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(str(num*num)) #call sample function here
            return

        if None != re.search('/api/mult/*', self.path):
            num1 = float(self.path.split('/')[-1])
            num2 = float(self.path.split('/')[-2])
            #This URL will trigger our sample function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(str(num1*num2)) #call sample function here
            return

        else:
            #serve files, and directory listings by following self.path from
            #current working directory
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
            
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', 0))
        print (content_len)
        post_body = self.rfile.read(content_len)
        
        predictionText = json.load(post_body)
        print(predictionText)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(predictionText)
        return

#Run the server
httpd = SocketServer.ThreadingTCPServer(('', PORT),CustomHandler)
print ("serving at port", PORT)
httpd.serve_forever()
