code = """import json
import re

# Load data from previous tool calls
with open(var_call_NZGYmigRm3Zpa9Anowdntrau, 'r') as f:
    funding = json.load(f)
with open(var_call_cF0ExqcNOqjZS2vUZ9qh04hs, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and names
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        r['Amount'] = 0
    r['Project_Name_l'] = r.get('Project_Name','').lower()

# Disaster keywords
disaster_keywords = ['fema', 'caloes', 'calo es', 'caljpia', 'disaster', 'woolsey', 'fire', 'emergency', 'storm', 'flood', 'drainage', 'culvert', 'retaining wall', 'water quality', 'debris']

included = []

# Iterate funding records and check civic docs
for r in funding:
    pname = r['Project_Name_l']
    base = re.sub(r"\(.*?\)", "", pname).strip()
    found = False
    for doc in civic_docs:
        text = doc.get('text','').lower()
        # Quick check: if neither name nor base appears and name doesn't contain disaster kw, skip
        if pname not in text and base not in text and not any(kw in pname for kw in disaster_keywords):
            continue
        # If doc mentions 2022 and disaster keywords somewhere, and project name appears in doc, include
        if '2022' in text and any(kw in text for kw in disaster_keywords) and (pname in text or base in text or any(kw in pname for kw in disaster_keywords)):
            included.append(r)
            found = True
            break
        # Otherwise, look for occurrences of name/base and inspect nearby window
        terms = [t for t in [pname, base] if t]
        for term in terms:
            for m in re.finditer(re.escape(term), text):
                start = max(0, m.start()-300)
                end = min(len(text), m.end()+300)
                window = text[start:end]
                if '2022' in window and (any(kw in window for kw in disaster_keywords) or any(kw in pname for kw in disaster_keywords)):
                    included.append(r)
                    found = True
                    break
            if found:
                break
        if found:
            break
    # End docs loop

# Deduplicate by Funding_ID
unique = {}
for p in included:
    unique[p['Funding_ID']] = p
included_list = list(unique.values())

total = sum(p['Amount'] for p in included_list)

result = {
    'total_funding': total,
    'projects_count': len(included_list),
    'projects': [ {'Funding_ID': p['Funding_ID'], 'Project_Name': p['Project_Name'], 'Amount': p['Amount']} for p in included_list]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NZGYmigRm3Zpa9Anowdntrau': 'file_storage/call_NZGYmigRm3Zpa9Anowdntrau.json', 'var_call_kPhMDTzPlJP1T2NZTKlIWKVh': ['civic_docs'], 'var_call_cF0ExqcNOqjZS2vUZ9qh04hs': 'file_storage/call_cF0ExqcNOqjZS2vUZ9qh04hs.json'}

exec(code, env_args)
