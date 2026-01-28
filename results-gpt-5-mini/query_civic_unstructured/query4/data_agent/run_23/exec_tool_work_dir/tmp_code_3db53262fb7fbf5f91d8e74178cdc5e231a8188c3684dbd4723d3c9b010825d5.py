code = """import json
import re
import string

# Load data
with open(var_call_4HdUiHnSFJBjIwK87YHCGUTC, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_wwbgDMXQ67DvK4hs4ybAOibf, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# normalize function
def normalize_name(s):
    if s is None:
        return ''
    s = s.lower()
    s = re.sub(r"\([^)]*\)", "", s)
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r"\s+", " ", s)
    return s.strip()

# prepare funding list
funding = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_val = int(amt)
    except:
        try:
            amt_val = int(float(amt))
        except:
            amt_val = 0
    funding.append({'orig_name': name, 'name': normalize_name(name), 'amount': amt_val})

# patterns for Spring 2022
spring_patterns = [r"spring\s*2022", r"2022\s*-?\s*spring", r"march\s*2022", r"mar\s*2022", r"april\s*2022", r"may\s*2022", r"2022-03", r"2022-04", r"2022-05", r"03/2022", r"04/2022", r"05/2022", r"2022/03", r"2022/04", r"2022/05"]
pat = re.compile('|'.join(spring_patterns), re.IGNORECASE)

candidate_projects = []

def is_generic_line(ln):
    low = ln.lower()
    generic_terms = ['updates', 'project schedule', 'project description', 'page', 'agenda', 'discussion', 'recommended action', 'subject', 'meeting date', 'item', 'approved by', 'date prepared']
    if any(gt in low for gt in generic_terms):
        return True
    if len(ln.strip()) < 3:
        return True
    return False

for doc in civic_docs:
    text = doc.get('text','')
    for m in pat.finditer(text):
        start = m.start()
        # take up to 400 chars before match to find project name
        context_start = max(0, start-400)
        context = text[context_start:start]
        # split into lines and examine last few lines
        lines = [ln.strip() for ln in context.splitlines() if ln.strip()]
        # look backwards for a plausible project name
        candidate = None
        for ln in reversed(lines[-8:]):
            if is_generic_line(ln):
                continue
            # Avoid lines that end with ':' as they are labels
            if ln.endswith(':'):
                ln = ln[:-1].strip()
            if 3 <= len(ln) <= 120:
                candidate = ln
                break
        if not candidate:
            # fallback: look ahead after the match for a title-like line
            after = text[m.end(): m.end()+200]
            alines = [ln.strip() for ln in after.splitlines() if ln.strip()]
            for ln in alines[:6]:
                if not is_generic_line(ln):
                    candidate = ln
                    break
        if candidate:
            candidate_projects.append(candidate)

# dedupe preserving order
seen = set()
projects = []
for p in candidate_projects:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        projects.append(p)

# match to funding
matches = {}
for p in projects:
    np = normalize_name(p)
    total_amt = 0
    matched = []
    for f in funding:
        if np and (np in f['name'] or f['name'] in np):
            total_amt += f['amount']
            matched.append(f['orig_name'])
    matches[p] = {'matched_funding_sum': total_amt, 'matched_funding_projects': matched}

project_count = len(projects)
total_funding = sum(v['matched_funding_sum'] for v in matches.values())

result = {'projects_count': project_count, 'total_funding': total_funding, 'projects_detail': matches}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_S3MK3XxRWpjcrpcZo6SEYkoA': ['civic_docs'], 'var_call_124Wlw9LcWtohjHmorwIF8ck': ['Funding'], 'var_call_4HdUiHnSFJBjIwK87YHCGUTC': 'file_storage/call_4HdUiHnSFJBjIwK87YHCGUTC.json', 'var_call_wwbgDMXQ67DvK4hs4ybAOibf': 'file_storage/call_wwbgDMXQ67DvK4hs4ybAOibf.json'}

exec(code, env_args)
