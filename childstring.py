# Solution to the "Common Child" problem: https://www.hackerrank.com/challenges/common-child/problem

def find_child(i1, i2, count):
    ch = s1[i1]
    found = s2[i2:].find(ch)
    if found != -1:
        if i1 < l - 1:
            return find_child(i1 + 1, found, count + 1)
        else:
            count += 1
    else:
        if i1 < l - 1:
            return find_child(i1 + 1, i2, count)
    return count

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    l = len(s1)
    max_length = 0

    rem = l
    while rem > max_length:
        max_length = max(max_length, find_child(l - rem, 0, 0))
        rem -= 1

    print(max_length)
