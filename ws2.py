from flask import Flask
from flask import jsonify
import subprocess

app = Flask(__name__)

@app.route('/status')
def display():

    temp = subprocess.Popen('hostname',stdout=subprocess.PIPE)
    hostname = ((temp.communicate()[0]).decode("utf-8")).strip('\n')
    temp = subprocess.Popen(['hostname', '-I'],stdout=subprocess.PIPE)
    ipaddress = ((temp.communicate()[0]).decode("utf-8")).strip('\n').rstrip()
    temp = subprocess.Popen("lscpu | grep 'CPU(s):'", shell=True, stdout=subprocess.PIPE)
    cpu = ((temp.communicate()[0]).decode("utf-8")).split()
    temp = subprocess.Popen("cat /proc/meminfo | grep 'MemTotal'", shell=True, stdout=subprocess.PIPE)
    mem = (temp.communicate()[0]).split()
    return jsonify(
                hostname=hostname,
                ip_address=ipaddress,
                cpus=cpu[1],
                memory=int(mem[1]) // 1000000
            )

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
