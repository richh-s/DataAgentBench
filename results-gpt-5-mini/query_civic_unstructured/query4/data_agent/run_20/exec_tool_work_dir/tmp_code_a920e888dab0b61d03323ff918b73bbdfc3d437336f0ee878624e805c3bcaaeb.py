code = """import json, re

# Load the large civic docs JSON file and funding table JSON file
with open(var_call_8Wx5JHW4BB36AwhFSKg7ssFq, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_Dr8ySo5A7qhCpT0BBoDXQNsd, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Prepare spring 2022 pattern (March-May 2022 or explicit Spring 2022)
spring_pattern = re.compile(r"(Spring[, ]*2022|2022[- ]Spring|Spring 2022|March 2022|April 2022|May 2022|Mar 2022|Apr 2022|May 2022|03[-/]?2022|04[-/]?2022|05[-/]?2022)", re.I)

found_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    # Search for lines indicating Begin Construction in spring 2022
    for i, line in enumerate(lines):
        if 'begin' in line.lower() and 'construction' in line.lower() and spring_pattern.search(line):
            # look back up to 10 lines to find a candidate project title
            proj_name = None
            for j in range(max(0, i-10), i)[::-1]:
                candidate = lines[j]
                if not candidate:
                    continue
                # skip lines that look like metadata or list markers
                if candidate.lower().startswith('(cid'):
                    continue
                if ':' in candidate and len(candidate.split(':')[0].split())<6:
                    # if line contains ':' and left of ':' is short, likely a label
                    continue
                # require candidate to have at least 2 words and not be the word 'Updates' etc
                if len(candidate.split()) >= 2 and candidate.lower() not in ('updates','project schedule','estimated schedule'):
                    proj_name = candidate
                    break
            if proj_name:
                found_projects.append(proj_name)

# deduplicate while preserving order
seen = set()
unique_projects = []
for p in found_projects:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        unique_projects.append(p)

# Matching projects to funding records
# Preprocess funding records: normalize project names and amounts
fund_records = funding
for rec in fund_records:
    # ensure Amount is int
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        try:
            rec['Amount'] = int(float(rec['Amount']))
        except:
            rec['Amount'] = 0
    rec['proj_norm'] = re.sub(r"[^a-z0-9 ]+", " ", rec['Project_Name'].lower())

results = []

for proj in unique_projects:
    proj_norm = re.sub(r"[^a-z0-9 ]+", " ", proj.lower())
    proj_tokens = set([t for t in proj_norm.split() if len(t)>2])
    matches = []
    for rec in fund_records:
        fund_tokens = set([t for t in rec['proj_norm'].split() if len(t)>2])
        if not proj_tokens:
            continue
        # substring match
        if proj_norm in rec['proj_norm'] or rec['proj_norm'] in proj_norm:
            matches.append(rec)
            continue
        # token overlap heuristic
        inter = proj_tokens & fund_tokens
        if len(inter)/max(1, len(proj_tokens)) >= 0.6 or len(inter)/max(1, len(fund_tokens)) >= 0.6:
            matches.append(rec)
    total_amt = sum([m['Amount'] for m in matches])
    results.append({'project_name': proj, 'matched_funding_sum': total_amt, 'matched_records': [{'Funding_ID': m['Funding_ID'], 'Project_Name': m['Project_Name'], 'Amount': m['Amount']} for m in matches]})

# Compute overall totals for projects that have any matched funding
projects_with_funding = [r for r in results if r['matched_funding_sum']>0]
num_projects = len(results)
# total funding across matched records but avoid double-counting the same funding record across projects
matched_record_ids = set()
total_funding = 0
for r in results:
    for rec in r['matched_records']:
        if rec['Funding_ID'] not in matched_record_ids:
            matched_record_ids.add(rec['Funding_ID'])
            total_funding += rec['Amount']

output = {'projects_found_starting_spring_2022_count': num_projects, 'total_funding_for_these_projects': total_funding, 'projects': results}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_C7VZYbTDFgXkQ1OjqtXTcK4k': ['civic_docs'], 'var_call_XxHj1ipYW2HEDpVsTp9icWLt': ['Funding'], 'var_call_8Wx5JHW4BB36AwhFSKg7ssFq': 'file_storage/call_8Wx5JHW4BB36AwhFSKg7ssFq.json', 'var_call_Dr8ySo5A7qhCpT0BBoDXQNsd': 'file_storage/call_Dr8ySo5A7qhCpT0BBoDXQNsd.json'}

exec(code, env_args)
