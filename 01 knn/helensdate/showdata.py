import matplotlib
import matplotlib.pyplot as plt
from loaddata import loadfile
print(matplotlib.get_backend())
def showdatas(data, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[:,0],data[:,2],c=labels)
    plt.savefig("3.png")

data, labels = loadfile('dataset.txt')
showdatas(data,labels)