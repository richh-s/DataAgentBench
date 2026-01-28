code = """import json, re, string
# Load results from storage file paths
with open(var_call_df8qViYTCLLtXU81Hgz3TO1e, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_jpv42uLhPUQHHm66rydnByEb, 'r') as f:
    funding_records = json.load(f)

# Filter funding records Amount > 50000
funding_filtered = [r for r in funding_records if int(r.get('Amount', 0)) > 50000]

# Simple cleaning function
def clean_name(s):
    if s is None:
        return ''
    s = s.lower()
    # remove parenthetical suffixes
    s = re.sub(r"\([^)]*\)", "", s)
    # replace punctuation with space
    s = ''.join(ch if ch.isalnum() or ch.isspace() else ' ' for ch in s)
    s = re.sub(r'\s+', ' ', s).strip()
    # remove common filler words
    fillers = ['project','projects','improvements','repair','repairs','infrastructure','phase','design','construction','project:', 'project -']
    for w in fillers:
        s = re.sub(r'\b' + re.escape(w) + r'\b', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Extract design section(s) from civic docs
design_sections = []
for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    marker = 'capital improvement projects (design)'
    idx = lower.find(marker)
    if idx == -1:
        continue
    # find end marker
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)']
    end_idx = None
    for em in end_markers:
        j = lower.find(em, idx+1)
        if j != -1:
            end_idx = j
            break
    section = text[idx:end_idx] if end_idx else text[idx:]
    design_sections.append(section)

# From sections, extract candidate project titles: look for lines that look like titles
design_titles = set()
for sec in design_sections:
    # split into paragraphs
    paras = re.split(r'\n\s*\n', sec)
    for p in paras:
        lines = [L.strip() for L in p.splitlines() if L.strip()]
        if not lines:
            continue
        # often the first non-empty line is the title
        candidate = lines[0]
        # filter out headings
        low = candidate.lower()
        if any(k in low for k in ['capital improvement','agenda','page','item','recommended action','discussion','updates','project schedule']):
            continue
        # further filter: must contain letters and be reasonable length
        if len(candidate) < 5 or len(candidate) > 200:
            continue
        # avoid lines that are sentences (contain ':' or start with '(')
        if ':' in candidate:
            # sometimes titles include ':' but skip
            pass
        design_titles.add(candidate)

# Clean titles
clean_design = {t: clean_name(t) for t in design_titles}

# Clean funding names
funding_names = [r['Project_Name'] for r in funding_filtered]
clean_funding = {n: clean_name(n) for n in funding_names}

# Matching function
def jaccard(a,b):
    sa = set(a.split()) if a else set()
    sb = set(b.split()) if b else set()
    if not sa and not sb:
        return 0.0
    inter = sa & sb
    uni = sa | sb
    return len(inter)/len(uni) if uni else 0.0

matched = []
for fname, fclean in clean_funding.items():
    found = False
    match_title = None
    for dtitle, dclean in clean_design.items():
        if not fclean or not dclean:
            continue
        # direct substring
        if fclean and dclean and (fclean in dclean or dclean in fclean):
            found = True
            match_title = dtitle
            break
        # token similarity
        if jaccard(fclean, dclean) >= 0.5:
            found = True
            match_title = dtitle
            break
    if found:
        amt = int([r for r in funding_filtered if r['Project_Name']==fname][0]['Amount'])
        matched.append({'Funding_Project': fname, 'Matched_Design_Title': match_title, 'Amount': amt})

# Deduplicate by funding project
unique = {m['Funding_Project']: m for m in matched}
count = len(unique)

result = {'count': count, 'matched_projects': list(unique.values())}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cpU66Y0nmO07pRNq09LTN6Bj': ['civic_docs'], 'var_call_jVRqXM2AtLoY3dT6tx43Xuuv': ['Funding'], 'var_call_df8qViYTCLLtXU81Hgz3TO1e': 'file_storage/call_df8qViYTCLLtXU81Hgz3TO1e.json', 'var_call_jpv42uLhPUQHHm66rydnByEb': 'file_storage/call_jpv42uLhPUQHHm66rydnByEb.json'}

exec(code, env_args)
