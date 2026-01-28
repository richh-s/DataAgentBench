code = """import json, re, os
# Load the query results from the provided storage file paths
with open(var_call_IkHKtTihYjPSZo8aZpBDmyFU, 'r') as f:
    funding = json.load(f)
with open(var_call_c6lEJx4mdV92C2C8eH4Z8cxt, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records (ensure types)
for r in funding:
    # ensure Amount as int
    try:
        r['Amount'] = int(r.get('Amount') if r.get('Amount') is not None else 0)
    except:
        try:
            r['Amount'] = int(float(r.get('Amount')))
        except:
            r['Amount'] = None

# Helper to strip parenthetical suffixes for matching
def normalize_name(name):
    if name is None:
        return ''
    # remove trailing parenthetical like ' (FEMA Project)'
    return re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()

# Build combined civic text
combined_text = "\n\n".join(d.get('text','') for d in civic_docs)
combined_text_lower = combined_text.lower()

# Determine relevant funding records: those related to FEMA or emergency
relevant = []
for r in funding:
    pname = r.get('Project_Name','')
    pname_lower = pname.lower()
    norm = normalize_name(pname)
    norm_lower = norm.lower()
    if ("fema" in pname_lower) or ("fema" in norm_lower) or ("emergency" in pname_lower) or ("emergency" in norm_lower) or ("warning" in pname_lower) or ("sirens" in pname_lower) or ("outdoor warning" in pname_lower) or ("outdoor warning" in norm_lower):
        # attempt to find status from civic docs by searching for normalized name
        status = None
        # search for several variants
        search_terms = [norm, pname]
        found_at = -1
        for term in search_terms:
            if term and term.lower() in combined_text_lower:
                found_at = combined_text_lower.find(term.lower())
                break
        # if not found, try matching shorter tokens
        if found_at == -1:
            # try splitting norm into pieces and search
            parts = [p for p in re.split(r"[,:\-\(\)]", norm) if p.strip()]
            for part in parts:
                if part.strip().lower() in combined_text_lower and len(part.strip())>4:
                    found_at = combined_text_lower.find(part.strip().lower())
                    break
        # classify status from nearby context
        if found_at != -1:
            start = max(0, found_at-500)
            end = min(len(combined_text_lower), found_at+500)
            context = combined_text[start:end].lower()
            if re.search(r"construction was completed|complete construction|notice of completion|completed,|completed\b", context):
                status = 'completed'
            elif re.search(r"capital improvement projects \(not started\)|not started|not begun|identified but not begun", context):
                status = 'not started'
            else:
                # default to design for planning/in-progress/awaiting approval
                status = 'design'
        else:
            # fallback classification using project name cues
            if re.search(r"not started", pname_lower):
                status = 'not started'
            elif re.search(r"completed|completion|complete", pname_lower):
                status = 'completed'
            else:
                status = 'design'
        relevant.append({
            'Project_Name': r.get('Project_Name'),
            'Funding_Source': r.get('Funding_Source'),
            'Amount': r.get('Amount'),
            'Status': status
        })

# Additionally, include projects mentioned in civic docs that reference FEMA/emergency but may not have explicit FEMA in funding table
# We'll scan civic docs for project headings that include 'fema' or 'emergency' or 'warning' or 'sirens' and try to match funding by normalized names
extra_names = set()
for match in re.finditer(r"^([A-Za-z0-9 '\-&(),]+)\n\n\(cid:190\) Updates:", combined_text, flags=re.MULTILINE):
    heading = match.group(1).strip()
    if any(k in heading.lower() for k in ['fema','emergency','warning','sirens','outdoor warning','outdoor']):
        extra_names.add(heading)
# Also look for lines like 'Outdoor Warning Signs' etc.
for line in combined_text.splitlines():
    line_s = line.strip()
    if len(line_s)>3 and any(k in line_s.lower() for k in ['outdoor warning','sirens','emergency','fema']):
        extra_names.add(line_s)

# Try to find funding matches for extra_names
for en in extra_names:
    # try to match to funding records by normalized substring
    matched = False
    en_norm = en.lower()
    for r in funding:
        if r.get('Project_Name') and normalize_name(r.get('Project_Name')).lower() in en_norm or en_norm in normalize_name(r.get('Project_Name')).lower():
            matched = True
            # check if already included
            if not any(x['Project_Name']==r.get('Project_Name') for x in relevant):
                # determine status from civic docs
                found_at = combined_text_lower.find(en_norm)
                status = 'design'
                if found_at!=-1:
                    start = max(0, found_at-500); end = min(len(combined_text_lower), found_at+500)
                    context = combined_text[start:end].lower()
                    if re.search(r"construction was completed|complete construction|notice of completion|completed,|completed\b", context):
                        status = 'completed'
                    elif re.search(r"capital improvement projects \(not started\)|not started|not begun|identified but not begun", context):
                        status = 'not started'
                    else:
                        status = 'design'
                relevant.append({
                    'Project_Name': r.get('Project_Name'),
                    'Funding_Source': r.get('Funding_Source'),
                    'Amount': r.get('Amount'),
                    'Status': status
                })
    # if no funding match, add with null funding info
    if not matched:
        # determine status from civic docs
        found_at = combined_text_lower.find(en_norm)
        status = 'design'
        if found_at!=-1:
            start = max(0, found_at-500); end = min(len(combined_text_lower), found_at+500)
            context = combined_text[start:end].lower()
            if re.search(r"construction was completed|complete construction|notice of completion|completed,|completed\b", context):
                status = 'completed'
            elif re.search(r"capital improvement projects \(not started\)|not started|not begun|identified but not begun", context):
                status = 'not started'
            else:
                status = 'design'
        if not any(x['Project_Name']==en for x in relevant):
            relevant.append({
                'Project_Name': en,
                'Funding_Source': None,
                'Amount': None,
                'Status': status
            })

# Deduplicate by Project_Name keeping first
seen = set(); cleaned = []
for r in relevant:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name']); cleaned.append(r)

# Sort by Project_Name
cleaned = sorted(cleaned, key=lambda x: (x['Project_Name'] or '').lower())

# Output JSON string
result_str = json.dumps(cleaned)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_IkHKtTihYjPSZo8aZpBDmyFU': 'file_storage/call_IkHKtTihYjPSZo8aZpBDmyFU.json', 'var_call_c6lEJx4mdV92C2C8eH4Z8cxt': 'file_storage/call_c6lEJx4mdV92C2C8eH4Z8cxt.json'}

exec(code, env_args)
