code = """import json, re
import pandas as pd

# Load funding per project
funding_path = var_call_nHRMYqSVnORVdcf9fNlGp5zY
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Load civic docs
docs_path = var_call_ES96BvPmC6nu2gxnR5QnBRTK
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

project_to_start_years = {}

def norm_name(s):
    return re.sub(r"\s+", " ", s.strip())

for d in docs:
    text = d.get('text','') or ''
    # Focus on Disaster Recovery section when present
    in_disaster = False
    current_project = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        low = line.lower()
        if 'disaster recovery projects' in low:
            in_disaster = True
            current_project = None
            continue
        # stop when next major section begins
        if in_disaster and ('capital improvement projects' in low or 'recommended action' in low or 'public works quarterly update' in low):
            # not necessarily stop, but if capital appears after disaster, end disaster section
            if 'capital improvement projects' in low:
                in_disaster = False
                current_project = None
            # else keep
        if not in_disaster:
            continue

        # identify a project line: in these docs, project names are standalone lines without colon and not bullets
        # We'll accept lines that are Title Case-ish and not starting with common labels.
        if any(low.startswith(x) for x in ['updates', 'project schedule', 'estimated schedule', 'project description', 'complete design', 'advertise', 'begin construction', 'begin construction:', 'complete construction', 'final design', 'project updates']):
            continue
        if low.startswith('page ' ) or low.startswith('agenda item'):
            continue
        if line.startswith('(cid:'):
            continue

        # If line contains "Project Schedule" etc skip; else treat as project name if it doesn't contain ':' and length reasonable
        if ':' not in line and len(line) <= 120 and not re.search(r"\b(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})\b", line):
            # likely project name
            current_project = norm_name(line)
            continue

        # parse schedule lines for start year
        if current_project:
            m = re.search(r"\b(Begin Construction|Start|Begin|Construction Start)\s*:\s*([A-Za-z]+\s+)?(\d{4})\b", line, flags=re.I)
            if not m:
                # also handle like 'Begin Construction: Fall 2023' already; year at end
                m2 = re.search(r"\b(Begin Construction|Start)\b.*?(\d{4})\b", line, flags=re.I)
                if m2:
                    year = m2.group(2)
                else:
                    year = None
            else:
                year = m.group(3)
            if year:
                project_to_start_years.setdefault(current_project,set()).add(int(year))

# Determine disaster projects that started in 2022
# Some projects may not have explicit disaster section parsing; fall back to heuristic: project name includes FEMA/CalOES/CalJPIA and any line 'Begin Construction' has 2022.
# We'll just use extracted ones; if none, compute based on names containing FEMA etc with begin construction 2022 from entire text.

disaster_started_2022 = set([p for p,yrs in project_to_start_years.items() if 2022 in yrs])

if not disaster_started_2022:
    # heuristic parse entire docs for begin construction 2022 lines near project names that include FEMA/CalOES/CalJPIA
    key_terms = re.compile(r"\((?:FEMA|CalOES|CalJPIA)[^)]*\)", re.I)
    for d in docs:
        lines = [ln.strip() for ln in (d.get('text','') or '').splitlines()]
        for i, line in enumerate(lines):
            if key_terms.search(line) and ':' not in line and len(line)<=120:
                # look ahead a few lines for begin construction 2022
                window = ' '.join(lines[i:i+15])
                if re.search(r"Begin Construction\s*:\s*.*\b2022\b", window, re.I):
                    disaster_started_2022.add(norm_name(line))

# Sum funding for these projects
funding_df = pd.DataFrame(funding_records)
# convert total_amount to int
funding_df['total_amount'] = funding_df['total_amount'].astype(int)

sel = funding_df[funding_df['Project_Name'].isin(disaster_started_2022)]

total = int(sel['total_amount'].sum())

out = {
    "total_funding": total,
    "project_count": int(len(disaster_started_2022)),
    "projects": sorted(disaster_started_2022)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nHRMYqSVnORVdcf9fNlGp5zY': 'file_storage/call_nHRMYqSVnORVdcf9fNlGp5zY.json', 'var_call_ES96BvPmC6nu2gxnR5QnBRTK': 'file_storage/call_ES96BvPmC6nu2gxnR5QnBRTK.json', 'var_call_bD0CMSEohTSzPUBNK2etoltd': ['Funding'], 'var_call_eFBAq1NpGU12CEd60t2iqiC1': ['civic_docs']}

exec(code, env_args)
