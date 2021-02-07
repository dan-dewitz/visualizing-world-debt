# %%
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

# import matplotlib.ticker as tick
import pandas as pd
import seaborn as sns

# import numpy as np
# % matplotlib inline
# sns.set_context('paper')
sns.set_theme()
sns.despine()
# %%

world = pd.read_csv("/Users/dan/Documents/talk/viz-the-debt/data/world_debt.csv", index_col=None)
ratio = pd.read_csv("/Users/dan/Documents/talk/viz-the-debt/data/gdp_v_debt.csv", index_col=None)

ratio['ratio_float'] = ratio['value'].astype(float)
ratio['ratio'] = ratio['ratio_float'] * 0.001
del ratio['ratio_float']

# world['color'] = 'grey'
# world.loc[world['country'] == 'United States', 'color'] = 'blue'

print(ratio.dtypes)
print(world.head(25))
# sns.set(rc={'figure.figsize':(11.7,50)})
# sns.set(font_scale=1.2)

fig, ax = plt.subplots(figsize=(12, 15))
color = ['steelblue' if country == 'United States' else 'grey'
         for country in world.country]

print(color)

# %%
from matplotlib.ticker import FuncFormatter
def trillions(x, pos):
    'The two args are the value and tick position'
    return '%1.0f' % (x * 1e-12)
formatter = FuncFormatter(trillions)
ax.xaxis.set_major_formatter(formatter)
sorted_world = world.sort_values(by='debt', ascending=False)
sns.barplot(ax=ax, x='debt', y='country', palette=color, data=sorted_world)
# ax[0].set_color('darkred')

# .plot(kind='barh', figsize=(10, 12), fontsize=30, palette=world['color'])
ax.set_ylabel('')
ax.set_xlabel('$ Trillion', fontsize=35)
# plt.xlabel("Net Worth [$]", labelpad=16)
# plt.ylabel("Name", labelpad=16)
# plt.title("Net Worth of a Sample of University of Michigan Alumni", y=1.02, fontsize=22);

# print(sorted_world.head(25))
# print(sorted_world.dtypes)

# for ax in plt.gcf().axes:
#     print(ax.get_labelsize())
ax.tick_params(labelsize=30)


plt.show()
plt.savefig('debt-bar.png')
# %%

# hist = sns.histplot(data=ratio, x="ratio")
# plt.show()

# box = sns.boxplot(data=ratio, x="ratio")
# plt.show()


# sns.set_theme(style="whitegrid")
#
#
#
# swarm = sns.boxplot(y="ratio", data=ratio, color="grey")
# swarm = sns.swarmplot(y="ratio", data=ratio, color=".25", alpha=0.8)
#
# for patch in swarm.artists:
#     r, g, b, a = patch.get_facecolor()
#     patch.set_facecolor((r, g, b, .3))
#
# plt.annotate('United States',
#              xy = (0, ratio['ratio'][ratio['country'] == 'United States']),
#              xytext = (0.1, ratio['ratio'][ratio['country'] == 'United States'] - 1),
#              arrowprops = {'facecolor':'gray', 'width': 2, 'shrink': 0.05, 'connectionstyle':"angle3"},
#              backgroundcolor = 'white',
#              color = 'grey')
#
# plt.annotate('Japan',
#              xy = (0, ratio['ratio'][ratio['country'] == 'Japan']),
#              xytext = (-0.2, ratio['ratio'][ratio['country'] == 'Japan'] - 1),
#              arrowprops = {'facecolor':'gray', 'width': 2, 'shrink': 0.05, 'connectionstyle':"angle3"},
#              backgroundcolor = 'white',
#              color = 'grey')
#
# plt.annotate('China',
#              xy = (0, ratio['ratio'][ratio['country'] == 'China']),
#              xytext = (-0.3, ratio['ratio'][ratio['country'] == 'China'] - 1),
#              arrowprops = {'facecolor':'gray', 'width': 2, 'shrink': 0.05, 'connectionstyle':"angle3"},
#              backgroundcolor = 'white',
#              color = 'grey')
#
# plt.annotate('United Kingdom',
#              xy = (0, ratio['ratio'][ratio['country'] == 'United Kingdom']),
#              xytext = (-0.35, ratio['ratio'][ratio['country'] == 'United Kingdom'] - 1),
#              arrowprops = {'facecolor':'gray', 'width': 2, 'connectionstyle':"angle3"},
#              backgroundcolor = 'white',
#              color = 'grey')
#
#
# plt.annotate('Canada',
#              xy = (0, ratio['ratio'][ratio['country'] == 'Canada']),
#              xytext = (0.15, ratio['ratio'][ratio['country'] == 'Canada'] - 1),
#              # Shrink the arrow to avoid occlusion
#              arrowprops = {'facecolor':'gray', 'width': 2, 'shrink': 0.05, 'connectionstyle': "angle3"},
#              backgroundcolor = 'white',
#              color = 'grey')

# plt.show()
# plt.savefig('swarm.jpeg')
# %%
# world_sorted_gdp = world.sort_values(by='gdp', ascending=True)
#
# fig, ax = plt.subplots(1, figsize=(12, 10))
#
# ax.barh(world_sorted_gdp.country, world_sorted_gdp.gdp)
#
#
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
#
# plt.show()
