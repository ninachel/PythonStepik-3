from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
result = 0
for tag in soup.find_all('td'):
    result += int(tag.string)
print(result)
