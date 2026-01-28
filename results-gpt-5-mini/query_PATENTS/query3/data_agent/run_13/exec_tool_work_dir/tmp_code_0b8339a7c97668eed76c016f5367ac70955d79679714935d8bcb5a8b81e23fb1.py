code = """import json
import re

# load data from previous tool calls
data_uc = json.loads(open(var_call_WQS6C0FIkO1PLo7yWplRnL1r).read())
data_cited = json.loads(open(var_call_e9K9FC2cSeE9c7PgDhih3Vwy).read())

# Extract publication numbers for UNIV CALIFORNIA
pub_nums_uc = set()
for rec in data_uc:
    pi = rec.get('Patents_info','')
    # look for patterns like 'pub. number ...', 'publication number ...', 'publication number ...'
    m = re.search(r'(?:pub\.|publication)\s*number\s*[:]?\s*([A-Z0-9\-]+)', pi, flags=re.IGNORECASE)
    if not m:
        # sometimes 'with pub. number' or 'has publication number'
        m = re.search(r'pub\.?\s*number\s*([A-Z0-9\-]+)', pi, flags=re.IGNORECASE)
    if not m:
        m = re.search(r'publication\s*number\s*([A-Z0-9\-]+)', pi, flags=re.IGNORECASE)
    if m:
        pub = m.group(1).strip().rstrip('.')
        pub_nums_uc.add(pub)

# also try to find patterns like 'with pub. number TW-201925402-A.' which earlier matches
# If none found, try searching for tokens like 'pub. number' elsewhere

# Helper to parse citation JSON string

def parse_json_field(s):
    try:
        return json.loads(s)
    except Exception:
        # try to fix common trailing commas or single quotes
        s2 = s.replace("'", '"')
        try:
            return json.loads(s2)
        except Exception:
            return []

# Helper to extract assignee from Patents_info
assignee_regex = re.compile(r'^(.*?)\s+(?:holds|held|is assigned to|is owned by|assigned to|owns|owned by|has|has publication number|has pub\.|with pub\.|with publication)', flags=re.IGNORECASE)

assignee_to_codes = {}
all_codes = set()

for rec in data_cited:
    citations = parse_json_field(rec.get('citation','[]'))
    cited_pubs = {c.get('publication_number','') for c in citations if c.get('publication_number')}
    # check intersection
    if pub_nums_uc & cited_pubs:
        # this record cites a UNIV CALIFORNIA patent
        pi = rec.get('Patents_info','')
        m = assignee_regex.search(pi)
        if m:
            assignee = m.group(1).strip()
        else:
            # fallback: take up to first comma
            assignee = pi.split(',')[0].strip()
        assignee = assignee.upper()
        if assignee == 'UNIV CALIFORNIA':
            continue
        # parse cpc field
        cpcs = parse_json_field(rec.get('cpc','[]'))
        primary_codes = []
        for c in cpcs:
            try:
                if c.get('first'):
                    code = c.get('code')
                    if code:
                        primary_codes.append(code)
            except Exception:
                pass
        if not primary_codes and cpcs:
            # fallback: take first code entry
            code = cpcs[0].get('code')
            if code:
                primary_codes.append(code)
        if primary_codes:
            if assignee not in assignee_to_codes:
                assignee_to_codes[assignee] = set()
            for code in primary_codes:
                assignee_to_codes[assignee].add(code)
                all_codes.add(code)

# convert sets to lists
assignee_to_codes = {k: sorted(list(v)) for k,v in assignee_to_codes.items()}
all_codes = sorted(list(all_codes))

output = {'assignee_to_codes': assignee_to_codes, 'codes': all_codes}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_RQE78oOVxD82z54dvi4GCBdC': 'file_storage/call_RQE78oOVxD82z54dvi4GCBdC.json', 'var_call_WQS6C0FIkO1PLo7yWplRnL1r': 'file_storage/call_WQS6C0FIkO1PLo7yWplRnL1r.json', 'var_call_e9K9FC2cSeE9c7PgDhih3Vwy': 'file_storage/call_e9K9FC2cSeE9c7PgDhih3Vwy.json', 'var_call_0iVQSPpbanCFSC8TDBFm8T8y': 'file_storage/call_0iVQSPpbanCFSC8TDBFm8T8y.json'}

exec(code, env_args)
