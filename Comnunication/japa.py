import matplotlib.pyplot as plt
import numpy as np
# pre_n = '010010000100001100000000000000000000000001010001001001001010000101'
# pre_n = '100110001000000111'
pre_n = '1100001000000000'
length = len(pre_n)
pre_list = list(pre_n)
for ch in range (0,length):
    pre_list[ch] = int (pre_list[ch])
store_list = pre_list

print(pre_list)
ich = -1 ;
for ch in range (0,length):
    if pre_list[ch] == 1 :
        ich = ich * (-1)
    pre_list[ch] = pre_list[ch]*ich;

pre_flag_num = 0;
flag_zero = 0;
for ch in range (0,length):
    if pre_list[ch] != 0 :
        flag_num = pre_list[ch];
        flag_zero = 0;
    else:
        flag_zero += 1;
    if flag_zero == 4 :
        if flag_num == pre_flag_num :
            pre_list[ch-3] = flag_num * -1;
            pre_list[ch] = flag_num * -1;
            pre_flag_num = flag_num * -1;
            for ch_temp in range(ch+1,length):
                pre_list[ch_temp] = pre_list[ch_temp] * -1
        else:
            pre_list[ch] = flag_num ;
        pre_flag_num = pre_list[ch];
        flag_zero = 0;
print(pre_list)

# flag_zero = 0;
# for ch in range (0,length):
#     if flag_zero == 2 :
#         if flag_num == pre_list[ch]:
#             flag_zero = 0
#             for ch_temp in range(ch-3, ch+1):
#                 pre_list[ch_temp] = 0;
#     if flag_zero == 3 :
#         if pre_list[ch] != 0 :
#             flag_zero = 0;
#             for ch_temp in range(ch-3, ch+1):
#                 pre_list[ch_temp] = 0;
#     if pre_list[ch] != 0 :
#         flag_num = pre_list[ch]
#         flag_zero = 0;
#     else:
#         flag_zero += 1;
#     pre_list[ch] = abs(pre_list[ch])


# if pre_list is store_list:
#     print(pre_list)


x = np.arange(len(pre_list))


pre_list = np.asarray(pre_list)

t = 0.5 * np.arange(len(pre_list) - 1)
t2 = np.arange(len(pre_list))

print(pre_list)
plt.step(t2, pre_list, 'r', linewidth = 1.5, where='post', label='data')
plt.xlim(-1, len(pre_list) + 1)
plt.ylim(-3, 3)
plt.title('HDB3 Encoding')
plt.show()
