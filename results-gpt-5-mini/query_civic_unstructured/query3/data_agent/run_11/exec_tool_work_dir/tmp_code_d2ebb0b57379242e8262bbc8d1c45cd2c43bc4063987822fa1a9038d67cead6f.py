code = """import json
path = var_call_2ajh9JRnLUZjcgZaBU1zv32y
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
results = []
seen = set()
for doc in docs:
    text = doc.get('text','')
    lines = [ln for ln in text.splitlines()]
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'fema' in low or 'emergency' in low:
            # find previous non-empty line up to 10 lines back
            name = None
            for j in range(idx-1, max(-1, idx-11), -1):
                if j < 0:
                    break
                cand = lines[j].strip()
                if cand:
                    name = ' '.join(cand.split())
                    break
            if not name:
                name = ' '.join(line.strip().split())
            if name not in seen:
                seen.add(name)
                # determine status from nearby 8 lines
                start = max(0, j-8)
                end = min(len(lines), idx+8)
                context = '\n'.join(lines[start:end]).lower()
                if any(k in context for k in ['construction was completed','complete construction','notice of completion','completed,','complete construction:']):
                    status = 'completed'
                elif any(k in context for k in ['awaiting','awaiting final','awaiting approval','waiting','not started','identified']):
                    status = 'not started'
                elif any(k in context for k in ['preliminary design','working with the consultant to finalize the design','finalize the design','complete design','design phase','design is','begin construction']):
                    status = 'design'
                else:
                    status = 'not started'
                results.append({'Project_Name': name, 'Status': status})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_2ajh9JRnLUZjcgZaBU1zv32y': 'file_storage/call_2ajh9JRnLUZjcgZaBU1zv32y.json'}

exec(code, env_args)
