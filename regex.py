import re


pattern = r"(ab)cdef"
s="abcdefghijklmn"

l = re.findall(pattern,s)
print(l)
regex = re.compile(pattern)
l=regex.findall(s)
print(l)