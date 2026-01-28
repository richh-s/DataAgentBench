code = """import json, re
# Load stored query results
# var_call_UCPD1RS4AZvlswJyAis5URH1 and var_call_TXF5iLgHVwuGHi0geYBudpqL are file paths
with open(var_call_UCPD1RS4AZvlswJyAis5URH1, 'r') as f:
    univ_rows = json.load(f)
with open(var_call_TXF5iLgHVwuGHi0geYBudpqL, 'r') as f:
    citing_rows = json.load(f)

# Function to extract publication numbers from Patents_info text
pubnum_regex = re.compile(r"\b([A-Z]{2}-[A-Z0-9\-]+)\b")
# More restrictive: look for patterns like US-..., WO-, EP-, AU-, JP-, CN-, KR-, etc.
# We'll collect all matches but filter likely ones containing digits

def extract_pubnums(text):
    if not text:
        return []
    candidates = pubnum_regex.findall(text)
    # keep those that contain a digit
    keep = [c for c in candidates if re.search(r"\d", c)]
    return keep

# Build set of UNIV CALIFORNIA publication numbers
univ_pubnums = set()
for r in univ_rows:
    text = r.get('Patents_info','')
    nums = extract_pubnums(text)
    for n in nums:
        univ_pubnums.add(n)

# Now for each citing row, parse citation JSON and check if any cited publication_number is in univ_pubnums
results = []
unique_primary_cpcs = set()

# helper to extract assignee name from Patents_info
def extract_assignee(text):
    if not text:
        return None
    # common patterns
    patterns = [r"^(.+?) holds the", r"^(.+?) holds", r"^(.+?) is assigned to", r"^(.+?) is owned by", r"^(.+?) owns the", r"^(.+?) belonging to", r"^(.+?) is belonging to", r"^(.+?) held by", r"^(.+?) has pub" ]
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            name = m.group(1).strip()
            # cleanup trailing articles
            name = re.sub(r"\s+(the|a)$", "", name, flags=re.IGNORECASE)
            return name.upper()
    # fallback: take up to first comma
    part = text.split(',')[0]
    return part.strip().upper()

for r in citing_rows:
    citation_field = r.get('citation')
    if not citation_field:
        continue
    # citation_field may be JSON string or already list
    try:
        citations = json.loads(citation_field) if isinstance(citation_field, str) else citation_field
    except Exception:
        # try to fix single quotes
        try:
            citations = json.loads(citation_field.replace("'","\""))
        except Exception:
            citations = []
    matched = False
    for c in citations:
        pubnum = c.get('publication_number') if isinstance(c, dict) else None
        if not pubnum:
            continue
        # normalize
        pubnum_norm = pubnum.strip()
        if pubnum_norm in univ_pubnums:
            matched = True
            break
    if matched:
        assignee = extract_assignee(r.get('Patents_info',''))
        if not assignee:
            continue
        # skip UNIV CALIFORNIA itself
        if 'UNIV CALIFORNIA' in assignee:
            continue
        # parse cpc JSON to get primary codes where first==true
        cpc_field = r.get('cpc')
        primary_codes = []
        try:
            cpcs = json.loads(cpc_field) if isinstance(cpc_field, str) else cpc_field
        except Exception:
            try:
                cpcs = json.loads(cpc_field.replace("'","\""))
            except Exception:
                cpcs = []
        if isinstance(cpcs, list):
            for entry in cpcs:
                if isinstance(entry, dict) and entry.get('first'):
                    code = entry.get('code')
                    if code:
                        primary_codes.append(code)
                        unique_primary_cpcs.add(code)
        # If no primary codes found, consider taking first code as fallback
        if not primary_codes and isinstance(cpcs, list) and len(cpcs)>0:
            code = cpcs[0].get('code') if isinstance(cpcs[0], dict) else None
            if code:
                primary_codes.append(code)
                unique_primary_cpcs.add(code)
        results.append({'assignee': assignee, 'primary_cpcs': primary_codes})

# Prepare output
output = {'mappings': results, 'unique_primary_cpcs': sorted(unique_primary_cpcs)}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_JmtpD4VJGFoecQO8VCX0zY1M': 'file_storage/call_JmtpD4VJGFoecQO8VCX0zY1M.json', 'var_call_UCPD1RS4AZvlswJyAis5URH1': 'file_storage/call_UCPD1RS4AZvlswJyAis5URH1.json', 'var_call_TXF5iLgHVwuGHi0geYBudpqL': 'file_storage/call_TXF5iLgHVwuGHi0geYBudpqL.json'}

exec(code, env_args)
