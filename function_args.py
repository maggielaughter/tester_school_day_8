def foo(x,y, *args, **kwargs): #może być jeden argument, który ma dwie gwiazki - może być tylko jeden
    print(x, y)
    print(args)
    print(kwargs)

foo(1,2,20,30, first_name='Adam', age=100)