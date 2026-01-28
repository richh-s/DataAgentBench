code = """import json
import re

# Load the civic docs query result from storage
path = var_call_4fX4CVxqrzrg2HK6TiF57mL4
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

spring_months = ['March 2022', 'April 2022', 'May 2022', 'Spring 2022', '2022-Spring', '2022 March', '2022-March', '2022 April', '2022-April', '2022 May', '2022-May']
month_regex = re.compile(r"(Spring 2022|2022-Spring|March 2022|April 2022|May 2022|2022-March|2022-April|2022-May|2022 March|2022 April|2022 May)", re.IGNORECASE)

# Keywords to help identify project title lines
title_keywords = ['Project', 'Repairs', 'Improvements', 'Park', 'Playground', 'Study', 'Plan', 'Facility', 'Repair', 'Restoration', 'Master Plan', 'Skate Park', 'Walkway', 'Traffic Study', 'Water Treatment', 'Green Streets', 'Retaining Wall', 'Drainage', 'Median', 'Signals', 'Slope', 'Biofilter', 'Trash Screens', 'Shade Structure', 'Road', 'Bridge']

found_projects = []

for doc in docs:
    text = doc.get('text', '')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, line in enumerate(lines):
        if month_regex.search(line):
            # search backwards for a plausible project title within previous 12 lines
            title = None
            for j in range(max(0, i-12), i)[::-1]:
                l = lines[j]
                if not l:
                    continue
                low = l.lower()
                if low.startswith('page') or low.startswith('agenda') or low.startswith('item'):
                    continue
                if l.startswith('(') and 'cid' in l.lower():
                    continue
                if ':' in l and len(l) < 30 and l.endswith(':'):
                    # skip short labels like "Updates:" or "Project Schedule:"
                    continue
                # if line contains any title keyword, take it
                if any(kw.lower() in low for kw in title_keywords):
                    title = l
                    break
                # otherwise, consider lines that look like titles: title-case and not too long
                if 3 < len(l) < 120 and sum(1 for c in l if c.isupper()) > 0:
                    title = l
                    break
            if title:
                # normalize whitespace
                title = re.sub(r"\s+", ' ', title).strip()
                found_projects.append(title)

# deduplicate preserving order
unique_projects = []
seen = set()
for p in found_projects:
    pk = p.lower()
    if pk not in seen:
        seen.add(pk)
        unique_projects.append(p)

# Print result as JSON list
print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_call_w2CjMMHrCINpDfT1q9U0L5Po': ['civic_docs'], 'var_call_8Z022tJgpWErMfAG6q81W7g0': ['Funding'], 'var_call_4fX4CVxqrzrg2HK6TiF57mL4': 'file_storage/call_4fX4CVxqrzrg2HK6TiF57mL4.json'}

exec(code, env_args)
