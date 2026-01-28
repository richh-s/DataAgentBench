code = """import json, re
# load civic docs
path_docs = var_call_BbHlkOS5ptYiDuPuA4GtohCC
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# load funding
path_fund = var_call_DXrPxEQ0SOU915sF3lFLSsKP
with open(path_fund, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# normalize funding names and ensure Amount ints
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0
    r['name_low'] = r['Project_Name'].lower()

found_projects = []

# scan for 'Begin Construction' lines mentioning Spring and 2022
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if 'begin construction' in low and 'spring' in low and '2022' in low:
            # search upward for project title
            j = i-1
            candidate = None
            skip_tokens = ['updates', 'project schedule', 'project description', 'page', 'agenda', 'item', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion', 'subject', 'project updates', 'estimated schedule']
            while j >= 0 and (lines[j].strip()=='' or any(tok in lines[j].lower() for tok in skip_tokens) or lines[j].strip().lower().startswith('(cid:')):
                j -= 1
            if j>=0:
                cand = lines[j].strip()
                if len(cand) > 3:
                    candidate = cand.rstrip(':')
            if candidate:
                found_projects.append(candidate)
        else:
            if 'begin construction' in low and 'spring' in low and '2022' not in low:
                look = ' '.join(lines[i:i+3]).lower()
                if '2022' in look:
                    j = i-1
                    candidate = None
                    skip_tokens = ['updates', 'project schedule', 'project description', 'page', 'agenda', 'item', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion', 'subject', 'project updates', 'estimated schedule']
                    while j >= 0 and (lines[j].strip()=='' or any(tok in lines[j].lower() for tok in skip_tokens) or lines[j].strip().lower().startswith('(cid:')):
                        j -= 1
                    if j>=0:
                        cand = lines[j].strip()
                        if len(cand) > 3:
                            candidate = cand.rstrip(':')
                    if candidate:
                        found_projects.append(candidate)

# also search with regex for patterns like 'Begin Construction: Spring/Summer 2022'
for doc in docs:
    text = doc.get('text','')
    for m in re.finditer(r'begin\s+construction[:\s-]*([^\n]{0,120})', text, re.IGNORECASE):
        seg = m.group(0)
        if re.search(r'spring', seg, re.IGNORECASE) and re.search(r'2022', text[max(0,m.start()-50):m.end()+50], re.IGNORECASE):
            start = m.start()
            window_start = max(0, start-500)
            snippet = text[window_start:start]
            lines = snippet.splitlines()
            candidate = None
            for line in reversed(lines):
                s = line.strip()
                if not s:
                    continue
                low = s.lower()
                if any(tok in low for tok in ['updates','project schedule','project description','page','agenda','item','approved by','date prepared','meeting date','recommended action','discussion','subject']):
                    continue
                if s.startswith('(') or s.startswith('cid:'):
                    continue
                candidate = s.rstrip(':')
                break
            if candidate:
                found_projects.append(candidate)

# normalize and deduplicate
seen = set()
projects = []
for p in found_projects:
    np = ' '.join(p.split())
    if np not in seen:
        seen.add(np)
        projects.append(np)

# if still empty, fallback: look for lines telling 'Begin Construction: Spring 2022' with months
if not projects:
    for doc in docs:
        text = doc.get('text','')
        for m in re.finditer(r'begin\s+construction[:\s-]*.*(March|April|May|Mar\.|Apr\.|May)\s*2022', text, re.IGNORECASE):
            start = m.start()
            window_start = max(0, start-400)
            snippet = text[window_start:start]
            lines = snippet.splitlines()
            candidate = None
            for line in reversed(lines):
                s = line.strip()
                if not s:
                    continue
                if any(tok in s.lower() for tok in ['updates','project schedule','project description','page','agenda','item']):
                    continue
                candidate = s.rstrip(':')
                break
            if candidate:
                if candidate not in seen:
                    seen.add(candidate)
                    projects.append(candidate)

# Now match projects to funding entries
proj_results = []
total_funding = 0
for p in projects:
    p_low = p.lower()
    matched = []
    sum_p = 0
    for r in funding:
        fname = r['Project_Name']
        if p_low in fname.lower() or fname.lower() in p_low:
            matched.append({'Project_Name': fname, 'Amount': r['Amount']})
            sum_p += r['Amount']
    # token-based fallback
    if not matched:
        p_tokens = set([w for w in re.findall(r"\w+", p_low) if len(w)>3])
        for r in funding:
            fname_low = r['Project_Name'].lower()
            f_tokens = set([w for w in re.findall(r"\w+", fname_low) if len(w)>3])
            if len(p_tokens & f_tokens) >= 2:
                matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})
                sum_p += r['Amount']
    proj_results.append({'name': p, 'matched_sum': sum_p, 'matched_records': matched})
    total_funding += sum_p

out = {'count': len(projects), 'total_funding': total_funding, 'projects': proj_results}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BbHlkOS5ptYiDuPuA4GtohCC': 'file_storage/call_BbHlkOS5ptYiDuPuA4GtohCC.json', 'var_call_wzdYOCoVDSdfZqe0nUNWVPJq': [], 'var_call_GlrSSShezpsTLg3CJ6gEOWVe': 'file_storage/call_GlrSSShezpsTLg3CJ6gEOWVe.json', 'var_call_p0BJfJnAHeSkmth79jwrGCCJ': 'file_storage/call_p0BJfJnAHeSkmth79jwrGCCJ.json', 'var_call_DXrPxEQ0SOU915sF3lFLSsKP': 'file_storage/call_DXrPxEQ0SOU915sF3lFLSsKP.json'}

exec(code, env_args)
