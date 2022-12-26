# Задача 5.
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random
koefs = {}
# k = 15
k = int(input('введите целое число больше 0: '))
for i in range(k + 1):
    koefs[i] = random.randint(1, 100)
print(koefs)
# {0: 71, 1: 62, 2: 44, 3: 89}
# 89x^3+44x^2
# print(max(koefs.keys()))
max_k = max(koefs.keys())
out_str = ''
# c = 0
first = True
for i in range(max_k, -1, -1):
    koef = koefs[i]
    pow_x = i
    if i > 1:
        # if c == 0:
        if first:
            out_str += f'{koef}x^{pow_x}'
            # 89x^3
        else:
            out_str += f'+{koef}x^{pow_x}'
            # +89x^3
    elif i == 1:
        if first:
            out_str += f'{koef}x'
            # 62x
        else:
            out_str += f'+{koef}x'
    else:
        out_str += f'+{koef}=0'
    # c += 1
    if first:
        first = False
print(out_str)
with open('result.txt', 'w', encoding='utf-8') as fd:
    fd.write(out_str)
    

# import random
# import re

# input_str = '54x^4-22x^3+34x^2+5x+18=0'
# pattern = r'([+-]?\d+)x\^?(\d*)|(\d*)=0$'
# # pattern = r'([-+]?\d*)(x\^*\d*)*'
# # pattern2 = r'([-+]?\d*)(x\^*\d*)*|(\=0)'

# # res = re.findall(pattern, input_str)
# # print(res)
# # re.compile()
# output = re.compile(pattern)
# result = output.findall(input_str)
# print(result)
# print(int(result[1][0]))
# res_dict = dict()
# for i in result:
#     if i[1]:
#         res_dict[int(i[1])] = int(i[0])
#     elif i[1] == '' and i[0]:
#         res_dict[1] = int(i[0])
#     elif i[2]:
#         res_dict[0] = int(i[2])
# print(res_dict)
# # '54x^4-22x^3+34x^2+5x+18=0'
# k = 3
# res_dict = dict()
# res_dict[2] = random.randint(0, 100)
# # res_dict = {
# #     3: 22,
# #     2: 34,
# #     1: 5,
# #     0: 18
# # }
# out = ''
# for k in res_dict:
#     out += f'{res_dict[k]}x^{k}'

# [18, 5, 34, -22, 54]
# [5, 0, 73, 14, 0]
# [23, 5, 107, -8, 54].reverse()

# res_list = []
# key_list = []
# max_x = 0
# for i in result:
#     try:
#         koef = float(i[0])
#     except ValueError:
#         continue
#     if i[1]:
#         x1 = i[1]
#         x1 = x1.replace('x^', '')
#         if x1.isdigit() and int(x1) > max_x:
#             max_x = int(x1)
#         key_list.append(x1)
#     res_list.append(koef)
#
#
# print(res_list)
# print(key_list)
# print(max_x)
#
# # [54.0, -22.0, 34.0, 5.0, 18.0]
# # {:+f}
