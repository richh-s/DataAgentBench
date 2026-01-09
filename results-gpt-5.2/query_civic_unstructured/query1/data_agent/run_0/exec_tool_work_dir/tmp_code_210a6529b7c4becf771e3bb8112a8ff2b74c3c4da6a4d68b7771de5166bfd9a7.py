code = """import json, re

# Load projects with funding > 50k
p = var_call_1gW8ECGjCuakNW2RfxyBUgJf
if isinstance(p, str):
    with open(p, 'r', encoding='utf-8') as f:
        p = json.load(f)
projects = sorted({r.get('Project_Name','').strip() for r in p if r.get('Project_Name')})

# Load civic docs
docs = var_call_9p2230LU7CbfnxTL1hXiE4AK
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

text_all = "\n".join(d.get('text','') for d in docs)
text_all_norm = re.sub(r"\s+", " ", text_all).lower()

# Determine if a project is in a 'design' context by keyword proximity

def is_design(project_name):
    pn_norm = re.sub(r"\s+", " ", project_name.strip()).lower()
    if not pn_norm:
        return False
    for m in re.finditer(re.escape(pn_norm), text_all_norm):
        start = max(0, m.start() - 500)
        end = min(len(text_all_norm), m.end() + 500)
        window = text_all_norm[start:end]
        if ("projects (design)" in window or "(design)" in window or "design phase" in window or
            "finalize the design" in window or "complete design" in window or "final design" in window):
            return True
    return False

design_projects = [pn for pn in projects if is_design(pn)]

result = {"count": int(len(design_projects))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_SdiyWBajstL6GZS2jGvuy3w1': [{'cnt': '276'}], 'var_call_9p2230LU7CbfnxTL1hXiE4AK': 'file_storage/call_9p2230LU7CbfnxTL1hXiE4AK.json', 'var_call_1gW8ECGjCuakNW2RfxyBUgJf': 'file_storage/call_1gW8ECGjCuakNW2RfxyBUgJf.json'}

exec(code, env_args)
