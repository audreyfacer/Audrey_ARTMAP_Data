import numpy as np
from sklearn.datasets import load_iris, make_blobs
import matplotlib.pyplot as plt
from tqdm import tqdm
from artlib import FuzzyART, SimpleARTMAP, QuadraticNeuronART

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
# import umap.plot

from pathlib import Path

blobfile = Path("data", "clusterblobs_stddev_rho_accuracy.txt")
irisfile = Path("data", "cluster_iris_rho_accuracy.txt")

def cluster_iris(rho):
    # from sklearn.model_selection import train_test_split
    # from sklearn.metrics import classification_report, accuracy_score
    # import umap.plot

    data, target = load_iris(return_X_y=True)
    #print("Data has shape:", data.shape)


    params = {"rho": rho, "alpha": 0.001, "beta": 1.0}
    art = FuzzyART(**params)
    # params = {
    #     "rho": 0.0,
    #     "s_init": 0.9,
    #     "lr_b": 0.1,
    #     "lr_w": 0.1,
    #     "lr_s": 0.1
    # }
    # art = QuadraticNeuronART(**params)

    X = art.prepare_data(data)
    print("Prepared data has shape:", X.shape)
    data = art.prepare_data(data)
    X_train, X_test, y_train, y_test = train_test_split(
        data, target, test_size=0.33, random_state=0
    )

    cls = SimpleARTMAP(art)

    cls = cls.fit(X_train, y_train)

    #print(f"{len(np.unique(cls.labels_a))} clusters found")

    y_pred = cls.predict(X_test)
    return accuracy_score(y_test, y_pred)
    # print(classification_report(y_test, y_pred))


    # mapper = umap.UMAP().fit(X_test)

    # umap.plot.points(
    #     mapper, labels=y_pred, color_key_cmap="Paired", background="black"
    # )
    # umap.plot.plt.show()



def cluster_blobs(rho, std):

    data, target = make_blobs(
        n_samples=150,
        #n_features=4, #dimensions
        centers=3,
        cluster_std=std,
        random_state=0,
        shuffle=False,
    )
    #print("Data has shape:", data.shape)

    params = {"rho": rho, "alpha": 0.001, "beta": 1.0}
    art = FuzzyART(**params)

    # params = {
    #     "rho": 0.0,
    #     "s_init": 0.9,
    #     "lr_b": 0.1,
    #     "lr_w": 0.1,
    #     "lr_s": 0.1
    # }
    # art = QuadraticNeuronART(**params)

    X = art.prepare_data(data)
    #print("Prepared data has shape:", X.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, target, test_size=0.33, random_state=0
    )

    cls = SimpleARTMAP(art)

    cls = cls.fit(X_train, y_train)
    #print(f"{cls.module_a.n_clusters} clusters found")
    y_pred = cls.predict(X_test)
    y = cls.labels_
    return accuracy_score(y_test, y_pred)
    '''
    print(classification_report(y_test, y_pred))

    mapper = umap.UMAP().fit(X_test)

    umap.plot.points(
        mapper, labels=y_pred, color_key_cmap="Paired", background="black"
    )
    umap.plot.plt.show()

    cls.visualize(X_train, y)

    plt.show()
    '''
def saving(rho, std, result):
    with open(blobfile, 'a') as f:
        dataline = f"{std}, {rho}, {result}\n"
        f.write(dataline)
def iris_saving(rho, result):
    with open(irisfile, 'a') as f:
        dataline = f"{rho}, {result}\n"
        f.write(dataline)
#audrey test loop
def loopedyloop():
    std_values = np.arange(0.1, 5.0, 0.1)
    for std in tqdm(std_values):
        rho_values = np.linspace(0.0, 1.0, 21)
        for rho in rho_values:
            result = cluster_blobs(rho, std)
            saving(rho, std, result)
#iris cluster test loop
def irisloop():
    rho_values = np.linspace(0.0, 1.0, 21)
    for rho in rho_values:
        result = cluster_iris(rho)
        iris_saving(rho, result)

def main():
    #cluster_iris()
    #cluster_blobs()
    loopedyloop()
    #irisloop()


if __name__ == "__main__":
    main()
