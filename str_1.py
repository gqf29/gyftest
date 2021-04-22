import random
import string


def create_str():
    with open('str.txt', 'a+', encoding='utf-8') as f:
        # 清空文件内容
        f.seek(0)
        f.truncate()
        for i in range(10):
            # join（）将序列中的元素以指定的字符连接生成一个新的字符串
            str1 = "".join(random.sample(string.ascii_lowercase, 6))
            f.write(str1 + "\n")
    f.close()


create_str()
