# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper

# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper

# def make_underlined(function):
#     def wrapper():
#         return "<u>" + function() + "</u>"
#     return wrapper

inputs= eval(input())

def logging_decorator(fn):
	def wrapper(*args):
		print(f"you called {fn.__name__}{args}")
		result = fn(args[0],args[1],args[2])
		print(f"It returned: {result}")
	return wrapper

@logging_decorator
def a_function(a,b,c):
	return a*b*c

a_function(input[0],input[1],input[2])