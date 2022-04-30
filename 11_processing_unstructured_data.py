filname = 'uday.txt'
with open(filname) as fn:  

# Read each line
   ln = fn.readline()

# Keep count of lines
   lncnt = 1
   while ln:
       print(f"Line {lncnt}: {ln.strip()}")
       ln = fn.readline()
       lncnt += 1


''' 
            COUNTER WORDS
'''

from collections import Counter

with open(r"uday.txt") as cw:
   p = Counter(cw.read().split())
   print(p)