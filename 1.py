"""
Python Challenge
given string aaabbbsbsbsabsbasbkidifif
find out each letter is repeated how many times
"""


# Import the library
import collections


class Test(object):
    def __init__(self):
        self.my=[]

    def fomatted(self, my_str=''):

        """

        :param my_str:  its a string
        :return: Return a Dict
        """
        results = collections.Counter(my_string)
        return results

    def unique(self,my_dict = {}):
        """

        :param my_dict: its a Dict
        :return: List
        """
        for x in my_dict:
            self.my.append(x)
        return self.my


if __name__ == "__main__":

    my_string = "aaabbbsbsbsabsbasbkidifif"
    c = Test()
    out = c.fomatted(my_str=my_string)
    print(out)

    unique_l = c.unique(out)
    print(unique_l)


