#%%
import pandas as pd

df = pd.read_csv("certificates.csv")

#%%
df.to_html("certificates.html")



# %%
