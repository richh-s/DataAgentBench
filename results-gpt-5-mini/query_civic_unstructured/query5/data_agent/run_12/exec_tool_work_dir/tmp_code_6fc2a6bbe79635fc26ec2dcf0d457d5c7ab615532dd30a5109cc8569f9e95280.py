code = """import json
import pandas as pd

# Load stored query results
with open(var_call_kYr0scjoSRkupx1549fyWvIy, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_jh3XKI5dJrA4acAmQLIT3BwR, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Create DataFrame
df = pd.DataFrame(funding)
# Convert Amount and Funding_ID to int
df['Amount'] = df['Amount'].astype(int)
try:
    df['Funding_ID'] = df['Funding_ID'].astype(int)
except Exception:
    pass

# Helper to strip parenthetical suffixes
def base_name(name):
    if not isinstance(name, str):
        return ''
    import re
    return re.sub(r"\s*\(.*?\)", '', name).strip()

# Lowercase civic texts for searching
docs_texts = [doc.get('text', '') for doc in civic_docs]
docs_texts_lower = [t.lower() for t in docs_texts]

matched_rows = []

for _, row in df.iterrows():
    pname = row.get('Project_Name', '')
    pname_low = pname.lower() if isinstance(pname, str) else ''
    source_low = str(row.get('Funding_Source', '')).lower()
    matched = False
    # Check if funding name or source indicates disaster
    if 'fema' in pname_low or 'caloes' in pname_low or 'caljpia' in pname_low or 'federal' in source_low:
        # Now verify 2022 appears in civic docs near this project name
        bname = base_name(pname)
        if bname:
            b_low = bname.lower()
            for txt in docs_texts_lower:
                idx = txt.find(b_low)
                if idx != -1:
                    s = max(0, idx-200)
                    e = min(len(txt), idx+len(b_low)+200)
                    snippet = txt[s:e]
                    if '2022' in snippet:
                        matched = True
                        break
        else:
            # If no base name, still include if any civic doc contains 2022
            for txt in docs_texts_lower:
                if '2022' in txt:
                    matched = True
                    break
    # Also consider funding rows whose base project name appears in civic docs with 2022 context even if no FEMA keyword
    if not matched:
        bname = base_name(pname)
        if bname:
            b_low = bname.lower()
            for txt in docs_texts_lower:
                idx = txt.find(b_low)
                if idx != -1:
                    s = max(0, idx-200)
                    e = min(len(txt), idx+len(b_low)+200)
                    snippet = txt[s:e]
                    # Check if doc is from 2022 via filename or snippet
                    # Also check filenames
                    has_2022 = False
                    if '2022' in snippet:
                        has_2022 = True
                    else:
                        # check filenames in civic_docs
                        for doc in civic_docs:
                            if b_low in doc.get('text','').lower() and '2022' in doc.get('filename',''):
                                has_2022 = True
                                break
                    if has_2022:
                        # Heuristic: also ensure project likely disaster-related by keywords in snippet
                        if any(k in snippet for k in ['fema', 'fire', 'disaster', 'caloes', 'caljpia', 'flood', 'recovery']):
                            matched = True
                            break
    if matched:
        matched_rows.append({
            'Funding_ID': int(row.get('Funding_ID')) if row.get('Funding_ID') else None,
            'Project_Name': row.get('Project_Name'),
            'Funding_Source': row.get('Funding_Source'),
            'Amount': int(row.get('Amount'))
        })

# Sum amounts
total = sum(r['Amount'] for r in matched_rows)

result = {
    'total_disaster_funding_started_in_2022': total,
    'matched_funding_rows_count': len(matched_rows),
    'matched_rows': matched_rows
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_LNP4ZyjRTM1X5aZ3RtzWo5HY': ['civic_docs'], 'var_call_kYr0scjoSRkupx1549fyWvIy': 'file_storage/call_kYr0scjoSRkupx1549fyWvIy.json', 'var_call_jh3XKI5dJrA4acAmQLIT3BwR': 'file_storage/call_jh3XKI5dJrA4acAmQLIT3BwR.json'}

exec(code, env_args)
