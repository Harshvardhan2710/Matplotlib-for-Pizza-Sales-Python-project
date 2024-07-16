import matplotlib.pyplot as plt
import pandas as pd

# data

data = pd.read_csv("pizza.csv")
months = data["months"]
sales = data["sales"]

#code

plt.figure(figsize=(10, 5))
plt.plot(months, sales, linewidth=10, marker="o", markersize=20,markerfacecolor="red")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Harsh's Cafe Pizza Sale")
plt.grid()
plt.savefig("Hpizza.png")
plt.savefig("Hcpizza.pdf")
plt.show()