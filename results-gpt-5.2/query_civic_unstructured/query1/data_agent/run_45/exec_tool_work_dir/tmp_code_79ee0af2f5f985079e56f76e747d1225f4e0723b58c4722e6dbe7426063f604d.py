code = """import json, re

proj_data = var_call_TGwgMLCsc1cvaGLsZvTYfkDZ
if isinstance(proj_data, str):
    with open(proj_data, 'r', encoding='utf-8') as f:
        proj_data = json.load(f)
funded_projects = sorted({r.get('Project_Name') for r in proj_data if r.get('Project_Name')})

civic_data = var_call_pUWrc4nGE400VtRszaqL5AOB
if isinstance(civic_data, str):
    with open(civic_data, 'r', encoding='utf-8') as f:
        civic_data = json.load(f)
texts = [d.get('text') or '' for d in civic_data]
combined_text = "\n".join(texts)

header_pat = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
end_pat_str = r"Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects"
end_pat = re.compile(end_pat_str, re.IGNORECASE)

headers = [m.start() for m in header_pat.finditer(combined_text)]

design_texts = []
for hs in headers:
    tail = combined_text[hs:hs+20000]
    em = end_pat.search(tail, 1)
    design_texts.append(tail[:em.start()] if em else tail)

design_blob = "\n".join(design_texts)
blob_low = re.sub(r"\s+", " ", design_blob).lower()

def in_design(p):
    p_norm = re.sub(r"\s+", " ", p).strip().lower()
    return bool(p_norm) and (p_norm in blob_low)

design_funded = sorted({p for p in funded_projects if in_design(p)})

result = {"count": int(len(design_funded)), "projects": design_funded}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HQA2CkSbk6hx2lHjvSJtc0q8': [{'cnt': '276'}], 'var_call_pUWrc4nGE400VtRszaqL5AOB': 'file_storage/call_pUWrc4nGE400VtRszaqL5AOB.json', 'var_call_TGwgMLCsc1cvaGLsZvTYfkDZ': 'file_storage/call_TGwgMLCsc1cvaGLsZvTYfkDZ.json'}

exec(code, env_args)
