code = """import json
import pandas as pd
import re

# Load the large JSON results from previous query_db calls
with open(var_call_QErfi6whaTAVqNZagFl92PEN, 'r') as f:
    latest_packages = json.load(f)
with open(var_call_TnWuGBXs5FW5MqQks5o1e0le, 'r') as f:
    project_mappings = json.load(f)

# Create DataFrames
df_latest = pd.DataFrame(latest_packages)
df_map = pd.DataFrame(project_mappings)

# Normalize column names if necessary
# Ensure Name and Version present
for df in (df_latest, df_map):
    if 'Name' not in df.columns or 'Version' not in df.columns:
        raise ValueError('Expected columns Name and Version in both datasets')

# Keep only relevant columns from mapping
df_map_sub = df_map[['Name', 'Version', 'ProjectName', 'Project_Information']].copy()
# Deduplicate mapping rows, keeping first occurrence
df_map_sub = df_map_sub.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])
# Merge latest packages with mapping to get project info for the latest versions
merged = pd.merge(df_latest[['Name','Version']], df_map_sub, on=['Name','Version'], how='left')

# Function to extract stars from Project_Information text
star_patterns = [r"(\d[\d,]*)\s+stars",
                 r"stars count of\s*(\d[\d,]*)",
                 r"a stars count of\s*(\d[\d,]*)",
                 r"has\s*(\d[\d,]*)\s+stars",
                 r"has an? open issues count of\s*\d+,?\s*a stars count of\s*(\d[\d]*)",
                ]

def extract_stars(text):
    if not isinstance(text, str) or not text:
        return None
    for pat in star_patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1)
            num = num.replace(',', '')
            try:
                return int(num)
            except:
                continue
    # fallback: try to find any standalone number before 'stars'
    m = re.search(r"(\d[\d,]*)[^\n\r]{0,20}stars", text, flags=re.IGNORECASE)
    if m:
        num = m.group(1).replace(',', '')
        try:
            return int(num)
        except:
            return None
    return None

merged['stars'] = merged['Project_Information'].apply(extract_stars)

# Replace None with -1 to ensure they sort to bottom; we'll treat missing as 0 in output
merged['stars_fill'] = merged['stars'].fillna(-1).astype(int)

# Sort by stars descending, then remove entries with no project info (stars is None) if desired
top5 = merged.sort_values(['stars_fill','Name'], ascending=[False, True]).head(50)
# We want only those with a non-null stars; but if too few, include zeros. Filter to stars>=0
top5_with_stars = top5[top5['stars_fill']>=0].head(5)
if len(top5_with_stars) < 5:
    # include additional rows with 0 stars if needed
    remaining = merged[merged['stars_fill']<0].head(5 - len(top5_with_stars))
    top5_final = pd.concat([top5_with_stars, remaining], ignore_index=True)
else:
    top5_final = top5_with_stars

# Prepare output list of dicts
output = []
for _, row in top5_final.iterrows():
    output.append({
        'Name': row['Name'],
        'Version': row['Version'],
        'stars': None if pd.isna(row['stars']) else int(row['stars']),
        'ProjectName': row['ProjectName'] if 'ProjectName' in row and pd.notna(row['ProjectName']) else None,
        'Project_Information': row['Project_Information'] if 'Project_Information' in row and pd.notna(row['Project_Information']) else None
    })

# Print result in required format
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_QErfi6whaTAVqNZagFl92PEN': 'file_storage/call_QErfi6whaTAVqNZagFl92PEN.json', 'var_call_TnWuGBXs5FW5MqQks5o1e0le': 'file_storage/call_TnWuGBXs5FW5MqQks5o1e0le.json'}

exec(code, env_args)
