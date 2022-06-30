question-->You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Sample Input

this is a string   
Sample Output

this-is-a-string

---****-------
def split_and_join(line):
        res1=line.split(" ")
        res="-".join(res1)
        return res
    # write your code here

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
