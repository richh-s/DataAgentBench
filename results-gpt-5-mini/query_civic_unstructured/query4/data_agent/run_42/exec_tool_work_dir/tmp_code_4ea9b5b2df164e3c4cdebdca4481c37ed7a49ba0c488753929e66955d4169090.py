code = """import json, re
# Load the large query results from storage file paths
civic_docs_path = var_call_qrxdi8MefnVrm43FVD6CrZIe
funding_path = var_call_jT5oagEZBOoolzpHj5J7r31Y
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Build list of funding project records with numeric amounts
funding_records = []
for r in funding:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_int = int(amt)
    except:
        # try to clean commas or strings
        amt_clean = re.sub(r"[^0-9]","", str(amt))
        amt_int = int(amt_clean) if amt_clean else 0
    funding_records.append({'Project_Name': name, 'Amount': amt_int})

# Prepare a set of indicator patterns for Spring 2022
indicators = [
    'spring 2022','2022-spring','2022 spring','2022 S','spring 2022',
    'march 2022','mar 2022','03-2022','2022-03','03/2022','2022/03',
    'april 2022','apr 2022','04-2022','2022-04','04/2022','2022/04',
    'may 2022','may. 2022','05-2022','2022-05','05/2022','2022/05'
]
# Lower-case indicators for search
indicators = [s.lower() for s in indicators]

# Helper to normalize names for searching
def normalize_text(s):
    return re.sub(r'\s+',' ', re.sub(r'[^a-z0-9 ]',' ', s.lower())).strip()

# Build civic text corpus
texts = []
for doc in civic_docs:
    txt = doc.get('text','')
    if txt:
        texts.append(txt.lower())

# For faster search, join texts with separators but keep originals in list
# We'll search each funding project in all docs
matched_projects = {}
for rec in funding_records:
    pname = rec['Project_Name']
    if not pname or not isinstance(pname,str):
        continue
    pname_norm = pname.lower()
    # create variants: original, remove parenthesis content, remove ' project' suffix
    variants = set([pname_norm])
    # remove parenthesis content
    variants.add(re.sub(r"\s*\(.*?\)\s*"," ", pname_norm).strip())
    # remove trailing word 'project'
    variants.add(re.sub(r"\bproject\b","", pname_norm).strip())
    variants.add(re.sub(r"\bproject\b","", variants.pop() if variants else pname_norm).strip())
    # also normalized no punctuation
    norm_variants = [normalize_text(v) for v in variants if v]
    # ensure unique
    norm_variants = list(set(norm_variants))
    found = False
    for doc_text in texts:
        for v in norm_variants:
            if not v:
                continue
            if v in doc_text:
                # find index positions
                for m in re.finditer(re.escape(v), doc_text):
                    start = max(0, m.start()-300)
                    end = m.end()+300
                    context = doc_text[start:end]
                    # check indicators
                    for ind in indicators:
                        if ind in context:
                            # matched as spring 2022
                            matched_projects[pname] = matched_projects.get(pname, 0) + rec['Amount']
                            found = True
                            break
                    if found:
                        break
            if found:
                break
        if found:
            break

# Now matched_projects contains funding records grouped by exact funding Project_Name
# But there may be multiple funding entries for same project name; handled by summing when inserted
count_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

# As fallback, also try to detect projects that have 'begin construction: spring 2022' etc in docs
# Search docs for patterns like '\n<PROJECT_NAME>\n...Begin Construction: Spring 2022' where project name is a heading line followed by schedule lines
# We'll attempt to extract headings followed by 'Begin Construction' with spring 2022
additional_matches = {}
pattern = re.compile(r"([A-Z][A-Za-z0-9 \-\'\&\.,]{5,80})\n(?:.*?\n){0,6}.*?(begin construction|advertise|advertise:|complete design|project schedule).{0,60}spring 2022", re.IGNORECASE)
for doc in civic_docs:
    txt = doc.get('text','')
    if not txt:
        continue
    for m in pattern.finditer(txt):
        heading = m.group(1).strip()
        # try to match this heading to funding projects
        heading_norm = normalize_text(heading)
        for rec in funding_records:
            fn = normalize_text(rec['Project_Name'])
            if heading_norm and heading_norm in fn or fn in heading_norm:
                additional_matches[rec['Project_Name']] = additional_matches.get(rec['Project_Name'],0) + rec['Amount']

# Merge additional matches
for k,v in additional_matches.items():
    if k not in matched_projects:
        matched_projects[k] = v

count_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

import json as _json
result = {'count_projects': count_projects, 'total_funding': total_funding, 'matched_project_names': list(matched_projects.keys())}
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_K0qOAkDO0eMnPuC9jQV6Bh9k': ['civic_docs'], 'var_call_QS4lmyqnhrpagIUstZ0h0XcG': ['Funding'], 'var_call_qrxdi8MefnVrm43FVD6CrZIe': 'file_storage/call_qrxdi8MefnVrm43FVD6CrZIe.json', 'var_call_jT5oagEZBOoolzpHj5J7r31Y': 'file_storage/call_jT5oagEZBOoolzpHj5J7r31Y.json'}

exec(code, env_args)
