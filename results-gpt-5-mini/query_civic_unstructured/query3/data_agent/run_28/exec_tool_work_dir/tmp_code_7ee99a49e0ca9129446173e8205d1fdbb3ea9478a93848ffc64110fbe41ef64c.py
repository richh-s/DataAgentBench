code = """import json, re
# Load the query_db result from file
path = var_call_QxtrsIHo3FAzElPyUC4rh1RS
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = []
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # normalize
    lower_lines = [ln.lower() for ln in lines]
    for i, ln in enumerate(lower_lines):
        if 'fema' in ln or 'emergency' in ln:
            # find nearest project title upwards within 8 lines
            proj_name = None
            for j in range(max(0, i-8), i+1)[::-1]:
                orig = lines[j].strip()
                # heuristics: title lines often end with 'Project' or contain 'Project' or are ALL CAPS and short
                if re.search(r'project\b', orig, flags=re.IGNORECASE):
                    proj_name = orig
                    break
                if orig.isupper() and 5 < len(orig) < 80:
                    proj_name = orig
                    break
            # if still none, take the previous non-empty line
            if not proj_name:
                for j in range(max(0, i-6), i)[::-1]:
                    s = lines[j].strip()
                    if s:
                        proj_name = s
                        break
            snippet = lines[max(0,i-2):i+3]
            candidates.append({
                'filename': doc.get('filename'),
                'match_line': lines[i].strip(),
                'project_name_candidate': proj_name,
                'context_snippet': "\\n".join(snippet)
            })

# Deduplicate by project_name_candidate
seen = {}
results = []
for c in candidates:
    name = c['project_name_candidate'] or ''
    key = name.lower()
    if key not in seen:
        seen[key] = True
        results.append(c)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_QxtrsIHo3FAzElPyUC4rh1RS': 'file_storage/call_QxtrsIHo3FAzElPyUC4rh1RS.json'}

exec(code, env_args)
