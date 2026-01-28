code = """import json, re

with open(var_call_BluEeKeRlnhnPiwlKGMEmLEa, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_jPItYFKSpJ9uZinUyW91jl6C, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build normalized funding map
def normalize_name(s):
    if not s:
        return ''
    s = s.lower()
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthetical suffixes
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

fund_map = {}
for r in funding_rows:
    name = r.get('Project_Name') or ''
    amt = r.get('Total_Amount') or 0
    try:
        amt_int = int(amt)
    except:
        digits = ''.join(ch for ch in str(amt) if ch.isdigit())
        amt_int = int(digits) if digits else 0
    key = normalize_name(name)
    fund_map.setdefault(key, 0)
    fund_map[key] += amt_int

# Indicators for spring 2022
indicators = ['spring 2022', 'spring/summer 2022', 'spring/summer', 'march 2022', 'april 2022', 'may 2022', '2022-03', '2022-04', '2022-05', 'begin construction', 'begin design', 'begin construction: spring']

# keywords likely in project titles
title_keywords = ['project', 'park', 'road', 'improvement', 'improvements', 'facility', 'median', 'culvert', 'bridge', 'skate', 'playground', 'storm', 'water', 'center', 'treatment', 'resurfacing', 'synchronization', 'signal', 'lane', 'right turn', 'retaining', 'paver', 'shade', 'bench', 'walkway', 'drain', 'drainage', 'guardrail', 'asphalt']

def is_title_line(line):
    if not line:
        return False
    s = line.strip()
    if len(s) < 5 or len(s) > 120:
        return False
    low = s.lower()
    if low.startswith(('to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject:', 'updates:', 'project schedule:', 'project description:', 'page', 'agenda item')):
        return False
    if low.startswith('(cid') or low.startswith('cid:'):
        return False
    if ':' in s and not any(k in low for k in ['pch at', 'pch', 'at']):
        # likely a schedule line like 'Begin Construction: Spring 2022'
        return False
    # if contains title keywords
    for kw in title_keywords:
        if kw in low:
            return True
    # else if Title Case heuristic: count capitalized words
    words = [w for w in s.split() if w]
    cap_count = sum(1 for w in words if w[0].isupper())
    if cap_count >= 2:
        return True
    return False

found = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if any(ind in low for ind in indicators):
            # search upwards for title candidate within 10 lines
            title = None
            for j in range(i-1, max(-1, i-12), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                if is_title_line(cand):
                    title = cand
                    break
            if title:
                # clean parentheses like (cid...) at start
                title = re.sub(r"^\(cid:[0-9]+\)\s*", '', title)
                # remove trailing words like 'Project' duplication? keep as is
                ntitle = title.strip()
                if ntitle.lower() not in [t.lower() for t in found]:
                    found.append(ntitle)

# Deduplicate
projects = []
seen = set()
for p in found:
    n = p.strip()
    if n.lower() not in seen:
        seen.add(n.lower())
        projects.append(n)

# Match projects to funding
matched_keys = set()
unmatched = []
for p in projects:
    np = normalize_name(p)
    matched = False
    # exact normalized match
    if np in fund_map:
        matched_keys.add(np)
        matched = True
    else:
        # containment matches
        for fk in fund_map:
            if np and (np in fk or fk in np):
                matched_keys.add(fk)
                matched = True
                break
    if not matched:
        unmatched.append(p)

total = sum(fund_map[k] for k in matched_keys)

result = {
    'count_projects_started_spring_2022': len(projects),
    'total_matched_funding': total,
    'extracted_projects': projects,
    'matched_funding_keys': sorted(list(matched_keys)),
    'unmatched_projects': unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cJibmufZIbpLLOJoY7hsw2Qi': ['civic_docs'], 'var_call_BluEeKeRlnhnPiwlKGMEmLEa': 'file_storage/call_BluEeKeRlnhnPiwlKGMEmLEa.json', 'var_call_jPItYFKSpJ9uZinUyW91jl6C': 'file_storage/call_jPItYFKSpJ9uZinUyW91jl6C.json', 'var_call_8mL8xs7Mp3WGdrp4zxBO2Mga': {'count_projects_started_spring_2022': 63, 'total_matched_funding': 0, 'extracted_projects': ['(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Advertise for Bidding: February 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: July 2022', '(cid:131) Complete Design: April 2021', '(cid:131) Complete Design: February 2021', '(cid:131) Advertise: July 2021', 'the County.', '(cid:131) Complete Design: Spring 2021', '(cid:131) Complete Design: December 2021', '(cid:131) Complete Design: Summer 2021', '(cid:131) Complete Design: Fall 2021', '(cid:131) Complete Design: Winter 2021', '(cid:131) Advertise: Summer 2022', '(cid:131) Complete Design: Summer 2022', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Complete Design: March 2021', '(cid:131) Complete Design: May 2021', 'from the County.', '(cid:131) Complete Design: July 2021', '(cid:131) Complete Design: late Summer 2021', '(cid:131) Advertise: August 2021', 'be signed and executed.', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Spring 2021 (Out to bid now)', '(cid:131) Complete Design: May 2022', 'Agenda Item # 4.A.', '(cid:190) Estimated Schedule:', '(cid:131) Complete Design: Fall 2022', '(cid:131) Complete Design: August 2021', '(cid:131) Advertise: September 2021', 'pre-construction meeting has been scheduled for June 17th.', 'and verifying that they comply with the project specifications.', '(cid:131) Advertise: Fall 2022', '(cid:131) Advertise: October 2021', 'submittals.', 'related submittals.', '(cid:131) Complete Design: September 2021', 'project related submittals.', '(cid:131) Advertise: November 2021', '(cid:131) Bids Received: September 7, 2021', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Advertise: February 2022', '(cid:131) Final Design: Completed.', '(cid:131) Complete Design: Winter 2022', '(cid:131) Advertise: TBD', '(cid:131) Advertise for Bidding: Summer 2023', '(cid:131) Complete Design: Spring 2023', '(cid:131) Advertise: Winter 2022', '(cid:131) Complete Design: January 2022', 'project will begin in conjunction with the PCH Median Improvement', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Staff is currently working on the design of the project and anticipates', 'draft plans are expected to be completed in early 2022. The Planning', '(cid:190) Updates:', '(cid:131) The City has hired a consultant to design this project. The design has', '(cid:131) Complete Design: April 2022', 'project will be advertised for construction bids with construction', '(cid:131) The project design has begun and preliminary design should be', 'the past several months to complete the engineering work, and the final'], 'matched_funding_projects': [], 'unmatched_projects': ['(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Advertise for Bidding: February 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: July 2022', '(cid:131) Complete Design: April 2021', '(cid:131) Complete Design: February 2021', '(cid:131) Advertise: July 2021', 'the County.', '(cid:131) Complete Design: Spring 2021', '(cid:131) Complete Design: December 2021', '(cid:131) Complete Design: Summer 2021', '(cid:131) Complete Design: Fall 2021', '(cid:131) Complete Design: Winter 2021', '(cid:131) Advertise: Summer 2022', '(cid:131) Complete Design: Summer 2022', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Complete Design: March 2021', '(cid:131) Complete Design: May 2021', 'from the County.', '(cid:131) Complete Design: July 2021', '(cid:131) Complete Design: late Summer 2021', '(cid:131) Advertise: August 2021', 'be signed and executed.', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Spring 2021 (Out to bid now)', '(cid:131) Complete Design: May 2022', 'Agenda Item # 4.A.', '(cid:190) Estimated Schedule:', '(cid:131) Complete Design: Fall 2022', '(cid:131) Complete Design: August 2021', '(cid:131) Advertise: September 2021', 'pre-construction meeting has been scheduled for June 17th.', 'and verifying that they comply with the project specifications.', '(cid:131) Advertise: Fall 2022', '(cid:131) Advertise: October 2021', 'submittals.', 'related submittals.', '(cid:131) Complete Design: September 2021', 'project related submittals.', '(cid:131) Advertise: November 2021', '(cid:131) Bids Received: September 7, 2021', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Advertise: February 2022', '(cid:131) Final Design: Completed.', '(cid:131) Complete Design: Winter 2022', '(cid:131) Advertise: TBD', '(cid:131) Advertise for Bidding: Summer 2023', '(cid:131) Complete Design: Spring 2023', '(cid:131) Advertise: Winter 2022', '(cid:131) Complete Design: January 2022', 'project will begin in conjunction with the PCH Median Improvement', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Staff is currently working on the design of the project and anticipates', 'draft plans are expected to be completed in early 2022. The Planning', '(cid:190) Updates:', '(cid:131) The City has hired a consultant to design this project. The design has', '(cid:131) Complete Design: April 2022', 'project will be advertised for construction bids with construction', '(cid:131) The project design has begun and preliminary design should be', 'the past several months to complete the engineering work, and the final']}}

exec(code, env_args)
