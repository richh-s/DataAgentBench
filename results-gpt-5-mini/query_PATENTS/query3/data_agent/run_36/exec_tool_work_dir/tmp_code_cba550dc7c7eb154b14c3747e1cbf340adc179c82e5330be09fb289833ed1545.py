code = """import json, re
# Load stored query results
with open(var_call_Ow9DeaE9wDuFRl2s0DGnZKEU, 'r') as f:
    uc_records = json.load(f)
with open(var_call_extKKtbNjMJuiqaFvagK1ONA, 'r') as f:
    cited_records = json.load(f)

# Extract publication numbers for UNIV CALIFORNIA patents from Patents_info
uc_pubnums = set()
pubnum_regex = re.compile(r'([A-Z]{2}-[0-9]{4,}[A-Z0-9\-]*)')
for rec in uc_records:
    pi = rec.get('Patents_info','')
    matches = pubnum_regex.findall(pi)
    for m in matches:
        uc_pubnums.add(m.strip())

# Fallback: also look into title_localized maybe contains pub number? but skip
uc_pubnums = set([u for u in uc_pubnums if '-' in u])

# Parse cited_records citations and find those that cite any UC pubnum
citing_matches = []
for rec in cited_records:
    citation = rec.get('citation','')
    if not citation or citation.strip() == '[]':
        continue
    try:
        cited_list = json.loads(citation)
    except Exception:
        # try to fix single quotes
        try:
            cited_list = json.loads(citation.replace("'", '"'))
        except Exception:
            cited_list = []
    cited_pubnums = [c.get('publication_number','').strip() for c in cited_list if c.get('publication_number')]
    # check intersection
    inter = set(cited_pubnums) & uc_pubnums
    if inter:
        # extract assignee heuristically from Patents_info
        pi = rec.get('Patents_info','')
        assignee = None
        # patterns
        m = re.match(r'^\s*([^,\.]+?)\s+(?:holds|owns|has)\b', pi, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
        if not assignee:
            m = re.search(r'is assigned to\s+([^,\.]+)', pi, re.IGNORECASE)
            if m:
                assignee = m.group(1).strip()
        if not assignee:
            m = re.search(r'is owned by\s+([^,\.]+)', pi, re.IGNORECASE)
            if m:
                assignee = m.group(1).strip()
        if not assignee:
            m = re.search(r'holds the .*?\), with publication number', pi, re.IGNORECASE)
            if m:
                # grab leading token
                m2 = re.match(r'^\s*([^,\.]+?)\s+', pi)
                if m2:
                    assignee = m2.group(1).strip()
        if not assignee:
            # fallback: take up to 'holds' or 'with' or first parenthesis
            m = re.split(r'\bholds\b|\bwith\b|\(|,', pi, 1)
            if m and m[0].strip():
                assignee = m[0].strip()
            else:
                assignee = pi.strip()
        # parse cpc codes
        cpc_field = rec.get('cpc','')
        codes = []
        try:
            cpc_list = json.loads(cpc_field)
        except Exception:
            try:
                cpc_list = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                cpc_list = []
        for c in cpc_list:
            if isinstance(c, dict) and c.get('first'):
                code = c.get('code')
                if code:
                    codes.append(code.strip())
        # if no primary flagged, take first code if exists
        if not codes and cpc_list:
            for c in cpc_list:
                if isinstance(c, dict) and c.get('code'):
                    codes.append(c.get('code').strip())
                    break
        citing_matches.append({
            'rowid': rec.get('rowid'),
            'assignee_extracted': assignee,
            'codes': codes,
            'cited_uc_pubnums': list(inter),
            'Patents_info': rec.get('Patents_info')
        })

# Unique codes
unique_codes = sorted({code for rec in citing_matches for code in rec['codes'] if code})

output = {'uc_pubnums': sorted(list(uc_pubnums)), 'unique_codes': unique_codes, 'citing_matches': citing_matches}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Ow9DeaE9wDuFRl2s0DGnZKEU': 'file_storage/call_Ow9DeaE9wDuFRl2s0DGnZKEU.json', 'var_call_extKKtbNjMJuiqaFvagK1ONA': 'file_storage/call_extKKtbNjMJuiqaFvagK1ONA.json'}

exec(code, env_args)
