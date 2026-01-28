code = """import json, re

path = var_call_Xnnh54iL6cs5wg7PT2JhApXO
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

keyword_pattern = re.compile(r"\b(fema|emergency)\b", re.IGNORECASE)
project_candidates = {}

title_indicators = ['project', 'repairs', 'improvements', 'repair', 'study', 'facility', 'project description', 'project updates', 'project schedule', 'slope', 'road', 'park', 'water', 'drain', 'bridge', 'playground', 'retaining wall']
topic_keywords = ['park','road','FEMA','fire','emergency warning','drainage','storm drain','highway','bridge','playground','water treatment','guardrail','emergency']

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if keyword_pattern.search(line):
            # look backwards up to 8 lines to find a likely project title
            title = None
            context_window = []
            start = max(0, idx-8)
            end = min(len(lines), idx+8)
            for j in range(start, end):
                context_window.append(lines[j].strip())
            # search backwards for a line with title indicators
            for back in range(idx, start-1, -1):
                candidate = lines[back].strip()
                if not candidate:
                    continue
                low = candidate.lower()
                # skip lines that are clearly metadata or headings
                if low.startswith('page') or low.startswith('agenda') or low.startswith('item') or low.startswith('to:') or low.startswith('subject:'):
                    continue
                if len(candidate) > 3 and len(candidate) < 150:
                    if any(ind in low for ind in title_indicators) or ('project' in low) or candidate.endswith('Project') or 'Project' in candidate:
                        title = candidate
                        break
            # fallback: first non-empty previous line
            if not title:
                for back in range(idx-1, start-1, -1):
                    candidate = lines[back].strip()
                    if candidate and not candidate.lower().startswith(('cid','(cid', 'page', 'agenda', 'item', 'to:', 'subject:')):
                        title = candidate
                        break
            if not title:
                # as ultimate fallback use a short snippet of the line itself
                title = line.strip()

            # derive status from following lines
            status = 'unknown'
            status_window = '\n'.join(lines[idx:min(len(lines), idx+12)])
            s_low = status_window.lower()
            if re.search(r'complete.*design|final design|in the preliminary design|preliminary design|design phase', s_low):
                status = 'design'
            if re.search(r'construction was completed|complete construction|notice of completion|complete construction:|completed', s_low):
                status = 'completed'
            if re.search(r'not started|not begun|not started', s_low):
                status = 'not started'
            if re.search(r'currently under construction|begin construction|begin construction:|begin construction', s_low):
                if status == 'unknown':
                    status = 'design'

            # derive type
            type_ = 'capital'
            surrounding = '\n'.join(lines[max(0, idx-6):min(len(lines), idx+6)]).lower()
            if 'fema' in surrounding or 'caloes' in surrounding or 'disaster recovery' in surrounding or 'caloes' in surrounding or 'fire' in surrounding:
                type_ = 'disaster'

            # derive topics by checking topic keywords in context
            topics = set()
            for kw in topic_keywords:
                if kw.lower() in surrounding:
                    topics.add(kw)
            if 'fema' in line.lower():
                topics.add('FEMA')
            if 'emergency' in line.lower():
                topics.add('emergency')

            pname = title
            pname = re.sub(r"\s+", " ", pname).strip()
            project_candidates[pname] = {
                'Project_Name': pname,
                'topic': ', '.join(sorted(topics)) if topics else '',
                'type': type_,
                'status': status
            }

projects = list(project_candidates.values())
print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_call_Xnnh54iL6cs5wg7PT2JhApXO': 'file_storage/call_Xnnh54iL6cs5wg7PT2JhApXO.json', 'var_call_PjOpgR2htSTRpdl1SaZYtAQk': {'doc_count': 5}}

exec(code, env_args)
