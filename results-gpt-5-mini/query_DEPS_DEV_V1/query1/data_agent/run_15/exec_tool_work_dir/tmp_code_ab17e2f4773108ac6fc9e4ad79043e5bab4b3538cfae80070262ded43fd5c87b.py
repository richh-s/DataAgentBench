code = """import json
import pandas as pd

# Load results from previous tool calls; these are file paths
path_latest = var_call_1NNWI9aTYRtJBI5r5wQdtLqQ
path_pp = var_call_EIZTDiEEemORFQSBm0ZwJyVH

with open(path_latest, 'r') as f:
    latest = json.load(f)
with open(path_pp, 'r') as f:
    pp = json.load(f)

df_latest = pd.DataFrame(latest)
df_pp = pd.DataFrame(pp)

# Keep only relevant columns
if 'Name' not in df_latest.columns or 'Version' not in df_latest.columns:
    raise ValueError('Expected Name and Version in latest packages')

# Merge to get project info for latest package versions
merged = pd.merge(df_latest, df_pp, on=['Name', 'Version'], how='left')

# Function to extract star counts from Project_Information
import re

def extract_stars(text):
    if text is None:
        return None
    s = str(text)
    if s.strip().lower() in ('none', 'null', ''):
        return None
    # Try patterns that mention stars near numbers
    patterns = [r'([0-9][0-9,]*)\s*(?:stars|star|stargazers)',
                r'(?:stars[:\s]+)([0-9][0-9,]*)',
                r'([0-9][0-9,]*)\s*(?:★|⭐)']
    for pat in patterns:
        m = re.search(pat, s, flags=re.IGNORECASE)
        if m:
            num = m.group(1)
            return int(num.replace(',', ''))
    # If no explicit 'stars' mention, try to find numbers and heuristically pick one
    nums = re.findall(r'([0-9][0-9,]{0,})', s)
    nums = [int(n.replace(',', '')) for n in nums]
    if not nums:
        return None
    # If the string contains the word 'fork', try to prefer a different number than forks
    if 'fork' in s.lower() and len(nums) >= 2:
        # assume format like "1,234 stars • 123 forks" -> stars likely the larger
        return max(nums)
    # Otherwise return the largest number as best guess
    return max(nums)

# Apply extraction
merged['Stars'] = merged['Project_Information'].apply(extract_stars)

# For clarity, fill missing ProjectName with None
merged['ProjectName'] = merged.get('ProjectName')

# Now select top 5 by Stars (treat None as 0)
merged['Stars_for_sort'] = merged['Stars'].fillna(0)

# Drop duplicates by Name to ensure distinct packages (should already be distinct)
merged_unique = merged.drop_duplicates(subset=['Name'])

top5 = merged_unique.sort_values(by='Stars_for_sort', ascending=False).head(5)

# Prepare output
result = []
for _, row in top5.iterrows():
    result.append({
        'Name': row['Name'],
        'Version': row['Version'],
        'ProjectName': row.get('ProjectName') if row.get('ProjectName') not in (None, 'None') else None,
        'Stars': int(row['Stars_for_sort']) if not pd.isna(row['Stars_for_sort']) else None,
        'Project_Information': row.get('Project_Information')
    })

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1NNWI9aTYRtJBI5r5wQdtLqQ': 'file_storage/call_1NNWI9aTYRtJBI5r5wQdtLqQ.json', 'var_call_dEbQyy7KC1XWBOqKtgUgdPzy': ['project_info', 'project_packageversion'], 'var_call_EIZTDiEEemORFQSBm0ZwJyVH': 'file_storage/call_EIZTDiEEemORFQSBm0ZwJyVH.json'}

exec(code, env_args)
