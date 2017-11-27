
people = ['england', 'spain', 'japanese', 'italy', 'norw']
color = ['red', 'white', 'green', 'blue', 'yellow']
pet = ['dog', 'snail', 'zebra', 'horse', 'fox']
drink = ['tea', 'juice', 'water', 'milk', 'coffee']
prof = ['doctor', 'violin', 'diplo', 'paint', 'photo']
row = ['Country', 'Color', 'Pet', 'Drink', 'Profession']

from itertools import permutations
from prettytable import PrettyTable

immediate = True
count = 0
for v0 in permutations(people):
    if v0.index('norw') != 0:
        continue
    for v1 in permutations(color):
        if v0.index('england') != v1.index('red'):
            continue
        if not immediate:
            if v1.index('green') < v1.index('white'):
                continue
        else :
            if v1.index('green') - v1.index('white') != 1:
                continue
        if abs(v0.index('norw') - v1.index('blue')) != 1:
            continue
        for v2 in permutations(pet):
            if v0.index('spain') != v2.index('dog'):
                continue
            for v3 in permutations(drink):
                if v3.index('milk') != 2:
                    continue
                if v3.index('coffee') != v1.index('green'):
                    continue
                if v0.index('italy') != v3.index('tea'):
                    continue
                for v4 in permutations(prof):
                    if v0.index('japanese') != v4.index('paint'):
                        continue
                    if v4.index('photo') != v2.index('snail'):
                        continue
                    if v4.index('diplo') != v1.index('yellow'):
                        continue
                    if v4.index('violin') != v3.index('juice'):
                        continue
                    if abs(v2.index('fox') - v4.index('doctor')) != 1:
                        continue
                    if abs(v2.index('horse') - v4.index('diplo')) != 1:
                        continue
                    count += 1
                    x = PrettyTable(['Property', '1','2','3','4','5'])
                    x.add_row([row[0]]+list(v0))
                    x.add_row([row[1]]+list(v1))
                    x.add_row([row[2]]+list(v2))
                    x.add_row([row[3]]+list(v3))
                    x.add_row([row[4]]+list(v4))
                    print x
print 'Totally %d answer'%(count,)+'s'*(count>1)