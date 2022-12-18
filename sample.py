# def outer():
#     outer_value = '外側の変数'
#     def inner():
#         nonlocal outer_value
#         outer_value = '内側の変数'
#         print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
#     inner()
#     print('outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

# outer()
        
#ジェネレータ関数
# def generator(max):
#     print('ジェネレータ作成')
#     for n in range(max):
#         yield n
#         print('yield実行')
        
# gen = generator(10)
# n = next(gen)
# print('n = {}'.format(n))
# n = next(gen)
# print('n = {}'.format(n))

# li = ['グー', 'チョキ', 'パー']
# input
#for in in 

# y = 10
# x = 0 if y > 0 else 1
# print(x)

# lambda_a = lambda x: x*x#引数x　返り値X*X

# print(lambda_a(10))

#条件付きlambda
# lambda_c = lambda x, y: y if x < y else x

# print(lambda_c(6, 4))

# def sample(a):
#     if a < 0:
#         return
#     else:
#         print(a)
#         sample(a-1)
        
# sample(10)

# def fib(n):
#     return 1 if n < 3 else fib(n-1)+fib(n-2)
    
# for x in range(1, 10):
#     print(fib(x))

# list_a = (1, 2, 3, 'a', 4, 'b')

# list_b = [x*2 for x in list_a if type(x) == int]
# print(list_b)

# list_c = [x for x in range(100) if x % 7 == 0]
# print(list_c)


# dict_a = {
#     'a':'Apple',
#     'b':'Banana'
# }

# list_c = [dict_a.get(x) for x in list_a if type(x)==str]
# print(list_c)


list_a = [1, 2, 3, 4, 5]
map_a = map(lambda x: x * 2, list_a)

for x in map_a:
    print(x)
    
