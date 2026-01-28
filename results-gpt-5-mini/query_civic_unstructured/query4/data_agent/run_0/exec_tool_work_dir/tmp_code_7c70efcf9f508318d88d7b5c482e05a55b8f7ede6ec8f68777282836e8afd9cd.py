code = """import json
from pathlib import Path
p = Path(var_call_zPiRFhL3SBrfqfEgEhKn3UKe)
data = json.loads(p.read_text())
projects = set()
for doc in data:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    lcount = len(lines)
    for i,ln in enumerate(lines):
        low = ln.lower()
        if 'spring' in low and '2022' in low:
            # search upwards for project title
            for j in range(max(0,i-6), i):
                cand = lines[j].strip()
                if not cand: 
                    continue
                # heuristics
                lowc = cand.lower()
                if ('project' in lowc) or ('park' in lowc) or ('study' in lowc) or ('facility' in lowc) or ('improvements' in lowc) or ('repair' in lowc) or ('restoration' in lowc) or ('treatment' in lowc) or ('improvement' in lowc) or ('walkway' in lowc) or ('playground' in lowc) or ('resurfacing' in lowc):
                    # clean punctuation
                    cand = cand.strip('- ').strip()
                    projects.add(cand)
                    break
            else:
                # if not found, also possibly the previous non-empty line
                for j in range(i-1, max(-1,i-6), -1):
                    if j<0: break
                    cand = lines[j].strip()
                    if cand:
                        projects.add(cand)
                        break
# convert to sorted list
proj_list = sorted(projects)
# print results as JSON string
result = json.dumps(proj_list)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_zPiRFhL3SBrfqfEgEhKn3UKe': 'file_storage/call_zPiRFhL3SBrfqfEgEhKn3UKe.json'}

exec(code, env_args)
