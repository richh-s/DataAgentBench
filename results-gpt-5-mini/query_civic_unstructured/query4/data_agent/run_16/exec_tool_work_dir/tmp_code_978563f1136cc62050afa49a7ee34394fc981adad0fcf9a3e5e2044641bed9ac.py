code = """import json
import re
import pandas as pd
import string

# Load data from stored files
with open(var_call_Kqe8QTpekLz4EwQniEZR9A2A, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_KZCWsxPte5HmqRZFlgUSFQAY, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
fund_df['Project_Name_raw'] = fund_df['Project_Name']

# normalize function
def normalize(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r"\s+", ' ', s).strip()
    return s

fund_df['proj_norm'] = fund_df['Project_Name_raw'].apply(normalize)
fund_names = list(fund_df['Project_Name_raw'])
proj_norms = list(fund_df['proj_norm'])

# months and season to consider for Spring
months = ['spring', 'march', 'mar', 'april', 'apr', 'may']

found_projects = set()

for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    for idx, line in enumerate(lines):
        low = line.lower()
        if '2022' in low and any(m in low for m in months):
            # look back up to 8 lines to find a project title candidate
            for j in range(max(0, idx-8), idx):
                cand = lines[j].strip()
                if not cand:
                    continue
                lowc = cand.lower()
                if any(x in lowc for x in ['agenda', 'page', 'item', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion']):
                    continue
                # skip very short lines
                if len(cand) < 6:
                    continue
                # skip lines that are clearly a description (start with '(' or 'cid')
                if cand.lstrip().startswith('(') or 'cid' in cand.lower():
                    continue
                # likely a project title
                found_projects.add(cand)
                break
        # also handle case where line contains 'Project Schedule:' and nearby lines contain season
        if 'project schedule' in low:
            # scan next 6 lines for date mention
            for k in range(idx, min(len(lines), idx+6)):
                if '2022' in lines[k].lower() and any(m in lines[k].lower() for m in months):
                    # find previous title
                    for j in range(max(0, idx-8), idx):
                        cand = lines[j].strip()
                        if not cand or len(cand) < 6:
                            continue
                        if any(x in cand.lower() for x in ['updates', 'project schedule', 'project description', 'page', 'agenda', 'item']):
                            continue
                        found_projects.add(cand)
                        break
                    break

# Match found projects to funding table
matched_projects = {}

for proj in sorted(found_projects):
    p_norm = normalize(proj)
    matched_rows = set()
    p_tokens = set([t for t in re.split(r"\s+", p_norm) if len(t) > 2])
    for i, fn_norm in enumerate(proj_norms):
        if not p_norm:
            continue
        if p_norm in fn_norm or fn_norm in p_norm:
            matched_rows.add(i)
            continue
        f_tokens = set([t for t in re.split(r"\s+", fn_norm) if len(t) > 2])
        if p_tokens and p_tokens.issubset(f_tokens):
            matched_rows.add(i)
            continue
        if p_tokens:
            inter = p_tokens.intersection(f_tokens)
            if len(inter) / max(1, len(p_tokens)) >= 0.6:
                matched_rows.add(i)
                continue
    if matched_rows:
        total = int(fund_df.loc[list(matched_rows), 'Amount'].sum())
        matched_projects[proj] = {
            'matched_count': len(matched_rows),
            'matched_amount': total,
            'matches': list(fund_df.loc[list(matched_rows), 'Project_Name_raw'].unique())
        }

num_projects = len(matched_projects)
total_funding = sum(v['matched_amount'] for v in matched_projects.values())
result = {'count': num_projects, 'total_funding': int(total_funding), 'matched_projects': matched_projects}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9DGl3prs7dXEX2JILUhPO4w0': ['civic_docs'], 'var_call_Cc1iK1XHvuR9GFnBEkdNhc9A': ['Funding'], 'var_call_Kqe8QTpekLz4EwQniEZR9A2A': 'file_storage/call_Kqe8QTpekLz4EwQniEZR9A2A.json', 'var_call_KZCWsxPte5HmqRZFlgUSFQAY': 'file_storage/call_KZCWsxPte5HmqRZFlgUSFQAY.json'}

exec(code, env_args)
