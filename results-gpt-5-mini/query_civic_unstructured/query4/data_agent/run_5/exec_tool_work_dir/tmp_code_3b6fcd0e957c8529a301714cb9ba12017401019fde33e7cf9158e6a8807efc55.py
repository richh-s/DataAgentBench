code = """import json, re
from collections import defaultdict

# Load data
with open(var_call_VAIIgByZSdgcjr25PevQ2kkY, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_GS48k3w0jE3Dso9vMsDQ40Z4, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Build funding dict
funding_projects = []
for r in funding:
    name = r.get('Project_Name','').strip()
    try:
        amt = int(r.get('Amount'))
    except:
        try:
            amt = int(float(r.get('Amount')))
        except:
            amt = 0
    funding_projects.append({'name': name, 'amount': amt, 'name_l': name.lower()})

# Helper tokenize
def tokens(s):
    return [t for t in re.findall(r"[a-zA-Z0-9]+", s.lower()) if len(t)>2]

# Find candidate project titles near mentions of Spring and 2022
candidates = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    n = len(lines)
    for i in range(n):
        # Build window of lines i..i+5
        window = ' '.join(lines[i:i+6]).lower()
        if '2022' in window and 'spring' in window:
            # find nearest non-empty preceding line up to 10 lines above
            title = None
            for j in range(max(0,i-10), i+1)[::-1]:
                l = lines[j].strip()
                if l and len(l) < 120 and not l.lower().startswith('cid:') and not l.lower().startswith('page'):
                    title = l
                    break
            if title:
                candidates.append(title.strip())
        else:
            # also check for specific months March/Apr/May + 2022
            if '2022' in window and any(m in window for m in ['march','mar','april','apr','may']):
                title = None
                for j in range(max(0,i-10), i+1)[::-1]:
                    l = lines[j].strip()
                    if l and len(l) < 120 and not l.lower().startswith('cid:') and not l.lower().startswith('page'):
                        title = l
                        break
                if title:
                    candidates.append(title.strip())

# Deduplicate candidates
cand_set = []
for c in candidates:
    c2 = re.sub(r"\s+"," ", c)
    if c2 not in cand_set:
        cand_set.append(c2)

# Now match candidate titles to funding projects via token overlap
matched = {}
for cand in cand_set:
    cand_tok = set(tokens(cand))
    if not cand_tok:
        continue
    best_match = None
    best_score = 0.0
    for fp in funding_projects:
        fp_tok = set(tokens(fp['name']))
        if not fp_tok:
            continue
        # score = intersection / union
        inter = len(cand_tok & fp_tok)
        union = len(cand_tok | fp_tok)
        score = inter/union if union>0 else 0
        # also allow substring matches
        if cand.lower() in fp['name_l'] or fp['name_l'] in cand.lower():
            score = max(score, 0.9)
        if score > best_score:
            best_score = score
            best_match = fp
    # accept matches with score >= 0.4
    if best_match and best_score >= 0.4:
        matched[best_match['name']] = matched.get(best_match['name'], 0) + best_match['amount']

# Prepare final list
matched_projects = sorted(matched.keys())
count = len(matched_projects)
total_funding = sum(matched.values())
result = {'count': count, 'total_funding': total_funding, 'projects': matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VAIIgByZSdgcjr25PevQ2kkY': 'file_storage/call_VAIIgByZSdgcjr25PevQ2kkY.json', 'var_call_GS48k3w0jE3Dso9vMsDQ40Z4': 'file_storage/call_GS48k3w0jE3Dso9vMsDQ40Z4.json', 'var_call_cvu1QWV7xwrq0hFks9LiZSZ1': 'file_storage/call_cvu1QWV7xwrq0hFks9LiZSZ1.json'}

exec(code, env_args)
