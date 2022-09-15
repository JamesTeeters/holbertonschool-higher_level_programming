#!/usr/bin/python3
"""inheritance"""

class MyList(list):
    """My_list"""
    def print_sorted(self):
        """print soreted list"""
        print(sorted(self))