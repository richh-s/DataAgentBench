code = """import json, re

with open(var_call_bucVb3W2z83iDPOLIhhOK9yk, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_XvWnTXH0R38cyF13CtmdgsEj, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

texts = [d.get('text','') for d in civic_docs]
full_text = '  '.join(texts).lower()

def normalize(name):
    return re.sub(r'\s*\(.*?\)\s*', '', name).strip()

keywords = ['fema', 'emergency', 'outdoor warning', 'warning']

candidates = []
for rec in funding:
    pname = rec.get('Project_Name','')
    psource = rec.get('Funding_Source','') or ''
    low = (pname + ' ' + psource).lower()
    if any(k in low for k in keywords) or 'federal assistance' in psource.lower():
        candidates.append(rec)

for rec in funding:
    pname = rec.get('Project_Name','')
    if '(fema' in pname.lower() and rec not in candidates:
        candidates.append(rec)

seen = set()
unique_candidates = []
for c in candidates:
    key = c.get('Project_Name')
    if key not in seen:
        unique_candidates.append(c)
        seen.add(key)


def infer_status(project_name, text_corpus):
    name_norm = normalize(project_name).lower()
    idx = text_corpus.find(name_norm)
    if idx == -1:
        parts = name_norm.split()
        if len(parts) >= 2:
            seq = ' '.join(parts[:3]) if len(parts) >=3 else ' '.join(parts[:2])
            idx = text_corpus.find(seq)
    if idx == -1:
        if 'outdoor warning' in text_corpus and (('siren' in project_name.lower()) or ('sign' in project_name.lower()) or ('warning' in project_name.lower())):
            idx = text_corpus.find('outdoor warning')
    if idx == -1:
        return None
    start = max(0, idx-300)
    end = min(len(text_corpus), idx+300)
    snippet = text_corpus[start:end]
    if any(x in snippet for x in ['construction was completed','complete construction','notice of completion','completed,']):
        return 'completed'
    if any(x in snippet for x in ['under construction','begin construction','project is currently under construction','begin construction:']):
        return 'design'
    if any(x in snippet for x in ['complete design','preliminary design','final design','design plans']):
        return 'design'
    if any(x in snippet for x in ['not started','not yet','identified in the','is proposed']):
        return 'not started'
    return None

results = []
for rec in unique_candidates:
    pname = rec.get('Project_Name')
    psource = rec.get('Funding_Source')
    try:
        amt = int(rec.get('Amount'))
    except:
        try:
            amt = int(float(rec.get('Amount')))
        except:
            amt = None
    status = infer_status(pname, full_text)
    results.append({
        'Project_Name': pname,
        'Funding_Source': psource,
        'Amount': amt,
        'Status': status
    })

results = sorted(results, key=lambda x: x['Project_Name'] or '')

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_XvWnTXH0R38cyF13CtmdgsEj': 'file_storage/call_XvWnTXH0R38cyF13CtmdgsEj.json', 'var_call_bucVb3W2z83iDPOLIhhOK9yk': 'file_storage/call_bucVb3W2z83iDPOLIhhOK9yk.json'}

exec(code, env_args)
