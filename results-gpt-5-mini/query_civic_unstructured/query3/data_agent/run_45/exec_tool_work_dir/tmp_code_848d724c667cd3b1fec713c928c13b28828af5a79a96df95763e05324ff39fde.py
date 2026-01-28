code = """import json, re
path = var_call_tbBFwe7x7VueL51tEf2jx0fE
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
seen = set()
for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    clean_lines = [re.sub(r"\(cid:[0-9]+\)", "", l).strip() for l in lines]
    for i, line in enumerate(clean_lines):
        if re.search(r'\bfema\b', line, re.I) or re.search(r'\bemergency\b', line, re.I):
            proj_name = None
            for j in range(i-1, max(i-12, -1), -1):
                candidate = clean_lines[j]
                if not candidate:
                    continue
                if re.search(r'Project|Repairs|Park|Facility|Playground|Study|Improvements|Repair|Master Plan|Water Treatment|Backup Power|Warning|Walkway|Retaining Wall', candidate, re.I):
                    proj_name = candidate
                    break
                if 3 < len(candidate) < 120 and candidate == candidate.title() and len(candidate.split()) <= 7:
                    proj_name = candidate
                    break
            if not proj_name:
                for j in range(i-1, max(i-12, -1), -1):
                    candidate = clean_lines[j]
                    if candidate:
                        proj_name = candidate
                        break
            if not proj_name:
                continue
            proj_name = proj_name.strip(':').strip()
            proj_name = re.sub(r'Updates$', '', proj_name, flags=re.I).strip()
            proj_name = re.sub(r'Project Schedule.*$', '', proj_name, flags=re.I).strip()
            if proj_name.lower() in seen:
                continue
            seen.add(proj_name.lower())
            status = None
            tindex = None
            for k, cl in enumerate(clean_lines):
                if cl.strip() == proj_name:
                    tindex = k
                    break
            start = tindex or 0
            combined = "\n".join(clean_lines[start:min(start+15, len(clean_lines))])
            combined_low = combined.lower()
            if re.search(r'construction was completed|complete construction|notice of completion|completed', combined_low):
                status = 'completed'
            elif re.search(r'awaiting final fema|fema', combined_low):
                if re.search(r'plans and specifications have been completed|plans and specifications are being finalized|final design', combined_low):
                    status = 'design'
                else:
                    status = 'not started'
            elif re.search(r'complete design|preliminary design|design is|working with the consultant|preliminary design', combined_low):
                status = 'design'
            elif re.search(r'project is currently under construction|begin construction', combined_low):
                status = 'design'
            else:
                status = 'not started'
            topics = []
            if re.search(r'\bfema\b', line, re.I):
                topics.append('FEMA')
            if re.search(r'\bemergency\b', line, re.I):
                topics.append('emergency')
            for kw in ['park', 'road', 'fire', 'emergency warning', 'drainage', 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 'guardrail', 'backup power', 'warning']:
                if re.search(r'\b' + re.escape(kw) + r'\b', combined_low, re.I):
                    topics.append(kw)
            topics = list(dict.fromkeys([t for t in topics if t]))
            projects.append({'Project_Name': proj_name, 'status': status, 'topics': topics})

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_call_uqzI9WhyYiig4Zo5laqd7bQk': ['civic_docs'], 'var_call_KVKlIYloVTvXJ6fo0ZGDdXai': ['Funding'], 'var_call_tbBFwe7x7VueL51tEf2jx0fE': 'file_storage/call_tbBFwe7x7VueL51tEf2jx0fE.json'}

exec(code, env_args)
