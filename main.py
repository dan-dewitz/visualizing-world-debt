# %%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams
import seaborn as sns

# %%
world = pd.read_csv(
    "/Users/dan/Documents/talk/viz-the-debt/data/world_debt.csv", index_col=None
)
ratio = pd.read_csv(
    "/Users/dan/Documents/talk/viz-the-debt/data/gdp_v_debt.csv", index_col=None
)

ratio["ratio_float"] = ratio["value"].astype(float)
ratio["ratio"] = ratio["ratio_float"] * 0.001
del ratio["ratio_float"]
print(ratio.head())

#%%
# DEBT
sorted_debt = world.sort_values(by="debt", ascending=False)

sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12, 15))

color = [
    "steelblue" if country == "United States" else "grey"
    for country in sorted_debt.country
]


def trillions(x, pos):
    "The two args are the value and tick position"
    return "%1.0f" % (x * 1e-12)


formatter = FuncFormatter(trillions)
ax.xaxis.set_major_formatter(formatter)

sns.barplot(ax=ax, x="debt", y="country", palette=color, data=sorted_debt)

ax.set_ylabel("")
ax.set_xlabel("$ Trillion", fontsize=35)
ax.tick_params(labelsize=30)
sns.despine(ax=ax, fig=fig, right=True, bottom=True)

# plt.show()
# plt.savefig('debt-bar.png')


#%%

# GDP
# ratio_chart = ratio[ratio.country.isin(world.country)]

print(sorted_ratio.head())
# print(world.head())
# print(ratio_chart.head(100))


#%%
sns.set_style("whitegrid")
sorted_ratio = world.sort_values(by="debt_v_gdp", ascending=False)

fig, ax = plt.subplots(figsize=(12, 15))

color = [
    "steelblue" if country == "United States" else "grey"
    for country in sorted_ratio.country
]


# def trillions(x, pos):
#     'The two args are the value and tick position'
#     return '%1.0f' % (x * 1e-12)
#
# formatter = FuncFormatter(trillions)
# ax.xaxis.set_major_formatter(formatter)

sns.barplot(
    ax=ax, x=sorted_ratio.debt_v_gdp * 100, y=sorted_ratio.country, palette=color
)

ax.set_ylabel("")
ax.set_xlabel("Debt / GDP", fontsize=35)
ax.tick_params(labelsize=30)
sns.despine(ax=ax, fig=fig, right=True, bottom=True)

# plt.show()
plt.savefig("debt-bar.png")

#%%

# DEBT-to-GDP ratio
sorted_debt = world.sort_values(by="debt", ascending=False)

sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12, 15))

color = [
    "steelblue" if country == "United States" else "grey"
    for country in sorted_debt.country
]


def trillions(x, pos):
    "The two args are the value and tick position"
    return "%1.0f" % (x * 1e-12)


formatter = FuncFormatter(trillions)
ax.xaxis.set_major_formatter(formatter)

sns.barplot(ax=ax, x="debt", y="country", palette=color, data=sorted_debt)

ax.set_ylabel("")
ax.set_xlabel("$ Trillion", fontsize=35)
ax.tick_params(labelsize=30)
sns.despine(ax=ax, fig=fig, right=True, bottom=True)

# plt.show()
# plt.savefig('debt-bar.png')


#%%


#%%


sns.set_theme(style="whitegrid")

color = ["steelblue" if country == "United States"
            else "grey" for country in ratio.country]


ratio["color"] = 1
ratio.loc[ratio["country"] == "United States", "color"] = 0
# print(ratio.head(25))
print(color)
# 'steelblue'
#%%

# fig, ax = plt.subplots(figsize=(12, 10))
# rcParams["figure.figsize"] = 11.7, 8.27
ax = sns.boxplot(y=ratio.ratio, color="grey", fliersize=0.0, linewidth=0.5)
ax = sns.swarmplot(y=ratio.ratio, color="0.25", alpha=0.8)

for patch in ax.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, 0.3))

plt.annotate(
    "United States",
    xy=(0, ratio["ratio"][ratio["country"] == "United States"]),
    xytext=(0.1, ratio["ratio"][ratio["country"] == "United States"] - 1),
    arrowprops={
        "facecolor": "gray",
        "width": 2,
        "shrink": 0.05,
        "connectionstyle": "angle3",
    },
    # backgroundcolor = 'white',
    # color = 'grey',
    fontsize=16,
)

plt.annotate(
    "Japan",
    xy=(0, ratio["ratio"][ratio["country"] == "Japan"]),
    xytext=(-0.2, ratio["ratio"][ratio["country"] == "Japan"] - 1),
    arrowprops={
        "facecolor": "gray",
        "width": 2,
        "shrink": 0.05,
        "connectionstyle": "angle3",
    },
    # backgroundcolor = 'white',
    # color = 'grey',
    fontsize=16,
)

plt.annotate(
    "China",
    xy=(0, ratio["ratio"][ratio["country"] == "China"]),
    xytext=(-0.3, ratio["ratio"][ratio["country"] == "China"] - 1),
    arrowprops={
        "facecolor": "gray",
        "width": 2,
        "shrink": 0.05,
        "connectionstyle": "angle3",
    },
    # backgroundcolor = 'white',
    # color = 'grey',
    fontsize=16,
)

plt.annotate(
    "United Kingdom",
    xy=(0, ratio["ratio"][ratio["country"] == "United Kingdom"]),
    xytext=(-0.35, ratio["ratio"][ratio["country"] == "United Kingdom"] - 1),
    arrowprops={"facecolor": "gray", "width": 2, "connectionstyle": "angle3"},
    # backgroundcolor = 'white',
    # color = 'grey',
    fontsize=16,
)


plt.annotate(
    "Canada",
    xy=(0, ratio["ratio"][ratio["country"] == "Canada"]),
    xytext=(0.15, ratio["ratio"][ratio["country"] == "Canada"] - 1),
    # Shrink the arrow to avoid occlusion
    arrowprops={
        "facecolor": "gray",
        "width": 2,
        "shrink": 0.05,
        "connectionstyle": "angle3",
    },
    # backgroundcolor = 'white',
    # color = 'grey',
    fontsize=16,
)


sns.despine(ax=ax, right=True, bottom=True, left=True, top=True)

ax.set_ylabel("Debt / GDP", fontsize=16)
plt.show()
# plt.savefig('swarm.jpeg')


#%%
world_sorted_gdp = world.sort_values(by="gdp", ascending=True)

fig, ax = plt.subplots(1, figsize=(12, 10))

ax.barh(world_sorted_gdp.country, world_sorted_gdp.gdp)


ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

plt.show()

#%%
