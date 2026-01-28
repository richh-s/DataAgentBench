code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_DRuQOXASmn0qIo18F2mkmCjX, 'r') as f:
    civic_docs = json.load(f)

# Load funding
with open(var_call_p6NvxYJKWS8lh2aaNaSqjZu4, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# naive project extraction: use lines that look like project titles followed by 'Updates' or 'Project Description'
projects = []
for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if ('Project' in line or 'Improvements' in line or 'Repairs' in line or 'Park' in line or 'Facility' in line or 'Road' in line) and len(line.split()) < 15:
            # look ahead for a schedule mentioning Begin Construction or similar with a season/year
            window = '\n'.join(lines[i:i+15])
            m = re.search(r'Begin Construction: ([A-Za-z]+) (20\d{2})', window)
            if not m:
                m = re.search(r'Advertise: ([A-Za-z]+) (20\d{2})', window)
            if not m:
                m = re.search(r'Complete Design: ([A-Za-z]+) (20\d{2})', window)
            if m:
                month = m.group(1)
                year = m.group(2)
                date_str = f"{year}-{month}"
                projects.append({'Project_Name': line, 'st': date_str})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','st'])

# map months to seasons
spring_months = {'March','April','May'}

proj_df['season_2022_spring'] = proj_df['st'].apply(lambda x: 1 if any(m in x for m in spring_months) and '2022' in x else 0)

spring_2022_projects = proj_df[proj_df['season_2022_spring'] == 1]

# join with funding on Project_Name (exact match)
merged = pd.merge(spring_2022_projects, fund_df, on='Project_Name', how='inner')

result = {
    'projects_started_spring_2022_count': int(merged['Project_Name'].nunique()),
    'total_funding_spring_2022': int(merged['Amount'].sum()),
    'project_names': sorted(merged['Project_Name'].unique().tolist())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_DRuQOXASmn0qIo18F2mkmCjX': 'file_storage/call_DRuQOXASmn0qIo18F2mkmCjX.json', 'var_call_p6NvxYJKWS8lh2aaNaSqjZu4': 'file_storage/call_p6NvxYJKWS8lh2aaNaSqjZu4.json'}

exec(code, env_args)
