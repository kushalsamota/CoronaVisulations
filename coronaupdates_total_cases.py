import random
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']  = 12, 6
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5
plt.rcParams['axes.labelcolor'] = 'red'
plt.rcParams['axes.labelsize']  = 20
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['legend.fontsize'] = 20

url = "https://www.worldometers.info/coronavirus/"
page = requests.get(url)
data = pd.read_html(page.content)
df = data[0]
df.columns = ['Country', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths',
       'TotalRecovered', 'ActiveCases', 'Serious,Critical', 'Tot Cases/1M pop',
       'Deaths/1M pop', 'TotalTests', 'Tests/ 1M pop']
world = df[0:1]
india = df[df['Country'] == 'India']
df = df[1:-1]
df = df.sort_values('TotalCases', ascending=False)
choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
def make_color():
    ch = [ random.choice(choices) for i in range(6)]
    return "#"+"".join(ch)
colors = []
while len(colors) != 30:
    color = make_color()
    if color in colors:
        continue
    colors.append(color)
#df.iloc[0, 1] = 468895
fig, ax = plt.subplots()
ax.bar(df['Country'][:30], df['TotalCases'][:30], color=colors)
ax.set_xticklabels(df['Country'][:30],rotation=90)
ax.set_ylim([0, 175000])
ax.set_yticklabels(range(0,1800000, 200000))
ax.set_title("Infected Corona Patients Till Now", fontsize=25, color='red', pad=80)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlabel('Countries')
ax.set_ylabel("Total Cases")
c = 1
for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
    x  = patch.get_x() + 0.2
    h = patch.get_height()
    y = h + 10000 if c != 1 else 180000
    if c == 1:
        text = df.iloc[0, 1]
    else:
        text = h
    c += 1
    ax.text(x, y, text, fontsize=20, color=color, rotation=90)
    lb.set_color(color)

c = "#000000"
i = 6
for ylb in ax.get_yticklabels():
    c = list(c)
    if i <= 9:
        c[1] = str(i)
        c[2] = str(i)
    else:
        c[1] = chr(i+97-10)
        c[2] = chr(i+97-10)
    c = "".join(c)
    i += 1
    ylb.set_color(c)
plt.tight_layout()
plt.text(18, 150000, f"World - {world['TotalCases'][0]}", fontsize=20, color='blue')
plt.text(18, 180000, f"{time.strftime('%d %b, %Y %I:%M %p')}", fontsize=20, color="#333333")
plt.text(18, 130000, f"India - {india['TotalCases'].values[0]}", fontsize=20, color='green')
plt.show()
