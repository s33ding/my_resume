#%%
import pandas as pd

certificates = pd.read_csv("certificates.csv")
certificates = certificates.sort_values('date').reset_index(drop=True)
html_certificates = df.to_html() #README.md
# %%
