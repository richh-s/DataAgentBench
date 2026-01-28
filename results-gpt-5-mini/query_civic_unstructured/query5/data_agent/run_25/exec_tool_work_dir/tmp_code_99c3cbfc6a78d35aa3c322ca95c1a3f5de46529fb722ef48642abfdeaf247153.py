code = """import json
import re

# Load data from storage keys (file paths)
with open(var_call_lKT8uPWviNN3rRqoFcXonicP, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_fS8Y5kTNulIFeAWyFvtLhN3D, 'r') as f:
    funding = json.load(f)

# Convert funding amounts to int
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        r['Amount'] = 0

# Helper to find project title lines
project_blocks = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # Identify project title heuristically: contains 'Project' and not too long
        if 'Project' in line and 3 < len(line) < 200:
            # clean line
            title = line.strip()
            # capture block: this line + next 20 lines
            block_lines = lines[i:i+20]
            block = '\n'.join(block_lines)
            project_blocks.append({'title': title, 'block': block, 'filename': doc.get('filename')})

# Now detect disaster-related blocks that started in 2022
keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'woolsey', 'fire', 'fema/']
disaster_projects = []
for pb in project_blocks:
    block = pb['block'].lower()
    title = pb['title'].strip()
    is_disaster = any(k in block for k in keywords)
    started_2022 = '2022' in block
    # also if title itself includes disaster keywords
    if not is_disaster:
        is_disaster = any(k in title.lower() for k in keywords)
    if is_disaster and started_2022:
        # clean title remove trailing punctuation
        clean_title = re.sub(r"\s+", ' ', title)
        clean_title = clean_title.strip(' :\t\n-')
        disaster_projects.append(clean_title)

# Deduplicate
disaster_projects = list(dict.fromkeys(disaster_projects))

# If no projects found by heuristic, also consider funding entries with FEMA/CalOES and check civic docs for 2022 mention of that base name anywhere
if not disaster_projects:
    # find funding projects with fema/caloes
    candidates = [r['Project_Name'] for r in funding if any(k in r['Project_Name'].lower() for k in ['fema','caloes','caljpia'])]
    # search civic docs text for these names plus 2022
    for cand in candidates:
        cand_low = cand.lower()
        for doc in civic_docs:
            if '2022' in doc.get('text','') and cand_low.split('(')[0].strip() in doc.get('text','').lower():
                disaster_projects.append(cand)
                break

# Matching funding records to disaster_projects
matched_funding = []
for r in funding:
    pname = r['Project_Name'].lower()
    for dp in disaster_projects:
        dp_clean = dp.lower()
        # match if dp_clean in pname or significant overlap of words
        if dp_clean in pname or pname in dp_clean:
            matched_funding.append(r)
            break
        else:
            # word overlap: count common words length>3
            pwords = set([w for w in re.findall(r"\w+", pname) if len(w)>3])
            dwords = set([w for w in re.findall(r"\w+", dp_clean) if len(w)>3])
            if pwords and dwords and len(pwords & dwords) >= 2:
                matched_funding.append(r)
                break

# Sum amounts
total = sum(r['Amount'] for r in matched_funding)

# Prepare output
result = {
    'disaster_projects_found': disaster_projects,
    'matched_funding_count': len(matched_funding),
    'total_disaster_funding_started_2022': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8CSv4MQuV8zmMnSqLtgrYNGU': ['civic_docs'], 'var_call_eLTMZjr8CgQ9dUU26Ub6TmYQ': ['Funding'], 'var_call_lKT8uPWviNN3rRqoFcXonicP': 'file_storage/call_lKT8uPWviNN3rRqoFcXonicP.json', 'var_call_fS8Y5kTNulIFeAWyFvtLhN3D': 'file_storage/call_fS8Y5kTNulIFeAWyFvtLhN3D.json'}

exec(code, env_args)
