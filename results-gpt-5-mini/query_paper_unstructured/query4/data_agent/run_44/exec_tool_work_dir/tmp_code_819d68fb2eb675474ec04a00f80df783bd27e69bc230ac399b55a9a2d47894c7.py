code = """import json, re

# Load the large results from storage file paths
with open(var_call_ezWe4akpDaUk6PQc2M4tnIGi, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_0nrnvpvG147vYhuSa4ch32tR, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation mapping: normalize titles by stripping surrounding quotes and whitespace
def normalize_title(t):
    if not isinstance(t, str):
        return ''
    t2 = t.strip()
    # remove surrounding quotes if present
    if (t2.startswith('"') and t2.endswith('"')) or (t2.startswith("'") and t2.endswith("'")):
        t2 = t2[1:-1].strip()
    # collapse whitespace
    t2 = re.sub(r'\s+', ' ', t2)
    return t2

cit_map = {}
for c in citations:
    t = normalize_title(c.get('title',''))
    try:
        val = int(c.get('total_citations'))
    except:
        try:
            val = int(str(c.get('total_citations')).replace(',', ''))
        except:
            val = 0
    if t:
        cit_map[t] = val

# Find papers in docs that are in domain 'physical activity' and published in 2016
results = []
for doc in docs:
    filename = doc.get('filename','')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    text = doc.get('text','') or ''
    text_low = text.lower()
    # check domain substring
    if 'physical activity' not in text_low:
        continue
    # check year 2016 occurrence
    if re.search(r'\b2016\b', text):
        year = 2016
    else:
        # try to find patterns like "CHI '16" or "'16" near venue lines - fallback: skip if explicit 2016 not found
        # We will skip documents that do not contain explicit 2016
        continue
    # lookup citations
    cit = cit_map.get(title, 0)
    results.append({'title': title, 'total_citations': cit})

# Sort results by total_citations descending
results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

import json
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_ezWe4akpDaUk6PQc2M4tnIGi': 'file_storage/call_ezWe4akpDaUk6PQc2M4tnIGi.json', 'var_call_0nrnvpvG147vYhuSa4ch32tR': 'file_storage/call_0nrnvpvG147vYhuSa4ch32tR.json'}

exec(code, env_args)
