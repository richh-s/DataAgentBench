code = """import json, re
# Load the large result file from previous query
path = var_call_VPIjJV0MwaTNmYb1IXbnb3Ip
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
pattern_title = re.compile(r'.{0,200}(Project|Repairs|Repair|Improvements|Facility|Phase|Playground|Walkway|Project\b)', re.IGNORECASE)
keywords = re.compile(r'\b(FEMA|CalOES|emergency|Federal|disaster)\b', re.IGNORECASE)

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # find lines that look like project titles
    for i, line in enumerate(lines):
        if pattern_title.search(line):
            # gather a block of following lines for context
            block = "\n".join(lines[i:i+12])
            if keywords.search(block):
                title = line.strip()
                # clean title: remove leading bullets or markers
                title = re.sub(r'^[\u00a0\s\(cid:0-9\)\\.\-]+', '', title)
                # determine status via heuristics
                status = None
                blk_low = block.lower()
                if 'complete design' in blk_low or 'preliminary design' in blk_low or 'design' in blk_low and 'complete construction' not in blk_low:
                    status = 'design'
                if 'construction was completed' in blk_low or 'complete construction' in blk_low or 'notice of completion' in blk_low or 'completed' in blk_low:
                    status = 'completed'
                if 'not started' in blk_low or 'not begun' in blk_low or 'identified but not begun' in blk_low:
                    status = 'not started'
                # if still None, check for 'under construction' or 'begin construction'
                if status is None:
                    if 'under construction' in blk_low or 'begin construction' in blk_low or 'begin construction:' in blk_low:
                        # treat as design if future begin construction, or completed if currently under construction
                        if 'under construction' in blk_low:
                            status = 'completed'
                        else:
                            status = 'design'
                projects.append({'Project_Name': title, 'status': status, 'context': block})

# deduplicate by Project_Name
seen = {}
for p in projects:
    name = p['Project_Name']
    if name not in seen:
        seen[name] = p
projects_unique = list(seen.values())

# Output the list of project names
output = [{'Project_Name': p['Project_Name'], 'status': p['status']} for p in projects_unique]

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_VPIjJV0MwaTNmYb1IXbnb3Ip': 'file_storage/call_VPIjJV0MwaTNmYb1IXbnb3Ip.json'}

exec(code, env_args)
