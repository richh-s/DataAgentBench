code = """import json
import re

# Load storage variables (file paths)
path_funding = var_call_EYCzqE7wqrvzvymzEmvMM8Wh
path_docs = var_call_0ulYhEwqv70kRYFJ4yo60ckA

with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Helper normalize
import string

def normalize(s):
    if s is None:
        return ""
    s = s.lower()
    # remove punctuation
    s = re.sub(r"[\(\)\,\./\-:]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Keywords for park-related
keywords = ['park','playground','walkway','bench','benches','shade structure','play area','playground']

completed_projects = set()

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'completed' in line.lower() and '2022' in line:
            # backscan up to 8 lines to find a candidate project name
            for j in range(i-1, max(i-9, -1), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                low = cand.lower()
                # skip generic lines
                if any(tok in low for tok in ['updates','project schedule','agenda','page','item','to:','prepared by','approved by','date prepared','meeting date','subject','discussion','recommended action']):
                    continue
                # skip lines that look like labels or bullets
                if low.endswith(':'):
                    continue
                # if line is short and likely a title
                if 1 <= len(cand) <= 120:
                    # Clean candidate
                    cand_clean = cand.strip()
                    completed_projects.add(cand_clean)
                    break
        # also catch lines like 'Complete Construction: April 2023' but with 2022
        m = re.search(r'complete construction:\s*(.*)', line, re.I)
        if m and '2022' in m.group(1):
            # backscan
            for j in range(i-1, max(i-9, -1), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                if any(tok in cand.lower() for tok in ['updates','project schedule',':']):
                    continue
                completed_projects.add(cand)
                break

# Filter completed projects to park-related using keywords
park_completed = set()
for p in completed_projects:
    lp = p.lower()
    if any(k in lp for k in keywords):
        park_completed.add(p)

# Also include explicit matches where the project name line itself contains 'Bluffs Park Shade Structure' from preview
# Prepare normalized funding list
for rec in funding:
    # Amount as int
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        try:
            rec['Amount'] = int(float(rec['Amount']))
        except:
            rec['Amount'] = 0

# Match funding records by name
matched_records = []
matched_names = set()

def norm_cmp(a,b):
    na = normalize(a)
    nb = normalize(b)
    return na, nb

for p in park_completed:
    np = normalize(p)
    for rec in funding:
        nf = normalize(rec.get('Project_Name',''))
        if np and (np in nf or nf in np):
            matched_records.append(rec)
            matched_names.add(rec.get('Project_Name'))

# It's possible some funding records exactly match project names that include park and were completed in 2022 but weren't captured above.
# To be safer, also scan funding for names containing park and look for civic doc text mentioning completion of that project in 2022.
for rec in funding:
    pname = rec.get('Project_Name','')
    if any(k in pname.lower() for k in keywords):
        # search docs for lines mentioning this project name and completed + 2022
        found = False
        for doc in docs:
            if pname in doc.get('text','') and 'completed' in doc.get('text','').lower() and '2022' in doc.get('text',''):
                matched_records.append(rec)
                matched_names.add(rec.get('Project_Name'))
                break

# Deduplicate matched_records by Funding_ID
seen = set()
uniq_matched = []
for r in matched_records:
    fid = r.get('Funding_ID')
    if fid not in seen:
        seen.add(fid)
        uniq_matched.append(r)

total = sum(r.get('Amount',0) for r in uniq_matched)

result = {
    'park_projects_completed_2022_found_in_docs': list(park_completed),
    'matched_funding_records': uniq_matched,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Bd5UBiudHji4mDsQ6kt1Spy5': ['civic_docs'], 'var_call_HoFAmUYycjq9e6euUCkRP0Bo': ['Funding'], 'var_call_EYCzqE7wqrvzvymzEmvMM8Wh': 'file_storage/call_EYCzqE7wqrvzvymzEmvMM8Wh.json', 'var_call_0ulYhEwqv70kRYFJ4yo60ckA': 'file_storage/call_0ulYhEwqv70kRYFJ4yo60ckA.json'}

exec(code, env_args)
