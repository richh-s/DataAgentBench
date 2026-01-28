code = """import json
import re

# Load data
civic_docs = json.load(open('var_function-call-3208934928829351036.json'))
funding_docs = json.load(open('var_function-call-14892292881911513259.json'))

# Get project names
funding_map = {}
for item in funding_docs:
    funding_map[item['Project_Name']] = item['Amount']

project_names_list = list(funding_map.keys())

# Regex for date
# Matches: Spring 2022, March 2022, etc. (case insensitive)
date_re = re.compile(r'(?i)\b(Spring|March|April|May)\b.{0,10}\b2022\b|\b2022\b.{0,10}\b(Spring|March|April|May)\b')

# Regex for start/begin
start_re = re.compile(r'(?i)(Begin|Start|Advertise|Award|Commence)')
# Regex for exclude
exclude_re = re.compile(r'(?i)(Complete|Finish|End|Completion|Closure)')

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Identify project locations
    matches = []
    for pname in project_names_list:
        pname_esc = re.escape(pname)
        for m in re.finditer(pname_esc, text):
            matches.append({
                'start': m.start(),
                'end': m.end(),
                'name': pname
            })
    
    if not matches:
        continue
        
    # Sort matches
    matches.sort(key=lambda x: (x['start'], -(x['end'] - x['start'])))
    
    final_matches = []
    last_end = -1
    for m in matches:
        if m['start'] >= last_end:
            final_matches.append(m)
            last_end = m['end']
    
    # Process segments
    for i in range(len(final_matches)):
        pname = final_matches[i]['name']
        start_idx = final_matches[i]['end']
        
        if i + 1 < len(final_matches):
            end_idx = final_matches[i+1]['start']
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        
        lines = segment.split('\n')
        for line in lines:
            line_clean = line.strip()
            if not line_clean:
                continue
                
            if date_re.search(line_clean):
                if exclude_re.search(line_clean):
                    continue
                if start_re.search(line_clean):
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
