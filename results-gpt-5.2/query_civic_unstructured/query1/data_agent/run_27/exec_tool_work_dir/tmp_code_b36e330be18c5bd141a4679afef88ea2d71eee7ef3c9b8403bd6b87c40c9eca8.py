code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

civic_docs = load_json_maybe(var_call_K8M3hThoENRlQEZ44Flc2vL8)
funding_projects = load_json_maybe(var_call_jrkxjDgMNeHiYJw62UrmDpBt)
funding_set = {r.get('Project_Name') for r in funding_projects}
funding_set.discard(None)

section_start_re = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
section_end_re = re.compile(r"Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects|\n\s*Page\s+\d+\s+of\s+\d+", re.IGNORECASE)

bad_line_re = re.compile(r"^(Updates|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|Page\s+\d+\s+of\s+\d+)\b", re.IGNORECASE)

project_names_design = set()

for doc in civic_docs:
    text = doc.get('text') or ''
    m = section_start_re.search(text)
    if not m:
        continue
    sub = text[m.end():]
    endm = section_end_re.search(sub)
    if endm:
        sub = sub[:endm.start()]

    for line in sub.splitlines():
        ln = line.strip()
        if not ln:
            continue
        ln = ln.strip('•*-')
        ln = ln.strip()
        if not ln:
            continue
        if bad_line_re.search(ln):
            continue
        if re.match(r"^(Complete Design|Advertise|Begin Construction|Final Design|Begin construction|Complete Construction)\s*:\s*", ln, flags=re.IGNORECASE):
            continue
        if len(ln) < 4:
            continue
        if re.search(r"\bProjects\b", ln, flags=re.IGNORECASE) and '(' in ln and ')' in ln:
            continue
        ln = ln.rstrip(' .')
        if ln in funding_set:
            project_names_design.add(ln)

out = {
    "count": len(project_names_design),
    "project_names": sorted(project_names_design)
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_2Sxtww5u6YXWOmWX3fP8VYjS': [{'cnt': '276'}], 'var_call_K8M3hThoENRlQEZ44Flc2vL8': 'file_storage/call_K8M3hThoENRlQEZ44Flc2vL8.json', 'var_call_jrkxjDgMNeHiYJw62UrmDpBt': 'file_storage/call_jrkxjDgMNeHiYJw62UrmDpBt.json'}

exec(code, env_args)
