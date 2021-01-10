import collections
import requests
import re

r = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html', verify=False)
html = r.text
regex = '<code>(.*?)</code>'
strings = sorted(re.findall(regex, html))
c = collections.Counter(strings)
lst = list(c.most_common())
max_count = lst[0][1]
result = []
for x in lst:
    if x[1] == max_count:
        result.append(x[0])
    else:
        break
print(' '.join(result))
