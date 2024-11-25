def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
        print("Adding more sprinkles")
        return "Finished product is ready"
    return wrapper


# @decorator_func
# def bake():
#     print ("Cake is baking")


# @decorator_func
# def make_shoes(x,y):
#     result=x+y
#     print(f"Making {result} shoes")

# # print(bake())
# print(make_shoes(10, 5))

# decorated_cake=decorator_func(make_shoes(10, 5))
# print(decorated_cake())


import time 

# def timer(func):
#     def wrapper(*args, **kwargs):
#         print(f"{func.__name__} is sleeping")
#         start=time.time()
#         result=func(*args, **kwargs)
#         end=time.time()
#         duration=end-start
#         print (f"{func.__name__} took {duration} to sleep")
#     return wrapper

# @timer
# def alee():
#     time.sleep(3)
#     print("Alee is awake") 

# alee()


def memoizer(func):
    cache={}
    def wrapper(*item):
        if item in cache:
            return cache[item] 
        result=func(*item)
        cache[item]=result
        return result
    return wrapper

@memoizer
def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)

start=time.perf_counter_ns()
print(fib(20))
end=time.perf_counter_ns()-start
print(f"Fib took {end}")




























