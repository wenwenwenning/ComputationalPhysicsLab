"""

 This is a "hello world" program in Python


 Author:  Your Name 
 Email:   xxxx@xxx.x.xx.x
 Version: 1.0 
 Copyrghit: Your Name
 Liscence: ... <could be important> ...

"""
import sys

def say_hello_to(name: str):
    """
    A function to print hello to someone


    :param name: the person to greet
    """
    print("Hello ",name)
    return

def say_hello_from_argv():
    """
    Print hello to someone from system arguments

    Alternatively, you could use the "argparse" module as well

    """
    if (len(sys.argv) != 2):
        print(len(sys.argv))
        print("This program requires one argument.")
        quit()
    my_name = sys.argv[1]
    print("Hello ",my_name, " !!")
    return


if __name__ == '__main__':

    # run the main function
    say_hello_to("Kuo-Chuan")
    
    # greeting from sys argv
    say_hello_from_argv()
