code = """import json

# Load file paths from storage variables
civic_path = var_call_eA0xJZWygM8q62BlCiIPmWwv
funding_path = var_call_CVAV72xeKdGMECzEU9GvpR7x

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Indicators for disaster-related projects
disaster_indicators = ['fema', 'caloes', 'caljpia']

# Combine all civic text
all_text = "\n".join([doc.get('text', '') for doc in civic_docs])
all_text_lower = all_text.lower()

matches = []

for rec in funding:
    proj_name = rec.get('Project_Name', '')
    proj_name_lower = proj_name.lower()
    fs = (rec.get('Funding_Source') or '').lower()

    # parse amount
    amt_raw = rec.get('Amount', 0)
    try:
        amount = int(str(amt_raw))
    except:
        try:
            amount = int(float(str(amt_raw)))
        except:
            amount = 0

    # determine disaster-related
    is_disaster = any(ind in proj_name_lower for ind in disaster_indicators) or any(ind in fs for ind in disaster_indicators) or 'federal assistance' in fs
    if not is_disaster:
        continue

    # prepare search terms: full name and base before '('
    base = proj_name_lower.split('(')[0].strip()
    search_terms = [proj_name_lower]
    if base and base != proj_name_lower:
        search_terms.append(base)

    found = False
    started_2022 = False
    for term in search_terms:
        if not term:
            continue
        idx = all_text_lower.find(term)
        if idx != -1:
            found = True
            start = max(0, idx-300)
            end = min(len(all_text_lower), idx+300)
            window = all_text_lower[start:end]
            if '2022' in window:
                started_2022 = True
            break

    if not found:
        # per-doc search
        for doc in civic_docs:
            txt = doc.get('text','').lower()
            for term in search_terms:
                if not term:
                    continue
                idx = txt.find(term)
                if idx != -1:
                    start = max(0, idx-300)
                    end = min(len(txt), idx+300)
                    window = txt[start:end]
                    if '2022' in window:
                        started_2022 = True
                    found = True
                    break
            if found:
                break

    if started_2022:
        try:
            fid = int(rec.get('Funding_ID'))
        except:
            fid = rec.get('Funding_ID')
        matches.append({'Funding_ID': fid, 'Project_Name': rec.get('Project_Name'), 'Amount': amount})

# sum
total = sum(m['Amount'] for m in matches)

result = {'total_funding': total, 'matched_projects_count': len(matches), 'matched_projects': matches}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_9m8TflfbCJWo96QQhMCIesyq': ['civic_docs'], 'var_call_eA0xJZWygM8q62BlCiIPmWwv': 'file_storage/call_eA0xJZWygM8q62BlCiIPmWwv.json', 'var_call_81lfzMGYLNjxzefeEW7o1uY3': ['Funding'], 'var_call_CVAV72xeKdGMECzEU9GvpR7x': 'file_storage/call_CVAV72xeKdGMECzEU9GvpR7x.json', 'var_call_yZiaFc25sB2M7suCKEOol9JH': {'v1': 'str', 'v2': 'str'}}

exec(code, env_args)
