code = """import json, re
path = var_call_VPIjJV0MwaTNmYb1IXbnb3Ip
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
pattern_title = re.compile(r"(Project|Repairs|Repair|Improvements|Facility|Phase|Playground|Walkway)", re.IGNORECASE)
keywords = re.compile(r"\b(FEMA|CalOES|emergency|Federal|disaster)\b", re.IGNORECASE)

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if pattern_title.search(line):
            block = "\n".join(lines[i:i+12])
            if keywords.search(block):
                title = line.strip()
                title = re.sub(r'^[^A-Za-z0-9]+', '', title)
                blk_low = block.lower()
                status = None
                if ('complete design' in blk_low) or (('design' in blk_low) and ('complete construction' not in blk_low) and ('construction was completed' not in blk_low)):
                    status = 'design'
                if ('construction was completed' in blk_low) or ('complete construction' in blk_low) or ('notice of completion' in blk_low) or ('completed' in blk_low):
                    status = 'completed'
                if ('not started' in blk_low) or ('not begun' in blk_low) or ('identified but not begun' in blk_low):
                    status = 'not started'
                if status is None:
                    if 'under construction' in blk_low:
                        status = 'completed'
                    elif 'begin construction' in blk_low:
                        status = 'design'
                projects.append({'Project_Name': title, 'status': status, 'context': block})

# deduplicate
seen = {}
for p in projects:
    name = p['Project_Name']
    if name not in seen:
        seen[name] = p
projects_unique = list(seen.values())

output = [{'Project_Name': p['Project_Name'], 'status': p['status']} for p in projects_unique]
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_VPIjJV0MwaTNmYb1IXbnb3Ip': 'file_storage/call_VPIjJV0MwaTNmYb1IXbnb3Ip.json'}

exec(code, env_args)
