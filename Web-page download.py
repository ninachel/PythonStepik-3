# from urllib.request import urlopen

# html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
# print(str(html))

html = open('1.html', 'r').read()
count_py = html.count('Python')
count_c = html.count('C++')
print(count_py, count_c)

# import requests
#
# url = "https://decor-boutique.com"
# data = requests.get(url)
# print(data.text)
