code = """import json

# Get file paths from locals
civic_path = locals()['var_function-call-3208934928829351036']
funding_path = locals()['var_function-call-14892292881911513259']

civic_docs = json.load(open(civic_path))
funding_docs = json.load(open(funding_path))

funding_map = {}
for item in funding_docs:
    try:
        amount = int(item['Amount'])
    except:
        amount = 0
    funding_map[item['Project_Name']] = amount

project_names_list = list(funding_map.keys())

months = ["Spring", "March", "April", "May"]
starts = ["Begin", "Start", "Advertise", "Award", "Commence"]
excludes = ["Complete", "Finish", "End", "Completion"]

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    matches = []
    for pname in project_names_list:
        idx = text.find(pname)
        while idx != -1:
            matches.append({'start': idx, 'end': idx + len(pname), 'name': pname})
            idx = text.find(pname, idx + 1)
            
    if not matches:
        continue

    matches.sort(key=lambda x: (x['start'], -(x['end'] - x['start'])))
    
    final_matches = []
    last_end = -1
    for m in matches:
        if m['start'] >= last_end:
            final_matches.append(m)
            last_end = m['end']
            
    for i in range(len(final_matches)):
        pname = final_matches[i]['name']
        start_idx = final_matches[i]['end']
        if i + 1 < len(final_matches):
            end_idx = final_matches[i+1]['start']
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        lines = segment.splitlines()
        
        for line in lines:
            line_lower = line.lower()
            if "2022" not in line:
                continue
            
            has_month = False
            for m in months:
                if m.lower() in line_lower:
                    has_month = True
                    break
            if not has_month:
                continue
                
            is_excluded = False
            for exc in excludes:
                if exc.lower() in line_lower:
                    is_excluded = True
                    break
            if is_excluded:
                continue
                
            is_start = False
            for s in starts:
                if s.lower() in line_lower:
                    is_start = True
                    break
            if is_start:
                found_projects.add(pname)
                break

count = 0
total_funding = 0
matched_projects = []

for pname in found_projects:
    if pname in funding_map:
        count += 1
        total_funding += funding_map[pname]
        matched_projects.append(pname)

result = {
    "count": count,
    "total_funding": total_funding,
    "projects": matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14897974976340963418': 'file_storage/function-call-14897974976340963418.json', 'var_function-call-14892292881911513259': 'file_storage/function-call-14892292881911513259.json', 'var_function-call-3208934928829351036': 'file_storage/function-call-3208934928829351036.json'}

exec(code, env_args)
