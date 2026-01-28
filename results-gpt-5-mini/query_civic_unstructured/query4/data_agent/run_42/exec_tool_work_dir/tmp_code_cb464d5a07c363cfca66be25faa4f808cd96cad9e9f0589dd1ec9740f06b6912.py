code = """import json, re
# Load data files from storage keys
civic_docs_path = var_call_qrxdi8MefnVrm43FVD6CrZIe
funding_path = var_call_jT5oagEZBOoolzpHj5J7r31Y
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize and parse funding amounts
funding_records = []
for r in funding:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_int = int(amt)
    except Exception:
        amt_clean = re.sub(r"[^0-9]", "", str(amt))
        amt_int = int(amt_clean) if amt_clean else 0
    funding_records.append({'Project_Name': name, 'Amount': amt_int})

# Indicators for Spring 2022 (lowercase)
indicators = [
    'spring 2022','2022-spring','2022 spring','march 2022','mar 2022','2022-03','2022/03','03-2022','03/2022',
    'april 2022','apr 2022','2022-04','2022/04','04-2022','04/2022',
    'may 2022','may. 2022','2022-05','2022/05','05-2022','05/2022'
]
indicators = [s.lower() for s in indicators]

# Helper normalize
def normalize_text(s):
    if not s:
        return ''
    s2 = s.lower()
    s2 = re.sub(r"\(.*?\)", "", s2)
    s2 = re.sub(r"[^a-z0-9 ]", " ", s2)
    s2 = re.sub(r"\s+", " ", s2).strip()
    return s2

# Prepare document texts lowercased
doc_texts = [doc.get('text','').lower() for doc in civic_docs if doc.get('text')]

matched = {}

for rec in funding_records:
    pname = rec['Project_Name']
    if not pname or not isinstance(pname, str):
        continue
    variants = set()
    variants.add(pname.lower())
    variants.add(re.sub(r"\(.*?\)", "", pname.lower()).strip())
    variants.add(re.sub(r"\bproject\b", "", pname.lower()).strip())
    norm_variants = [normalize_text(v) for v in variants if v]
    norm_variants = list(set([v for v in norm_variants if v]))
    found_flag = False
    for vt in norm_variants:
        for doc in doc_texts:
            if vt in doc:
                # find positions
                for m in re.finditer(re.escape(vt), doc):
                    start = max(0, m.start()-300)
                    end = m.end()+300
                    context = doc[start:end]
                    for ind in indicators:
                        if ind in context:
                            matched[pname] = matched.get(pname, 0) + rec['Amount']
                            found_flag = True
                            break
                    if found_flag:
                        break
            if found_flag:
                break
        if found_flag:
            break

count_projects = len(matched)
total_funding = sum(matched.values())

result = {'count_projects': count_projects, 'total_funding': total_funding, 'matched_project_names': list(matched.keys())}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_K0qOAkDO0eMnPuC9jQV6Bh9k': ['civic_docs'], 'var_call_QS4lmyqnhrpagIUstZ0h0XcG': ['Funding'], 'var_call_qrxdi8MefnVrm43FVD6CrZIe': 'file_storage/call_qrxdi8MefnVrm43FVD6CrZIe.json', 'var_call_jT5oagEZBOoolzpHj5J7r31Y': 'file_storage/call_jT5oagEZBOoolzpHj5J7r31Y.json'}

exec(code, env_args)
