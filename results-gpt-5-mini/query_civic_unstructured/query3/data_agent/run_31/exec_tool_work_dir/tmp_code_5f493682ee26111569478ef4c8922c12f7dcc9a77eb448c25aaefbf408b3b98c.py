code = """import json
from pathlib import Path
import re

p = Path(var_call_uegX5YtT5sjI2pkA0DpZVoVm)
with p.open('r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
seen = set()

for doc in docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current_status = None
    for i, ln in enumerate(lines):
        hdr = ln.lower()
        if 'capital improvement projects' in hdr and 'design' in hdr:
            current_status = 'design'
        elif 'capital improvement projects' in hdr and 'construction' in hdr:
            current_status = 'completed'
        elif 'capital improvement projects' in hdr and 'not started' in hdr:
            current_status = 'not started'
        if re.search(r"\bdesign\b", hdr) and 'capital improvement' in hdr:
            current_status = 'design'
        if re.search(r"\bconstruction\b", hdr) and 'capital improvement' in hdr:
            current_status = 'completed'
        if re.search(r"\bnot started\b", hdr):
            current_status = 'not started'

        if re.search(r"\b(fema|caloes)\b", ln, re.IGNORECASE) or re.search(r"\bemergency\b", ln, re.IGNORECASE):
            if re.search(r"\bfema\b", ln, re.IGNORECASE) or re.search(r"\bcaloes\b", ln, re.IGNORECASE):
                keyword = 'FEMA'
            else:
                keyword = 'emergency'
            title = None
            for j in range(max(0, i-8), i+1)[::-1]:
                candidate = lines[j]
                if not candidate:
                    continue
                cond = False
                if re.search(r"\bProject\b", candidate, re.IGNORECASE):
                    cond = True
                if re.search(r"\bProjects\b", candidate, re.IGNORECASE):
                    cond = True
                if re.search(r"\bRepair\b", candidate, re.IGNORECASE):
                    cond = True
                if re.search(r"\bImprovement\b", candidate, re.IGNORECASE):
                    cond = True
                if re.search(r"\bPlayground\b", candidate, re.IGNORECASE):
                    cond = True
                if re.search(r"\bFacility\b", candidate, re.IGNORECASE):
                    cond = True
                if re.search(r"\bWarning Signs\b", candidate, re.IGNORECASE):
                    cond = True
                if re.search(r"\bRetaining Wall\b", candidate, re.IGNORECASE):
                    cond = True
                if re.search(r"\bDrainage\b", candidate, re.IGNORECASE):
                    cond = True
                if not cond and len(candidate.split())>2 and candidate[0].isupper():
                    cond = True
                if cond:
                    title = candidate
                    break
            if title:
                title_norm = re.sub(r"\s+", " ", title).strip()
                ptype = 'disaster' if keyword=='FEMA' else 'capital'
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

if not results:
    for doc in docs:
        text = doc.get('text','')
        for m in re.finditer(r'([A-Z][A-Za-z0-9 \-\(\)]+?(?:Project|Repairs|Improvements|Facility|Playground|Repair))', text):
            seg = m.group(1).strip()
            if re.search(r"\bfema\b|\bemergency\b", text[m.end():m.end()+200], re.IGNORECASE):
                title_norm = re.sub(r"\s+", " ", seg)
                results.append({'Project_Name': title_norm, 'matched_keyword': 'FEMA or emergency', 'status': None, 'type': 'disaster', 'source_file': doc.get('filename')})

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uegX5YtT5sjI2pkA0DpZVoVm': 'file_storage/call_uegX5YtT5sjI2pkA0DpZVoVm.json'}

exec(code, env_args)
