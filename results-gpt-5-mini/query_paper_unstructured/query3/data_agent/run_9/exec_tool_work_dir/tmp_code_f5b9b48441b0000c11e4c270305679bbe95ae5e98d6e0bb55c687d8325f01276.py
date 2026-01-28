code = """import json, re

# Load data from previous tool calls
with open(var_call_ZrVgVXK8GoUo150t4olnEKVG, 'r') as f:
    papers = json.load(f)
with open(var_call_jUbSZTRIjFTANO62z1pdPTrF, 'r') as f:
    citations = json.load(f)

# helper functions
def extract_year(text):
    header = text[:1000]
    yrs = re.findall(r"\b(19[5-9][0-9]|20[0-9]{2})\b", header)
    if yrs:
        return int(yrs[0])
    yrs2 = re.findall(r"\b(19[5-9][0-9]|20[0-9]{2})\b", text)
    if yrs2:
        return int(yrs2[0])
    return None

import string
trans = str.maketrans('', '', string.punctuation)
def normalize(s):
    if s is None:
        return ''
    s = s.strip().lower()
    s = s.translate(trans)
    s = re.sub(r"\s+", " ", s)
    return s

# build citation lookup by normalized title
cit_lookup = {}
for rec in citations:
    t = rec.get('title') or rec.get('Title')
    tot = rec.get('total_citations') or rec.get('citation_count')
    if t is None:
        continue
    key = normalize(t)
    try:
        tot_int = int(tot)
    except:
        try:
            tot_int = int(float(tot))
        except:
            tot_int = 0
    cit_lookup[key] = tot_int

results = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    year = extract_year(text)
    if year is None:
        continue
    if year <= 2016:
        continue
    # check for empirical contribution: look for the word 'empirical' in text or 'empiric' variants
    if 'empirical' in text.lower() or 'empiric' in text.lower():
        key = normalize(title)
        total_citations = cit_lookup.get(key, 0)
        results.append({'title': title, 'year': year, 'total_citations': total_citations})

# sort by total_citations desc
results.sort(key=lambda x: x['total_citations'], reverse=True)

# prepare JSON-serializable string
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4gaHGrHOwcQewZsrcMFfdwqe': ['paper_docs'], 'var_call_ZrVgVXK8GoUo150t4olnEKVG': 'file_storage/call_ZrVgVXK8GoUo150t4olnEKVG.json', 'var_call_YSkYeuVKVDHLVPkNT93EHmO8': ['Citations', 'sqlite_sequence'], 'var_call_jUbSZTRIjFTANO62z1pdPTrF': 'file_storage/call_jUbSZTRIjFTANO62z1pdPTrF.json'}

exec(code, env_args)
