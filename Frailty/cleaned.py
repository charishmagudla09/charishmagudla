import pandas as pd
df=pd.read_csv("//content/drive/MyDrive/Frailty/Frailty_Raw_Data.csv")
df['Frailty']=df['Frailty'].map({"Y":1,"N":0})
df
