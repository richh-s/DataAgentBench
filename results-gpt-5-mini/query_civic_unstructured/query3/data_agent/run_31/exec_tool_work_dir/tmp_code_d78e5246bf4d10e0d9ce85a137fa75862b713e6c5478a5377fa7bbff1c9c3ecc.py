code = """import json
from pathlib import Path

# Load the civic docs query result from storage file
p = Path(var_call_uegX5YtT5sjI2pkA0DpZVoVm)
with p.open('r', encoding='utf-8') as f:
    docs = json.load(f)

import re

results = []
seen = set()

for doc in docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    # track section header (status)
    current_status = None
    for i, ln in enumerate(lines):
        # update status based on section headers
        hdr = ln.lower()
        if 'capital improvement projects' in hdr and 'design' in hdr:
            current_status = 'design'
        elif 'capital improvement projects' in hdr and 'construction' in hdr:
            current_status = 'completed'
        elif 'capital improvement projects' in hdr and 'not started' in hdr:
            current_status = 'not started'
        # also explicit headings
        if re.search(r'\bdesign\b', hdr) and 'capital improvement' in hdr:
            current_status = 'design'
        if re.search(r'\bconstruction\b', hdr) and 'capital improvement' in hdr:
            current_status = 'completed'
        if re.search(r'\bnot started\b', hdr):
            current_status = 'not started'

        # look for lines mentioning fema or emergency
        if re.search(r'\b(fema|caloes|caloes|caloes)\b', ln, re.IGNORECASE) or re.search(r'\bemergency\b', ln, re.IGNORECASE):
            keyword = 'FEMA' if re.search(r'\bfema\b', ln, re.IGNORECASE) or re.search(r'caloes', ln, re.IGNORECASE) or re.search(r'caloes', ln, re.IGNORECASE) else 'emergency'
            # search backward up to 8 lines for a title-like line
            title = None
            for j in range(max(0, i-8), i+1)[::-1]:
                candidate = lines[j]
                if not candidate:
                    continue
                # heuristics for project title
                if re.search(r'\bProject\b', candidate) or re.search(r'\bProjects\b', candidate) or re.search(r'\bRepairs?\b', candidate, re.IGNORECASE) or re.search(r'\bImprovement(s)?\b', candidate, re.IGNORECASE) or re.search(r'\bPlayground\b', candidate, re.IGNORECASE) or re.search(r'\bFacility\b', candidate, re.IGNORECASE) or re.search(r'\bWarning Signs\b', candidate, re.IGNORECASE) or re.search(r'\bRetaining Wall\b', candidate, re.IGNORECASE) or re.search(r'\bDrainage\b', candidate, re.IGNORECASE) or len(candidate.split())>2 and candidate[0].isupper():
                    title = candidate
                    break
            if title:
                # normalize title
                title_norm = re.sub(r'\s+', ' ', title).strip()
                # decide type
                ptype = 'disaster' if keyword=='FEMA' or re.search(r'caloes|caloes|fema|caloes', ln, re.IGNORECASE) else 'capital'
                status = current_status if current_status in ('design','completed','not started') else None
                key = (title_norm, status, ptype)
                if key not in seen:
                    seen.add(key)
                    results.append({
                        'Project_Name': title_norm,
                        'matched_keyword': keyword,
                        'status': status,
                        'type': ptype,
                        'source_file': doc.get('filename')
                    })

# If no results found (unlikely), fallback: search whole text for FEMA occurrences and try to extract nearby title-like phrases using regex
if not results:
    for doc in docs:
        text = doc.get('text','')
        for m in re.finditer(r'([A-Z][A-Za-z0-9 \-\'\(\)]+?(?:Project|Repairs|Improvements|Facility|Playground|Repair))', text):
            seg = m.group(1).strip()
            if re.search(r'\bfema\b|\bemergency\b', text[m.end():m.end()+200], re.IGNORECASE):
                title_norm = re.sub(r'\s+', ' ', seg)
                results.append({'Project_Name': title_norm, 'matched_keyword': 'FEMA or emergency', 'status': None, 'type': 'disaster', 'source_file': doc.get('filename')})

# output JSON string
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uegX5YtT5sjI2pkA0DpZVoVm': 'file_storage/call_uegX5YtT5sjI2pkA0DpZVoVm.json'}

exec(code, env_args)
