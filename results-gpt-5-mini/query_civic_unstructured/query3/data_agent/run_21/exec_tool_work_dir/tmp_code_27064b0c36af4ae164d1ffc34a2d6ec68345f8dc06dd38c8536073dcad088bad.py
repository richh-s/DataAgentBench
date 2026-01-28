code = """import json
import re

# Load the civic docs query result file
path = var_call_Xnnh54iL6cs5wg7PT2JhApXO
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = {}

for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'fema' in low or 'emergency' in low:
            # find title by looking backwards up to 8 lines for a likely project title
            title = None
            start = max(0, idx-8)
            for back in range(idx-1, start-1, -1):
                candidate = lines[back].strip()
                if not candidate:
                    continue
                cl = candidate.lower()
                if cl.startswith(('page', 'agenda', 'item', 'to:', 'subject:', 'cid:', '(cid')):
                    continue
                # pick a reasonable length line
                if 3 < len(candidate) < 150:
                    title = candidate
                    break
            if not title:
                title = line.strip()

            # status heuristics from following lines
            status = 'unknown'
            look = '\n'.join(lines[idx: idx+12]).lower()
            if 'complete design' in look or 'final design' in look or 'preliminary design' in look or 'design phase' in look:
                status = 'design'
            if 'construction was completed' in look or 'complete construction' in look or 'notice of completion' in look or 'completed' in look:
                status = 'completed'
            if 'not started' in look or 'not begun' in look:
                status = 'not started'
            if 'under construction' in look or 'begin construction' in look:
                if status == 'unknown':
                    status = 'design'

            # type
            surrounding = '\n'.join(lines[max(0, idx-6): idx+6]).lower()
            type_ = 'capital'
            if 'fema' in surrounding or 'caloes' in surrounding or 'disaster recovery' in surrounding or 'fire' in surrounding:
                type_ = 'disaster'

            # topics
            topic_kws = ['park','road','fema','fire','emergency warning','drainage','storm drain','highway','bridge','playground','water treatment','guardrail','emergency']
            topics = set()
            for kw in topic_kws:
                if kw in surrounding:
                    topics.add(kw)

            pname = re.sub(r"\s+", " ", title).strip()
            projects[pname] = {
                'Project_Name': pname,
                'topic': ', '.join(sorted(topics)) if topics else '',
                'type': type_,
                'status': status
            }

proj_list = list(projects.values())

print("__RESULT__:")
print(json.dumps(proj_list))"""

env_args = {'var_call_Xnnh54iL6cs5wg7PT2JhApXO': 'file_storage/call_Xnnh54iL6cs5wg7PT2JhApXO.json'}

exec(code, env_args)
