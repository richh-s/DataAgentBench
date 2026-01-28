code = """import json, re
path = var_call_kESzRD6axEvtHVPDcXvLTW1P
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = {}

keywords = ['project', 'repairs', 'improvements', 'facility', 'park', 'road', 'drainage', 'warning', 'signal', 'playground', 'water']

for doc in docs:
    text = doc.get('text', '')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if 'fema' in ln.lower() or 'emergency' in ln.lower():
            # look backwards for a title-like line
            title_found = False
            for j in range(1, 8):
                idx = i - j
                if idx < 0:
                    break
                cand = lines[idx]
                if not cand:
                    continue
                # skip generic headers
                low = cand.lower()
                if any(skip in low for skip in ['agenda', 'page', 'meeting', 'item', 'report', 'updates', 'discussion', 'prepared', 'approved', 'subject']):
                    continue
                # require one of keywords or the word 'project' in cand
                if any(k in low for k in keywords) or 'project' in low:
                    # normalize title
                    title = re.sub('\s+', ' ', cand).strip(' :\n')
                    # infer status by checking nearby lines (forward and backward)
                    context = ' '.join(lines[max(0, idx-2):min(len(lines), i+4)])
                    s = context.lower()
                    status = 'design'
                    if 'construction was completed' in s or 'complete construction' in s or 'notice of completion' in s or 'completed' in s:
                        status = 'completed'
                    elif 'not started' in s or 'not begun' in s or 'identified' in s:
                        status = 'not started'
                    elif 'design' in s or 'preliminary design' in s or 'complete design' in s or 'working with the consultant' in s or 'finalize the design' in s:
                        status = 'design'
                    elif 'under construction' in s or 'begin construction' in s:
                        status = 'design'
                    candidates[title] = status
                    title_found = True
                    break
            if not title_found:
                # fallback: try to extract a project-like phrase from the same line
                m = re.search(r"([A-Z][A-Za-z0-9 &\'\-]{5,80})", ln)
                if m:
                    title = m.group(1)
                    context = ' '.join(lines[max(0, i-2):min(len(lines), i+3)])
                    s = context.lower()
                    status = 'design'
                    if 'completed' in s:
                        status = 'completed'
                    candidates[title] = status

# prepare output
out = []
for name, status in sorted(candidates.items()):
    out.append({'Project_Name': name, 'Status': status})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WKtxU0jxPJ15joDyaPmwBSnF': ['civic_docs'], 'var_call_jGUa9xleKbwSjDyorm3VrObQ': ['Funding'], 'var_call_kESzRD6axEvtHVPDcXvLTW1P': 'file_storage/call_kESzRD6axEvtHVPDcXvLTW1P.json'}

exec(code, env_args)
