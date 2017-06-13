import sys

if len(sys.argv) < 2:
	sys.exit('Fewer arguments than expected')

classes = sys.argv[1].split(',')
train_ratio = 0.9

wns = []

def persist_lines(classname, lines):
    formatted_lines = []
    for line in lines:
        line = line.strip()
        d = {}
        for wi in line.split(';'):
            wn, ws = wi.split(':')
            d[wn] = ws

        formatted_lines.append(','.join([d.get(wn, '0') for wn in wns] + [classname]))

    return formatted_lines

for classname in classes:
    f = open(classname+'.txt', 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        wnst = [ wn for wn, ws in [wi.split(':') for wi in line.strip().split(';')]]
        wns += wnst

wns = list(set(wns))

train_h = open('train.txt', 'w')
test_h = open('test.txt', 'w')


train_h.write(','.join(wns + ['room']) + '\n')
test_h.write(','.join(wns + ['room'])+ '\n')

train_lines = []
test_lines = []
for classname in classes:
    f = open(classname+'.txt', 'r')
    lines = f.readlines()
    f.close()

    l = int(len(lines) * train_ratio)
    train_lines += persist_lines(classname, lines[:l])
    test_lines += persist_lines(classname, lines[l:])

train_h.write('\n'.join(train_lines))
test_h.write('\n'.join(test_lines))

train_h.close()
test_h.close()
