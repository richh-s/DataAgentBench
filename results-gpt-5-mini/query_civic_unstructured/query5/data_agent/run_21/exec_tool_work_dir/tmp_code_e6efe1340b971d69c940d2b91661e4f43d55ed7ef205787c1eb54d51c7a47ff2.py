code = """import json, re

# Load file paths from storage variables
civic_path = var_call_eA0xJZWygM8q62BlCiIPmWwv
funding_path = var_call_CVAV72xeKdGMECzEU9GvpR7x

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Define indicators for disaster-related projects
disaster_indicators = ['fema', 'caloes', 'caljpia', 'fema/caloes', 'caloes project', 'fema project', 'caljpia project']

matches = []

# Combine all civic text for searching
all_text = "\n".join([doc.get('text', '') for doc in civic_docs])
all_text_lower = all_text.lower()

for rec in funding:
    proj_name = rec.get('Project_Name', '')
    proj_name_lower = proj_name.lower()
    amt_raw = rec.get('Amount', 0)
    try:
        amount = int(str(amt_raw))
    except:
        try:
            amount = int(float(str(amt_raw)))
        except:
            amount = 0

    # Identify disaster by project name or funding source
    is_disaster = any(ind in proj_name_lower for ind in disaster_indicators)
    fs = rec.get('Funding_Source', '')
    if not is_disaster and fs:
        fs_lower = fs.lower()
        if 'federal assistance' in fs_lower or 'fema' in fs_lower or 'caloes' in fs_lower:
            is_disaster = True

    if not is_disaster:
        continue

    # Prepare search terms: full name and base name without parenthetical
    search_terms = [proj_name_lower]
    base = re.sub(r"\s*\([^)]*\)", "", proj_name_lower).strip()
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
            start = max(0, idx - 400)
            end = min(len(all_text_lower), idx + 400)
            window = all_text_lower[start:end]
            # Simple check for '2022' in nearby text
            if '2022' in window:
                started_2022 = True
            else:
                # Look for patterns indicating 2022 near construction dates
                if re.search(r'begin construction[:\s].{0,80}2022', window) or re.search(r'complete construction[:\s].{0,80}2022', window) or re.search(r'construction was completed.{0,80}2022', window):
                    started_2022 = True
            break

    # If not found in combined text, search per document
    if not found:
        for doc in civic_docs:
            txt = doc.get('text', '').lower()
            for term in search_terms:
                if not term:
                    continue
                idx = txt.find(term)
                if idx != -1:
                    found = True
                    start = max(0, idx - 400)
                    end = min(len(txt), idx + 400)
                    window = txt[start:end]
                    if '2022' in window:
                        started_2022 = True
                    else:
                        if re.search(r'begin construction[:\s].{0,80}2022', window) or re.search(r'complete construction[:\s].{0,80}2022', window) or re.search(r'construction was completed.{0,80}2022', window):
                            started_2022 = True
                    break
            if found:
                break

    if started_2022:
        try:
            fid = int(rec.get('Funding_ID'))
        except:
            fid = rec.get('Funding_ID')
        matches.append({'Funding_ID': fid, 'Project_Name': rec.get('Project_Name'), 'Amount': amount})

# Sum amounts
total = sum(item['Amount'] for item in matches)

result = {'total_funding': total, 'matched_projects_count': len(matches), 'matched_projects': matches}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9m8TflfbCJWo96QQhMCIesyq': ['civic_docs'], 'var_call_eA0xJZWygM8q62BlCiIPmWwv': 'file_storage/call_eA0xJZWygM8q62BlCiIPmWwv.json', 'var_call_81lfzMGYLNjxzefeEW7o1uY3': ['Funding'], 'var_call_CVAV72xeKdGMECzEU9GvpR7x': 'file_storage/call_CVAV72xeKdGMECzEU9GvpR7x.json', 'var_call_yZiaFc25sB2M7suCKEOol9JH': {'v1': 'str', 'v2': 'str'}}

exec(code, env_args)
