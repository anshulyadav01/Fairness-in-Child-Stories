import pandas as pd
import seaborn as sns
import numpy as np
import itertools
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
# get_ipython().run_line_magic('', 'matplotlib inline')

# df_F = pd.read_csv('odd_ratio_female.csv')
# df_F.columns = ['Event','Odds_ratio_Female']
# df_F['Odds_ratio_Female'] = df_F['Odds_ratio_Female']*10
# df_M = pd.read_csv('odd_ratio_male.csv')
# df_M.columns = ['Event','Odds_ratio_Male']
# df_M = df_M[df_M.Odds_ratio_Male != 100]
# df_M['Odds_ratio_Male'] = df_M['Odds_ratio_Male']*10

# data_Male = df_M.sort_values(by=['Odds_ratio_Male'],ascending=False)
# data_Female = df_F.sort_values(by=['Odds_ratio_Female'],ascending=False)


# df_M_pl = data_Male[:10]
# df_M_pl.plot(kind="bar", x="Event", title="Top 10 Male Events", fontsize = 15, ylabel="Odds_Ratio")
# df_F_pl = data_Female[:10]
# df_F_pl.plot(kind="bar", x="Event", title="Top 10 female Events", fontsize = 15, ylabel="Odds_Ratio")


df_F_C = pd.read_csv('odds_ratio/odd_ratio_female_Children.csv')
df_F_C.columns = ['Event','Odds_ratio_Female_Children']
df_F_C['Odds_ratio_Female_Children'] = df_F_C['Odds_ratio_Female_Children'] * 10
df_M_C = pd.read_csv('odds_ratio/odd_ratio_male_Children.csv')
df_M_C.columns = ['Event','Odds_ratio_Male_Children']
df_M_C['Odds_ratio_Male_Children'] = df_M_C['Odds_ratio_Male_Children'] * 10

data_Children_Male = df_M_C.sort_values(by=['Odds_ratio_Male_Children'],ascending=False)
data_Children_Female = df_F_C.sort_values(by=['Odds_ratio_Female_Children'],ascending=False)

df_M_C_pl = data_Children_Male[:10]
df_M_C_pl.plot(kind="bar", x="Event", title="Story Genre:Children, Top 10 Male Events", fontsize = 15, ylabel="Odds_Ratio")
df_F_C_pl = data_Children_Female[:10]
df_F_C_pl.plot(kind="bar", x="Event", title="Story Genre:Children, Top 10 Female Events", fontsize = 15, ylabel="Odds_Ratio")


df_F_F = pd.read_csv('odds_ratio/odd_ratio_female_Fiction.csv')
df_F_F.columns = ['Event','Odds_ratio_Female_Fiction']
df_F_F['Odds_ratio_Female_Fiction'] = df_F_F['Odds_ratio_Female_Fiction'] * 10
df_M_F = pd.read_csv('odds_ratio/odd_ratio_male_Fiction.csv')
df_M_F.columns = ['Event','Odds_ratio_Male_Fiction']
df_M_F['Odds_ratio_Male_Fiction'] = df_M_F['Odds_ratio_Male_Fiction'] * 10

data_Fiction_Male = df_M_F.sort_values(by=['Odds_ratio_Male_Fiction'],ascending=False)
data_Fiction_Female = df_F_F.sort_values(by=['Odds_ratio_Female_Fiction'],ascending=False)

df_M_F_pl = data_Fiction_Male[:10]
df_M_F_pl.plot(kind="bar", x="Event", title="Story Genre:Fiction, Top 10 Male Events", fontsize = 15, ylabel="Odds_Ratio")
df_F_F_pl = data_Fiction_Female[:10]
df_F_F_pl.plot(kind="bar", x="Event", title="Story Genre:Fiction, Top 10 Female Events", fontsize = 15, ylabel="Odds_Ratio")

df_F_M_author = pd.read_csv('odds_ratio/odd_ratio_female_M_author.csv')
df_F_M_author.columns = ['Event','Odds_ratio_Female_M_author']
df_F_M_author['Odds_ratio_Female_M_author'] = df_F_M_author['Odds_ratio_Female_M_author'] * 10
df_M_M_author = pd.read_csv('odds_ratio/odd_ratio_male_M_author.csv')
df_M_M_author.columns = ['Event','Odds_ratio_Male_M_author']
df_M_M_author = df_M_M_author[df_M_M_author.Odds_ratio_Male_M_author != 100]
df_M_M_author['Odds_ratio_Male_M_author'] = df_M_M_author['Odds_ratio_Male_M_author'] * 10

data_Male_M_Author = df_M_M_author.sort_values(by=['Odds_ratio_Male_M_author'],ascending=False)
data_Female_M_Author = df_F_M_author.sort_values(by=['Odds_ratio_Female_M_author'],ascending=False)

df_M_M_author_pl = data_Male_M_Author[:10]
df_M_M_author_pl.plot(kind="bar", x="Event", title="Author Gender:Male, Top 10 Male Events", fontsize = 15, ylabel="Odds_Ratio")
df_F_M_author_pl = data_Female_M_Author[:10]
df_F_M_author_pl.plot(kind="bar", x="Event", title="Author Gender:Male, Top 10 Female Events", fontsize = 15, ylabel="Odds_Ratio")

df_F_F_author = pd.read_csv('odds_ratio/odd_ratio_female_F_author.csv')
df_F_F_author.columns = ['Event','Odds_ratio_Female_F_author']
df_F_F_author['Odds_ratio_Female_F_author'] = df_F_F_author['Odds_ratio_Female_F_author'] * 10
df_M_F_author = pd.read_csv('odds_ratio/odd_ratio_male_F_author.csv')
df_M_F_author.columns = ['Event','Odds_ratio_Male_F_author']
df_M_F_author['Odds_ratio_Male_F_author'] = df_M_F_author['Odds_ratio_Male_F_author'] * 10

data_Male_F_Author = df_M_F_author.sort_values(by=['Odds_ratio_Male_F_author'],ascending=False)
data_Female_F_Author = df_F_F_author.sort_values(by=['Odds_ratio_Female_F_author'],ascending=False)

df_M_F_author_pl = data_Male_F_Author[:10]
df_M_F_author_pl.plot(kind="bar", x="Event", title="Author Gender:Female, Top 10 Male Events", fontsize = 15, ylabel="Odds_Ratio")
df_F_F_author_pl = data_Female_F_Author[:10]
df_F_F_author_pl.plot(kind="bar", x="Event", title="Author Gender:Female, Top 10 Female Events", fontsize = 15, ylabel="Odds_Ratio")
plt.show()


