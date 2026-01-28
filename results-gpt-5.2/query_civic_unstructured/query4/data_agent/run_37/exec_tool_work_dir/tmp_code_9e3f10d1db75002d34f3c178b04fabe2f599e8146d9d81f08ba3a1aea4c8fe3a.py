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

projects = []
start_priority = ['Begin Construction', 'Begin construction', 'Start Construction', 'Advertise', 'Advertisement', 'Bid', 'Bids Due', 'Complete Design', 'Final Design', 'Design']

season_re = re.compile(r'(Spring|Summer|Fall|Winter)\s*,?\s*(20\d{2})')
month_re = re.compile(r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s*(20\d{2})')

fund_names = fund_df['Project_Name'].dropna().unique().tolist() if not fund_df.empty else []

for d in docs:
    text = d.get('text','') or ''
    for pname in fund_names:
        if len(pname) < 5 or pname not in text:
            continue
        idx = text.find(pname)
        window = text[idx: idx+1500]
        lines = [ln.strip() for ln in window.splitlines() if ln.strip()]
        schedule_lines = []
        for l in lines:
            if any(k in l for k in ['Complete Design','Final Design','Advertise','Begin Construction','Begin construction','Complete Construction','Estimated Schedule','Project Schedule']):
                schedule_lines.append(l)
        # include lines that look like schedule bullets with season/month
        for l in lines:
            if season_re.search(l) or month_re.search(l):
                schedule_lines.append(l)

        start_str = None
        for key in start_priority:
            for l in schedule_lines:
                if key in l:
                    m = season_re.search(l)
                    if m:
                        start_str = f"{m.group(2)}-{m.group(1)}"
                        break
                    m = month_re.search(l)
                    if m:
                        start_str = f"{m.group(2)}-{m.group(1)}"
                        break
            if start_str:
                break
        if not start_str:
            m = season_re.search(window)
            if m:
                start_str = f"{m.group(2)}-{m.group(1)}"
            else:
                m = month_re.search(window)
                if m:
                    start_str = f"{m.group(2)}-{m.group(1)}"

        if start_str:
            projects.append({'Project_Name': pname, 'st': start_str})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

spring_2022 = proj_df[proj_df['st'].str.contains('2022-Spring', na=False)]
merged = spring_2022.merge(fund_df, on='Project_Name', how='left')

count = int(merged['Project_Name'].nunique())
total_funding = int(merged['total_amount'].fillna(0).sum())

out = {'projects_started_spring_2022': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KfBgXKfHibTvwqQpobVdi35S': 'file_storage/call_KfBgXKfHibTvwqQpobVdi35S.json', 'var_call_uCdMcTRamacrMJXchoeZhUdf': 'file_storage/call_uCdMcTRamacrMJXchoeZhUdf.json'}

exec(code, env_args)
