code = """import json
import re

# Load data from previous tool calls (file paths provided in storage variables)
with open(var_call_NZGYmigRm3Zpa9Anowdntrau, 'r') as f:
    funding = json.load(f)
with open(var_call_cF0ExqcNOqjZS2vUZ9qh04hs, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records
for r in funding:
    # Ensure Amount is int
    try:
        r['Amount'] = int(r['Amount'])
    except:
        r['Amount'] = 0
    r['Project_Name_norm'] = r['Project_Name'].lower()

# Build a single combined civic text
all_texts = [d.get('text','') for d in civic_docs]
combined_text = "\n".join(all_texts).lower()

# Disaster keywords
disaster_keywords = ['fema', 'caloes', 'calo es', 'caljpia', 'disaster', 'woolsey', 'fire', 'emergency', 'storm', 'flood', 'drainage', 'culvert', 'retaining wall', 'water quality', 'debris']

# For each funding project, search for project name in civic documents and check nearby for 2022 and disaster keywords
included_projects = []
for r in funding:
    pname = r['Project_Name']
    pname_l = pname.lower()
    matched = False
    # Find all occurrences in combined_text
    for m in re.finditer(re.escape(pname_l), combined_text):
        start = max(0, m.start()-300)
        end = min(len(combined_text), m.end()+300)
        window = combined_text[start:end]
        if '2022' in window:
            # Check disaster keywords in window
            if any(kw in window for kw in disaster_keywords) or any(kw in pname_l for kw in disaster_keywords):
                included_projects.append(r)
                matched = True
                break
    if matched:
        continue
    # If no exact match, try fuzzy: check if base name without parentheses exists
    base = re.sub(r"\(.*?\)", "", pname_l).strip()
    if base and base != pname_l:
        for m in re.finditer(re.escape(base), combined_text):
            start = max(0, m.start()-300)
            end = min(len(combined_text), m.end()+300)
            window = combined_text[start:end]
            if '2022' in window:
                if any(kw in window for kw in disaster_keywords) or any(kw in base for kw in disaster_keywords):
                    included_projects.append(r)
                    matched = True
                    break
    if matched:
        continue
    # As fallback: if project name itself contains disaster keyword and the combined_text contains the project name (or base) and somewhere in doc there's '2022' within 1000 chars of some disaster keyword
    if any(kw in pname_l for kw in disaster_keywords):
        # search for project name or base
        search_terms = [pname_l, base]
        for term in search_terms:
            if not term:
                continue
            idx = combined_text.find(term)
            if idx!=-1:
                # look for 2022 within +/-1000 chars of this occurrence
                start = max(0, idx-1000)
                end = min(len(combined_text), idx+1000)
                window = combined_text[start:end]
                if '2022' in window:
                    included_projects.append(r)
                    matched = True
                    break
    # End loop

# Remove duplicates
unique = { (p['Funding_ID']): p for p in included_projects }
included_list = list(unique.values())

# Sum amounts
total = sum(p['Amount'] for p in included_list)

# For transparency, also prepare list of included project names and amounts
result = {
    'total_funding': total,
    'projects_count': len(included_list),
    'projects': [ {'Funding_ID': p['Funding_ID'], 'Project_Name': p['Project_Name'], 'Amount': p['Amount']} for p in included_list]
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NZGYmigRm3Zpa9Anowdntrau': 'file_storage/call_NZGYmigRm3Zpa9Anowdntrau.json', 'var_call_kPhMDTzPlJP1T2NZTKlIWKVh': ['civic_docs'], 'var_call_cF0ExqcNOqjZS2vUZ9qh04hs': 'file_storage/call_cF0ExqcNOqjZS2vUZ9qh04hs.json'}

exec(code, env_args)
