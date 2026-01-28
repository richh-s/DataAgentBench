code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_gFQpP3vihmPYY6m3zYEroo8R, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_7IPftSKhiKN3Q3entp8j8xre, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

fund_df = pd.DataFrame(funding_records)
# Normalize Amount to int
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Prepare civic texts combined for searching
civic_texts = [d.get('text','') for d in civic_docs]

disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'disaster recovery', 'fire', 'woolsey', 'emergency', 'flood', 'flooding']

matched_funding_ids = set()
matched_details = []

for rec in funding_records:
    pid = rec['Funding_ID']
    pname_orig = rec['Project_Name']
    pname = pname_orig.lower()
    # variants: strip parenthetical suffix
    pname_no_paren = re.sub(r"\s*\([^)]*\)", "", pname).strip()
    candidates = list({pname, pname_no_paren})
    found_match = False
    for text in civic_texts:
        t = text.lower()
        for cand in candidates:
            if not cand:
                continue
            idx = t.find(cand)
            if idx != -1:
                # window around match
                start = max(0, idx-300)
                end = min(len(t), idx + len(cand) + 300)
                window = t[start:end]
                has_2022 = '2022' in window
                # check disaster keywords in window or in project name
                has_disaster_kw = any(kw in window for kw in disaster_keywords) or any(kw in pname for kw in disaster_keywords)
                if has_2022 and has_disaster_kw:
                    matched_funding_ids.add(pid)
                    matched_details.append({'Funding_ID': pid, 'Project_Name': rec['Project_Name'], 'Amount': int(rec['Amount']), 'Matched_Window': window[:300]})
                    found_match = True
                    break
        if found_match:
            break

# As an additional heuristic, include funding records whose project name contains disaster suffix and whose civic docs include '2022' anywhere (even if name not found)
for rec in funding_records:
    pid = rec['Funding_ID']
    if pid in matched_funding_ids:
        continue
    pname = rec['Project_Name'].lower()
    if any(s in pname for s in ['(fema', '(caloes', '(caljpia', 'fema)', 'caloes)']):
        # check if any civic doc contains '2022' and project name base words
        base = re.sub(r"\s*\([^)]*\)", "", pname).strip()
        # attempt to find base or key tokens
        tokens = [tok for tok in re.split(r"[^a-z0-9]+", base) if tok]
        for text in civic_texts:
            t = text.lower()
            if '2022' in t:
                # check if most tokens appear in text
                if tokens and sum(1 for tok in tokens if tok in t) >= max(1, len(tokens)//2):
                    matched_funding_ids.add(pid)
                    matched_details.append({'Funding_ID': pid, 'Project_Name': rec['Project_Name'], 'Amount': int(rec['Amount']), 'Heuristic_Match': True})
                    break

# Sum amounts
total = 0
matched_list = []
for rec in funding_records:
    if rec['Funding_ID'] in matched_funding_ids:
        amt = int(rec['Amount'])
        total += amt
        matched_list.append({'Funding_ID': rec['Funding_ID'], 'Project_Name': rec['Project_Name'], 'Amount': amt})

result = {'total_disaster_funding_2022': total, 'count_projects': len(matched_list), 'projects': matched_list}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gFQpP3vihmPYY6m3zYEroo8R': 'file_storage/call_gFQpP3vihmPYY6m3zYEroo8R.json', 'var_call_7IPftSKhiKN3Q3entp8j8xre': 'file_storage/call_7IPftSKhiKN3Q3entp8j8xre.json'}

exec(code, env_args)
