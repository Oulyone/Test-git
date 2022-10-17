def hello(time):
    for count in range(1,time):
        print('hello')
try:
    time = int(input('Enter how many time do you want to print hello: '))
except ValueError as err:
    print(err)

hello(time)