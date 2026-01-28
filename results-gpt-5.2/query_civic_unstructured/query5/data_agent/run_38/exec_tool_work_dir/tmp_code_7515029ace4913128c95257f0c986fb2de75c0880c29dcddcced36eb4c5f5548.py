code = """import json, re
import pandas as pd

# Load funding totals by project
funding_path = var_call_Kg6NqBoEPX5FZHGCn6pWJjjb
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Load civic docs
docs_path = var_call_osN1aBustPtFa70A04jgfTvr
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Parse projects from docs: look for lines in Disaster Recovery Projects sections and capture schedule lines.
# We'll build a map: project_name -> start_string (best guess) and mark disaster.
proj_info = {}

# Regex helpers
section_disaster_re = re.compile(r"Disaster\s+Recovery\s+Projects", re.IGNORECASE)
section_capital_re = re.compile(r"Capital\s+Improvement\s+Projects", re.IGNORECASE)

# A project name line tends to be a standalone-ish line with letters and maybe punctuation, not too long.
# We'll match any non-empty line that isn't a bullet and isn't a header.

schedule_begin_re = re.compile(r"\b(Begin\s+Construction|Start\s+Construction|Begin\s+Design|Start\s+Design)\b\s*:\s*(.+)$", re.IGNORECASE)
project_schedule_re = re.compile(r"Project\s+Schedule|Estimated\s+Schedule", re.IGNORECASE)

# Some docs list projects without explicit schedule; try to find 'Project Schedule' block and pick 'Begin Construction' line.

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]

    in_disaster = False
    in_capital = False
    current_project = None
    # We capture project when line looks like a project name (not empty and not obviously header)
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if section_disaster_re.search(ln):
            in_disaster = True
            in_capital = False
            current_project = None
            continue
        if section_capital_re.search(ln):
            in_capital = True
            in_disaster = False
            current_project = None
            continue
        # Exit disaster section if another big header appears
        if in_disaster and (re.search(r"^Page\s+\d+\b", ln) or re.search(r"^Agenda\s+Item", ln, re.IGNORECASE)):
            # don't necessarily exit
            pass

        if in_disaster:
            # Identify candidate project line: not starting with '(' or 'cid' artifacts, not starting with 'Updates', 'Project', etc.
            if re.match(r"^(Updates|Project\s+Schedule|Estimated\s+Schedule|Project\s+Description|RECOMMENDED\s+ACTION|DISCUSSION)\b", ln, re.IGNORECASE):
                continue
            if ln.startswith(('(cid', '•', '·', '-', '—', '*')):
                continue
            # If line is short enough and has letters
            if 3 <= len(ln) <= 120 and re.search(r"[A-Za-z]", ln):
                # Avoid lines that are clearly sentences (contain period) unless it's part of name
                if ln.count('.') >= 2:
                    continue
                # Many project lines have no colon
                if ':' in ln and not re.search(r"\(.*\)", ln):
                    continue
                # Set as current project
                current_project = ln
                if current_project not in proj_info:
                    proj_info[current_project] = {'is_disaster': True, 'start': None}
                continue

            # Capture schedule start lines following project context
            m = schedule_begin_re.search(ln)
            if m and current_project:
                st = m.group(2).strip()
                # keep the earliest/first seen
                if not proj_info[current_project].get('start'):
                    proj_info[current_project]['start'] = st

# Also consider disaster projects identifiable by suffix in funding names; mark them as disaster even if not found.
# But need start in 2022 from docs.

# Determine which disaster projects have start in 2022 based on parsed start strings containing '2022'
started_2022 = set()
for pn, info in proj_info.items():
    if info.get('is_disaster') and info.get('start') and '2022' in info['start']:
        started_2022.add(pn)

# Join with funding totals using exact match on Project_Name
fund_started_2022 = fund_df[fund_df['Project_Name'].isin(started_2022)]

total_funding = int(fund_started_2022['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total_funding,
    'matched_projects_count': int(fund_started_2022.shape[0]),
    'matched_projects': fund_started_2022.sort_values('total_amount', ascending=False).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Kg6NqBoEPX5FZHGCn6pWJjjb': 'file_storage/call_Kg6NqBoEPX5FZHGCn6pWJjjb.json', 'var_call_osN1aBustPtFa70A04jgfTvr': 'file_storage/call_osN1aBustPtFa70A04jgfTvr.json', 'var_call_lLOTO8ea6JafFE0pIrYI8W4l': ['Funding']}

exec(code, env_args)
