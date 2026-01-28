code = """import json, re
civic = load = None
# load variables from storage
civic = var_call_Vl0TG7LtyyMTUxdDBWkduxwO
funding = var_call_DIpBJRT5NI77OMdOhicKMrCM

# helper load
def load_maybe_path(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

civic_docs = load_maybe_path(civic)
funding = load_maybe_path(funding)

# normalize
if isinstance(civic_docs, dict):
    civic_docs = [civic_docs]

# disaster keywords
disaster_k = ['fema','caloes','caljpia','disaster','fire','woolsey','recovery','emergency']

# function to normalize names
def normalize_name(n):
    if not n: return ''
    # remove parenthetical suffixes
    n2 = re.sub(r"\([^)]*\)", "", n)
    n2 = re.sub(r"[^A-Za-z0-9 ]", " ", n2)
    n2 = re.sub(r"\s+", " ", n2).strip().lower()
    return n2

# build index of civic doc text lower
civic_texts = [(d.get('filename'), d.get('text','')) for d in civic_docs]

matches = []
total = 0

for fr in funding:
    pname = fr.get('Project_Name')
    amt_raw = fr.get('Amount', 0)
    try:
        amount = int(str(amt_raw))
    except:
        s = re.sub(r"[^0-9-]", "", str(amt_raw))
        amount = int(s) if s else 0
    norm = normalize_name(pname)
    base = norm
    # check disaster by name
    is_disaster = any(k in (pname or '').lower() for k in disaster_k)
    started_2022 = False
    found = False
    matched_filename = None
    matched_snippet = None
    # search for exact or partial match in civic texts
    for fname, text in civic_texts:
        text_lower = text.lower()
        if not norm:
            continue
        if norm in text_lower or ' '.join(norm.split()[:4]) in text_lower:
            found = True
            matched_filename = fname
            # find index
            idx = text_lower.find(norm)
            if idx==-1:
                idx = 0
            start = max(0, idx-300)
            end = min(len(text_lower), idx+1500)
            snippet = text[start:end]
            matched_snippet = snippet
            # check disaster keywords in snippet
            if any(k in snippet for k in disaster_k):
                is_disaster = True
            # check for 2022 in snippet
            if '2022' in snippet:
                started_2022 = True
            else:
                # look for 'Begin Construction' or 'Project Schedule' near occurrence anywhere in doc
                # search doc vicinity of project name for lines containing 2022
                if re.search(r'project schedule[\s\S]{0,2000}?2022', text_lower):
                    started_2022 = True
                elif re.search(r'begin construction[\s\S]{0,2000}?2022', text_lower):
                    started_2022 = True
                elif re.search(r'complete construction[\s\S]{0,2000}?2022', text_lower):
                    started_2022 = True
            break
    # Additional heuristic: if funding name contains disaster keyword and civic docs have any mention of the base project with 2022
    if not found:
        # try matching by first 3 words
        tokens = norm.split()
        if len(tokens)>=3:
            frag = ' '.join(tokens[:3])
            for fname, text in civic_texts:
                if frag in text.lower():
                    matched_filename = fname
                    matched_snippet = text.lower()[:1500]
                    found = True
                    if '2022' in text.lower()[:2000]:
                        started_2022 = True
                    if any(k in text.lower() for k in disaster_k):
                        is_disaster = True
                    break
    # If still not found, but name contains disaster marker, we may still include if civic docs show any disaster projects with 2022
    if not started_2022:
        # search civic docs for any disaster project mention with 2022 and see if project base token overlaps
        for fname, text in civic_texts:
            low = text.lower()
            if '2022' in low and any(k in low for k in disaster_k):
                # if some tokens overlap
                common = sum(1 for t in norm.split() if t and t in low)
                if common>=2:
                    started_2022 = True
                    matched_filename = fname
                    matched_snippet = low
                    is_disaster = True
                    break
    if is_disaster and started_2022:
        matches.append({'Project_Name': pname, 'Amount': amount, 'Funding_ID': fr.get('Funding_ID'), 'Filename': matched_filename})
        total += amount

result = {'total_disaster_2022_funding': total, 'matches_count': len(matches), 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Vl0TG7LtyyMTUxdDBWkduxwO': 'file_storage/call_Vl0TG7LtyyMTUxdDBWkduxwO.json', 'var_call_DIpBJRT5NI77OMdOhicKMrCM': 'file_storage/call_DIpBJRT5NI77OMdOhicKMrCM.json', 'var_call_lQEvLPTlB8jjLoP6ZpzPN0YR': {'total_disaster_2022_funding': 0, 'matches': []}}

exec(code, env_args)
