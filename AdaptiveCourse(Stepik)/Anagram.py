# a=input().lower()
# a=list(a)
# b=input().lower()
# b=list(b)
# # print(a)
# # print(b)
# f=0
# if(len(a)!=len(b)):
#     f=1
#     print('False')
# else:
#     while a:
#         try:
#             b.remove(a[0])
#         except ValueError:
#             f = 1
#             print('False')
#             break
#         a.remove(a[0])
#         # print(a)
#         # print(b)
# if(f==0):
#     print('True')

# def get_int(start_message, error_message, end_message):
#     a = input(start_message + '\n')
#     while True:
#         try:
#             if not (int(a)):
#                 raise ValueError
#             print(end_message)
#             return int(a)
#         except ValueError:
#             a = input(error_message + '\n')
# x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
# print(x)

a=[]
while True:
    a.append(input())
    if(a[len(a)-1]=='End'):
        break
for i in range (len(a)-1):
    print('Processing "'+a[i]+'" command...')
print('Good bye!')