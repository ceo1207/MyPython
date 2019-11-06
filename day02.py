# coding=utf-8
# Day 02 数据类型和运算符
# 运算符
a = 12
b = 7
c = a / b  # int
d = float(a) / b  # float
e = a**b
# 字符串
# python2 默认是str 存储已编码的字节数据， 可以使用unicode
a = 'fef'  # str
print type(a)
b = u'fef'  # unicode
a = u"李白"
print a
with open('test', 'a') as f:
    # f.write(a)  UnicodeEncodeError: 'ascii' codec can't encode characters in
    # position 0-1: ordinal not in range(128)
    f.write(a.encode('utf-8'))
