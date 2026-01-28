code = """import json, re

# Load MongoDB query result (paper documents)
with open(var_call_usSEjUtT2IWF6PvzKjAUuDtw, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Load Citations table result
with open(var_call_7gKBgYMSZNpz0J1drwuCFJsn, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citations sum per title
cit_sum = {}
for r in citations:
    title = r.get('title')
    try:
        count = int(r.get('citation_count', 0))
    except:
        try:
            count = int(float(r.get('citation_count', 0)))
        except:
            count = 0
    cit_sum[title] = cit_sum.get(title, 0) + count

# Helper to get publication year
venues = ["CHI", "Ubicomp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]

def get_pub_year(text):
    txt = text
    # Search for venue + year patterns
    for v in venues:
        # look for patterns like 'CHI 2016' or 'CHI 2016,' or 'CHI 2016.' within proximity
        m = re.search(r'(?i)'+re.escape(v)+r'[^\n]{0,100}?(20\d{2})', txt)
        if m:
            return int(m.group(1))
    # Search for copyright year
    m = re.search(r'©\s*(20\d{2})', txt)
    if m:
        return int(m.group(1))
    m = re.search(r'Copyright[^\n]{0,50}?(20\d{2})', txt, re.I)
    if m:
        return int(m.group(1))
    # Fallback: first 20xx year
    m = re.search(r'(20\d{2})', txt)
    if m:
        return int(m.group(1))
    return None

results = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # Ensure domain 'physical activity' present
    if 'physical activity' not in text.lower():
        continue
    pub_year = get_pub_year(text)
    if pub_year != 2016:
        continue
    total_citations = cit_sum.get(title, 0)
    results.append({"title": title, "total_citation_count": total_citations})

# Sort results by title
results = sorted(results, key=lambda x: x['title'])

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_cql4grllXOR9TdyPMEBiUmP9': ['paper_docs'], 'var_call_usSEjUtT2IWF6PvzKjAUuDtw': 'file_storage/call_usSEjUtT2IWF6PvzKjAUuDtw.json', 'var_call_7gKBgYMSZNpz0J1drwuCFJsn': 'file_storage/call_7gKBgYMSZNpz0J1drwuCFJsn.json'}

exec(code, env_args)
