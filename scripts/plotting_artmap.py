import matplotlib.pyplot as plt
import pandas as pd

#plots 2d graph of rho vs accuracy for each std dev in blob data set
def plot_blobs_2d(filename):
    data = pd.read_csv(filename, names = ["Std Dev", "Rho", "Accuracy"])
    std_devs = set(data["Std Dev"])
    rhos = set(data["Rho"])
    fig, ax = plt.subplots()
    for std_dev in std_devs:
        local_data = data[data["Std Dev"] == std_dev]
        ax.plot(
            local_data["Rho"],
            local_data["Accuracy"],
            label= f"{std_dev}",
            marker="o",
        )
    ax.set_xlabel("Rho")
    ax.set_ylabel("Accuracy")
    plt.title("Effect on Accuracy with Vigilance and Standard Deviation")
    # ax.legend()
    plt.show()

#plots accuracy vs rho for iris data set
def plot_iris(filename):
    data = pd.read_csv(filename, names = ["Rho", "Accuracy"])
    rhos = set(data["Rho"])
    fig, ax = plt.subplots()
    ax.plot(
        data["Rho"],
        data["Accuracy"],
        color="pink"
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

#calls each plot function with corresponding data file
def main():
    blobfile = "data/clusterblobs_stddev_rho_accuracy.txt"
    irisfile = "data/cluster_iris_rho_accuracy.txt"
    plot_blobs_2d(blobfile)
    plot_iris(irisfile)
    plot_blobs_2d_accuracy_groups(blobfile)
    plot_3d_blobs(blobfile)

if __name__ == "__main__":
    main()