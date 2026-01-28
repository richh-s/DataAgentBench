code = """import json
# Load data from previous query_db results stored as file paths
with open(var_call_80gJxusCS5BI6n1wRDDunj2M, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_oJZODJKfViLdxvf4Lt1yG6n4, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build mapping from filename without .txt to detected venue (simple heuristic)
venue_map = {}
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    text_upper = text.upper()
    # Heuristic: if 'CHI' appears as a separate token or followed by punctuation/number
    if 'CHI' in text_upper:
        venue_map[title.strip()] = 'CHI'
    else:
        venue_map[title.strip()] = None

# Filter citations to those whose title maps to CHI
chi_citations = []
for rec in citations:
    t = rec.get('title','').strip()
    count_raw = rec.get('citation_count',0)
    try:
        count = int(count_raw)
    except:
        try:
            count = int(float(count_raw))
        except:
            count = 0
    if venue_map.get(t) == 'CHI':
        chi_citations.append({'title': t, 'citation_count': count})

# Sort by citation_count desc
chi_citations_sorted = sorted(chi_citations, key=lambda x: x['citation_count'], reverse=True)

# Compute total
total = sum(x['citation_count'] for x in chi_citations_sorted)

result = {
    'papers': chi_citations_sorted,
    'total_citations_2020': total,
    'num_papers': len(chi_citations_sorted)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_80gJxusCS5BI6n1wRDDunj2M': 'file_storage/call_80gJxusCS5BI6n1wRDDunj2M.json', 'var_call_oJZODJKfViLdxvf4Lt1yG6n4': 'file_storage/call_oJZODJKfViLdxvf4Lt1yG6n4.json'}

exec(code, env_args)
