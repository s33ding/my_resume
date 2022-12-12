#%%
import pandas as pd

certificates = pd.read_csv("midia/certificates.csv")
certificates['date'] = certificates['date'].apply(lambda x: pd.to_datetime(x))
certificates = certificates.sort_values('date', ascending=False).reset_index(drop=True)
certificates.head()
#%%
#%%
certificates = certificates.to_html() #README.md
with open("teste.md",'w') as f:
    f.write(certificates)
# %%
