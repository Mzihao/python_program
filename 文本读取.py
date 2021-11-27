import re

with open('C://Users/admin/Desktop/小肩膀易语言POST JS网页全能班.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pat = '\n(.*?)\n'
content = re.compile(pat).findall(text)
print(len(content))
# for i in content:
#     print(str(id(i)) + '    ' + i)