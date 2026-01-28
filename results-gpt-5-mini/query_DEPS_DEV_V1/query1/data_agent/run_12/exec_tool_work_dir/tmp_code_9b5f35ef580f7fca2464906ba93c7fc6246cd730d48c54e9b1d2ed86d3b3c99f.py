code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_Al857qrlxezObN3hPmoLuP3N, 'r') as f:
    latest = json.load(f)
with open(var_call_iwgvIHpFwapoAmtDrnZltLgt, 'r') as f:
    ppv = json.load(f)
with open(var_call_cPyvO7jlnS7E6s1V4hBQbrIT, 'r') as f:
    pinfo = json.load(f)

latest_df = pd.DataFrame(latest)
ppv_df = pd.DataFrame(ppv)
pinfo_df = pd.DataFrame(pinfo)

# Merge latest package versions with project_packageversion to get ProjectName
merged = pd.merge(latest_df, ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')

# Function to extract stars count from Project_Information text
def extract_stars(text):
    if not isinstance(text, str):
        return None
    txt = text
    # find positions of 'star' occurrences
    star_positions = [m.start() for m in re.finditer(r'star', txt, flags=re.IGNORECASE)]
    # find all numbers with positions
    numbers = [(m.start(), m.group(1)) for m in re.finditer(r'([0-9][0-9,]*)', txt)]
    if not numbers:
        return None
    if star_positions:
        # find the number closest to any star position
        best = None
        best_dist = None
        for sp in star_positions:
            for pos, num in numbers:
                dist = abs(sp - pos)
                if best is None or dist < best_dist:
                    best = num
                    best_dist = dist
        # clean number
        try:
            return int(best.replace(',', ''))
        except:
            pass
    # fallback strategies: look for patterns
    patterns = [r'stars count of\s*([0-9,]+)', r'has garnered a total of\s*([0-9,]+)\s*stars', r'has\s*([0-9,]+)\s*stars', r'([0-9,]+)\s*stars']
    for pat in patterns:
        m = re.search(pat, txt, flags=re.IGNORECASE)
        if m:
            try:
                return int(m.group(1).replace(',', ''))
            except:
                pass
    # last fallback: return largest number in text (often stars or forks)
    nums = [int(n.replace(',', '')) for _, n in numbers]
    if nums:
        return max(nums)
    return None

# For each merged row, find the Project_Information text matching the ProjectName
results = []
for _, row in merged.iterrows():
    name = row.get('Name')
    version = row.get('Version')
    proj = row.get('ProjectName')
    stars = None
    matched_proj_info = None
    if isinstance(proj, str):
        # try to find a project_info entry that contains the project name
        mask = pinfo_df['Project_Information'].str.contains(proj, case=False, na=False)
        matches = pinfo_df[mask]
        if not matches.empty:
            # take first match
            matched_proj_info = matches.iloc[0]['Project_Information']
            stars = extract_stars(matched_proj_info)
    # append
    results.append({'Name': name, 'Version': version, 'ProjectName': proj, 'Stars': stars})

res_df = pd.DataFrame(results)
# For packages with multiple project mappings, take the max stars
agg = res_df.groupby(['Name','Version']).agg({'Stars': 'max', 'ProjectName': lambda x: x.dropna().iat[0] if any(x.dropna().tolist()) else None}).reset_index()
# Sort by Stars desc, treat None as -1
agg['Stars_sort'] = agg['Stars'].fillna(-1)
agg_sorted = agg.sort_values(by='Stars_sort', ascending=False)

top5 = agg_sorted.head(5)
# prepare output
out = []
for _, r in top5.iterrows():
    out.append({'Name': r['Name'], 'Version': r['Version'], 'Stars': None if pd.isna(r['Stars']) else int(r['Stars']), 'ProjectName': r['ProjectName']})

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_D9cD9tpUgeY3J80yKR1gTvUh': ['packageinfo'], 'var_call_QMxIgVgYkwJESH3wQQo8lFOg': ['project_info', 'project_packageversion'], 'var_call_Al857qrlxezObN3hPmoLuP3N': 'file_storage/call_Al857qrlxezObN3hPmoLuP3N.json', 'var_call_iwgvIHpFwapoAmtDrnZltLgt': 'file_storage/call_iwgvIHpFwapoAmtDrnZltLgt.json', 'var_call_cPyvO7jlnS7E6s1V4hBQbrIT': 'file_storage/call_cPyvO7jlnS7E6s1V4hBQbrIT.json'}

exec(code, env_args)
