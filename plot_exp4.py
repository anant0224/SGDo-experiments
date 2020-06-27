import matplotlib.pyplot as plt

# experiment4
f = open('plotdata/experiment4_parallel', 'r')
output = f.read()
output = output.split("\n")
x_list = output[0].split(",")
results = output[1:]
eps3 = [float(res.split(",")[0]) for res in results]
epsr1 = [float(res.split(",")[1]) for res in results]
epsr2 = [float(res.split(",")[2]) for res in results]

l1=[x/eps3[0] for x in eps3]
l2=[x/epsr1[0] for x in epsr1]
l3=[x/epsr2[0] for x in epsr2]

plt.plot(x_list,l1, label=r'$\|x_T - x^*\|^2$')
plt.plot(x_list,l2, label=r'$\frac{1}{n}$')
plt.plot(x_list,l3, label=r'$\frac{(\log T)^2}{n}$')

plt.yscale('log')
plt.legend()
# plt.title('eta=0.07')
# plt.ylim([0.001, 1])
plt.show()
