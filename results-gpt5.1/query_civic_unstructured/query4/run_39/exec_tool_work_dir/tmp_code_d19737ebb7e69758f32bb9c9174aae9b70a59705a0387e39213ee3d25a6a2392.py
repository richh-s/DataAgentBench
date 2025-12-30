code = """import re, json, pandas as pd
from pathlib import Path

with open(var_call_DRuQOXASmn0qIo18F2mkmCjX, 'r') as f:
    civic_docs = json.load(f)

with open(var_call_p6NvxYJKWS8lh2aaNaSqjZu4, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

projects = []
for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if (('Project' in line or 'Improvements' in line or 'Repairs' in line or 'Park' in line or 'Facility' in line or 'Road' in line) and len(line.split()) < 15):
            window = '\n'.join(lines[i:i+15])
            m = re.search(r'Begin Construction: ([A-Za-z]+) (20\d{2})', window)
            if not m:
                m = re.search(r'Advertise: ([A-Za-z]+) (20\d{2})', window)
            if not m:
                m = re.search(r'Complete Design: ([A-Za-z]+) (20\d{2})', window)
            if m:
                month = m.group(1)
                year = m.group(2)
                date_str = year + '-' + month
                projects.append({'Project_Name': line, 'st': date_str})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','st'])

spring_months = {'March','April','May'}

def is_spring_2022(s):
    return (any(m in s for m in spring_months) and '2022' in s)

proj_df['season_2022_spring'] = proj_df['st'].apply(is_spring_2022)

spring_2022_projects = proj_df[proj_df['season_2022_spring']]

merged = pd.merge(spring_2022_projects, fund_df, on='Project_Name', how='inner')

result = {
    'projects_started_spring_2022_count': int(merged['Project_Name'].nunique()),
    'total_funding_spring_2022': int(merged['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_DRuQOXASmn0qIo18F2mkmCjX': 'file_storage/call_DRuQOXASmn0qIo18F2mkmCjX.json', 'var_call_p6NvxYJKWS8lh2aaNaSqjZu4': 'file_storage/call_p6NvxYJKWS8lh2aaNaSqjZu4.json'}

exec(code, env_args)
