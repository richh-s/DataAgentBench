code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_VBhtC9hpJRbNT16WmdZtMk4W, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_DFwD6qNOXINdKlJ7slVtPbBE, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding records: convert Amount to int
fundings = []
for r in funding_records:
    try:
        amt = int(str(r.get('Amount','0')).replace(',','').strip())
    except:
        amt = 0
    name = r.get('Project_Name','').strip()
    fundings.append({'name': name, 'name_l': name.lower(), 'amount': amt})

# Extract 'Design' capital project names from civic documents
design_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    # find all occurrences of the Design section
    start_idx = 0
    while True:
        si = text.find('Capital Improvement Projects (Design)', start_idx)
        if si == -1:
            break
        # find next occurrence of 'Capital Improvement Projects (' after si+1
        ni = text.find('Capital Improvement Projects (', si+1)
        if ni == -1:
            section = text[si:]
            start_idx = len(text)
        else:
            section = text[si:ni]
            start_idx = ni
        # find project titles in section
        # pattern: title line followed by blank line(s) and then '(cid:###)\n\nUpdates' or '(cid:190) Updates' etc.
        # We'll look for a non-empty line that is followed within next 100 chars by 'Updates' (case-insensitive)
        # Split section into lines and examine
        lines = section.splitlines()
        for i, line in enumerate(lines):
            ln = line.strip()
            if not ln:
                continue
            # look ahead in the next 6 lines to find 'Updates' indicator
            lookahead = ' '.join(lines[i+1:i+7]).lower() if i+1 < len(lines) else ''
            if 'updates' in lookahead or 'project description' in lookahead or 'project updates' in lookahead:
                # consider this line a project title
                # filter out header lines
                if ln.lower().startswith('capital improvement') or ln.lower().startswith('agenda item'):
                    continue
                # ignore lines that look like 'Page x of y' or 'Discussion' etc
                if re.match(r'page\s+\d+', ln.lower()):
                    continue
                if len(ln) > 3 and len(ln) < 200:
                    # clean trailing punctuation
                    pname = ln.strip(' \t\n\r:')
                    design_projects.add(pname)
        
# Also, sometimes project titles appear as lines with no immediate 'Updates' but followed by 'Project Schedule' etc.
# As backup, capture lines in section that are title-case and relatively short and not starting with parentheses
if not design_projects:
    for doc in civic_docs:
        text = doc.get('text','')
        si = text.find('Capital Improvement Projects (Design)')
        if si == -1:
            continue
        ni = text.find('Capital Improvement Projects (', si+1)
        section = text[si:ni] if ni!=-1 else text[si:]
        parts = re.split(r"\n\n+", section)
        for p in parts:
            pstr = p.strip()
            if not pstr:
                continue
            # if part contains 'Updates' and first line looks like title
            if 'updates' in pstr.lower():
                first_line = pstr.splitlines()[0].strip()
                if len(first_line)>3 and len(first_line)<200:
                    design_projects.add(first_line)

# Now match design_projects to funding records with amount > 50000
matched = []
for proj in sorted(design_projects):
    pl = proj.lower()
    matches = []
    for f in fundings:
        if f['amount'] <= 50000:
            continue
        fn = f['name_l']
        # match if exact equal or one contains the other
        if fn == pl or fn in pl or pl in fn:
            matches.append({'funding_name': f['name'], 'amount': f['amount']})
    if matches:
        matched.append({'project_name': proj, 'funding_matches': matches})

# Count unique matched projects
count = len(matched)

result = {'count': count, 'matches': matched, 'design_projects_extracted_count': len(design_projects)}

import json
print('----BEGIN PRINT FORMAT----')
print('__RESULT__:')
print(json.dumps(result))
print('----END PRINT FORMAT----')"""

env_args = {'var_call_VBhtC9hpJRbNT16WmdZtMk4W': 'file_storage/call_VBhtC9hpJRbNT16WmdZtMk4W.json', 'var_call_DFwD6qNOXINdKlJ7slVtPbBE': 'file_storage/call_DFwD6qNOXINdKlJ7slVtPbBE.json'}

exec(code, env_args)
