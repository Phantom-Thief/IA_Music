import pickle

li = ['Georges', 'Micheal']
pickle.dump(li, open('aaaaaaTEST.dat', 'wb'))

li = ['Charles', 'Henry']
pickle.dump(li, open('aaaaaaTEST.dat', 'wb'))

li = pickle.load(open('aaaaaaTEST.dat', 'rb'))

print(li)