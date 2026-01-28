code = """import json, re

# Load data from storage paths provided by previous tool calls
with open(var_call_wLnc3OqtCZyurcOKDhRmWfMy, 'r') as f:
    funding = json.load(f)
with open(var_call_oaAn6uXz8V3SXUIojafC6soe, 'r') as f:
    docs = json.load(f)

# Normalize funding amounts and prepare records
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        # try removing non-digits
        digits = re.sub(r"[^0-9]", "", str(r.get('Amount','0')))
        r['Amount'] = int(digits) if digits else 0
    r['Project_Name_orig'] = r['Project_Name']
    # base name without parenthetical suffix
    r['base_name'] = re.sub(r"\s*\(.*?\)", "", r['Project_Name']).strip()
    r['base_name_l'] = r['base_name'].lower()
    r['name_l'] = r['Project_Name'].lower()

# Build combined text corpus from civic docs
texts = [d.get('text','') for d in docs]
texts_l = [t.lower() for t in texts]

# Disaster indicators
disaster_kw = ['fema', 'caloes', 'caljpia', 'fema/caloes', 'fema/caloes', 'woolsey', 'fire', 'disaster', 'emergency', 'outdoor warning', 'flood']

matched = []

for rec in funding:
    included = False
    reasons = []
    # Quick check: if project name itself contains disaster keywords, mark disaster
    name_is_disaster = any(k in rec['name_l'] for k in disaster_kw)

    # Search for base_name occurrences in civic docs
    for doc_text_l in texts_l:
        idx = doc_text_l.find(rec['base_name_l'])
        if idx != -1:
            # context window
            start = max(0, idx-300)
            end = idx + len(rec['base_name_l']) + 300
            ctx = doc_text_l[start:end]
            has_2022 = '2022' in ctx
            ctx_has_disaster = any(k in ctx for k in disaster_kw)
            # Also look for construction phrases near with 2022
            phrases = ['begin construction', 'complete construction', 'construction was completed', 'complete design', 'advertise', 'begin construction:']
            phrase_with_2022 = any((ph in ctx and '2022' in ctx) for ph in phrases)

            if (name_is_disaster or ctx_has_disaster) and has_2022:
                included = True
                reasons.append('name_is_disaster' if name_is_disaster else 'context_has_disaster')
                break
            # If context has 2022 and any construction/completion phrase, consider started in 2022
            if has_2022 and phrase_with_2022:
                # if also disaster indicated by name or context nearby
                if name_is_disaster or ctx_has_disaster:
                    included = True
                    reasons.append('phrase_with_2022_and_disaster')
                    break
                else:
                    # If not explicitly disaster but base name contains words like 'repair' or 'recovery' and context has fema/cal
                    if ctx_has_disaster:
                        included = True
                        reasons.append('ctx_has_disaster_and_phrase')
                        break
            # Also allow if name has disaster keyword even if doc doesn't have 2022 but doc elsewhere mentions 2022 for base name
            if name_is_disaster and has_2022:
                included = True
                reasons.append('name_disaster_and_2022_in_ctx')
                break
    # If not found in docs, still consider name-is-disaster and search docs for base name without parentheses
    if not included and name_is_disaster:
        # look for base_name elsewhere with 2022
        for doc_text_l in texts_l:
            if rec['base_name_l'] in doc_text_l and '2022' in doc_text_l:
                included = True
                reasons.append('name_disaster_and_2022_elsewhere')
                break

    if included:
        matched.append({'Project_Name': rec['Project_Name_orig'], 'base_name': rec['base_name'], 'Amount': rec['Amount'], 'reasons': reasons})

# As a fallback, also look for any funding records whose base_name appears in civic docs with 2022 and context contains disaster keywords, even if the funding name lacked disaster keywords
for rec in funding:
    if any(m['Project_Name'] == rec['Project_Name_orig'] for m in matched):
        continue
    for doc_text_l in texts_l:
        idx = doc_text_l.find(rec['base_name_l'])
        if idx != -1:
            start = max(0, idx-300)
            end = idx + len(rec['base_name_l']) + 300
            ctx = doc_text_l[start:end]
            if '2022' in ctx and any(k in ctx for k in disaster_kw):
                matched.append({'Project_Name': rec['Project_Name_orig'], 'base_name': rec['base_name'], 'Amount': rec['Amount'], 'reasons': ['found_by_context_2022_and_disaster']})
                break

# Sum amounts
total = sum(m['Amount'] for m in matched)

# Prepare output
out = {'total': total, 'matched_count': len(matched), 'matched_projects': matched}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_6vYp1gKgiDeqchLvIDXND6X9': ['civic_docs'], 'var_call_4nwGubHW1YwpKR2xW27s8dMy': ['Funding'], 'var_call_oaAn6uXz8V3SXUIojafC6soe': 'file_storage/call_oaAn6uXz8V3SXUIojafC6soe.json', 'var_call_wLnc3OqtCZyurcOKDhRmWfMy': 'file_storage/call_wLnc3OqtCZyurcOKDhRmWfMy.json'}

exec(code, env_args)
