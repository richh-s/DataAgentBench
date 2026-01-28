code = """import json, re

# Load the query_db JSON result from storage
with open(var_call_HmKEPxHFYVCDxkTNVoAewSKJ, 'r', encoding='utf-8') as f:
    records = json.load(f)

assignee_to_codes = {}
all_codes = set()

patterns = [
    re.compile(r'belonging to ([A-Z0-9 &\.-]{3,100}?)(?:\s|,|\.|and|has)', re.IGNORECASE),
    re.compile(r'is assigned to ([A-Z0-9 &\.-]{3,100}?)(?:\s|,|\.|and|has)', re.IGNORECASE),
    re.compile(r'belongs to ([A-Z0-9 &\.-]{3,100}?)(?:\s|,|\.|and|has)', re.IGNORECASE),
    re.compile(r'assignee[:=]\s*([A-Z0-9 &\.-]{3,100}?)\b', re.IGNORECASE),
    re.compile(r'assignee_harmonized[:=]\s*([A-Z0-9 &\.-]{3,100}?)\b', re.IGNORECASE),
]

for rec in records:
    pat_info = rec.get('Patents_info') or ''
    assignee = None
    for p in patterns:
        m = p.search(pat_info)
        if m:
            assignee = m.group(1).strip()
            break
    if not assignee:
        # fallback: try to find a sequence of uppercase words of length >=3
        m = re.search(r'([A-Z][A-Z0-9&\./\-]{2,}(?:\s+[A-Z][A-Z0-9&\./\-]{2,})*)', pat_info)
        if m:
            assignee = m.group(1).strip()
        else:
            assignee = 'UNKNOWN'

    # normalize whitespace
    assignee = re.sub(r'\s+', ' ', assignee)

    # parse cpc field (it's a JSON-like string)
    codes = []
    cpc_field = rec.get('cpc')
    if cpc_field:
        try:
            cpc_list = json.loads(cpc_field)
        except Exception:
            # try to fix single quotes
            try:
                cpc_list = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                cpc_list = []
        if isinstance(cpc_list, list) and cpc_list:
            first_codes = [entry.get('code') for entry in cpc_list if entry.get('first')]
            # filter None
            first_codes = [c for c in first_codes if c]
            if first_codes:
                codes = first_codes
            else:
                # take first entry code
                code0 = cpc_list[0].get('code')
                if code0:
                    codes = [code0]

    # add to mapping
    if assignee.upper() == 'UNIV CALIFORNIA' or 'UNIV CALIFORNIA' in assignee.upper():
        # skip citing assignee UNIV CALIFORNIA
        continue

    if assignee not in assignee_to_codes:
        assignee_to_codes[assignee] = set()
    for c in codes:
        assignee_to_codes[assignee].add(c)
        all_codes.add(c)

# convert sets to lists
assignee_to_codes_list = {k: sorted([c for c in v if c]) for k, v in assignee_to_codes.items()}
all_codes_list = sorted([c for c in all_codes if c])

output = {
    'assignee_to_codes': assignee_to_codes_list,
    'codes': all_codes_list
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_HmKEPxHFYVCDxkTNVoAewSKJ': 'file_storage/call_HmKEPxHFYVCDxkTNVoAewSKJ.json'}

exec(code, env_args)
