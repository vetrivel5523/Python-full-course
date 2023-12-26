#ex-1
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()
#ex-2

def func_name(fname):
 print(fname)
func_name("kongu")
func_name("vetri")
func_name("ece")
    
#
def func_name(fname,lname):
    print(fname,lname)
func_name("vetri","welcome")
func_name("tech","welcome")
func_name("python","welcome")

#orbitary arguments
def func_name(*fname):
    print(fname)
func_name("vetri","welcome")
func_name("tech","welcome")
func_name("python","welcome")

#

