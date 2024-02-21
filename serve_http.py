from http.server import HTTPServer, SimpleHTTPRequestHandler

if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', 8888), SimpleHTTPRequestHandler)
    print(f'Serving directory on http://0.0.0.0:8888 (plain HTTP, you need to use ngrok or similar tool for SSL)')
    httpd.serve_forever()
