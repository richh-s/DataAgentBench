code = """import json, re

# Load previous tool results from storage variables
with open(var_call_TkjHazDggb6cTj5sko2ijCic, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_oBnAWlCfqnC1xumd6lo9ZeSo, 'r') as f:
    funding_rows = json.load(f)

# Extract project names under 'Capital Improvement Projects (Design)'
capital_design_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    start_idx = text.find('Capital Improvement Projects (Design)')
    if start_idx == -1:
        continue
    rest = text[start_idx:]
    # find end of design section
    end_cands = []
    for cand in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Completed)']:
        i = rest.find(cand)
        if i != -1:
            end_cands.append(i)
    if end_cands:
        end_idx = min(end_cands)
        section = rest[:end_idx]
    else:
        section = rest
    # split into lines and extract probable project title lines
    lines = [ln.strip() for ln in section.splitlines()]
    # skip the header line(s) until we find the first likely project name
    for ln in lines:
        if not ln:
            continue
        low = ln.lower()
        # filter out lines that are not titles
        if low.startswith('(cid') or low.startswith('(cid:') or low.startswith('updates:') or low.startswith('\ufeff'):
            continue
        if low.startswith('page'):
            continue
        if 'agenda item' in low or 'recommended action' in low:
            continue
        # avoid lines that are clearly content lines (contain ":" early or start with bullets)
        if ':' in ln and ln.find(':') < 30:
            continue
        # avoid lines that are clearly subheaders
        if low.startswith('capital improvement projects'):
            continue
        # heuristics: treat lines that look like project titles (contain letters and not many stopwords)
        if len(ln) > 5:
            # Often project titles are Title Case and may contain digits (years) or acronyms like SRF
            # Exclude lines that are sentences (contain multiple clauses) by checking if they end with a period
            if ln.endswith('.'):
                continue
            # Exclude lines that start with words like 'Updates' or 'Project Schedule'
            if ln.lower().startswith('project schedule') or ln.lower().startswith('updates'):
                continue
            # Add line as project candidate
            capital_design_projects.append(ln)

# Deduplicate while preserving order
seen = set()
cap_projects = []
for p in capital_design_projects:
    key = p.strip()
    if key and key not in seen:
        seen.add(key)
        cap_projects.append(key)

# Prepare funding records (already filtered >50000 by the SQL query)
funding = []
for r in funding_rows:
    # ensure Amount is int
    amt = r.get('Amount')
    try:
        amt_int = int(str(amt))
    except:
        try:
            amt_int = int(float(str(amt)))
        except:
            amt_int = None
    funding.append({'Project_Name': r.get('Project_Name',''), 'Amount': amt_int})

# Matching function
def normalize(s):
    s2 = s.lower()
    s2 = s2.replace('&', ' and ')
    s2 = re.sub(r"\([^)]*\)", " ", s2)  # remove parenthesis content
    s2 = re.sub(r'[^a-z0-9 ]', ' ', s2)
    s2 = re.sub(r'\s+', ' ', s2).strip()
    return s2

stop_tokens = set(['project','projects','improvements','repair','repairs','design','construction','phase','project','project:', 'the','and','at','of','in','a','to','road','roadway','roadway/retaining','retaining','road','project','improvement','improvements'])

matched = []
for cp in cap_projects:
    cclean = normalize(cp)
    c_tokens = set([t for t in cclean.split() if len(t)>2 and t not in stop_tokens])
    found = False
    matched_fundings = []
    for fr in funding:
        fclean = normalize(fr['Project_Name'])
        f_tokens = set([t for t in fclean.split() if len(t)>2 and t not in stop_tokens])
        # direct substring check
        if cclean and (cclean in fclean or fclean in cclean):
            found = True
            matched_fundings.append(fr)
            continue
        # token intersection heuristic
        if c_tokens and f_tokens:
            inter = c_tokens & f_tokens
            # require at least 2 shared meaningful tokens or high fraction
            if len(inter) >= 2 or (len(inter) >= 1 and len(inter) >= 0.6 * max(1, len(c_tokens))):
                found = True
                matched_fundings.append(fr)
                continue
    if found:
        # record project and matched funding details
        matched.append({'Project_Name': cp, 'Matched_Funding': matched_fundings})

# Count unique capital-design projects that have funding > 50000
count = len(matched)
projects_list = [m['Project_Name'] for m in matched]

# Prepare printable JSON string
result = {'count': count, 'projects': projects_list}
import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_wiTp9omBdRESNUT1sRYYo7gE': ['civic_docs'], 'var_call_7RnkyynYHUaUOvGpzsmThhed': ['Funding'], 'var_call_TkjHazDggb6cTj5sko2ijCic': 'file_storage/call_TkjHazDggb6cTj5sko2ijCic.json', 'var_call_oBnAWlCfqnC1xumd6lo9ZeSo': 'file_storage/call_oBnAWlCfqnC1xumd6lo9ZeSo.json'}

exec(code, env_args)
