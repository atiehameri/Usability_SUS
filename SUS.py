import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir("/Users/macbook/Documents/pyhton/portfolio/SUS_Testing")
df = pd.read_excel("Test_result.xlsx")

df= df.iloc[:, 1:]
for i in range(len(df)):
    if i%2 == 0:
        df.iloc[i, :]= df.iloc[i, :]-1
    else:
        df.iloc[i, :] = 5- df.iloc[i, :]
df2 = df.transpose()
df["sum"] = (df.sum(axis = 1))/(df.shape[1]*5) *100

# score = (df.sum(axis = 0) *2.5).mean()
# print("The score is ", score)
print(df)


#### Plotting the bars
# plt.rcParams['font.family'] = "sans-serif"
index_list = ["Question 1", "Question 2","Question 3", "Question 4",
              "Question 5", "Question 6","Question 7", "Question 8",
              "Question 9", "Question 10"]

pos = []
for i in range(len(index_list)):
    pos.append(i)
width = 0.3

fig, axs = plt.subplots(2, figsize=(12, 12))

axs[0].set_ylim([0,100])
axs[0].set_xticks([(p + 1 * width)-0.3 for p in pos])
axs[0].bar(pos,  df["sum"], width , color='#735698', alpha = .5, linewidth=1 )
axs[0].set_xticklabels(index_list, rotation=45, fontsize=8, ha='right')
axs[0].grid(color='grey', axis='y', linestyle='-', linewidth=0.25, alpha=0.5)

bp = axs[1].boxplot(df2, patch_artist=True)

for box in bp['boxes']:
    # change outline color
    box.set( color="black", linewidth=.2)
    # change fill color
    box.set( facecolor = '#735698', alpha = .3 )

## change color and linewidth of the plot
for median in bp['medians']:
    median.set(color='black', linewidth=.5)

for flier in bp['fliers']:
    flier.set(marker='o', color='black', linewidth=.3, alpha = 1)

for cap in bp['caps']:
    cap.set(color='black', linewidth=.3)

for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=.3)




axs[1].set_xticklabels(index_list, rotation=45, fontsize=8, ha='right')
axs[1].grid(color='grey', axis='y', linestyle='-', linewidth=0.25, alpha=0.5)

plt.subplots_adjust(wspace=0.1, hspace=.3, bottom=.1, top = .95)

figname  = "sus.png"
if os.path.exists(figname):
    os.remove(figname)

plt.savefig(figname, dpi=180)
plt.show()