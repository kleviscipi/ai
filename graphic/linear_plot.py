import matplotlib.pyplot as plt

price = [7,8,8,9,9,9,10,11,14,14,15]
size  = [50,60,70,80,90,100,110,120,130,140,150] 

plt.scatter(size,price)
plt.ylabel("Size")
plt.xlabel("Price")
plt.show()