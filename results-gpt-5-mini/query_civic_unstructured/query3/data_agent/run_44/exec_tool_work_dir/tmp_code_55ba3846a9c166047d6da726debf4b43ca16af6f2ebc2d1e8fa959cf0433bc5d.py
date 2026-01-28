code = """import json
import re
from pathlib import Path

# Load the query results from the stored JSON files (paths provided in variables)
with open(var_call_CHWKaz9CJKOfQ2VL3FnKxhnX, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_0EQqnWVhr6zNhR7UcxXNBDd9, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Convert funding amounts to ints where possible
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        try:
            r['Amount'] = int(float(r.get('Amount', 0)))
        except:
            r['Amount'] = None

# Prepare search keywords
kw_emergency = re.compile(r"\bemergency\b", re.IGNORECASE)
kw_fema = re.compile(r"\bFEMA\b", re.IGNORECASE)
kw_warning = re.compile(r"\bwarning\b|\bsiren|sirens\b", re.IGNORECASE)

# Helper to normalize project name for matching
def normalize_name(name):
    if not name:
        return name
    # remove parenthetical suffixes and extra spaces
    name2 = re.sub(r"\s*\([^)]*\)", "", name)
    name2 = re.sub(r"[^\w\s]", " ", name2)
    return re.sub(r"\s+", " ", name2).strip().lower()

# Build a single string of all civic docs texts (with filenames) for searching
all_texts = []
for doc in civic_docs:
    text = doc.get('text','')
    all_texts.append({'filename': doc.get('filename',''), 'text': text})

# For each funding record, determine if it's related to FEMA or emergency
results = []
for row in funding:
    pname = row.get('Project_Name','')
    pname_norm = normalize_name(pname)
    include = False
    reason = None
    status = None

    # Criterion 1: project name contains 'FEMA'
    if re.search(r"fema", pname, re.IGNORECASE):
        include = True
        reason = 'Project name contains FEMA'

    # Criterion 2: project name contains emergency-related keywords
    if not include and re.search(r"emergenc|warning|siren", pname, re.IGNORECASE):
        include = True
        reason = 'Project name suggests emergency/warning'

    # Criterion 3: project name appears in any civic doc that mentions 'emergency' or 'FEMA'
    if not include:
        for doc in all_texts:
            text = doc['text']
            if (kw_emergency.search(text) or kw_fema.search(text)):
                # check for project name substring match
                if pname_norm and pname_norm in text.lower():
                    include = True
                    reason = f"Found in civic doc {doc['filename']} containing emergency/FEMA"
                    # capture surrounding context
                    idx = text.lower().find(pname_norm)
                    start = max(0, idx-300)
                    end = min(len(text), idx+300)
                    context = text[start:end]
                    # Look for status-like keywords in context
                    m = re.search(r"(Updates:.*?)(?:\n|$)", context, re.IGNORECASE|re.DOTALL)
                    if m:
                        status = m.group(1).strip()
                    # fallback: search for sentences containing status words
                    if not status:
                        sent_m = re.search(r"([^.\n]{0,200}(?:completed|complete|under construction|construction|design|designs|preliminary design|not started|awaiting|awaiting final)[^.\n]{0,200})", context, re.IGNORECASE)
                        if sent_m:
                            status = sent_m.group(0).strip()
                    break

    # Criterion 4: also search civic docs for project name even if doc doesn't contain emergency; but we only want related to emergency/FEMA so skip

    # If still not included but project name itself contains FEMA/CalOES etc captured earlier
    if include:
        # If no status found yet, try to find project name in any civic doc and extract status nearby regardless of emergency keyword
        if not status:
            for doc in all_texts:
                text = doc['text']
                if pname_norm and pname_norm in text.lower():
                    idx = text.lower().find(pname_norm)
                    start = max(0, idx-300)
                    end = min(len(text), idx+300)
                    context = text[start:end]
                    m = re.search(r"(Updates:.*?)(?:\n|$)", context, re.IGNORECASE|re.DOTALL)
                    if m:
                        status = m.group(1).strip()
                        break
                    sent_m = re.search(r"([^.\n]{0,200}(?:completed|complete|under construction|construction|design|designs|preliminary design|not started|awaiting|awaiting final)[^.\n]{0,200})", context, re.IGNORECASE)
                    if sent_m:
                        status = sent_m.group(0).strip()
                        break
        # If still not status, set to None
        results.append({
            'Project_Name': row.get('Project_Name'),
            'Funding_Source': row.get('Funding_Source'),
            'Amount': row.get('Amount'),
            'Status': status if status else None,
            'Match_Reason': reason
        })

# As an additional step, include funding records whose project_name doesn't include FEMA but whose name mentions 'Outdoor Warning' or 'Sirens' (emergency)
for row in funding:
    pname = row.get('Project_Name','')
    if re.search(r"warning|siren", pname, re.IGNORECASE):
        # check if already included
        if not any(r['Project_Name']==row['Project_Name'] for r in results):
            # attempt to extract status from civic docs
            pname_norm = normalize_name(pname)
            status = None
            for doc in all_texts:
                text = doc['text']
                if pname_norm and pname_norm in text.lower():
                    idx = text.lower().find(pname_norm)
                    start = max(0, idx-300)
                    end = min(len(text), idx+300)
                    context = text[start:end]
                    m = re.search(r"(Updates:.*?)(?:\n|$)", context, re.IGNORECASE|re.DOTALL)
                    if m:
                        status = m.group(1).strip()
                        break
                    sent_m = re.search(r"([^.\n]{0,200}(?:completed|complete|under construction|construction|design|designs|preliminary design|not started|awaiting|awaiting final)[^.\n]{0,200})", context, re.IGNORECASE)
                    if sent_m:
                        status = sent_m.group(0).strip()
                        break
            results.append({
                'Project_Name': row.get('Project_Name'),
                'Funding_Source': row.get('Funding_Source'),
                'Amount': row.get('Amount'),
                'Status': status if status else None,
                'Match_Reason': 'Project name suggests emergency/warning'
            })

# Deduplicate results by (Project_Name, Funding_Source, Amount) keeping first
unique = []
seen = set()
for r in results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'])
    if key in seen:
        continue
    seen.add(key)
    unique.append(r)

# Sort by Project_Name
unique_sorted = sorted(unique, key=lambda x: (x['Project_Name'] or '').lower())

# Prepare final output list with required fields only
final = []
for r in unique_sorted:
    final.append({
        'Project_Name': r['Project_Name'],
        'Funding_Source': r['Funding_Source'],
        'Amount': r['Amount'],
        'Status': r['Status']
    })

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_CHWKaz9CJKOfQ2VL3FnKxhnX': 'file_storage/call_CHWKaz9CJKOfQ2VL3FnKxhnX.json', 'var_call_0EQqnWVhr6zNhR7UcxXNBDd9': 'file_storage/call_0EQqnWVhr6zNhR7UcxXNBDd9.json'}

exec(code, env_args)
