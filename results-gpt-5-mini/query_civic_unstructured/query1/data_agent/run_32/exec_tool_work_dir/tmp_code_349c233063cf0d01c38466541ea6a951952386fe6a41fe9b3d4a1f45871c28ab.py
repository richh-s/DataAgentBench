code = """import json, re

funding_path = var_call_VzgihgZ7OwHfelcmF5z1sI2X
docs_path = var_call_zyKqzSQAopIHC3ukf8gNzESM

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build a combined design section text from documents
design_text = ''
for doc in docs:
    txt = doc.get('text','')
    lower = txt.lower()
    # look for explicit Design section
    marker = 'capital improvement projects (design)'
    if marker in lower:
        start = lower.find(marker) + len(marker)
        # end at next major section header if present
        end_markers = [
            'capital improvement projects (construction)',
            'capital improvement projects (not started)',
            'capital improvement projects (completed)',
            '\npage ', '\nagenda item', '\nagenda'
        ]
        end = len(lower)
        for em in end_markers:
            i = lower.find(em, start)
            if i != -1:
                end = min(end, i)
        snippet = lower[start:end]
        design_text += '\n' + snippet
    else:
        # fallback: if document mentions both phrases, include a larger snippet
        if 'capital improvement projects' in lower and 'design' in lower:
            start = lower.find('capital improvement projects')
            end = start + 20000
            design_text += '\n' + lower[start:end]

# If still empty, combine whole docs as fallback
if not design_text:
    design_text = '\n'.join([d.get('text','').lower() for d in docs])

# Extract candidate project title lines from design_text
lines = [ln.strip() for ln in re.split(r'\n|\r', design_text) if ln.strip()]
candidates = []
stop_words = set(['updates', 'project schedule', 'complete design', 'advertise', 'begin construction',
                  'project description', 'project updates', 'page', 'agenda', 'recommended action', 'discussion'])
for ln in lines:
    low = ln.lower()
    if any(sw in low for sw in stop_words):
        continue
    # discard very short lines
    if len(low) < 10:
        continue
    # discard lines that are sentences (contain too many stop punctuation)
    if low.count('.') > 0 and len(low.split())>10:
        continue
    # heuristics: likely project titles often end with words like 'project', 'improvements', 'repairs', 'study', 'plan', 'playground', 'walkway', 'project)'
    if re.search(r'\b(project|improvements|repairs|study|plan|walkway|project\)|park|road|drain|median|walkway|playground|roof|hvac|curb|signal|skate park|crosswalk|median)\b', low):
        candidates.append(ln)

# dedupe candidates
design_projects = []
seen = set()
for c in candidates:
    key = re.sub(r'\s+',' ', re.sub(r'[^a-z0-9 ]',' ', c.lower())).strip()
    if key and key not in seen:
        seen.add(key)
        design_projects.append(c)

# Prepare funding projects with Amount > 50000
funding_filtered = []
for r in funding:
    try:
        amt = int(r.get('Amount') if isinstance(r.get('Amount'), (int, float)) else int(str(r.get('Amount')).replace(',','')))
    except:
        try:
            amt = int(float(r.get('Amount')))
        except:
            amt = 0
    if amt > 50000:
        funding_filtered.append({'Project_Name': r.get('Project_Name',''), 'Amount': amt})

# Normalization helper
def norm_tokens(s):
    s2 = re.sub(r'\(.*?\)',' ', s.lower())
    s2 = re.sub(r'[^a-z0-9 ]',' ', s2)
    toks = [t for t in s2.split() if t]
    return toks

design_norm = [' '.join(norm_tokens(p)) for p in design_projects]

matched_funding = []
matched_design = []
for fr in funding_filtered:
    fname = fr['Project_Name']
    ftoks = norm_tokens(fname)
    fbase = ' '.join(ftoks)
    matched = False
    # direct substring
    if fbase and any(fbase in d for d in design_norm):
        matched = True
    else:
        # check overlap tokens with each design project
        for di, d in enumerate(design_norm):
            dtoks = d.split()
            if not dtoks:
                continue
            common = len(set(dtoks) & set(ftoks))
            # require at least 3 common tokens or 60% overlap of shorter
            shortest = min(len(dtoks), len(ftoks))
            if common >= 3 or (shortest>0 and common/shortest >= 0.6):
                matched = True
                if design_projects[di] not in matched_design:
                    matched_design.append(design_projects[di])
                break
    if matched:
        matched_funding.append(fname)

matched_funding = sorted(set(matched_funding))
matched_design = sorted(set(matched_design))

result = {'count': len(matched_funding), 'matched_funding_projects': matched_funding, 'matched_design_projects': matched_design}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w6mzZJWh1Qf1WequniXaReqc': ['civic_docs'], 'var_call_8FNlL82nAuBCB7zgbjsxnppT': ['Funding'], 'var_call_VzgihgZ7OwHfelcmF5z1sI2X': 'file_storage/call_VzgihgZ7OwHfelcmF5z1sI2X.json', 'var_call_zyKqzSQAopIHC3ukf8gNzESM': 'file_storage/call_zyKqzSQAopIHC3ukf8gNzESM.json', 'var_call_lVtDhaZ9wn4RKCdruIyGSd0p': {'funding_records': 276}}

exec(code, env_args)
