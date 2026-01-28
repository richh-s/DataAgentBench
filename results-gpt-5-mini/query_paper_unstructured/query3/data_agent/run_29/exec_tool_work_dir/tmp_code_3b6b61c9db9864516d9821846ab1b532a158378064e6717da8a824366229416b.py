code = """import json, re
# Load previous tool results
with open(var_call_W6TTIHF2bhn7c1rdew6d4PLw, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_UEPGTWuJt6u8yaj0QzgzqB2z, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation totals per title
cit_totals = {}
for rec in citations:
    title = rec.get('title')
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    cit_totals[title] = cit_totals.get(title, 0) + count

# Helper to extract year
year_rx = re.compile(r"\b(19|20)\d{2}\b")
results = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = doc.get('text','') or ''
    # search for year in first 500 chars then whole
    head = text[:500]
    m = year_rx.search(head)
    if not m:
        m = year_rx.search(text)
    year = int(m.group(0)) if m else None
    # contribution: check if 'empirical' appears
    is_empirical = 'empirical' in text.lower()
    if is_empirical and year and year > 2016:
        total_cites = cit_totals.get(title, 0)
        results.append({'title': title, 'total_citation_count': total_cites, 'year': year})

# Sort results by total citations desc
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

# Prepare JSON string
out = json.dumps(results)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Fso26m7jQjOEUgOdmHoy7f36': ['paper_docs'], 'var_call_0wGl4xmFLPwgFqZjIIXYlCnI': ['Citations', 'sqlite_sequence'], 'var_call_W6TTIHF2bhn7c1rdew6d4PLw': 'file_storage/call_W6TTIHF2bhn7c1rdew6d4PLw.json', 'var_call_UEPGTWuJt6u8yaj0QzgzqB2z': 'file_storage/call_UEPGTWuJt6u8yaj0QzgzqB2z.json'}

exec(code, env_args)
