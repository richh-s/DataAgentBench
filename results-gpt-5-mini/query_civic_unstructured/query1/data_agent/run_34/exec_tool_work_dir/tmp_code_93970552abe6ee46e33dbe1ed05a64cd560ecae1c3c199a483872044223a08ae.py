code = """import json
# Load the large civic_docs query result from the storage file path
path = var_call_SitqQeQgm0QXhLVXJ5E5S5bL
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

import re
project_names = []
for doc in docs:
    text = doc.get('text','')
    # find design section
    m = re.search(r'Capital Improvement Projects \(Design\)', text)
    if not m:
        continue
    start = m.end()
    # find end markers
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Construction)']
    end = len(text)
    for em in end_markers:
        idx = text.find(em, start)
        if idx != -1:
            end = min(end, idx)
    section = text[start:end]
    # split into lines
    lines = section.splitlines()
    # helper to get next non-empty line
    def next_nonempty(i):
        j = i+1
        while j < len(lines) and lines[j].strip() == '':
            j += 1
        return lines[j].strip() if j < len(lines) else ''

    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        ls = s.lower()
        if ls.startswith(('cid:','(cid','page','agenda','item','to:','prepared by:','approved by:','date prepared:','meeting date:','subject:')):
            continue
        if any(k in s for k in ['Updates','Project Schedule','Project Description','Estimated Schedule','Project Updates','Project is currently','Project Description:']):
            continue
        # if next nonempty looks like an updates marker, this line is likely a title
        nxt = next_nonempty(i)
        if nxt.startswith('(cid:') or 'Updates' in nxt or 'Project Schedule' in nxt or nxt.startswith('Updates:') or nxt.startswith('Project Schedule:'):
            # filter out lines that are too short or likely not titles
            if 3 < len(s) < 120:
                # remove leading bullets or numbering
                s_clean = re.sub(r'^[^A-Za-z0-9]+','',s)
                project_names.append(s_clean)
        else:
            # also consider lines that end with 'Project' or contain keywords
            if re.search(r'\bProject\b', s) or re.search(r'\bImprovements\b', s) or re.search(r'\bRepairs\b', s) or re.search(r'\bResurfacing\b', s) or re.search(r'\bDrainage\b', s) or re.search(r'\bWater\b', s):
                if 3 < len(s) < 120:
                    s_clean = re.sub(r'^[^A-Za-z0-9]+','',s)
                    project_names.append(s_clean)

# deduplicate while preserving order
seen = set()
proj_list = []
for p in project_names:
    if p not in seen:
        seen.add(p)
        proj_list.append(p)

result = proj_list
import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_xWBqhZjvVzRFPrcyF1m6w9tD': ['civic_docs'], 'var_call_SitqQeQgm0QXhLVXJ5E5S5bL': 'file_storage/call_SitqQeQgm0QXhLVXJ5E5S5bL.json'}

exec(code, env_args)
