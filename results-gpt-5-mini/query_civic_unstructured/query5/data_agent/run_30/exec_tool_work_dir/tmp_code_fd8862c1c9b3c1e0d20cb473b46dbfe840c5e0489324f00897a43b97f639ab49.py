code = """import json
from pathlib import Path

# Load data from storage-provided file paths
funding_path = Path(var_call_sK41BtYb2el82Z4oDCzMktLa)
civic_path = Path(var_call_HkkNDQewlqPXKW3Qv5AHGC1B)

funding = json.load(open(funding_path, 'r', encoding='utf-8'))
civic = json.load(open(civic_path, 'r', encoding='utf-8'))

# Normalize funding amounts and prepare records
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount') if r.get('Amount') not in (None, '') else 0)
    except:
        # remove commas and other chars
        amt = r.get('Amount', '0')
        amt = ''.join(ch for ch in str(amt) if ch.isdigit())
        r['Amount'] = int(amt) if amt else 0

# Keywords to identify disaster-related projects
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency']

matches = []
total = 0

# For each funding record, search civic docs for mentions and context indicating disaster and 2022 start
for fr in funding:
    pname = fr.get('Project_Name', '')
    pname_low = pname.lower()
    amount = fr.get('Amount', 0)
    matched = False
    # search across all civic documents
    for doc in civic:
        text = doc.get('text', '')
        text_low = text.lower()
        idx = text_low.find(pname_low)
        if idx != -1:
            # define window around match
            start = max(0, idx - 500)
            end = min(len(text_low), idx + len(pname_low) + 500)
            window = text_low[start:end]
            # Check for disaster keyword in window or project name itself
            has_disaster_kw = any(k in window for k in disaster_keywords) or any(k in pname_low for k in disaster_keywords)
            has_2022 = '2022' in window or '2022' in text_low
            if has_disaster_kw and has_2022:
                matched = True
                break
    if matched:
        matches.append({'Project_Name': pname, 'Amount': amount})
        total += amount

# As a fallback, also include projects whose name itself contains disaster keywords and whose funding table entry might not be found in civic docs matches
# but ensure there's some mention of 2022 anywhere in civic docs
all_civic_text = '\n'.join(d.get('text','') for d in civic).lower()
for fr in funding:
    pname = fr.get('Project_Name', '')
    pname_low = pname.lower()
    amount = fr.get('Amount', 0)
    if any(k in pname_low for k in disaster_keywords) and '2022' in all_civic_text:
        # Check if already included
        if not any(m['Project_Name'] == pname for m in matches):
            matches.append({'Project_Name': pname, 'Amount': amount})
            total += amount

# Remove possible duplicates if added twice
seen = set()
unique_matches = []
unique_total = 0
for m in matches:
    key = m['Project_Name']
    if key not in seen:
        seen.add(key)
        unique_matches.append(m)
        unique_total += m['Amount']

result = {'total_funding': unique_total, 'matches': unique_matches}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vGqZjFy1hiG4jBrsj5lbPjuK': ['civic_docs'], 'var_call_qLHfZfu6d3IXNtIxkCJYCbxo': ['Funding'], 'var_call_sK41BtYb2el82Z4oDCzMktLa': 'file_storage/call_sK41BtYb2el82Z4oDCzMktLa.json', 'var_call_HkkNDQewlqPXKW3Qv5AHGC1B': 'file_storage/call_HkkNDQewlqPXKW3Qv5AHGC1B.json'}

exec(code, env_args)
