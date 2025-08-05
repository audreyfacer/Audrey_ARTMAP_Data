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

#sorting through the data by accuracy and plots std dev vs rho points for each accuracy value
def plot_blobs_2d_accuracy_groups(filename):
    data = pd.read_csv(filename, names = ["Std Dev", "Rho", "Accuracy"])
    for accuracy in sorted(set(data["Accuracy"])):
        data_filtered = data[data['Accuracy']== accuracy]
        fig, ax = plt.subplots()
        ax.set_xlabel("Std Dev")
        ax.set_ylabel("Rho")
        plt.scatter(
            data_filtered["Std Dev"],
            data_filtered["Rho"],
            color="pink")
        plt.title(f"Blobs with {accuracy} Accuracy")
        plt.show()

#plots 3d graph of std dev, rho, and accuracy of blob data set
def plot_3d_blobs(filename):
    data = pd.read_csv(filename, names = ["Std Dev", "Rho", "Accuracy"])
    std_devs = set(data["Std Dev"])
    rhos = set(data["Rho"])
    fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})
    ax1.plot_trisurf(
        data["Rho"],
        data["Std Dev"],
        data["Accuracy"],
        color="pink"
    )
    ax1.set_xlabel("Rho")
    ax1.set_ylabel("Std Dev")
    ax1.set_zlabel("Accuracy")
    ax1.view_init(45, 45, 0)
    plt.show()

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