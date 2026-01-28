code = """import json, re

# Load data from storage-provided file paths
funding_path = var_call_qtuy2uyCXJFbo2jy186azTWZ
docs_path = var_call_e97eVcnX80aVs2FJSz0zameH

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize funding amounts to integers
for rec in funding:
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        # remove non-digits
        nums = re.findall(r"\d+", str(rec.get('Amount','0')))
        rec['Amount'] = int(nums[0]) if nums else 0

# Disaster keywords
dis_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'Woolsey', 'FEMA/CalOES', 'CalOES Project', 'FEMA Project']

def is_disaster_name(name):
    up = name.upper()
    return any(k.upper() in up for k in dis_keywords)

matched_projects = set()

# For each funding record, search in civic docs for occurrences and check nearby context for 2022 and disaster cues
for rec in funding:
    pname = rec['Project_Name']
    pname_lower = pname.lower()
    found = False
    for d in docs:
        text = d.get('text','')
        text_lower = text.lower()
        # search for project name occurrence (loose match: exact substring)
        idx = text_lower.find(pname_lower)
        if idx != -1:
            # get context window
            start = max(0, idx-300)
            end = min(len(text), idx+300)
            context = text[start:end]
            ctx_up = context.upper()
            # check for year 2022 in context
            if '2022' in context:
                # check for disaster cues either in project name or in context
                if is_disaster_name(pname) or any(k.upper() in ctx_up for k in dis_keywords):
                    matched_projects.add(pname)
                    found = True
                    break
        # also check if project name not present but disaster keyword near a likely project heading matching funding name tokens
        # skip for performance
    # If not found by direct occurrence but project name itself contains disaster keyword and any doc contains '2022', include it
    if not found and is_disaster_name(pname):
        for d in docs:
            if '2022' in d.get('text',''):
                matched_projects.add(pname)
                break

# Additionally, find project names mentioned in docs near disaster keywords even if funding name lacks the suffix
# We'll search for capitalized lines (project headings) followed by schedule with 2022 and disaster keywords
for d in docs:
    text = d.get('text','')
    # split into lines and look for lines that look like project titles
    lines = text.splitlines()
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        # consider lines shorter than 120 chars and containing letters and digits, treat as possible project name
        if len(line_stripped) < 120 and re.search(r'[A-Za-z]', line_stripped):
            # look ahead a few lines for schedule/context
            context = ' '.join(lines[i:i+8])
            if '2022' in context:
                # if context also has disaster keywords, treat this line as disaster project name
                if any(k.upper() in context.upper() for k in dis_keywords):
                    # find closest matching funding project name by simple substring matching
                    for rec in funding:
                        if rec['Project_Name'].lower() in line_stripped.lower() or line_stripped.lower() in rec['Project_Name'].lower():
                            matched_projects.add(rec['Project_Name'])

# Sum amounts for matched projects
total = 0
matched_list = sorted(list(matched_projects))
for rec in funding:
    if rec['Project_Name'] in matched_list:
        total += rec['Amount']

# Prepare result
result = {
    'matched_projects': matched_list,
    'total_funding': total
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3mglF6Vw0HP6gwF4tNqrQ8Wz': ['Funding'], 'var_call_YC5lW32v35tkeeAPvXKPBV60': ['civic_docs'], 'var_call_qtuy2uyCXJFbo2jy186azTWZ': 'file_storage/call_qtuy2uyCXJFbo2jy186azTWZ.json', 'var_call_e97eVcnX80aVs2FJSz0zameH': 'file_storage/call_e97eVcnX80aVs2FJSz0zameH.json'}

exec(code, env_args)
