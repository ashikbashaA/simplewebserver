from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <center>
        <table border="1" cellspacing="2" cellpadding="10" >
            <caption><i>ASHIK</i><BR>
                <b>26018692</b></caption>
            <tr>
                <th>s.no</th>
                <th>features</th>
                <th>info</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Device name</td>
                <td>Ashik-25-08</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Processor</td>
                <td>Intel(R) CORE(TM) 5 201 (2.20GHz)</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed RAM</td>
                <td>16 GB (15.9 GB usable)</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Graphics card</td>
                <td>Intel(R) Graphics (128 MB)</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Storage</td>
                <td>123 GB of 477 GB used</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Device ID</td>
                <td>9BED6B1D-C22A-46BF-9925-F3D1DD881CF9</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Product ID</td>
                <td>00342-42945-51933-AAOEM</td>
            </tr>
            <tr>
                <td>8</td>
                <td>System type</td>
                <td>64-bit operating system, x64-based processor</td>
            </tr>
            <tr>
                <td>9</td>
                <td>Pen and touch</td>
                <td>No pen or touch input is available for this display</td>
            </tr>
        </table>
        </center>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()