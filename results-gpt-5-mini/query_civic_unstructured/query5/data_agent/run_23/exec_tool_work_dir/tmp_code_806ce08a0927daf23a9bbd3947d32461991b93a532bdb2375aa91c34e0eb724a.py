code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_LOCCBqtPWFCUn6YYeXqomeiq, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_4G5yHoOrQ19mXr7KvMIWZiA9, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding records: convert Amount to int
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount') or 0)
    except:
        # remove non-digits
        s = re.sub(r"[^0-9]", "", str(r.get('Amount') or "0"))
        r['Amount'] = int(s) if s else 0

# Keywords to identify disaster-related projects
disaster_keywords = ["fema", "caloes", "caljpia", "disaster", "fire", "woolsey", "emergency", "fema/caloes", "caloes/fema"]

def strip_parenthetical(name):
    return re.sub(r"\s*\(.*?\)\s*", "", name).strip()

matches = []

for rec in funding:
    pname = rec.get('Project_Name','')
    base_name = strip_parenthetical(pname)
    pname_lower = pname.lower()
    base_lower = base_name.lower()
    matched = False
    date_found = False
    disaster_found = False
    matched_doc = None
    matched_snippet = None

    # Heuristic: if project name itself contains disaster keywords, mark disaster_found True
    for kw in disaster_keywords:
        if kw in pname_lower:
            disaster_found = True
            break

    # Search in civic docs for occurrences of the base_name
    for doc in civic_docs:
        text = doc.get('text','')
        text_lower = text.lower()
        idx = text_lower.find(base_lower)
        if idx != -1:
            matched = True
            matched_doc = doc.get('filename')
            # snippet around occurrence
            start = max(0, idx-200)
            end = min(len(text), idx+400)
            snippet = text[start:end]
            matched_snippet = snippet
            # check for '2022' in nearby snippet
            if '2022' in snippet:
                date_found = True
            else:
                # also check a bit more context: next 1000 chars
                ext_end = min(len(text), idx+1000)
                if '2022' in text[idx:ext_end].lower():
                    date_found = True
            # check disaster keywords in snippet
            for kw in disaster_keywords:
                if kw in snippet.lower():
                    disaster_found = True
                    break
            # if not found in snippet, check nearby entire doc for keywords near the project name occurrence
            if not disaster_found:
                # check within +/-1000 chars
                start2 = max(0, idx-1000)
                end2 = min(len(text), idx+1000)
                if any(kw in text_lower[start2:end2] for kw in disaster_keywords):
                    disaster_found = True
            # We found an occurrence; break after first doc match
            break

    # Also tag as disaster if funding source or project name contains disaster words
    if any(kw in (rec.get('Funding_Source') or '').lower() for kw in disaster_keywords):
        disaster_found = True

    # Collect match info
    matches.append({
        'Funding_ID': rec.get('Funding_ID'),
        'Project_Name': rec.get('Project_Name'),
        'Amount': rec.get('Amount'),
        'Matched_in_docs': bool(matched),
        'Matched_doc_filename': matched_doc,
        'Date_near_project_contains_2022': bool(date_found),
        'Disaster_keyword_found': bool(disaster_found),
        'Matched_snippet_preview': (matched_snippet[:500] if matched_snippet else None)
    })

# Now filter for records that are disaster-related and have date_found True
selected = [m for m in matches if m['Disaster_keyword_found'] and m['Date_near_project_contains_2022']]

total = sum(m['Amount'] for m in selected)

# Prepare result
result = {
    'total_disaster_funding_started_in_2022': total,
    'matched_projects': selected
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_57RBUcJtwXZx4ZuVcbIwbJGQ': ['civic_docs'], 'var_call_4G5yHoOrQ19mXr7KvMIWZiA9': 'file_storage/call_4G5yHoOrQ19mXr7KvMIWZiA9.json', 'var_call_f3Mq0GMNK5Cw6OIK5PQWY6mA': ['Funding'], 'var_call_LOCCBqtPWFCUn6YYeXqomeiq': 'file_storage/call_LOCCBqtPWFCUn6YYeXqomeiq.json'}

exec(code, env_args)
