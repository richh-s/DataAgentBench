code = """import json
import re
import pandas as pd

# Load the large JSON results from storage variables
with open(var_call_Kqe8QTpekLz4EwQniEZR9A2A, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_KZCWsxPte5HmqRZFlgUSFQAY, 'r') as f:
    funding = json.load(f)

# Build funding DataFrame
fund_df = pd.DataFrame(funding)
# Normalize Amount to int
fund_df['Amount'] = fund_df['Amount'].astype(int)
fund_df['Project_Name_raw'] = fund_df['Project_Name']

# Helper normalize function
import string

def normalize(s):
    s = s.lower()
    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r'\s+', ' ', s).strip()
    return s

fund_df['proj_norm'] = fund_df['Project_Name_raw'].apply(normalize)

# Patterns for Spring 2022 (include March-April-May 2022 variants)
pattern = re.compile(r"\b(?:spring\s*,?\s*2022|2022[-/ ]*spring|2022[-/ ]*march|march\s*2022|mar\s*2022|2022[-/ ]*april|april\s*2022|apr\s*2022|2022[-/ ]*may|may\s*2022)\b", re.IGNORECASE)

found_projects = set()

for doc in civic_docs:
    text = doc.get('text','')
    # find all matches
    for m in pattern.finditer(text):
        start_idx = m.start()
        # look back up to 400 characters to capture preceding title line
        window_start = max(0, start_idx-400)
        snippet = text[window_start:start_idx]
        # split into lines and find last non-empty candidate line
        lines = [ln.strip() for ln in re.split(r"\r?\n", snippet) if ln.strip()]
        # traverse lines from end to start to find a plausible project title
        candidate = None
        for ln in reversed(lines[-20:]):
            # skip lines that are generic headings or contain ':' or are short
            if len(ln) < 5:
                continue
            low = ln.lower()
            if any(x in low for x in ['updates', 'project schedule', 'project description', 'page', 'agenda item', 'meeting date', 'subject', 'recommended action', 'discussion', 'prepared by', 'approved by']):
                continue
            if ':' in ln:
                # sometimes titles include colon but skip
                # but accept if line looks like title (no lowercase words like 'city')? we'll skip
                continue
            candidate = ln
            break
        if candidate:
            # Clean candidate: remove trailing words like 'Project' if duplicated spaces
            cand = candidate.strip()
            # Remove extra multiple spaces
            cand = re.sub(r'\s+', ' ', cand)
            found_projects.add(cand)

# Fallback: also look for patterns like lines that include 'Advertise: Spring 2022' and take previous title before 'Project Schedule:'
# (already covered above)

# Now attempt to match found_projects to funding table
matched_projects = {}

fund_names = list(fund_df['Project_Name_raw'])
proj_norms = list(fund_df['proj_norm'])

for proj in sorted(found_projects):
    p_norm = normalize(proj)
    matched_amount = 0
    matched_rows = []
    for i, fn_norm in enumerate(proj_norms):
        fn_raw = fund_names[i]
        # direct containment
        if p_norm and (p_norm in fn_norm or fn_norm in p_norm):
            matched_rows.append(i)
            continue
        # token overlap: require majority of tokens in proj to be in funding name
        p_tokens = set([t for t in re.split(r"\s+", p_norm) if len(t)>2])
        f_tokens = set([t for t in re.split(r"\s+", fn_norm) if len(t)>2])
        if p_tokens and p_tokens.issubset(f_tokens):
            matched_rows.append(i)
            continue
        # partial overlap: at least 60% of proj tokens in funding tokens
        if p_tokens:
            inter = p_tokens.intersection(f_tokens)
            if len(inter)/len(p_tokens) >= 0.6:
                matched_rows.append(i)
                continue
    # Sum unique matched funding amounts
    if matched_rows:
        total = int(fund_df.loc[matched_rows, 'Amount'].sum())
        matched_amount = total
        matched_projects[proj] = {
            'matched_count': len(matched_rows),
            'matched_amount': matched_amount,
            'matches': list(fund_df.loc[matched_rows, 'Project_Name_raw'].unique())
        }

# Compute final counts: number of unique projects that matched and total funding
num_projects = len(matched_projects)
total_funding = sum(v['matched_amount'] for v in matched_projects.values())

# Prepare result
result = {'count': num_projects, 'total_funding': int(total_funding), 'matched_projects': matched_projects}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9DGl3prs7dXEX2JILUhPO4w0': ['civic_docs'], 'var_call_Cc1iK1XHvuR9GFnBEkdNhc9A': ['Funding'], 'var_call_Kqe8QTpekLz4EwQniEZR9A2A': 'file_storage/call_Kqe8QTpekLz4EwQniEZR9A2A.json', 'var_call_KZCWsxPte5HmqRZFlgUSFQAY': 'file_storage/call_KZCWsxPte5HmqRZFlgUSFQAY.json'}

exec(code, env_args)
