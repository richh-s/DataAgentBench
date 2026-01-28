code = """import json, re
# load the previous execute_python output file
path = var_call_nk3UJd1gvwIdkU5NgDjoZ9tX
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

names = []
for r in records:
    candidates = []
    if r.get('project_name_candidate'):
        candidates.append(r['project_name_candidate'])
    if r.get('match_line'):
        candidates.append(r['match_line'])
    if r.get('context_snippet'):
        # also extract lines that look like project titles within snippet
        for line in r['context_snippet'].splitlines():
            line = line.strip()
            if not line: continue
            # heuristic: lines containing 'Project' or '(FEMA' or 'FEMA' or 'Sirens' or 'Storm Drain' etc
            if re.search(r'project|fema|sirens|storm drain|guardrail|culvert|bridge|repairs|improvements', line, flags=re.IGNORECASE):
                candidates.append(line)
    for c in candidates:
        if not c: continue
        s = c
        # remove cid markers like (cid:131)
        s = re.sub(r"\(cid:\d+\)", "", s)
        s = s.strip()
        # remove leading bullets
        s = re.sub(r"^[\-\u2022\*\d\.\)\s]+", "", s)
        # normalize whitespace
        s = re.sub(r"\s+", " ", s)
        # filter out lines that are obviously not titles
        if len(s) < 5: continue
        # only keep those that mention FEMA or Emergency or look like project titles (contain Project or Repair/Repairs/Improvements)
        if re.search(r'fema|emergency|siren|storm drain|guardrail|culvert|bridge|trancas canyon|latigo|corral canyon|outdoor warning|planting and irrigation|retaining wall', s, flags=re.IGNORECASE):
            names.append(s)

# unique and preserve order
seen = set()
clean_names = []
for n in names:
    key = n.lower()
    if key not in seen:
        seen.add(key)
        clean_names.append(n)

print("__RESULT__:")
print(json.dumps(clean_names))"""

env_args = {'var_call_QxtrsIHo3FAzElPyUC4rh1RS': 'file_storage/call_QxtrsIHo3FAzElPyUC4rh1RS.json', 'var_call_nk3UJd1gvwIdkU5NgDjoZ9tX': 'file_storage/call_nk3UJd1gvwIdkU5NgDjoZ9tX.json'}

exec(code, env_args)
