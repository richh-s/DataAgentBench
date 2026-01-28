code = """import json, re

# Load the previous tool results from files
with open(var_call_i9fPgsVIaQXx6Vwcf9GVFWgf, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_kq69hvHWYSRKtORLwXydbpNC, 'r') as f:
    funding_rows = json.load(f)

# Normalize funding rows
for r in funding_rows:
    r['Project_Name'] = r.get('Project_Name','')
    try:
        r['Amount'] = int(r.get('Amount'))
    except:
        try:
            r['Amount'] = int(float(r.get('Amount')))
        except:
            r['Amount'] = None

found_projects = {}

def extract_title_heuristic(text, match_start):
    start = max(0, match_start-400)
    pre = text[start:match_start]
    lines = re.split(r"\r?\n", pre)
    for line in reversed(lines):
        s = line.strip()
        if not s:
            continue
        if s.startswith('(') or s.lower().startswith('cid:'):
            continue
        if re.search(r'updates?:$', s.lower()):
            continue
        if len(s) > 3 and len(s) < 200:
            return s
    window = text[start:match_start+300]
    m = re.search(r'([A-Z][A-Za-z0-9 &\-/]{3,120}(?:Project|Improvements|Repairs|Repair|Signs|Sirens|Bridge|Facility|Study|Infrastructure|Drainage|Road|Roads|Plan|Park))', window)
    if m:
        return m.group(1).strip()
    return None

# status mapping function
def determine_status(window):
    w = window.lower()
    if 'construction was completed' in w or 'complete construction' in w or 'completed' in w:
        return 'completed'
    if 'complete design' in w or 'project is in the preliminary design' in w or 'preliminary design' in w or 'design' in w:
        return 'design'
    if 'not started' in w or ('identified' in w and 'not' in w):
        return 'not started'
    if 'awaiting' in w or 'awaiting final' in w or 'awaiting final fema' in w:
        return 'design'
    if 'currently under construction' in w or 'begin construction' in w:
        return 'design'
    return None

# iterate documents and look for 'fema' or 'emergency'
for doc in civic_docs:
    text = doc.get('text','')
    text_low = text.lower()
    for m in re.finditer(r'fema|emergency', text_low):
        match_start = m.start()
        mention = m.group(0)
        title = extract_title_heuristic(text, match_start)
        window = text[max(0, match_start-400): match_start+400]
        status = determine_status(window)
        if not title:
            sents = re.split(r'[\.\n]', window)
            cand = None
            for s in sents:
                if 'project' in s.lower() or 'sirens' in s.lower() or 'warning' in s.lower() or 'repairs' in s.lower():
                    cand = s.strip()
                    break
            if cand:
                title = cand if len(cand) < 200 else cand[:200]
        if not title:
            title = '(unknown project near "{}")'.format(mention)
        key = (title, doc.get('filename'))
        if key not in found_projects:
            found_projects[key] = {
                'Extracted_Project_Name': title,
                'Filename': doc.get('filename'),
                'Mention': mention,
                'Status': status,
                'Funding_Matches': []
            }

# Now match funding rows to extracted projects
def normalize(s):
    return re.sub(r'[^a-z0-9]', ' ', s.lower())

for (title, filename), info in list(found_projects.items()):
    norm_title = normalize(title)
    matches = []
    for fr in funding_rows:
        fn = fr.get('Project_Name','')
        norm_fn = normalize(fn)
        if norm_title.strip() == '(unknown project near "fema")':
            if 'fema' in fn.lower():
                matches.append(fr)
            continue
        if norm_title in norm_fn or norm_fn in norm_title:
            matches.append(fr)
            continue
        tset = set([w for w in norm_title.split() if len(w)>3])
        fset = set([w for w in norm_fn.split() if len(w)>3])
        if len(tset & fset) >= 2:
            matches.append(fr)
            continue
        if info['Mention'] == 'fema' and 'fema' in fn.lower():
            matches.append(fr)
            continue
    if matches:
        for m in matches:
            info['Funding_Matches'].append({
                'Funding_ID': m.get('Funding_ID'),
                'Project_Name': m.get('Project_Name'),
                'Funding_Source': m.get('Funding_Source'),
                'Amount': m.get('Amount')
            })
    else:
        info['Funding_Matches'].append(None)

# Prepare output list
output = []
for (title, filename), info in found_projects.items():
    if info['Funding_Matches']:
        for fm in info['Funding_Matches']:
            if fm:
                output.append({
                    'Project_Name': fm.get('Project_Name'),
                    'Funding_Source': fm.get('Funding_Source'),
                    'Amount': fm.get('Amount'),
                    'Status': info.get('Status'),
                    'Mentioned_In_File': filename,
                    'Mention_Type': info.get('Mention')
                })
            else:
                output.append({
                    'Project_Name': info['Extracted_Project_Name'],
                    'Funding_Source': None,
                    'Amount': None,
                    'Status': info.get('Status'),
                    'Mentioned_In_File': filename,
                    'Mention_Type': info.get('Mention')
                })

# remove duplicates by Project_Name + Funding_Source + Amount
seen = set()
final = []
for r in output:
    key = (r.get('Project_Name'), r.get('Funding_Source'), r.get('Amount'))
    if key in seen:
        continue
    seen.add(key)
    final.append(r)

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_i9fPgsVIaQXx6Vwcf9GVFWgf': 'file_storage/call_i9fPgsVIaQXx6Vwcf9GVFWgf.json', 'var_call_JwmRPtqX1MX9rXaQGM5997gn': ['Funding'], 'var_call_kq69hvHWYSRKtORLwXydbpNC': 'file_storage/call_kq69hvHWYSRKtORLwXydbpNC.json'}

exec(code, env_args)
