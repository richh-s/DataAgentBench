code = """import json, re

with open(var_call_l55xEibBEPLvcbgsB4ym2Tu7, 'r') as f:
    uc_records = json.load(f)
with open(var_call_F0XFlqDiYITWL1MBYbrkembO, 'r') as f:
    all_records = json.load(f)
with open(var_call_lRNyp9wRymrVkIyIL4PoXol6, 'r') as f:
    cpc_defs = json.load(f)

cpc_map = {r['symbol']: r.get('titleFull') for r in cpc_defs}

pubnum_re = re.compile(r"\b[A-Z]{2}-\d{4,}[-A-Z0-9/]*\b")

def extract_pubnums(text):
    if not text:
        return []
    return pubnum_re.findall(text)

uc_pubnums = set()
for rec in uc_records:
    txt = rec.get('Patents_info','')
    for n in extract_pubnums(txt):
        uc_pubnums.add(n)
    # also from citation field
    cit = rec.get('citation')
    if cit and cit.strip():
        try:
            cited = json.loads(cit)
            for c in cited:
                pn = c.get('publication_number') if isinstance(c, dict) else None
                if pn:
                    uc_pubnums.add(pn)
        except Exception:
            pass

# assignee extraction heuristic
def extract_assignee(text):
    if not text:
        return 'UNKNOWN'
    s = text
    s_low = s.lower()
    for kw in [" is owned by ", " is assigned to ", " holds the ", " holds ", " has the ", " owns the "]:
        i = s_low.find(kw)
        if i != -1:
            candidate = s[:i]
            if ')' in candidate:
                candidate = candidate.split(')')[-1]
            candidate = candidate.replace('In US,', '').replace('In US', '')
            candidate = candidate.strip(' ,.')
            if candidate:
                return candidate.upper()
    # fallback: longest uppercase sequence
    candidates = re.findall(r'([A-Z][A-Z0-9 &/\-\.]{1,})', s)
    if candidates:
        cand = max(candidates, key=len).strip()
        cand = re.split(r' holds| has| owns| is ', cand)[0]
        return cand.strip().upper()
    return 'UNKNOWN'

results = {}
for rec in all_records:
    cit = rec.get('citation')
    if not cit or not cit.strip():
        continue
    try:
        cited = json.loads(cit)
    except Exception:
        cited = []
        for pn in extract_pubnums(cit or ''):
            cited.append({'publication_number': pn})
    cited_pubnums = set()
    for c in cited:
        if isinstance(c, dict):
            pn = c.get('publication_number')
            if pn:
                cited_pubnums.add(pn)
    if not cited_pubnums:
        continue
    if uc_pubnums.intersection(cited_pubnums):
        assignee = extract_assignee(rec.get('Patents_info',''))
        if assignee == 'UNIV CALIFORNIA':
            continue
        cpc_field = rec.get('cpc')
        primary_codes = []
        if cpc_field and cpc_field.strip():
            try:
                cpc_list = json.loads(cpc_field)
                for item in cpc_list:
                    if item.get('first'):
                        code = item.get('code')
                        if code and code not in primary_codes:
                            primary_codes.append(code)
                if not primary_codes and cpc_list:
                    code = cpc_list[0].get('code')
                    if code:
                        primary_codes.append(code)
            except Exception:
                for code in re.findall(r"[A-Z]\w+\d*/\d+", cpc_field):
                    primary_codes.append(code)
        if not primary_codes:
            primary_codes = ['UNKNOWN']
        titles = []
        for code in primary_codes:
            title = cpc_map.get(code)
            if title:
                titles.append(title)
            else:
                found = None
                if code != 'UNKNOWN':
                    for sym, t in cpc_map.items():
                        if sym == code or sym.startswith(code) or code.startswith(sym):
                            found = t
                            break
                if found:
                    titles.append(found)
                else:
                    titles.append(None)
        uniq_titles = []
        for t in titles:
            if t not in uniq_titles:
                uniq_titles.append(t)
        results[assignee] = uniq_titles

output = []
for assignee, titles in results.items():
    output.append({'assignee': assignee, 'cpc_titles': titles})

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_6Kreubw6sda70vrL4hVhh4Px': ['publicationinfo'], 'var_call_c23BeMWTAwQXdF8yov9bBp9t': ['cpc_definition'], 'var_call_l55xEibBEPLvcbgsB4ym2Tu7': 'file_storage/call_l55xEibBEPLvcbgsB4ym2Tu7.json', 'var_call_F0XFlqDiYITWL1MBYbrkembO': 'file_storage/call_F0XFlqDiYITWL1MBYbrkembO.json', 'var_call_lRNyp9wRymrVkIyIL4PoXol6': 'file_storage/call_lRNyp9wRymrVkIyIL4PoXol6.json'}

exec(code, env_args)
