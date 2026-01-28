code = """import json, re

# Load funding project names > 50000
proj_data = var_call_TGwgMLCsc1cvaGLsZvTYfkDZ
if isinstance(proj_data, str):
    with open(proj_data, 'r', encoding='utf-8') as f:
        proj_data = json.load(f)
funded_projects = sorted({r['Project_Name'] for r in proj_data if r.get('Project_Name')})

# Load civic docs
civic_data = var_call_pUWrc4nGE400VtRszaqL5AOB
if isinstance(civic_data, str):
    with open(civic_data, 'r', encoding='utf-8') as f:
        civic_data = json.load(f)
texts = [d.get('text','') or '' for d in civic_data]
combined_text = "\n".join(texts)

# Identify projects that are explicitly listed under "Capital Improvement Projects (Design)"
# We'll search within windows after that header.
header_pat = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
headers = [m.start() for m in header_pat.finditer(combined_text)]

# Window until next section header (Construction/Not Started/Disaster) or 4000 chars
end_pat = re.compile(r"Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects", re.IGNORECASE)

design_texts = []
for hs in headers:
    tail = combined_text[hs:hs+20000]
    em = end_pat.search(tail, 1)
    if em:
        design_texts.append(tail[:em.start()])
    else:
        design_texts.append(tail)

design_blob = "\n".join(design_texts)

# Determine which funded projects appear in design section.
# Use case-insensitive substring match; also try to normalize whitespace.
blob_low = re.sub(r"\s+", " ", design_blob).lower()

def in_design(p):
    p_norm = re.sub(r"\s+", " ", p).strip().lower()
    if not p_norm:
        return False
    return p_norm in blob_low

design_funded = [p for p in funded_projects if in_design(p)]

result = {
    "count": int(len(set(design_funded))),
    "projects": sorted(set(design_funded))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HQA2CkSbk6hx2lHjvSJtc0q8': [{'cnt': '276'}], 'var_call_pUWrc4nGE400VtRszaqL5AOB': 'file_storage/call_pUWrc4nGE400VtRszaqL5AOB.json', 'var_call_TGwgMLCsc1cvaGLsZvTYfkDZ': 'file_storage/call_TGwgMLCsc1cvaGLsZvTYfkDZ.json'}

exec(code, env_args)
