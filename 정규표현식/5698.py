import re

text = "a*b"
text_mod = re.sub('*',".*",text)
print(text_mod)