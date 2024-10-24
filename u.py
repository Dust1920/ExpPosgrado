import matplotlib.pyplot as plt

msi = 3
days = 30 * msi
r = 0.12
r_d = r / 365

x_0 = 3000
x_init = x_0
x_0m = x_0 / msi
msi_c = 0
x = []
for i in range(1, days + 1):
    u = 1 if i % 30 == 0 else 0
    if u:
        x_0 = x_0 * (1 + r_d) - x_0m
        msi_c += 1
    else:
        x_0 = x_0 * (1 + r_d)
    x.append(x_0)



print("Monto Inicial",x_init)
print(x[-1],x_init)
print("Cashback Esperado", x[-1] / x_init * 100)

plt.plot(x)
plt.show()