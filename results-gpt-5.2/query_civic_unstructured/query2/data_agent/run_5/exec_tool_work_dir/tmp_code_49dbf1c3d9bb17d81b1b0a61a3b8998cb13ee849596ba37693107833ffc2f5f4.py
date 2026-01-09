code = """import json, re
import pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str) and maybe_path_or_records.endswith('.json'):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

docs = load_records(var_call_gEfKeao4kM437eGsbb7cyAaz)
fund = load_records(var_call_qdjvtfFTJp45N8z7mN0IBsPP)

# parse a project status list blocks; focus on lines containing projects under headings.
# We'll identify "completed" projects and capture nearby schedule/end info if present.

completed_projects = {}

for d in docs:
    text = d.get('text','') or ''
    if 'Capital Improvement Projects' not in text and 'Disaster Recovery Projects' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    cur_section = None
    for i, ln in enumerate(lines):
        lnl = ln.lower()
        if 'capital improvement projects' in lnl or 'disaster recovery projects' in lnl:
            # section header, but we want status subheaders
            pass
        if 'projects (construction)' in lnl:
            cur_section = 'construction'
        elif 'projects (completed)' in lnl:
            cur_section = 'completed'
        elif 'projects (design)' in lnl:
            cur_section = 'design'
        elif 'projects (not started)' in lnl:
            cur_section = 'not started'

        # project name lines tend to be non-empty and not bullet markers
        if cur_section == 'completed':
            if not ln or ln.startswith('(') or ln.startswith('cid:'):
                continue
            if any(kw in lnl for kw in ['updates', 'project schedule', 'page ', 'agenda item', 'recommended action', 'discussion', 'prepared by', 'approved by', 'subject:']):
                continue
            # Heuristic: project name lines are followed by 'Updates:'
            nxt = lines[i+1].lower() if i+1 < len(lines) else ''
            if 'updates' in nxt or 'updates:' in nxt:
                pname = ln
                # capture nearby completion date lines in following 10 lines
                window = ' '.join(lines[i:i+15])
                completed_projects.setdefault(pname, []).append(window)

# Filter to park-related: project name contains 'park' OR window contains 'park'
park_completed_2022 = set()
for pname, windows in completed_projects.items():
    is_park = 'park' in pname.lower() or any('park' in w.lower() for w in windows)
    if not is_park:
        continue
    # completed in 2022: look for 'completed' or 'construction was completed' and '2022' in window
    # since we are already in completed section, check if any window mentions 2022.
    if any('2022' in w for w in windows):
        park_completed_2022.add(pname)

# Build funding sum for these project names
fund_df = pd.DataFrame(fund)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce')
sel = fund_df[fund_df['Project_Name'].isin(sorted(park_completed_2022))]

total = float(sel['Amount'].sum())

out = {
    'total_funding': int(total) if pd.notna(total) else 0,
    'projects': sorted(park_completed_2022),
    'matched_funding_records': sel.to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gEfKeao4kM437eGsbb7cyAaz': 'file_storage/call_gEfKeao4kM437eGsbb7cyAaz.json', 'var_call_qdjvtfFTJp45N8z7mN0IBsPP': 'file_storage/call_qdjvtfFTJp45N8z7mN0IBsPP.json'}

exec(code, env_args)
