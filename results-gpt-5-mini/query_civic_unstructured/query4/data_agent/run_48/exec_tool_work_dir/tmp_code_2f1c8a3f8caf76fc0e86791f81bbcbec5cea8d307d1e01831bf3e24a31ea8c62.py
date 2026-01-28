code = """import json
# Load documents and funding from storage variables
path_docs = var_call_BbHlkOS5ptYiDuPuA4GtohCC
path_fund = var_call_DXrPxEQ0SOU915sF3lFLSsKP
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(path_fund, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# normalize funding amounts
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0

skip_tokens = ['updates', 'project schedule', 'project description', 'page', 'agenda', 'item', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion', 'subject', 'project updates', 'estimated schedule']

candidates = []
for doc in docs:
    lines = doc.get('text','').splitlines()
    n = len(lines)
    for i, line in enumerate(lines):
        low = line.lower()
        # check for begin construction lines mentioning spring and 2022 on same line
        if 'begin construction' in low and 'spring' in low and '2022' in low:
            # look upward for project title
            j = i-1
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
                candidates.append(s.rstrip(':'))
                break
        # check for begin construction and spring but 2022 nearby next lines
        elif 'begin construction' in low and 'spring' in low and '2022' not in low:
            look = ' '.join(lines[i:i+3]).lower()
            if '2022' in look:
                j = i-1
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
                    candidates.append(s.rstrip(':'))
                    break
        # check for month names and 2022 and 'Begin Construction' maybe not needed
        else:
            low_line = low
            if ('march' in low_line or 'april' in low_line or 'may' in low_line) and '2022' in low_line:
                # find previous project title
                j = i-1
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
                    candidates.append(s.rstrip(':'))
                    break

# dedupe preserving order
seen = set()
projects = []
for p in candidates:
    np = ' '.join(p.split())
    if np not in seen:
        seen.add(np)
        projects.append(np)

# If still empty, try scanning for lines that explicitly say 'Begin Construction: Spring/Summer 2022' in the entire text
if not projects:
    for doc in docs:
        text = doc.get('text','')
        if 'begin construction' in text.lower() and 'spring' in text.lower() and '2022' in text.lower():
            # heuristic: find headings that look like project names: lines in Title Case before 'Project' word
            lines = text.splitlines()
            for i, line in enumerate(lines):
                if 'begin construction' in line.lower() and 'spring' in line.lower() and '2022' in line.lower():
                    j = i-1
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
                        if s.rstrip(':') not in seen:
                            seen.add(s.rstrip(':'))
                            projects.append(s.rstrip(':'))
                        break
                    
# match projects to funding
results = []
total = 0
for p in projects:
    p_low = p.lower()
    matched = []
    sum_amt = 0
    for r in funding:
        fname = r['Project_Name']
        if p_low in fname.lower() or fname.lower() in p_low:
            matched.append({'Project_Name': fname, 'Amount': r['Amount']})
            sum_amt += r['Amount']
    # token overlap fallback
    if not matched:
        p_tokens = set(w for w in p_low.split() if len(w) > 3)
        for r in funding:
            f_tokens = set(w for w in r['Project_Name'].lower().split() if len(w) > 3)
            if len(p_tokens & f_tokens) >= 2:
                matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})
                sum_amt += r['Amount']
    results.append({'name': p, 'matched_sum': sum_amt, 'matched_records': matched})
    total += sum_amt

out = {'count': len(projects), 'total_funding': total, 'projects': results}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BbHlkOS5ptYiDuPuA4GtohCC': 'file_storage/call_BbHlkOS5ptYiDuPuA4GtohCC.json', 'var_call_wzdYOCoVDSdfZqe0nUNWVPJq': [], 'var_call_GlrSSShezpsTLg3CJ6gEOWVe': 'file_storage/call_GlrSSShezpsTLg3CJ6gEOWVe.json', 'var_call_p0BJfJnAHeSkmth79jwrGCCJ': 'file_storage/call_p0BJfJnAHeSkmth79jwrGCCJ.json', 'var_call_DXrPxEQ0SOU915sF3lFLSsKP': 'file_storage/call_DXrPxEQ0SOU915sF3lFLSsKP.json', 'var_call_iNK6sukz2U7vTGFyR2wJgxFK': 'file_storage/call_iNK6sukz2U7vTGFyR2wJgxFK.json'}

exec(code, env_args)
