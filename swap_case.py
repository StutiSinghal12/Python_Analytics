question--->You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  

def swap_case(s):
    m=""
    for letter in s:
        if letter.islower():
            m+=letter.upper()
        else:
            m+=letter.lower()
    return m
    

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
