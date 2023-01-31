def _if(bool, func1, func2):
    if bool:
        return func1()
    else:
        return func2()



def truthy():
  print("True")

def falsey():
  print("False")

_if(True, truthy, falsey)
# prints 'True' to the consol
