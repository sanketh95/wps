import pickle
import subprocess
import numpy as np

f = open('model.txt', 'r')
m = pickle.loads(f.read())
f.close()

f = open('fields.txt', 'r')
fields = pickle.loads(f.read())
f.close()

command = ["nmcli", "-t", "-f", "SSID,SIGNAL", "dev", "wifi", "list"]
out = subprocess.check_output(command)

print out

d = {}
for line in out.split('\n'):
    if not line.strip():
        continue
    wn, wsi = line.split(':')
    d[wn] = int(wsi)

v = []
for field in fields:
    v.append(d.get(field, 0))

print m.predict(np.array([v]))
