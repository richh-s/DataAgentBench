code = """import json, re
from collections import defaultdict
import string

with open(var_call_4HdUiHnSFJBjIwK87YHCGUTC, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_wwbgDMXQ67DvK4hs4ybAOibf, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Prepare funding map: normalized name -> total amount (sum duplicates)
def normalize(s):
    if s is None:
        return ''
    s = s.lower()
    s = re.sub(r"\([^)]*\)", "", s)  # remove parentheses
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r"\s+", " ", s).strip()
    return s

funding_map = defaultdict(int)
funding_entries = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt_raw = r.get('Amount')
    try:
        amt = int(float(amt_raw))
    except:
        amt = 0
    norm = normalize(name)
    funding_map[norm] += amt
    funding_entries.append({'orig': name, 'norm': norm, 'amount': amt})

# Patterns for spring 2022
spring_patterns = [r"spring[^\n,]*2022", r"2022[^\n,]*spring", r"march\s*2022", r"april\s*2022", r"may\s*2022", r"2022-03", r"2022-04", r"2022-05", r"03/2022", r"04/2022", r"05/2022", r"2022/03", r"2022/04", r"2022/05"]
pat = re.compile('|'.join(spring_patterns), re.IGNORECASE)

keywords = ["project","park","road","repair","repairs","improvement","improvements","resurfacing","drain","storm","culvert","bridge","slope","playground","skate","walkway","water","treatment","signal","median","crosswalk","traffic","retaining","bluffs","malibu","pch","broad beach","encinal","latigo","westward","trancas","marie canyon","civic center","malibu road","point dume","slope","drainage"]

candidates = []

for doc in civic_docs:
    text = doc.get('text','')
    for m in pat.finditer(text):
        start = m.start()
        context = text[max(0, start-800): start+200]
        # clean (remove weird cid tokens)
        context_clean = re.sub(r"\(cid:\d+\)", "", context)
        lines = [ln.strip() for ln in context_clean.splitlines() if ln.strip()]
        # search backward for keyword-containing line
        candidate = None
        for ln in reversed(lines[:-0] if len(lines)>0 else []):
            low = ln.lower()
            # skip generic
            if any(g in low for g in ['updates', 'project schedule', 'project description', 'agenda', 'discussion', 'recommended action', 'subject', 'meeting date', 'item', 'approved by', 'date prepared', 'page']):
                continue
            if len(ln) < 4:
                continue
            # if line contains any keyword, choose
            if any(k in low for k in keywords):
                candidate = ln
                break
            # also pick lines that look like title case (many capitals)
            words = ln.split()
            cap_count = sum(1 for w in words if w[:1].isupper())
            if cap_count >= max(1, len(words)/2) and len(words) <= 8:
                candidate = ln
                break
        # fallback: look ahead
        if not candidate:
            after = text[m.end(): m.end()+400]
            after_clean = re.sub(r"\(cid:\d+\)", "", after)
            alines = [ln.strip() for ln in after_clean.splitlines() if ln.strip()]
            for ln in alines[:8]:
                low = ln.lower()
                if any(k in low for k in keywords) and not any(g in low for g in ['updates','project schedule']):
                    candidate = ln
                    break
        if candidate:
            # cleanup
            cand = re.sub(r"\s+", " ", candidate)
            cand = cand.strip(' -:')
            candidates.append(cand)

# dedupe
seen = set()
projects = []
for c in candidates:
    key = c.lower()
    if key not in seen:
        seen.add(key)
        projects.append(c)

# match to funding entries
project_matches = {}
for p in projects:
    pnorm = normalize(p)
    amt_sum = 0
    matched_entries = []
    # direct substring matches
    for fe in funding_entries:
        if pnorm and (pnorm in fe['norm'] or fe['norm'] in pnorm):
            amt_sum += fe['amount']
            matched_entries.append(fe['orig'])
    # token intersection heuristic if no matches
    if amt_sum == 0:
        p_tokens = set([t for t in pnorm.split() if len(t)>3])
        for fe in funding_entries:
            f_tokens = set(fe['norm'].split())
            if len(p_tokens & f_tokens) >= 2:
                amt_sum += fe['amount']
                matched_entries.append(fe['orig'])
    project_matches[p] = {'matched_amount': amt_sum, 'matched_funding_projects': list(set(matched_entries))}

# total
project_count = len(projects)
# sum matched amounts across projects
total_funding = sum(v['matched_amount'] for v in project_matches.values())

result = {'projects_count': project_count, 'total_funding': total_funding, 'projects_detail': project_matches}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_S3MK3XxRWpjcrpcZo6SEYkoA': ['civic_docs'], 'var_call_124Wlw9LcWtohjHmorwIF8ck': ['Funding'], 'var_call_4HdUiHnSFJBjIwK87YHCGUTC': 'file_storage/call_4HdUiHnSFJBjIwK87YHCGUTC.json', 'var_call_wwbgDMXQ67DvK4hs4ybAOibf': 'file_storage/call_wwbgDMXQ67DvK4hs4ybAOibf.json', 'var_call_Er04skSPeO40hF9ntHhKeCnq': {'projects_count': 22, 'total_funding': 0, 'projects_detail': {'anticipated to have a final design by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Complete Design': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Begin Construction': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'project will have final approval by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'approval by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Complete Final Design': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'Commission will then review the project in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'consultant. It is anticipated that this agreement will go to Council in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Begin Design': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Completion Date': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'beginning in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) The project design will commence during the': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) This project will be presented to the Planning Commission in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'final approval. It is anticipated that the project will have final approval': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'go to Council in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Begin Design: Late': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Advertise': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'anticipated that the final design will be complete by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'completed by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'draft plans are expected to be completed in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Began Design': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Award Contract and Begin Construction': {'matched_funding_sum': 0, 'matched_funding_projects': []}}}}

exec(code, env_args)
