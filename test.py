import pandas as pd
import pickle

test = pd.read_csv('test.txt')

tX = test.iloc[:, :-1]
ty = test.room

f = open('model.txt', 'r')
m = pickle.loads(f.read())
f.close()
print "Score: ", m.score(tX, ty)
