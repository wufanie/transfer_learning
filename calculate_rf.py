#
def cal_stride(s):
    length = len(s)
    s_sum = 1
    if length > 0:
        for idx in range(length):
            s_sum *= int(s[idx])
    return s_sum


def open_txt(dir):
    kernel, stride = None, None
    with open(dir, "r", encoding="utf-8") as f:
        str = f.read()
        kernel = (str.split('\n')[0]).split(' ')
        stride = (str.split('\n')[1]).split(' ')
    return kernel, stride


def cal_all(kernel, stride):
    n = len(kernel)
    r = 1
    for i in range(n):
        s = [stride[sn] for sn in range(i)]
        r += int((int(kernel[i]) - 1) * cal_stride(s))
        print(r)


if __name__ == '__main__':
    kernel, stride = open_txt('net_params1.txt')
    cal_all(kernel, stride)
