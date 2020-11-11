p1 = int(input())
p2 = int(input())
p3 = int(input())
j1 = int(input())
j2 = int(input())

pizza = []
pizza.append(p1)
pizza.append(p2)
pizza.append(p3)
pizza.sort()

juice = []
juice.append(j1)
juice.append(j2)
juice.sort()

price = (pizza[0] + juice[0])*1.1
print('%.1f' %price)




