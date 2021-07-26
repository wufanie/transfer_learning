#
def cal_stride(s):
    length = len(s)
    s_sum = 1
    for idx in range(length):
        s_sum *= int(s[idx])
    return s_sum


def open_txt(dir):
    insize, kernel, stride = None, None, None
    with open(dir, "r", encoding="utf-8") as f:
        str = f.read()
        insize = (str.split('\n')[0]).split(' ')
        if len(str.split('\n')) > 2:
            kernel = (str.split('\n')[1]).split(' ')
            stride = (str.split('\n')[2]).split(' ')
        # print(insize)
    return insize, kernel, stride


def cal_all(input, kernel, stride):
    try:
        n = len(input)
        r = 1
        if n == 1:
            return r
        if ((len(input) - 1) == len(kernel) == len(stride)) is True:
            r = int(kernel[0])
            if n == 2:
                return r
            else:
                n -= 1
                for i in range(n - 1):
                    s = [stride[sn] for sn in range(i)]
                    r += int((int(kernel[i]) - 1) * cal_stride(s))
                return r
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    insize, kernel, stride = open_txt('net_params1.txt')
    for i in range(len(insize) - 1):
        print(cal_all(insize, kernel, stride))
        insize.pop()
        kernel.pop()
        stride.pop()
