import pandas as pd

df = pd.read_excel("/content/BROWNMAIL TEST FILE.xlsx")

# Print exact column names
for col in df.columns:
    print(repr(col))
