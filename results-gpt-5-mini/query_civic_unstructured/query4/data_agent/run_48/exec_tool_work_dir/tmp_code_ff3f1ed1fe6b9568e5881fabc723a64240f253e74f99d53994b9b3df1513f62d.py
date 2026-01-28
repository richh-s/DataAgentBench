code = """import json, re
# load civic docs
path_docs = var_call_BbHlkOS5ptYiDuPuA4GtohCC
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# load funding
path_fund = var_call_DXrPxEQ0SOU915sF3lFLSsKP
with open(path_fund, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# normalize funding
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0

fund_names = [r['Project_Name'] for r in funding]

skip_tokens = ['updates', 'project schedule', 'project description', 'page', 'agenda', 'item', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion', 'subject', 'project updates', 'estimated schedule']

found = []

for doc in docs:
    lines = doc.get('text','').splitlines()
    # find lines that mention spring and 2022
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'spring' in low and '2022' in low:
            # look upward for candidate title
            j = idx-1
            while j >= 0:
                s = lines[j].strip()
                if not s:
                    j -= 1
                    continue
                low_s = s.lower()
                if any(tok in low_s for tok in skip_tokens) or low_s.startswith('(cid:') or low_s.startswith('('):
                    j -= 1
                    continue
                if len(s) < 4:
                    j -= 1
                    continue
                # accept this line as project name
                found.append(s.rstrip(':'))
                break
        # also check for explicit month mentions
        m = re.search(r'\b(march|april|may)\b', low)
        if m and '2022' in low:
            j = idx-1
            while j >= 0:
                s = lines[j].strip()
                if not s:
                    j -= 1
                    continue
                low_s = s.lower()
                if any(tok in low_s for tok in skip_tokens) or low_s.startswith('(cid:') or low_s.startswith('('):
                    j -= 1
                    continue
                if len(s) < 4:
                    j -= 1
                    continue
                found.append(s.rstrip(':'))
                break

# dedupe preserving order
seen = set()
projects = []
for p in found:
    np = ' '.join(p.split())
    if np not in seen:
        seen.add(np)
        projects.append(np)

# If still empty, try lines containing 'Begin Construction' with nearby 2022/months
if not projects:
    for doc in docs:
        text = doc.get('text','')
        for m in re.finditer(r'begin construction[:\s-]*([^\n]{0,120})', text, re.IGNORECASE):
            seg = m.group(0).lower()
            if 'spring' in seg or 'march' in seg or 'april' in seg or 'may' in seg or '2022' in text[max(0,m.start()-50):m.end()+50].lower():
                # find previous line
                start = m.start()
                snippet = text[max(0,start-300):start]
                lines2 = snippet.splitlines()
                for line in reversed(lines2):
                    s = line.strip()
                    if not s:
                        continue
                    low_s = s.lower()
                    if any(tok in low_s for tok in skip_tokens) or low_s.startswith('(cid:') or low_s.startswith('('):
                        continue
                    projects.append(s.rstrip(':'))
                    break

# dedupe again
seen = set(); projects2 = []
for p in projects:
    np = ' '.join(p.split())
    if np not in seen:
        seen.add(np)
        projects2.append(np)

projects = projects2

# match to funding
results = []
total = 0
for p in projects:
    p_low = p.lower()
    matched = []
    sum_amt = 0
    for r in funding:
        if p_low in r['Project_Name'].lower() or r['Project_Name'].lower() in p_low:
            matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})
            sum_amt += r['Amount']
    # token overlap fallback
    if not matched:
        p_tokens = set([w for w in re.findall(r"\w+", p_low) if len(w)>3])
        for r in funding:
            f_tokens = set([w for w in re.findall(r"\w+", r['Project_Name'].lower()) if len(w)>3])
            if len(p_tokens & f_tokens) >= 2:
                matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})
                sum_amt += r['Amount']
    results.append({'name': p, 'matched_sum': sum_amt, 'matched_records': matched})
    total += sum_amt

out = {'count': len(projects), 'total_funding': total, 'projects': results}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BbHlkOS5ptYiDuPuA4GtohCC': 'file_storage/call_BbHlkOS5ptYiDuPuA4GtohCC.json', 'var_call_wzdYOCoVDSdfZqe0nUNWVPJq': [], 'var_call_GlrSSShezpsTLg3CJ6gEOWVe': 'file_storage/call_GlrSSShezpsTLg3CJ6gEOWVe.json', 'var_call_p0BJfJnAHeSkmth79jwrGCCJ': 'file_storage/call_p0BJfJnAHeSkmth79jwrGCCJ.json', 'var_call_DXrPxEQ0SOU915sF3lFLSsKP': 'file_storage/call_DXrPxEQ0SOU915sF3lFLSsKP.json'}

exec(code, env_args)
