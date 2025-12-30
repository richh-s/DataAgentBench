code = """import json
import re

civic_path = locals()['var_function-call-18248731954071622536']
with open(civic_path, 'r') as f:
    docs = json.load(f)

projects = []
for doc in docs:
    txt = doc['text']
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    update_indices = [i for i, line in enumerate(lines) if 'Updates:' in line]
    project_starts = sorted(list(set([i-1 for i in update_indices if i > 0])))
    for k in range(len(project_starts)):
        start_idx = project_starts[k]
        end_idx = project_starts[k+1] if k+1 < len(project_starts) else len(lines)
        name = lines[start_idx]
        chunk = lines[start_idx+1 : end_idx]
        full_text = " ".join(chunk).lower()
        projects.append({'name': name, 'text': full_text})

debug_out = []
for p in projects:
    if "Shade Structure" in p['name']:
        name = p['name']
        text = p['text']
        is_park = bool(re.search(r'\bpark(s?)\b', name.lower()) or re.search(r'\bpark(s?)\b', text))
        
        match1 = re.search(r'completed.{1,30}2022', text)
        match2 = re.search(r'complete construction.{1,30}2022', text)
        is_completed = bool(match1 or match2)
        
        debug_out.append({
            "name": name,
            "is_park": is_park,
            "is_completed": is_completed,
            "text_preview": text[:100],
            "match1": str(match1),
            "match2": str(match2)
        })

print("__RESULT__:")
print(json.dumps(debug_out))"""

env_args = {'var_function-call-17862480380810104238': 'file_storage/function-call-17862480380810104238.json', 'var_function-call-18328159169731343039': 'file_storage/function-call-18328159169731343039.json', 'var_function-call-18248731954071622536': 'file_storage/function-call-18248731954071622536.json', 'var_function-call-18090166936097834747': {'total': 210001600024000.0, 'projects': ['PCH Signal Synchronization System Improvements Project', 'Storm Drain Trash Screens Phase Two', 'Bluffs Park Shade Structure']}, 'var_function-call-8858882187705849382': {'total': 35000.0, 'projects': ['Bluffs Park Shade Structure', 'Birdview Avenue Improvements (FEMA/CalOES Project)']}, 'var_function-call-1422339580314657284': {'total': 0.0, 'projects': []}, 'var_function-call-9189892170030117897': {'total': 0.0, 'projects': []}, 'var_function-call-11166089951078103463': [{'name': 'Bluffs Park Shade Structure', 'text': '(cid:190) updates: construction was completed november 2022. notice of completion filed january 2023 page 4 of 6 agenda item # 4.b.'}], 'var_function-call-16923250808172815366': {'total': 0.0, 'final_projects_extracted': [], 'matched_funding': []}}

exec(code, env_args)
