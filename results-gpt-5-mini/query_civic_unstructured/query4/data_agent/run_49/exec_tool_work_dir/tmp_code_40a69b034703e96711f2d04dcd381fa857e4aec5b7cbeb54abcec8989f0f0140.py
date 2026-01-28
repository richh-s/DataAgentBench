code = """import json, re

# Load data files from storage variables
with open(var_call_mE21EkZMD6kWWBeEVNBTfcmh, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_9dDVhlsKhiCUoWoIszsMD5pk, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding dicts
funding_list = funding

# Helper to parse amounts
def parse_amount(a):
    try:
        return int(str(a).replace(',', '').strip())
    except:
        try:
            return int(float(a))
        except:
            return 0

# Build index of funding by lowercase name for matching
fund_index = {}
for rec in funding_list:
    name = rec.get('Project_Name', '').strip()
    key = name.lower()
    amt = parse_amount(rec.get('Amount', 0))
    if key in fund_index:
        fund_index[key].append((name, amt))
    else:
        fund_index[key] = [(name, amt)]

# Extract project names that have a 'Begin Construction' with 'Spring' in same line
projects_found = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'begin construction', line, re.I) and re.search(r'spring', line, re.I):
            # search upwards for a plausible project name
            name = None
            for j in range(max(0, i-8), i)[::-1]:
                cand = lines[j].strip()
                if not cand:
                    continue
                low = cand.lower()
                # skip lines that are obviously not titles
                if any(k in low for k in ['updates', 'project schedule', 'project description', 'agenda', 'page', 'item', 'cid:', '(']):
                    continue
                # if line is short and has letters, take it
                if len(cand) > 3 and len(cand) < 200:
                    name = cand
                    break
            if name:
                projects_found.append(name)

# Also consider 'Begin Construction: Spring/Summer' and similar captured by above since contains 'spring'
# Deduplicate and clean names
unique_projects = []
seen = set()
for p in projects_found:
    p_clean = re.sub(r'\s+', ' ', p).strip()
    if p_clean.lower() not in seen:
        unique_projects.append(p_clean)
        seen.add(p_clean.lower())

# Try to match funding records for each project
project_matches = []
total_funding = 0
for p in unique_projects:
    matched_amount = 0
    matched_records = []
    p_low = p.lower()
    # exact matches
    if p_low in fund_index:
        for name, amt in fund_index[p_low]:
            matched_amount += amt
            matched_records.append({'fund_name': name, 'amount': amt})
    else:
        # try contains matches
        for key, recs in fund_index.items():
            if p_low in key or key in p_low:
                for name, amt in recs:
                    matched_amount += amt
                    matched_records.append({'fund_name': name, 'amount': amt})
    total_funding += matched_amount
    project_matches.append({'project_name': p, 'matched_funding': matched_amount, 'matched_records': matched_records})

# Prepare result
result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': project_matches
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json'}

exec(code, env_args)
