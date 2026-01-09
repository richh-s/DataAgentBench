code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_gF8lyKZZcti0adGt48dKp2G2)
fund = load_json_maybe(var_call_cmOeD70QKis9L2dfbYlheNTD)

# Identify park-related projects completed in 2022 from documents.
# Heuristic: find project blocks (lines) and completion statements.
park_completed_2022 = set()

for d in docs:
    text = d.get('text','')
    if 'completed' not in text.lower() and 'Construction was completed' not in text:
        continue

    lines = [ln.strip() for ln in text.splitlines()]

    # Track current project name when line looks like a standalone title.
    current = None
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # project title candidates: not bullet, not header, reasonably short
        if len(ln) <= 120 and not re.search(r'^(To:|Prepared by:|Approved by:|Date prepared|Meeting date|Subject:|RECOMMENDED ACTION|DISCUSSION|Page \d+ of \d+|Agenda Item|Updates:|Project Schedule|Estimated Schedule|Project Description)', ln):
            # Titles often have no ':' and not start with '(' or '(cid'
            if ':' not in ln and not ln.startswith('(') and 'cid' not in ln and not ln.startswith('•') and not ln.startswith('-'):
                # Exclude all-caps section titles
                if not re.fullmatch(r'[A-Z0-9 &/()\-]+', ln) or 'Project' in ln or 'Park' in ln or 'Bluffs' in ln or 'Playground' in ln:
                    # set current when next non-empty line contains 'Updates' or similar
                    nxt = ''
                    for j in range(i+1, min(i+6, len(lines))):
                        if lines[j]:
                            nxt = lines[j]
                            break
                    if re.search(r'Updates', nxt, re.I) or re.search(r'Project (Schedule|Description)', nxt, re.I) or re.search(r'Construction was completed', nxt, re.I):
                        current = ln
        # look for completion in 2022
        if current:
            if re.search(r'completed', ln, re.I) and re.search(r'2022', ln):
                # park-related keyword in project name or nearby context
                context = ' '.join(lines[max(0,i-2):min(len(lines), i+3)])
                if re.search(r'park|playground|bluffs|skate', (current + ' ' + context), re.I):
                    park_completed_2022.add(current)
            # Also specific phrase "Construction was completed <month> 2022"
            if re.search(r'Construction was completed', ln, re.I) and re.search(r'2022', ln):
                context = ' '.join(lines[max(0,i-2):min(len(lines), i+3)])
                if re.search(r'park|playground|bluffs|skate', (current + ' ' + context), re.I):
                    park_completed_2022.add(current)
            # Reset current at section boundaries
            if re.search(r'^Capital Improvement Projects \(', ln):
                current = None

# Now join with funding totals
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = fund_df['Total_Amount'].astype(int)

# Some project names might not match exactly; attempt direct match only per instructions.
match_df = fund_df[fund_df['Project_Name'].isin(sorted(park_completed_2022))]

total = int(match_df['Total_Amount'].sum())

out = {
    'park_projects_completed_2022': sorted(park_completed_2022),
    'matched_funded_projects': match_df.sort_values('Project_Name').to_dict(orient='records'),
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VDBc145nugyC4KADjnEvWoFB': ['Funding'], 'var_call_kmDNSMwGjuuySCanjANvnI0N': ['civic_docs'], 'var_call_gF8lyKZZcti0adGt48dKp2G2': 'file_storage/call_gF8lyKZZcti0adGt48dKp2G2.json', 'var_call_cmOeD70QKis9L2dfbYlheNTD': 'file_storage/call_cmOeD70QKis9L2dfbYlheNTD.json'}

exec(code, env_args)
