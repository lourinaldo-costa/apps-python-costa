import shelve

db = shelve.open('shelve.db')
print(list(db))
