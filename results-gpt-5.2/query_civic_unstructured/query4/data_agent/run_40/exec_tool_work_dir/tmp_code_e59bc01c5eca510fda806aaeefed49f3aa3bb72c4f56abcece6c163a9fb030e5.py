code = """import json, re, pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str) and maybe_path_or_records.endswith('.json'):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

civic = load_records(var_call_m5cZetYeQU6Ei8417OtJG1Ac)
fund = load_records(var_call_ZcFusJIip3J5DyCA5UC5YRH0)

fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype(int)

# Collect all candidate project names from funding table
project_names = [p for p in fund_df['Project_Name'].dropna().astype(str).unique().tolist()]

# Build regex to find a project name as a whole line-ish. We'll search via simple substring to avoid huge regex.
# Determine which projects have 'Start' in Spring 2022 nearby.

def is_spring_2022_near(text, name):
    # quick check
    idx = text.find(name)
    if idx == -1:
        return False
    start = max(0, idx-800)
    end = min(len(text), idx+1200)
    window = text[start:end]
    wlow = window.lower()
    # must indicate start in spring 2022
    # patterns: 'Start ... Spring 2022', 'Begin ... Spring 2022', 'Start: Spring 2022', 'Begin Construction: Spring 2022', 'st: 2022-spring'
    patterns = [
        r'(start|begin|begins|start date|begin construction|construction start)\s*[:\-]?\s*(spring\s*2022|2022\s*[-/ ]\s*spring)',
        r'(spring\s*2022)'
    ]
    if not re.search(patterns[0], wlow, flags=re.I):
        # fallback: sometimes schedule lines like 'Advertise: Spring 2022' not start. Avoid those.
        # Accept if we see 'start' or 'begin' within 120 chars of 'Spring 2022'
        for m in re.finditer(r'spring\s*2022', wlow):
            a = max(0, m.start()-120)
            b = min(len(wlow), m.end()+40)
            if re.search(r'(start|begin|begins)', wlow[a:b]):
                return True
        return False
    # exclude if only advertise/complete design etc with spring 2022 but not start
    # if window contains 'advertise: spring 2022' but no start/begin near, already handled.
    return True

spring_projects = set()
for doc in civic:
    text = doc.get('text','') or ''
    if '2022' not in text or 'Spring' not in text and 'spring' not in text:
        continue
    for name in project_names:
        if name in text and is_spring_2022_near(text, name):
            spring_projects.add(name)

spring_df = fund_df[fund_df['Project_Name'].isin(sorted(spring_projects))]
count_projects = int(spring_df['Project_Name'].nunique())
total_funding = int(spring_df['Total_Amount'].sum())

out = {"projects_started_spring_2022": count_projects, "total_funding_usd": total_funding, "matched_project_names": sorted(spring_projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cgt6gggu5B6Rbv80acNNkfCM': ['Funding'], 'var_call_m5cZetYeQU6Ei8417OtJG1Ac': 'file_storage/call_m5cZetYeQU6Ei8417OtJG1Ac.json', 'var_call_ZcFusJIip3J5DyCA5UC5YRH0': 'file_storage/call_ZcFusJIip3J5DyCA5UC5YRH0.json'}

exec(code, env_args)
