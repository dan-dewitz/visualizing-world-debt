#%%

import matplotlib.pyplot as plt
# import matplotlib.ticker as tick
import pandas as pd
# import seaborn as sns
import numpy as np
% matplotlib inline


#%%

world = pd.read_csv("/Users/dan/Documents/talk/the_office_area_plot/data/world_debt.csv", index_col=None)
world.head()

#%%

world.dtypes

#%%



#%%

world_sorted_gdp = world.sort_values(by='gdp', ascending=True)

fig, ax = plt.subplots(1, figsize=(12, 10))

ax.barh(world_sorted_gdp.country, world_sorted_gdp.gdp)

# remove spines
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.show()

#%%

world_sorted_debt = world.sort_values(by='debt', ascending=True)

fig, ax = plt.subplots(1, figsize=(12, 10))

ax.barh(world_sorted_debt.country, world_sorted_debt.debt)

# remove spines
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.show()


#%%

world_sorted_debt.set_index('country')['debt'].sort_values().plot(kind='barh', figsize=(10, 8))
# plt.xlabel("Net Worth [$]", labelpad=16)
# plt.ylabel("Name", labelpad=16)
# plt.title("Net Worth of a Sample of University of Michigan Alumni", y=1.02, fontsize=22);







#%%

world_sorted_ratio = world.sort_values(by='debt_v_gdp', ascending=True)

fig, ax = plt.subplots(1, figsize=(12, 10))

ax.barh(world_sorted_ratio.country, world_sorted_ratio.debt_v_gdp)

# remove spines
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.show()

#%%



#%%



#%%


