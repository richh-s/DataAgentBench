code = """import json, re
import pandas as pd

path_docs = var_call_TUyzQDUuBNfMgCrDpx3Q4u3H
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_projects_from_text(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = []
    current_section = None

    section_pat = re.compile(r'^(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started)\)\s*$', re.I)

    def looks_like_title(ln):
        if not ln:
            return False
        if len(ln) > 120:
            return False
        low = ln.lower()
        if low.startswith(('to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion', 'project schedule', 'updates', 'project description', 'page ')):
            return False
        if low.startswith(('agenda item', 'staff', 'city will', 'complete design', 'advertise', 'begin construction', 'complete construction')):
            return False
        if ln.startswith('(cid'):
            return False
        if ':' in ln:
            return False
        if re.match(r'^(Public Works|Commission|Agenda Report)$', ln):
            return False
        if not re.search(r'[A-Za-z]', ln):
            return False
        if len(ln.split()) < 2:
            return False
        return True

    i = 0
    while i < len(lines):
        ln = lines[i]
        msec = section_pat.match(ln)
        if msec:
            current_section = f"{msec.group(1)} ({msec.group(2)})"
            i += 1
            continue

        if looks_like_title(ln) and current_section is not None:
            name = ln
            block = []
            j = i + 1
            while j < len(lines):
                ln2 = lines[j]
                if section_pat.match(ln2):
                    break
                if looks_like_title(ln2) and ln2 != name and (j - i) > 1:
                    break
                block.append(ln2)
                j += 1
            block_text = "\n".join(block)

            status = None
            if re.search(r'construction was completed', block_text, re.I):
                status = 'completed'
            elif re.search(r'project is currently under construction', block_text, re.I):
                status = 'construction'
            elif re.search(r'preliminary design|finalize the design|complete design', block_text, re.I):
                status = 'design'
            elif re.search(r'project description', block_text, re.I) and re.search(r'identified', block_text, re.I):
                status = 'not started'

            et = None
            m3 = re.search(r'construction was completed\s*,?\s*([A-Za-z]+)\s+(\d{4})', block_text, re.I)
            if m3:
                et = f"{m3.group(1)} {m3.group(2)}"
            else:
                m2 = re.search(r'complete construction:\s*([A-Za-z]+\s+\d{4}|\w+\s+\d{4}|\d{4})', block_text, re.I)
                if m2:
                    et = m2.group(1)

            projects.append({'Project_Name': name, 'section': current_section, 'status': status, 'et': et, 'block_text': block_text})
            i = j
            continue
        i += 1

    return projects

all_projects = []
for d in docs:
    all_projects.extend(extract_projects_from_text(d.get('text', '')))

proj_df = pd.DataFrame(all_projects)
if proj_df.empty:
    completed_projects = pd.DataFrame(columns=['Project_Name'])
else:
    proj_df['is_park_related'] = proj_df['Project_Name'].str.contains(r'\bpark\b', case=False, na=False) | proj_df['block_text'].str.contains(r'\bpark\b', case=False, na=False)
    proj_df['completed_2022'] = proj_df['is_park_related'] & proj_df['block_text'].str.contains(r'construction was completed', case=False, na=False) & proj_df['block_text'].str.contains('2022', case=False, na=False)
    completed_projects = proj_df.loc[proj_df['completed_2022'], ['Project_Name']].drop_duplicates()

path_fund = var_call_Jmi8UhdfHAynqpxuKZ7QYJhT
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

merged = completed_projects.merge(fund_df, on='Project_Name', how='left')
if not merged.empty:
    merged['Total_Amount'] = merged['Total_Amount'].fillna(0)
    total = int(merged['Total_Amount'].sum())
else:
    total = 0

out = {'total_funding_completed_2022_park_related': total, 'projects': merged.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YVr6YsGg98GUbY989wj39zDB': ['Funding'], 'var_call_44cSXvBgDbGLbNPd4odSmpfZ': ['civic_docs'], 'var_call_TUyzQDUuBNfMgCrDpx3Q4u3H': 'file_storage/call_TUyzQDUuBNfMgCrDpx3Q4u3H.json', 'var_call_Jmi8UhdfHAynqpxuKZ7QYJhT': 'file_storage/call_Jmi8UhdfHAynqpxuKZ7QYJhT.json'}

exec(code, env_args)
