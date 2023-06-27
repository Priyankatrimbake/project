import pandas as pd
df_today = pd.read_csv("20.06.2023.csv")
df_yesterday = pd.read_csv("20.06.2023 1.csv")
# print(df_today.head())
# print(df_yesterday.head())


today_tomor = pd.merge(df_today, df_yesterday, on ='name')


print(today_tomor)
# print(dir(mergedRes))