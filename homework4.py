dic1 = {1:'Zahar', 2:'Andrew', 3:'Vova'}
dic2 = {4:'Play', 5:'code', 6:'try', 7:20}
dic3 = {8:19, 9:18, 10:17, 11:16, 12:15}
dic4 = {}
for conc in (dic1, dic2, dic3): dic4.update(conc)
print(dic4)