# age = 18
# print(f'{age=}')

# msg = ' ABC '
# print(msg.lstrip())

# msg = 'ABCDEABC'

# msg_r = msg.replace('ABC', 'FFF', 1)
# print(msg_r)

# msg = 'hello world'
# print(msg.capitalize())

# name = 'jiro'
# print(f'hello {name}')


# msg = 'ABCDEABC'

# print(msg.index('ABC'))
# print(msg.rindex('ABC'))

# list_a = [1,2,3,4,5]
# # list_a.remove(3)
# # print(list_a)
# # # list_b = list_a[:3]

# # # list_a.clear()
# # # print(list_a)

# # value = list_a.pop()
# # print(list_a, value)

# print(list_a)
# list_b = list_a.copy()
# list_b[0] = 'AA'
# print(list_a)

#辞書型
# car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

# print(car.get('bran', 12))

# print(car.keys())
# print(car.values())
# print(car.items())

# for key, value in car.items():
#     print('key:{}, value:{}'.format(key, value))

# if 'brand' in car:
#     print('carのブランドは{}'.format(car['brand']))



# car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

# tmp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

# car.update(tmp_car)
# print(car)

# value = car.popitem()
# print(car)
# print(value)

# car.clear()
# print(car)

# pos = (135, 35)

# countries = {pos: 'Japan'}

# print(countries.get((135,35)))

# class ClassA():
    
#     def __init__(self, a):
#         self.a = a
    
#     def __bool__(self):
#         if self.a = 'a':
#             return True
#         return False

# if all((True, 'a'=='a')):
#     print('allの中の処理')

# human = {
#     'name': 'taro',
#     'age': 20,
#     'gender': 'man'
# }

# for h in human:
#     print(h, human.get(h))#get()の括弧内にはkeyを入れる

# #enumerate関数　配列の中の値とインデックスを同時に取得する
# sample = ['A', 'B', 'C']
# for index, value in enumerate(sample):
#     print(index)
#     print(value)
    
# #zip関数　二つの配列の中の値を同時に取得する
# for a, b in zip(list1, list2):

# fruits = ['grape', 'Pine', 'Apple']

# for index, value in enumerate(fruits):
#     print('index = {}'.format(index))
#     print('value = {}'.format(value))
    
# classA = ['taro', 'hanako', 'jiro']
# classB = ['katsuo', 'wakame', 'taro']

# for a, b in zip(classA, classB):
#     print(f'classA = {a}')
#     print(f'classB = {b}')

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)
# else:
#     print('ループ処理終了')
    
# num = 0
# while num < 10:
#     if num == 5:
#         num += 1
#         continue
#     # if num == 7:
#     #     break
#     print(num)
#     num +=1

# else:
#     print('ループ処理終了')

#セイウチ演算子 変数の代入と変数の使用を同時に実行できる

# if (n := 10) > 5:
#     print('5より大きい: {}'.format(n))
    
# n = 0
# while (n := n + 1) < 10:
#     print(n)

#例外処理 実行時に発生するエラー（実行時エラー）を制御して処理を行う
# try:
#     b = [10,20,30]
#     a = 10/0
#     # b = [0, 2, 4]
#     # b.method_a()
# except ZeroDivisionError as e:
#     import traceback
#     traceback.print_exc()
#     # print(e, type(e))
#     pass
# except Exception as e:
#     print('Exception', e, type(e))
# else:
#     print('else処理')
# finally:
#     print('finally処理')
# print('処理が完了しました')

#raise 例外自作

# class MyException(Exception):
#     pass

# def devide(a, b):
#     if b == 0:
#         raise MyException('0では割り切れません')
#     else:
#         return a/b

# try:
#     c = devide(10, 0)
# except Exception as e:
#     print(e, type(e))

# def print_hello():
#     print('hello')
    
# print_hello()

# def num_max(a: int, b: int):
#     print('a = {}, b = {}'.format(a,b))
#     if a>b:
#         return a
#     else:
#         return b
    
# print(num_max(10,20))

# def sample(arg1, **arg2):
#     print('arg1 = {}, arg2  {}'.format(arg1, arg2))
#     print(type(arg2))
    
# sample(1, name = 'taro', age = 20)

x = 1
print(x)