code = """import json, re
import pandas as pd

# Load civic docs
path_docs = var_call_TUyzQDUuBNfMgCrDpx3Q4u3H
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Heuristic extraction: find lines that look like project titles, then capture nearby status and schedule.
# We'll scan each doc for sections and project blocks.

def extract_projects_from_text(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = []
    current_section = None

    # Patterns
    section_pat = re.compile(r'^(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started)\)\s*$', re.I)

    # A project title line is usually Title Case without trailing punctuation and not a bullet label
    def looks_like_title(ln):
        if not ln: return False
        if len(ln) > 120: return False
        if ln.lower().startswith(('to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion', 'project schedule', 'updates', 'project description', 'page ')):
            return False
        if ln.startswith(('(cid', 'agenda item', 'staff', 'city will', 'complete design', 'advertise', 'begin construction', 'complete construction')):
            return False
        if ':' in ln: return False
        # exclude headings
        if re.match(r'^(Public Works|Commission|Agenda Report)$', ln):
            return False
        # must contain a letter
        if not re.search(r'[A-Za-z]', ln): return False
        # Often project titles have multiple words
        if len(ln.split()) < 2: return False
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
            # capture up to next blank-title or section
            while j < len(lines):
                ln2 = lines[j]
                if section_pat.match(ln2):
                    break
                if looks_like_title(ln2) and ln2 != name and (j - i) > 1:
                    break
                block.append(ln2)
                j += 1
            block_text = "\n".join(block)

            # status inference
            status = None
            if re.search(r'Construction was completed', block_text, re.I) or re.search(r'Complete(d)? Construction', block_text, re.I) and re.search(r'2022', block_text):
                status = 'completed'
            if re.search(r'Project is currently under construction', block_text, re.I):
                status = 'construction'
            if re.search(r'preliminary design|finalize the design|Complete Design', block_text, re.I):
                status = status or 'design'
            if re.search(r'Project Description', block_text, re.I) and re.search(r'identified', block_text, re.I):
                status = status or 'not started'

            # schedule end time: look for 'Construction was completed <month> 2022' or 'Complete Construction: ...'
            et = None
            m = re.search(r'Construction was completed\s*,?\s*([A-Za-z]+\s+\d{4})', block_text, re.I)
            if m:
                et = m.group(1)
            else:
                m2 = re.search(r'Complete Construction:\s*([A-Za-z]+\s+\d{4}|\w+\s+\d{4}|\d{4})', block_text, re.I)
                if m2:
                    et = m2.group(1)
            # also notice: 'Construction was completed November 2022. Notice of completion filed January 2023'
            m3 = re.search(r'Construction was completed\s+([A-Za-z]+)\s+(\d{4})', block_text, re.I)
            if m3:
                et = f"{m3.group(1)} {m3.group(2)}"

            projects.append({
                'Project_Name': name,
                'section': current_section,
                'status': status,
                'et': et,
                'block_text': block_text
            })
            i = j
            continue
        i += 1
    return projects

all_projects = []
for d in docs:
    all_projects.extend(extract_projects_from_text(d.get('text','')))

proj_df = pd.DataFrame(all_projects)
# Identify park-related: name or block contains 'park' (including skate park) or section names referencing parks? Use keyword.
proj_df['is_park_related'] = proj_df['Project_Name'].str.contains(r'\bpark\b', case=False, na=False) | proj_df['block_text'].str.contains(r'\bpark\b', case=False, na=False)

# Completed in 2022: status completed and et contains 2022 OR block has 'completed' and 2022.
proj_df['completed_2022'] = (
    proj_df['is_park_related'] & (
        proj_df['block_text'].str.contains(r'completed', case=False, na=False) & proj_df['block_text'].str.contains(r'2022', case=False, na=False)
    )
)
completed_projects = proj_df.loc[proj_df['completed_2022'], ['Project_Name']].drop_duplicates()

# Load funding totals
path_fund = var_call_Jmi8UhdfHAynqpxuKZ7QYJhT
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

merged = completed_projects.merge(fund_df, on='Project_Name', how='left')
merged['Total_Amount'] = merged['Total_Amount'].fillna(0)

total = int(merged['Total_Amount'].sum())

out = {'total_funding_completed_2022_park_related': total, 'projects': merged.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YVr6YsGg98GUbY989wj39zDB': ['Funding'], 'var_call_44cSXvBgDbGLbNPd4odSmpfZ': ['civic_docs'], 'var_call_TUyzQDUuBNfMgCrDpx3Q4u3H': 'file_storage/call_TUyzQDUuBNfMgCrDpx3Q4u3H.json', 'var_call_Jmi8UhdfHAynqpxuKZ7QYJhT': 'file_storage/call_Jmi8UhdfHAynqpxuKZ7QYJhT.json'}

exec(code, env_args)
