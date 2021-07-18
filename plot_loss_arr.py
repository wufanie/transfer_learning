#定义两个数组
from matplotlib import pyplot as plt

def plot_la(phase ,acc_list, loss_list):
    #我这里迭代了200次，所以x的取值范围为(0，200)，然后再将每次相对应的准确率以及损失率附在x上
    x1 = range(0, len(acc_list))
    x2 = range(0, len(loss_list))
    y1 = acc_list
    y2 = loss_list
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'o-')
    plt.title(phase + ' accuracy vs. epoches')
    plt.ylabel(phase + ' accuracy')
    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, '.-')
    plt.xlabel(phase + ' loss vs. epoches')
    plt.ylabel(phase + ' loss')
    plt.show()
    # plt.savefig("accuracy_loss.jpg")