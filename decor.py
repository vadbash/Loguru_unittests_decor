import time

#main func
def logging(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        #time params
        prog_time = end - start
        #finish output
        print(f"Time = {round(prog_time, 10)} seconds")
        return res
    return wrapper

#decorator
@logging
def calc():
    print("hello hello")
calc()

