code = """import json
import pandas as pd
import re

# Load data from storage variables
with open(var_call_QErfi6whaTAVqNZagFl92PEN, 'r') as f:
    latest_packages = json.load(f)
with open(var_call_TnWuGBXs5FW5MqQks5o1e0le, 'r') as f:
    project_mappings = json.load(f)

# DataFrames
df_latest = pd.DataFrame(latest_packages)
df_map = pd.DataFrame(project_mappings)

# Ensure required cols
for df in (df_latest, df_map):
    if 'Name' not in df.columns or 'Version' not in df.columns:
        raise ValueError('Expected columns Name and Version in both datasets')

# Subset mapping
df_map_sub = df_map[['Name', 'Version', 'ProjectName', 'Project_Information']].copy()
df_map_sub = df_map_sub.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])

# Merge
merged = pd.merge(df_latest[['Name','Version']], df_map_sub, on=['Name','Version'], how='left')

# Extract stars with simple regex
def extract_stars(text):
    if not isinstance(text, str) or not text:
        return None
    m = re.search(r"(\d[\d,]*)\s*stars", text, flags=re.IGNORECASE)
    if m:
        num = m.group(1).replace(',', '')
        try:
            return int(num)
        except:
            return None
    # try alternative phrase
    m = re.search(r"stars count of\s*(\d[\d,]*)", text, flags=re.IGNORECASE)
    if m:
        num = m.group(1).replace(',', '')
        try:
            return int(num)
        except:
            return None
    return None

merged['stars'] = merged['Project_Information'].apply(extract_stars)
merged['stars_fill'] = merged['stars'].fillna(-1).astype(int)

# Sort and pick top 5 by stars (treat missing as -1)
top_sorted = merged.sort_values(['stars_fill','Name'], ascending=[False, True])
# Prefer rows with project info (stars>=0)
top_with = top_sorted[top_sorted['stars_fill']>=0].head(5)
if len(top_with) < 5:
    others = top_sorted.head(5)
    top5_final = others.head(5)
else:
    top5_final = top_with

# Build output
output = []
for _, row in top5_final.iterrows():
    output.append({
        'Name': row['Name'],
        'Version': row['Version'],
        'stars': None if pd.isna(row['stars']) else int(row['stars']),
        'ProjectName': row['ProjectName'] if 'ProjectName' in row and pd.notna(row['ProjectName']) else None,
        'Project_Information': row['Project_Information'] if 'Project_Information' in row and pd.notna(row['Project_Information']) else None
    })

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_QErfi6whaTAVqNZagFl92PEN': 'file_storage/call_QErfi6whaTAVqNZagFl92PEN.json', 'var_call_TnWuGBXs5FW5MqQks5o1e0le': 'file_storage/call_TnWuGBXs5FW5MqQks5o1e0le.json'}

exec(code, env_args)
