code = """import json, re

# Load the query_db result stored as a JSON file path in var_call_tbBFwe7x7VueL51tEf2jx0fE
path = var_call_tbBFwe7x7VueL51tEf2jx0fE
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
seen = set()

status_map = {
    'design': ['design', 'preliminary design', 'final design', 'Complete Design', 'complete design', 'Design:'],
    'completed': ['construction was completed', 'completed', 'Complete Construction', 'Complete construction', 'Notice of completion', 'Complete Design:'],
    'not started': ['not started', 'identified', 'will be', 'planned', 'proposed']
}

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # clean lines
    clean_lines = [re.sub(r"\(cid:[0-9]+\)", '', l).strip() for l in lines]
    for i, line in enumerate(clean_lines):
        if re.search(r'\bfema\b', line, re.I) or re.search(r'\bemergency\b', line, re.I):
            # search upward for a project title within previous 10 lines
            proj_name = None
            for j in range(i-1, max(i-12, -1), -1):
                candidate = clean_lines[j]
                if not candidate:
                    continue
                # Heuristic: title lines often contain 'Project' or 'Repairs' or 'Park' or 'Facility' or 'Project Description'
                if re.search(r'Project|Repairs|Park|Facility|Playground|Study|Improvements|Repair|Repairs|Master Plan|Water Treatment|Backup Power|Warning|Walkway|Retaining Wall', candidate, re.I):
                    proj_name = candidate
                    break
                # Or lines that are Title Case and reasonably short
                if 3 < len(candidate) < 120 and candidate == candidate.title() and len(candidate.split())<=7:
                    proj_name = candidate
                    break
            if not proj_name:
                # fallback: take previous non-empty line
                for j in range(i-1, max(i-12, -1), -1):
                    candidate = clean_lines[j]
                    if candidate:
                        proj_name = candidate
                        break
            if not proj_name:
                continue
            # normalize
            proj_name = proj_name.strip(':').strip()
            # remove trailing words like 'Updates' or 'Project Schedule'
            proj_name = re.sub(r'Updates$', '', proj_name, flags=re.I).strip()
            proj_name = re.sub(r'Project Schedule.*$', '', proj_name, flags=re.I).strip()
            if proj_name.lower() in seen:
                continue
            seen.add(proj_name.lower())

            # infer status by searching nearby lines (within 10 lines after title)
            status = None
            tindex = None
            # find title index
            for k, cl in enumerate(clean_lines):
                if cl.strip() == proj_name:
                    tindex = k
                    break
            search_range = range((tindex or 0), min((tindex or 0)+15, len(clean_lines)))
            combined = '\n'.join([clean_lines[x] for x in search_range])
            combined_low = combined.lower()
            # simple heuristics
            if re.search(r'construction was completed|complete construction|notice of completion|completed', combined_low):
                status = 'completed'
            elif re.search(r'awaiting final fema|fema', combined_low):
                # likely disaster recovery waiting on FEMA -> not started or design; mark as design if plans/specs done else not started
                if re.search(r'plans and specifications have been completed|plans and specifications are being finalized|final design', combined_low):
                    status = 'design'
                else:
                    status = 'not started'
            elif re.search(r'complete design|preliminary design|design is|working with the consultant|preliminary design', combined_low):
                status = 'design'
            elif re.search(r'project is currently under construction|begin construction|begin construction:', combined_low):
                status = 'design'
            else:
                # default: not started
                status = 'not started'

            # gather topics: if the line contained the words, add them
            topics = []
            if re.search(r'\bfema\b', line, re.I):
                topics.append('FEMA')
            if re.search(r'\bemergency\b', line, re.I):
                topics.append('emergency')
            # also scan nearby for keywords
            for kw in ['park','road','fire','emergency warning','drainage','storm drain','highway','bridge','playground','water treatment','guardrail','backup power','warning']:
                if re.search(r'\b'+re.escape(kw)+r'\b', combined_low, re.I):
                    topics.append(kw)
            topics = list(dict.fromkeys([t for t in topics if t]))

            projects.append({'Project_Name': proj_name, 'status': status, 'topics': topics})

# Return unique projects list
print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_call_uqzI9WhyYiig4Zo5laqd7bQk': ['civic_docs'], 'var_call_KVKlIYloVTvXJ6fo0ZGDdXai': ['Funding'], 'var_call_tbBFwe7x7VueL51tEf2jx0fE': 'file_storage/call_tbBFwe7x7VueL51tEf2jx0fE.json'}

exec(code, env_args)
