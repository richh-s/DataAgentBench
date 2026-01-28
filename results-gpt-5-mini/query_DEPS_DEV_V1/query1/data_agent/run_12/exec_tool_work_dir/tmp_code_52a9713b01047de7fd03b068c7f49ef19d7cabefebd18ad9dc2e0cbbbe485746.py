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

# Reduce dataset sizes by focusing on relevant joins
latest_df = pd.DataFrame(latest)[['System','Name','Version']]
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']]
pinfo_df = pd.DataFrame(pinfo)[['Project_Information']]

# Merge latest package versions with project_packageversion to get ProjectName
merged = pd.merge(latest_df, ppv_df, on=['System','Name','Version'], how='left')

# Function to extract stars count from Project_Information text
star_regex = re.compile(r'([0-9][0-9,]*)\s*(?:stars|star|stars count of|stars count)', flags=re.IGNORECASE)
number_regex = re.compile(r'([0-9][0-9,]*)')

def extract_stars(text):
    if not isinstance(text, str):
        return None
    m = star_regex.search(text)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            pass
    m2 = re.search(r'stars count of\s*([0-9,]+)', text, flags=re.IGNORECASE)
    if m2:
        try:
            return int(m2.group(1).replace(',', ''))
        except:
            pass
    # fallback: find all numbers and return the largest
    nums = [int(n.replace(',', '')) for n in number_regex.findall(text)]
    if nums:
        return max(nums)
    return None

# Create a mapping from ProjectName to stars by scanning project_info entries
proj_to_stars = {}
for entry in pinfo:
    txt = entry.get('Project_Information')
    # try to extract repo path from the text with pattern 'project <owner/repo>' or 'The project owner/repo'
    repo_match = re.search(r'project\s+([a-zA-Z0-9_.\-]+/[a-zA-Z0-9_.\-]+)', txt, flags=re.IGNORECASE)
    if repo_match:
        repo = repo_match.group(1)
    else:
        # try another pattern: hosted on GitHub under the name owner/repo
        repo_match2 = re.search(r'hosted on GitHub under the name\s+([a-zA-Z0-9_.\-]+/[a-zA-Z0-9_.\-]+)', txt, flags=re.IGNORECASE)
        if repo_match2:
            repo = repo_match2.group(1)
        else:
            # fallback: try to pull first token like owner/repo
            maybe = re.search(r'([a-zA-Z0-9_.\-]+/[a-zA-Z0-9_.\-]+)', txt)
            repo = maybe.group(1) if maybe else None
    stars = extract_stars(txt)
    if repo:
        # keep max stars if duplicate repo entries
        prev = proj_to_stars.get(repo)
        if prev is None or (stars is not None and stars > prev):
            proj_to_stars[repo] = stars

# Now for merged entries, map their ProjectName to stars
merged['Stars'] = merged['ProjectName'].map(proj_to_stars)

# Aggregate by package name and version
agg = merged.groupby(['Name','Version'], dropna=False).agg({'Stars': 'max', 'ProjectName': lambda x: next((v for v in x if pd.notna(v)), None)}).reset_index()
agg['Stars_sort'] = agg['Stars'].fillna(-1)
agg_sorted = agg.sort_values(by='Stars_sort', ascending=False)

# Get top 5
top5 = agg_sorted.head(5)
out = []
for _, r in top5.iterrows():
    out.append({'Name': r['Name'], 'Version': r['Version'], 'Stars': None if pd.isna(r['Stars']) else int(r['Stars']), 'ProjectName': r['ProjectName']})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_D9cD9tpUgeY3J80yKR1gTvUh': ['packageinfo'], 'var_call_QMxIgVgYkwJESH3wQQo8lFOg': ['project_info', 'project_packageversion'], 'var_call_Al857qrlxezObN3hPmoLuP3N': 'file_storage/call_Al857qrlxezObN3hPmoLuP3N.json', 'var_call_iwgvIHpFwapoAmtDrnZltLgt': 'file_storage/call_iwgvIHpFwapoAmtDrnZltLgt.json', 'var_call_cPyvO7jlnS7E6s1V4hBQbrIT': 'file_storage/call_cPyvO7jlnS7E6s1V4hBQbrIT.json'}

exec(code, env_args)
