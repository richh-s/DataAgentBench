code = """import json
import re

# Load the large results from the storage file paths provided by the previous tool calls
with open(var_call_PiVO4fMjvPZ9Ri2Sq3DmNv40, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_VWfCe7d7cKITCZHoI1fqcWri, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Combine all civic texts into a list
texts = [doc.get('text','') for doc in civic_docs]
combined_text = '\n'.join(texts).lower()

results = []
seen = set()

# helper to clean project name for searching
def canonical(name):
    return re.sub(r"\s+"," ", name.strip()).lower()

for rec in funding:
    pname = rec.get('Project_Name','')
    pname_l = pname.lower()
    match = False
    status_snippet = None

    # If project name explicitly includes 'fema' or 'emergency' mark as match
    if 'fema' in pname_l or 'emergency' in pname_l:
        match = True
    else:
        # search for occurrences of project name (or base name without parenthetical suffix)
        base = re.sub(r"\s*\(.*?\)\s*$","", pname, flags=re.IGNORECASE).strip()
        patterns = [re.escape(pname), re.escape(base)]
        for doc_text in texts:
            lower = doc_text.lower()
            for pat in patterns:
                for m in re.finditer(pat.lower(), lower):
                    start = max(0, m.start()-200)
                    end = min(len(lower), m.end()+200)
                    window = lower[start:end]
                    if 'fema' in window or 'caloes' in window or 'caloes' in lower or 'emergency' in window or 'outdoor warning' in window or 'sirens' in window:
                        match = True
                        # attempt to extract status from the window
                        # look for common status indicators
                        status_patterns = [r"updates\s*:\s*(.*?)\n\n", r"updates\s*:([\s\S]{0,200})", r"project schedule\s*:\s*([\s\S]{0,200})", r"project is currently ([^\n\.]*)", r"project is in the ([^\n\.]*)", r"construction was completed", r"complete construction", r"complete design", r"preliminary design", r"awaiting final fema", r"awaiting final fema/caloes approval for scope modification", r"awaiting final fema/caloes approval"]
                        found = None
                        for sp in status_patterns:
                            m2 = re.search(sp, window)
                            if m2:
                                found = m2.group(0)
                                # clean
                                found = found.strip().replace('\n',' ').strip()
                                break
                        if not found:
                            # broader search in window for keywords
                            keywords = ['under construction', 'construction was completed', 'complete construction', 'complete design', 'preliminary design', 'in the preliminary design phase', 'awaiting final fema', 'awaiting final fema/caloes approval', 'advertise', 'begin construction', 'design']
                            for kw in keywords:
                                if kw in window:
                                    found = kw
                                    break
                        if found:
                            status_snippet = found
                        else:
                            status_snippet = 'status not found in nearby text'
                        break
                if match:
                    break
            if match:
                break

    if match:
        key = (pname, rec.get('Funding_Source'), rec.get('Amount'))
        if key in seen:
            continue
        seen.add(key)
        results.append({
            'Project_Name': pname,
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': int(rec.get('Amount')) if str(rec.get('Amount','')).isdigit() else rec.get('Amount'),
            'Status': status_snippet if status_snippet else 'status not found in documents'
        })

# Additionally, search for projects mentioned in civic docs near the word 'emergency' even if not in funding table
# find phrases that look like project titles near 'emergency'
for doc in civic_docs:
    txt = doc.get('text','')
    lower = txt.lower()
    for m in re.finditer(r"emergency", lower):
        start = max(0, m.start()-200)
        # try to extract a title-like line before the word
        snippet = txt[start:m.end()+200]
        # find the nearest preceding line break and take the line as possible title
        lines = snippet.splitlines()
        if lines:
            candidate = lines[0].strip()
            if candidate and len(candidate) < 200:
                # check if not already in results and appears in funding table
                for rec in funding:
                    if canonical(rec.get('Project_Name','')) in canonical(candidate) or canonical(candidate) in canonical(rec.get('Project_Name','')):
                        key = (rec.get('Project_Name'), rec.get('Funding_Source'), rec.get('Amount'))
                        if key in seen:
                            continue
                        seen.add(key)
                        results.append({
                            'Project_Name': rec.get('Project_Name'),
                            'Funding_Source': rec.get('Funding_Source'),
                            'Amount': int(rec.get('Amount')) if str(rec.get('Amount','')).isdigit() else rec.get('Amount'),
                            'Status': 'status not found in documents (found via emergency proximity)'
                        })

# Sort results by Project_Name
results = sorted(results, key=lambda x: x['Project_Name'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_PiVO4fMjvPZ9Ri2Sq3DmNv40': 'file_storage/call_PiVO4fMjvPZ9Ri2Sq3DmNv40.json', 'var_call_VWfCe7d7cKITCZHoI1fqcWri': 'file_storage/call_VWfCe7d7cKITCZHoI1fqcWri.json'}

exec(code, env_args)
