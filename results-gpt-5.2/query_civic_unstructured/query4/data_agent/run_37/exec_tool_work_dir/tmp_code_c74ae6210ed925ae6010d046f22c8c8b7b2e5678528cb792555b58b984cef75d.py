code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

docs = load_records(var_call_KfBgXKfHibTvwqQpobVdi35S)
fund = load_records(var_call_uCdMcTRamacrMJXchoeZhUdf)

fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Parse civic docs for project blocks and schedules
projects = []
# Common schedule line formats in docs: "Begin Construction: Fall 2023", "Advertise: Spring 2023" etc.
# We treat start as earliest season/year mention in schedule lines for the project, prioritizing "Begin Construction" then "Advertise" then any other schedule.
start_priority = ['Begin Construction', 'Begin construction', 'Start Construction', 'Advertise', 'Advertisement', 'Bid', 'Bids Due', 'Complete Design', 'Final Design', 'Design']

season_pat = r'(Spring|Summer|Fall|Winter)\s*,?\s*(20\d{2})'
month_pat = r'((Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))\s*(20\d{2})'

for d in docs:
    text = d.get('text','')
    # find sections for projects: project name line followed by bullets. We'll use funding project names as anchors.
    for pname in fund_df['Project_Name'].unique():
        if not pname or len(pname) < 5:
            continue
        # quick check
        if pname not in text:
            continue
        # capture a window around first occurrence
        idx = text.find(pname)
        window = text[idx: idx+1200]
        # find schedule lines
        schedule_lines = []
        for line in window.splitlines():
            if 'Schedule' in line or ':' in line:
                if any(k in line for k in ['Complete Design','Final Design','Advertise','Begin Construction','Begin construction','Complete Construction','Estimated Schedule','Project Schedule']):
                    schedule_lines.append(line.strip())
        # also include subsequent lines after "Project Schedule" headings
        if 'Project Schedule' in window or 'Estimated Schedule' in window:
            for line in window.splitlines():
                l=line.strip()
                if re.search(season_pat, l):
                    schedule_lines.append(l)
                elif re.search(month_pat, l):
                    schedule_lines.append(l)
        # Determine start string: look for priority keys
        start_str = None
        for key in start_priority:
            for l in schedule_lines:
                if key in l and re.search(season_pat, l):
                    m=re.search(season_pat, l)
                    start_str=f"{m.group(2)}-{m.group(1)}"
                    break
                if key in l and re.search(month_pat, l):
                    m=re.search(month_pat, l)
                    mon=m.group(2)
                    year=m.group(4)
                    start_str=f"{year}-{mon}"
                    break
            if start_str:
                break
        # fallback: any season in schedule lines
        if not start_str:
            m=re.search(season_pat, window)
            if m:
                start_str=f"{m.group(2)}-{m.group(1)}"
            else:
                m=re.search(month_pat, window)
                if m:
                    start_str=f"{m.group(4)}-{m.group(2)}"
        if start_str:
            projects.append({'Project_Name': pname, 'st': start_str})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

# Filter Spring 2022
spring_2022 = proj_df[proj_df['st'].str.contains('2022-Spring', na=False)]

# join funding totals
merged = spring_2022.merge(fund_df, on='Project_Name', how='left')
count = int(merged['Project_Name'].nunique())
total_funding = int(merged['total_amount'].fillna(0).sum())

out = {'projects_started_spring_2022': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KfBgXKfHibTvwqQpobVdi35S': 'file_storage/call_KfBgXKfHibTvwqQpobVdi35S.json', 'var_call_uCdMcTRamacrMJXchoeZhUdf': 'file_storage/call_uCdMcTRamacrMJXchoeZhUdf.json'}

exec(code, env_args)
