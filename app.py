from flask import Flask, request, render_template_string
import socket

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Simple Port Scanner</title>
<h2>Simple Port Scanner</h2>
<form method=post>
  IP address or hostname:<br>
  <input type=text name=host required><br>
  Ports (e.g. 20-80):<br>
  <input type=text name=ports required><br><br>
  <input type=submit value=Scan>
</form>

{% if results %}
  <h3>Scan results for {{ host }}:</h3>
  <ul>
  {% for port, status in results.items() %}
    <li>Port {{ port }}: {{ status }}</li>
  {% endfor %}
  </ul>
{% endif %}
'''

def scan_ports(host, ports_range):
    results = {}
    try:
        for port in ports_range:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            sock.close()
            results[port] = "Open" if result == 0 else "Closed"
    except Exception as e:
        results = {"error": str(e)}
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    host = None
    if request.method == 'POST':
        host = request.form['host']
        ports = request.form['ports']
        try:
            start_port, end_port = map(int, ports.split('-'))
            ports_range = range(start_port, end_port + 1)
            results = scan_ports(host, ports_range)
        except Exception as e:
            results = {"error": f"Invalid input: {str(e)}"}
    return render_template_string(HTML, results=results, host=host)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

