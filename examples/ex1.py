from DPT import *

s = [0.1, 2, -3.5, 10]

print("DPT of s[.]: ", DPT(s))
print("IDPT of L{s}: ", IDPT(DPT(s)))