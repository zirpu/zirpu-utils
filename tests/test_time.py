
from zirpu.time import return_time_list, color_time_list, main
from colorama import Fore
import baseconv
import time
import datetime


ts=1440950558
expect_tl = ['14', '4', '0', '9', '5', '05', '58']
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]


def test_return_time_list():
    assert return_time_list(ts) == expect_tl
    
def test_color_time_list():
    cl = color_time_list(expect_tl)
    ecl = ["".join(i) for i in zip(colors, expect_tl, [Fore.RESET]*len(expect_tl))]
    for i in zip(cl, ecl):
        assert i[0] == i[1]

# this is a crap test.
def test_main():
    assert main([]) == None
    
##
