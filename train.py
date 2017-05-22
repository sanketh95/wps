import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegressionCV

train = pd.read_csv('train.txt')
test = pd.read_csv('test.txt')

X = train.iloc[:, :-1]
y = train.room

tX = test.iloc[:, :-1]
ty = test.room

cs = [0.00001, 0.00003, 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300]
m = LogisticRegressionCV(Cs=cs)
m.fit(X, y)

print "Score: ", m.score(tX, ty)

f = open('model.txt', 'w')
f.write(pickle.dumps(m))
f.close()

f = open('fields.txt', 'w')
f.write(pickle.dumps(list(X.columns)))
f.close()
