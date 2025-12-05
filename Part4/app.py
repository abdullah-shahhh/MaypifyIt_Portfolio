import pandas as pd

raw = pd.read_csv("Coord1.csv")

raw['road_name'] = raw['road_name'].str.title()

# Add a new column "road_category"
raw['road_category'] = raw['type'].apply(
    lambda x: 'Main' if x == 'primary' else ('Secondary' if x == 'secondary' else 'Local')
)

raw.to_excel("enriched_data.xlsx", index=False)

print("Enriched dataset saved as enriched_data.xlsx")
