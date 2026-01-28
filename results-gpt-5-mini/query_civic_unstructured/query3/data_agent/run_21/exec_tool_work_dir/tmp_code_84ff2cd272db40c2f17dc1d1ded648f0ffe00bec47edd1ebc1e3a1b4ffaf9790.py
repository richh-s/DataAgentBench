code = """import json
path = var_call_Xnnh54iL6cs5wg7PT2JhApXO
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for doc in docs:
    lines = doc.get('text','').splitlines()
    n = len(lines)
    for i, line in enumerate(lines):
        llow = line.lower()
        if 'fema' in llow or 'emergency' in llow:
            start = max(0, i-5)
            end = min(n, i+5)
            window = lines[start:end]
            # find title backwards
            title = None
            for j in range(i-1, start-1, -1):
                s = lines[j].strip()
                if not s:
                    continue
                sl = s.lower()
                if sl.startswith(('cid', '(cid', 'page', 'agenda', 'item', 'to:', 'subject:')):
                    continue
                title = s
                break
            if not title:
                for j in range(i, end):
                    s = lines[j].strip()
                    if s and not s.lower().startswith(('cid', '(cid', 'page', 'agenda', 'item', 'to:', 'subject:')):
                        title = s
                        break
            if not title:
                title = line.strip()
            title = ' '.join(title.split())
            look = ' '.join(window).lower()
            status = 'unknown'
            if 'notice of completion' in look or 'construction was completed' in look or 'complete construction' in look or 'completed' in look:
                status = 'completed'
            elif 'final design' in look or 'complete design' in look or 'preliminary design' in look or 'design phase' in look:
                status = 'design'
            elif 'not started' in look or 'not begun' in look:
                status = 'not started'
            type_ = 'capital'
            if 'fema' in look or 'caloes' in look or 'disaster recovery' in look or 'fire' in look:
                type_ = 'disaster'
            kws = ['park','road','fema','fire','emergency warning','drainage','storm drain','highway','bridge','playground','water treatment','guardrail','emergency']
            topics = []
            for kw in kws:
                if kw in look:
                    topics.append('FEMA' if kw=='fema' else kw)
            results.append({'Project_Name': title, 'topic': ', '.join(sorted(set(topics))), 'type': type_, 'status': status})

# deduplicate by Project_Name keeping first
uniq = {}
for r in results:
    if r['Project_Name'] not in uniq:
        uniq[r['Project_Name']] = r
out = list(uniq.values())
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Xnnh54iL6cs5wg7PT2JhApXO': 'file_storage/call_Xnnh54iL6cs5wg7PT2JhApXO.json', 'var_call_PjOpgR2htSTRpdl1SaZYtAQk': {'doc_count': 5}}

exec(code, env_args)
