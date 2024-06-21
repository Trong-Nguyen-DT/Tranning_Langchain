
def do_anything(func):
    def wrapper_do_anything():
        print("+++++++++++++++")
        return func("Nguyên")
    return wrapper_do_anything

@do_anything
def say_hi(name):
    print(f'Xin chào bạn {name}')
    
say_hi()