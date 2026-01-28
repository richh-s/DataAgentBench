code = """import json, re
path = var_call_2ajh9JRnLUZjcgZaBU1zv32y
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
seen = set()
# title keywords
kw = ['project','improvements','repair','repairs','facility','park','playground','study','plan','walkway','retaining wall','drive','road','signal','signs','water treatment','backup power','trash screens','slope','master plan']
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if 'fema' in low or 'emergency' in low:
            # search backwards for title-like line
            title = None
            title_idx = None
            for j in range(i-1, max(-1, i-11), -1):
                if j < 0:
                    break
                cand = lines[j].strip()
                if not cand:
                    continue
                cand_low = cand.lower()
                if any(k in cand_low for k in kw) and len(cand) < 200:
                    title = ' '.join(cand.split())
                    title_idx = j
                    break
            if title is None:
                # fallback: use the line itself shortened
                title = ' '.join(line.strip().split())
                title_idx = i
            if title in seen:
                continue
            seen.add(title)
            # context window
            start = max(0, title_idx-6)
            end = min(len(lines), title_idx+7)
            context = '\n'.join(lines[start:end]).lower()
            # determine status
            if any(x in context for x in ['construction was completed','complete construction','notice of completion','completed,','complete construction:']):
                status = 'completed'
            elif any(x in context for x in ['awaiting','awaiting final','awaiting approval','waiting for','not started','identified']):
                status = 'not started'
            elif any(x in context for x in ['preliminary design','working with the consultant to finalize the design','finalize the design','complete design','design phase','design is','begin construction','currently under construction','advertise','begin construction:']):
                status = 'design'
            else:
                status = 'not started'
            projects.append({'Project_Name': title, 'Status': status})

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_call_2ajh9JRnLUZjcgZaBU1zv32y': 'file_storage/call_2ajh9JRnLUZjcgZaBU1zv32y.json', 'var_call_QLNYso6DCSC7NVUDNVKM3KbR': {'doc_count': 19}}

exec(code, env_args)
