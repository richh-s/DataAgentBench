code = """import json

# Load files
with open(var_call_BluEeKeRlnhnPiwlKGMEmLEa, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_jPItYFKSpJ9uZinUyW91jl6C, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build funding map
fund_map = {}
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_int = int(amt)
    except:
        amt_int = 0
        if amt:
            digits = ''.join(ch for ch in str(amt) if ch.isdigit())
            if digits:
                amt_int = int(digits)
    fund_map[name] = amt_int

# Search for lines indicating begin construction in spring 2022
season_indicators = ['spring 2022', 'spring/summer 2022', 'spring/summer 2022', 'spring/summer', 'march 2022', 'april 2022', 'may 2022', '2022-03', '2022-04', '2022-05']

def is_good_title(line):
    s = line.strip()
    if not s:
        return False
    if len(s) < 3 or len(s) > 200:
        return False
    low = s.lower()
    bad_starts = ['to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject:', 'updates:', 'project schedule:', 'project description:', 'page', 'agenda item']
    for b in bad_starts:
        if low.startswith(b):
            return False
    if low.startswith('(cid') or low.startswith('cid:'):
        return False
    if ':' in s and len(s.split(':')[0].split())>4:
        return False
    return True

found = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'begin construction' in low or 'begin construction:' in low:
            # check for season indicators in the same line or nearby lines
            window = ' '.join(lines[max(0,i-2):min(len(lines), i+3)]).lower()
            if any(ind in window for ind in season_indicators) or 'spring' in window and '2022' in window:
                # find title by scanning backward
                title = None
                for j in range(i-1, max(-1, i-10), -1):
                    cand = lines[j].strip()
                    if is_good_title(cand):
                        title = cand
                        break
                if title:
                    # clean
                    title = title.replace('\ufeff', '').strip()
                    if title and title.lower() not in [t.lower() for t in found]:
                        found.append(title)

# Also search for lines with 'begin design: spring' or 'complete design: march 2022' that indicate start in spring
for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'begin design' in low or 'complete design' in low or 'begin design:' in low:
            window = ' '.join(lines[max(0,i-2):min(len(lines), i+3)]).lower()
            if any(ind in window for ind in season_indicators) or ('spring' in window and '2022' in window):
                title = None
                for j in range(i-1, max(-1, i-10), -1):
                    cand = lines[j].strip()
                    if is_good_title(cand):
                        title = cand
                        break
                if title and title.lower() not in [t.lower() for t in found]:
                    found.append(title)

# If none found, as fallback look for any paragraph mentioning spring 2022 and pick the first reasonable line
if not found:
    for doc in civic_docs:
        text = doc.get('text','')
        paras = [p.strip() for p in text.split('\n\n') if p.strip()]
        for p in paras:
            low = p.lower()
            if 'spring' in low and '2022' in low:
                lines = [ln.strip() for ln in p.splitlines() if ln.strip()]
                for ln in lines:
                    if is_good_title(ln):
                        if ln.lower() not in [t.lower() for t in found]:
                            found.append(ln)

# Match to funding
matched = set()
unmatched = []
for proj in found:
    plow = proj.lower()
    matched_flag = False
    for fk in fund_map:
        if not fk:
            continue
        fk_low = fk.lower()
        if fk_low == plow or plow in fk_low or fk_low in plow:
            matched.add(fk)
            matched_flag = True
            break
    if not matched_flag:
        unmatched.append(proj)

total_funding = sum(fund_map[k] for k in matched)

result = {
    'count_projects_started_spring_2022': len(found),
    'total_matched_funding': total_funding,
    'extracted_projects': found,
    'matched_funding_projects': sorted(list(matched)),
    'unmatched_projects': unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cJibmufZIbpLLOJoY7hsw2Qi': ['civic_docs'], 'var_call_BluEeKeRlnhnPiwlKGMEmLEa': 'file_storage/call_BluEeKeRlnhnPiwlKGMEmLEa.json', 'var_call_jPItYFKSpJ9uZinUyW91jl6C': 'file_storage/call_jPItYFKSpJ9uZinUyW91jl6C.json'}

exec(code, env_args)
