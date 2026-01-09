code = """import json, re

# Load large inputs

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

civic_docs = load_json_maybe(var_call_K8M3hThoENRlQEZ44Flc2vL8)
funding_projects = load_json_maybe(var_call_jrkxjDgMNeHiYJw62UrmDpBt)
funding_set = {r['Project_Name'] for r in funding_projects if r.get('Project_Name')}

# Heuristic extraction: find sections labeled "Capital Improvement Projects (Design)" and collect following project lines until next section header.
section_start_re = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
section_end_re = re.compile(r"Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects|\n\s*Page\s+\d+\s+of\s+\d+", re.IGNORECASE)

# project line: a line with letters and not starting with bullet chars, and not containing 'Updates' etc.
bad_line_re = re.compile(r"^(Updates|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|Page\s+\d+\s+of\s+\d+)\b", re.IGNORECASE)

project_names_design = set()

for doc in civic_docs:
    text = doc.get('text') or ''
    m = section_start_re.search(text)
    if not m:
        continue
    start = m.end()
    sub = text[start:]
    endm = section_end_re.search(sub)
    if endm:
        sub = sub[:endm.start()]
    # split lines
    for line in sub.splitlines():
        ln = line.strip()
        if not ln:
            continue
        # ignore bullets and symbols
        ln = ln.strip('•*-\uf0b7\uf0d8\uf0a7\uf0b0\uf0be\uf0a2\uf0a3\uf0a4\uf0a5\uf0a6\uf0a8\uf0a9\uf0aa\uf0ab\uf0ac\uf0ad\uf0ae\uf0af\uf0b1\uf0b2\uf0b3\uf0b4\uf0b5\uf0b6\uf0b8\uf0b9\uf0ba\uf0bb\uf0bc\uf0bd\uf0bf')
        if not ln:
            continue
        if bad_line_re.search(ln):
            continue
        if ':' in ln and ln.split(':',1)[0].strip().lower() in {'updates','project schedule','estimated schedule','project description'}:
            continue
        # filter out lines that are clearly schedule items
        if re.match(r"^(Complete Design|Advertise|Begin Construction|Final Design|Begin construction|Complete Construction)\s*:\s*", ln, flags=re.IGNORECASE):
            continue
        # exclude lines with mostly punctuation
        if len(ln) < 4:
            continue
        # likely project name lines often Title Case; allow numbers at start
        # stop at lines that look like section headers
        if re.search(r"\bProjects\b", ln, flags=re.IGNORECASE) and '(' in ln and ')' in ln:
            continue
        # Remove trailing periods
        ln = ln.rstrip(' .')
        # Keep only if it matches a funded project name exactly
        if ln in funding_set:
            project_names_design.add(ln)

count = len(project_names_design)

out = {
    "count": count,
    "projects": sorted(project_names_design)[:50],
    "projects_total_listed": len(project_names_design)
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_2Sxtww5u6YXWOmWX3fP8VYjS': [{'cnt': '276'}], 'var_call_K8M3hThoENRlQEZ44Flc2vL8': 'file_storage/call_K8M3hThoENRlQEZ44Flc2vL8.json', 'var_call_jrkxjDgMNeHiYJw62UrmDpBt': 'file_storage/call_jrkxjDgMNeHiYJw62UrmDpBt.json'}

exec(code, env_args)
