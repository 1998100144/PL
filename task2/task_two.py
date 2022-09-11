from sys import argv
a = sys.argv

m = sorted(a[1:])[len(a[1:]) // 2]
print(sum(abs(v - m) for v in a[1:]))
