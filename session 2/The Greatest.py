import sys
a = sys.stdin.readline()
new = a.split()
print(str(max(int(new[2]), int(new[1]), int(new[0]))) + " eh o maior")
