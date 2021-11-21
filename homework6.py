dic1 = {1: 15, 2: 'Geek', 3: 'Me'}
dic2 = {4: 30, 5: 40, 6: 'Hub', 7: 'Who'}
dic3 = {8: 50, 9: 60, 10: 70}
for conc in (dic2, dic3): dic1.update(conc)
print("Dictionary 1: " + str(dic1))