"""

 This is a "hello world" program in Python


 Author:  Your Name 
 Email:   xxxx@xxx.x.xx.x
 Version: 1.0 
 Copyrghit: Your Name
 Liscence: ... <could be important> ...

"""
# use the typing module (introduced in python3.5)
from typing import Union

def do_some_calculation(x,y):
    some_calculation = (x + y)**2
    return some_calculation

def do_some_calculation_v2(x:int, y:int)-> int:
    """
    Perform some math calculation 

    :param x: value 1
    :param y: value 2
    :return: (x+y)**2

    """
    return (x+y)**2

def do_some_calculation_v3(x: Union[float, int], y: Union[float, int]) -> Union[float,int]:
    """
    Perform some math calculation 

    :param x: value 1
    :param y: value 2
    :return: (x+y)**2

    """
    return (x+y)**2


if __name__=='__main__':

    print(do_some_calculation(2.5,3.5))
    print(do_some_calculation_v2(2.5,3.5))
    print(do_some_calculation_v3(2.5,3.5))
    print("Done")

