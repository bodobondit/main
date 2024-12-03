import  requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import webbrowser

# requests
r = requests.get('https://ya.ru')
print(r.headers)
str1 = r.content
query = {'text': 'питон'}
req = requests.get('https://yandex.ru/search/', params=query)
webbrowser.open(req.url)
res = requests.post('https://www.google.ru/', data = {'foo':3})

# pandas
data = { 'apples': [3, 2, 4, 1],
         'oranges': [0, 3, 7, 2]}
labels = ['June', 'Robert', 'Lily', 'David']
purchases = pd.DataFrame(data, index = labels)

print(purchases)
print(purchases.loc['Lily'])

print(purchases.head(1))
print(purchases.tail(1))

# matplotlib

x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
plt.plot(x, y,)

width = 0.35
fig, ax = plt.subplots()

ax.bar(labels, data['apples'], width, label = 'яблоки', color = 'green')
ax.bar(labels, data['oranges'], width, bottom = data['apples'], label = 'апельсины', color = 'orange')

ax.set_ylabel('Соотношение, в %')
ax.set_title('Распределение яблок и апельсинов')
ax.legend(loc='upper left', title='Фрукты')

plt.show()

#