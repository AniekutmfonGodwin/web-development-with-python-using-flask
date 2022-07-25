
class MyError(Exception):
    message = dict(name="hello")


try:
    raise MyError()
except Exception as e:
    args,*others = e.args
    print("error args ",args)



    