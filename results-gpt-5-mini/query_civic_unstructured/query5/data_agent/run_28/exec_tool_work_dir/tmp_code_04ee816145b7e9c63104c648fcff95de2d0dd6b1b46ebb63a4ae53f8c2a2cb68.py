code = """import json, re
# Load the previous tool results
# Variables from storage: var_call_Vl0TG7LtyyMTUxdDBWkduxwO, var_call_DIpBJRT5NI77OMdOhicKMrCM

civic_var = var_call_Vl0TG7LtyyMTUxdDBWkduxwO
funding_var = var_call_DIpBJRT5NI77OMdOhicKMrCM

# helper to load if the variable is a filepath
def load_maybe_path(v):
    if isinstance(v, str):
        try:
            with open(v, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            # if not a json file, return as is
            return v
    else:
        return v

civic_docs = load_maybe_path(civic_var)
funding = load_maybe_path(funding_var)

# normalize types
if isinstance(civic_docs, dict):
    civic_docs = [civic_docs]

# Prepare keywords
disaster_keywords = [r'FEMA', r'CalOES', r'CalJPIA', r'disaster', r'fire', r'Woolsey', r'recovery', r'emergency', r'FEMA/CalOES', r'CalOES/']

matches = []
total = 0

for fr in funding:
    pname = fr.get('Project_Name')
    try:
        amount = int(fr.get('Amount', 0))
    except:
        # try convert if string with commas
        s = fr.get('Amount','0')
        s = re.sub(r"[^0-9-]","", str(s))
        amount = int(s) if s else 0
    found = False
    is_disaster = False
    started_2022 = False
    matched_filename = None
    matched_snippet = None
    # quick disaster check from project name
    pname_lower = (pname or '').lower()
    if any(k.lower() in pname_lower for k in ['fema','caloes','caljpia','caloes','fema/']):
        is_disaster = True
    # search in civic docs
    if pname:
        for doc in civic_docs:
            text = doc.get('text','')
            idx = text.find(pname)
            if idx != -1:
                found = True
                # get a generous snippet after the match
                start_snip = max(0, idx-400)
                end_snip = min(len(text), idx+2000)
                snippet = text[start_snip:end_snip]
                matched_filename = doc.get('filename')
                matched_snippet = snippet
                # check disaster keywords in snippet
                for k in disaster_keywords:
                    if re.search(k, snippet, re.IGNORECASE):
                        is_disaster = True
                        break
                # check if 'Project Schedule' or 'Begin Construction' or 'Complete Construction' around contains 2022
                if re.search(r'\b2022\b', snippet):
                    started_2022 = True
                else:
                    # Also look for month names or seasons with 2022 elsewhere in nearby section
                    # search up to next 1500 chars after match
                    after = text[idx: idx+1500]
                    if re.search(r'\b2022\b', after):
                        started_2022 = True
                break
    # If not found in docs but project name itself contains disaster keywords and '2022' anywhere in funding name? unlikely
    if not found:
        # try searching by shorter tokens (split by spaces and check presence)
        # Also search in docs for occurrences of disaster keywords and 2022, and if project name similar
        for doc in civic_docs:
            text = doc.get('text','')
            if any(word.lower() in text.lower() for word in pname.split()[:3]):
                # approximate match
                if re.search(r'\b2022\b', text[:5000]):
                    started_2022 = True
                if any(re.search(k, text, re.IGNORECASE) for k in disaster_keywords):
                    is_disaster = True
                matched_filename = doc.get('filename')
                matched_snippet = text[:1000]
                break
    if is_disaster and started_2022:
        matches.append({'Project_Name': pname, 'Amount': amount, 'Funding_ID': fr.get('Funding_ID'), 'Filename': matched_filename})
        total += amount

# Prepare result
result = {'total_disaster_2022_funding': total, 'matches': matches}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Vl0TG7LtyyMTUxdDBWkduxwO': 'file_storage/call_Vl0TG7LtyyMTUxdDBWkduxwO.json', 'var_call_DIpBJRT5NI77OMdOhicKMrCM': 'file_storage/call_DIpBJRT5NI77OMdOhicKMrCM.json'}

exec(code, env_args)
