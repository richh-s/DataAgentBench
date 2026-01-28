code = """import json
path = var_call_tbBFwe7x7VueL51tEf2jx0fE
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
seen = set()

title_keywords = ['project','repairs','park','facility','playground','study','improvements','repair','master plan','water treatment','backup power','warning','walkway','retaining wall','retaining','road']
nearby_keywords = ['park','road','fire','emergency warning','drainage','storm drain','highway','bridge','playground','water treatment','guardrail','backup power','warning','drain']

for doc in docs:
    lines = doc.get('text','').splitlines()
    clean_lines = [l.replace('(cid:190)','').replace('(cid:131)','').strip() for l in lines]
    for i, line in enumerate(clean_lines):
        low = line.lower()
        if 'fema' in low or 'emergency' in low:
            proj_name = None
            # search upward for title
            for j in range(i-1, max(i-12, -1), -1):
                candidate = clean_lines[j].strip()
                if not candidate:
                    continue
                clow = candidate.lower()
                if any(k in clow for k in title_keywords):
                    proj_name = candidate
                    break
                # Title case heuristic
                if 3 < len(candidate) < 120 and candidate == candidate.title() and len(candidate.split()) <= 8:
                    proj_name = candidate
                    break
            if not proj_name:
                for j in range(i-1, max(i-12, -1), -1):
                    candidate = clean_lines[j].strip()
                    if candidate:
                        proj_name = candidate
                        break
            if not proj_name:
                continue
            proj_name = proj_name.rstrip(':').strip()
            proj_name = proj_name.rstrip('Updates').strip()
            key = proj_name.lower()
            if key in seen:
                continue
            seen.add(key)
            # find index of proj_name in clean_lines
            try:
                tindex = clean_lines.index(proj_name)
            except ValueError:
                tindex = max(0, i-2)
            # combine nearby lines
            start = tindex
            end = min(len(clean_lines), start+15)
            combined = ' '.join(clean_lines[start:end]).lower()
            # determine status
            status = 'not started'
            if 'construction was completed' in combined or 'complete construction' in combined or 'notice of completion' in combined or 'completed' in combined:
                status = 'completed'
            elif 'awaiting final fema' in combined or 'awaiting final fema/caloes' in combined or 'awaiting final fema/ caloes' in combined:
                # if plans done
                if 'plans and specifications have been completed' in combined or 'plans and specifications are being finalized' in combined or 'final design' in combined:
                    status = 'design'
                else:
                    status = 'not started'
            elif 'complete design' in combined or 'preliminary design' in combined or 'design' in combined or 'working with the consultant' in combined:
                status = 'design'
            elif 'project is currently under construction' in combined or 'begin construction' in combined:
                status = 'design'
            # topics
            topics = []
            if 'fema' in low:
                topics.append('FEMA')
            if 'emergency' in low:
                topics.append('emergency')
            for kw in nearby_keywords:
                if kw in combined and kw not in topics:
                    topics.append(kw)
            projects.append({'Project_Name': proj_name, 'status': status, 'topics': topics})

print('__RESULT__:')
print(json.dumps(projects))"""

env_args = {'var_call_uqzI9WhyYiig4Zo5laqd7bQk': ['civic_docs'], 'var_call_KVKlIYloVTvXJ6fo0ZGDdXai': ['Funding'], 'var_call_tbBFwe7x7VueL51tEf2jx0fE': 'file_storage/call_tbBFwe7x7VueL51tEf2jx0fE.json'}

exec(code, env_args)
