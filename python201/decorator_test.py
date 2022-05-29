#decoration in python is modify function behavior without modify function
#it will execute before the function do for logging, permission check and verify something
#use by @name_of_decorator or logger(func)
#useful for slow down bruteforce or check that token still valid during performing attack
from datetime import datetime
import time

def logger(func):
    def wrapper():
        print("-"*50)
        print(">Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        func()
        print(">Execution completed {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("-"*50)
    return wrapper

@logger
def demo_function():
    print("Executing task!")
    time.sleep(3)
    print("Task completed!")

#demo_function()
#logger(demo_function)

#case that function need to pass some arguments
def logger_args(func):
    def wrapper(*args,**kwargs):
        print("-"*50)
        print(">Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        func(*args,**kwargs)
        print(">Execution completed {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("-"*50)
    return wrapper

@logger_args
def demo_function_args(sleep_time):
    print("Executing task!")
    time.sleep(sleep_time)
    print("Task completed!")

demo_function_args(2)