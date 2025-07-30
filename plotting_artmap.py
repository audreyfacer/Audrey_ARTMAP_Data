import matplotlib.pyplot as plt
import pandas as pd
def plot
data = pd.read_csv(filename, names = ["Std Dev", "Rho", "Accuracy"])
std_devs = set(data["Std Dev"])
rhos = set(data["Rho"])
fig, ax = plt.subplots()
for std_dev in std_devs:
    local_data = data[data["Std Dev"] == std_dev]
    ax.plot(
        local_data["Rho"],
        local_data["Accuracy"],
        label= f"{std_dev}"
    )
ax.set_xlabel("Rho")
ax.set_ylabel("Accuracy")
plt.title("Effect on Accuracy with Vigilance and Standard Deviation")
# ax.legend()
# plt.show()

filename = input("Enter file to analyze: ") #"clusterblobs_stddev_rho_accuracy.txt"
data = pd.read_csv(filename, names = ["Rho", "Accuracy"])
rhos = set(data["Rho"])
fig, ax = plt.subplots()
ax.plot(
    data["Rho"],
    data["Accuracy"]
)
ax.set_xlabel("Rho")
ax.set_ylabel("Accuracy")
plt.title("Vigilance Effect on Accuracy")
ax.legend()
plt.show()

#sorting through the data by accuracy
data = pd.read_csv(filename, names = ["Std Dev", "Rho", "Accuracy"])
data_filtered = data[data['Accuracy']== '.98']

# fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})
# ax1.plot_trisurf(
#     data["Rho"],
#     data["Std Dev"],
#     data["Accuracy"]
# )
# ax1.set_xlabel("Rho")
# ax1.set_ylabel("Std Dev")
# ax1.set_zlabel("Accuracy")
# ax1.view_init(45, 45, 0)
# plt.show()
