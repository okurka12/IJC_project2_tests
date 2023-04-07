import sys
a = input()
if len(sys.argv) == 3:
    n = int(sys.argv[2])
    if n < 0:
        print("cauky jak je", file=sys.stderr)
        sys.exit(1)
else:
    n = 10

for i in range(n):
    print(127*"a")


print("ahoj", file=sys.stderr)
sys.exit(1)