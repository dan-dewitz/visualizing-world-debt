import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
sns.set_style("whitegrid")

world = pd.read_csv("/Users/dan/Documents/talk/viz-the-debt/data/world_debt.csv", index_col=None)
ratio = pd.read_csv("/Users/dan/Documents/talk/viz-the-debt/data/gdp_v_debt.csv", index_col=None)

# scale debt to gdp ratio for bar charts so it aligns with
# the debt to gdp source for every country used in the bee swarm plot
ratio["ratio_float"] = ratio["value"].astype(float)
ratio["ratio"] = ratio["ratio_float"] * 0.001
del ratio["ratio_float"]

# DEBT bar chart
# --------------

sorted_debt = world.sort_values(by="debt", ascending=False)

fig, ax = plt.subplots(figsize=(12, 15))

color = [
    "steelblue" if country == "United States" else "grey"
    for country in sorted_debt.country
]

# convert trillions from long format to simple integer
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

plt.show()

# GDP bar chart
# -------------

sorted_gdp = world.sort_values(by="gdp", ascending=False)

fig, ax = plt.subplots(figsize=(12, 15))

color = [
    "steelblue" if country == "United States" else "grey"
    for country in sorted_gdp.country
]

# convert trillions from long format to simple integer
def trillions(x, pos):
    "The two args are the value and tick position"
    return "%1.0f" % (x * 1e-12)

formatter = FuncFormatter(trillions)
ax.xaxis.set_major_formatter(formatter)

sns.barplot(ax=ax, x="gdp", y="country", palette=color, data=sorted_gdp)

ax.set_ylabel("")
ax.set_xlabel("$ Trillion", fontsize=35)
ax.tick_params(labelsize=30)
sns.despine(ax=ax, fig=fig, right=True, bottom=True)

plt.show()

# Debt-to-GDP bar chart
# ---------------------

sorted_ratio = world.sort_values(by="debt_v_gdp", ascending=False)

fig, ax = plt.subplots(figsize=(12, 15))

color = [
    "steelblue" if country == "United States" else "grey"
    for country in sorted_ratio.country
]

sns.barplot(ax=ax, x=sorted_ratio.debt_v_gdp * 100, y=sorted_ratio.country, palette=color)

ax.set_ylabel("")
ax.set_xlabel("Debt / GDP", fontsize=35)
ax.tick_params(labelsize=30)
sns.despine(ax=ax, fig=fig, right=True, bottom=True)

plt.show()


# bee swarm plot
# --------------

# make bee swarm plot with box plot overlay
ax = sns.boxplot(y=ratio.ratio, color="grey", fliersize=0.0, linewidth=0.8, width=0.32)
ax = sns.swarmplot(y=ratio.ratio, color="0.25", alpha=0.8)

# make box plot body transparent
for patch in ax.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, 0.15))

plt.annotate(
    "United States",
    xy=(0, ratio["ratio"][ratio["country"] == "United States"]),
    xytext=(0.1, ratio["ratio"][ratio["country"] == "United States"] - 1),
    arrowprops={
        "facecolor": "steelblue",
        "width": 2,
        "shrink": 0.1,
        "connectionstyle": "angle3",
    },
    color = 'steelblue',
    fontsize=16,
)

plt.annotate(
    "Japan",
    xy=(0, ratio["ratio"][ratio["country"] == "Japan"]),
    xytext=(-0.2, ratio["ratio"][ratio["country"] == "Japan"] - 1),
    arrowprops={
        "facecolor": "black",
        "width": 2,
        "shrink": 0.05,
        "connectionstyle": "angle3",
    },
    fontsize=16,
)

plt.annotate(
    "China",
    xy=(0, ratio["ratio"][ratio["country"] == "China"]),
    xytext=(-0.3, ratio["ratio"][ratio["country"] == "China"] - 1),
    arrowprops={
        "facecolor": "black",
        "width": 2,
        "shrink": 0.01,
        "connectionstyle": "angle3",
    },
    fontsize=16,
)

plt.annotate(
    "United Kingdom",
    xy=(0, ratio["ratio"][ratio["country"] == "United Kingdom"]),
    xytext=(-0.4, ratio["ratio"][ratio["country"] == "United Kingdom"] - 1),
    arrowprops={"facecolor": "black", "width": 2, "connectionstyle": "angle3"},
    fontsize=16,
)


plt.annotate(
    "Canada",
    xy=(0, ratio["ratio"][ratio["country"] == "Canada"]),
    xytext=(0.15, ratio["ratio"][ratio["country"] == "Canada"] - 1),
    # Shrink the arrow to avoid occlusion
    arrowprops={
        "facecolor": "black",
        "width": 2,
        "shrink": 0.1,
        "connectionstyle": "angle3",
    },
    fontsize=16,
)

sns.despine(ax=ax, right=True, bottom=True, left=True, top=True)
ax.set_ylabel("Debt / GDP", fontsize=16)

plt.show()

