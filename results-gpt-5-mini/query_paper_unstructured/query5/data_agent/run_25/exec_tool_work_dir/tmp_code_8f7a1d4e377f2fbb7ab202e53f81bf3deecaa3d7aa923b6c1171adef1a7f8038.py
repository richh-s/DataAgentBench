code = """import json, re
with open(var_call_O4nkGAb8V0cu2IJL0DJFErKf, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_dhOgPAH5yYQRj271OIlkZkX7, 'r', encoding='utf-8') as f:
    cites = json.load(f)

# map filenames (without .txt) to text
doc_map = {}
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    doc_map[title] = d.get('text','') or ''

# Patterns indicating CHI venue
patterns = [r"\bCHI\b", r"SIGCHI", r"Proceedings of the SIGCHI", r"Proceedings of the ACM CHI", r"CHI Conference", r"ACM CHI"]
pat_regex = re.compile('|'.join(patterns), re.IGNORECASE)

matched = []
missing_docs = []
for r in cites:
    t = r.get('title')
    cc = r.get('citation_count')
    try:
        cc_int = int(cc)
    except:
        try:
            cc_int = int(float(cc))
        except:
            cc_int = 0
    text = doc_map.get(t)
    if text is None:
        missing_docs.append(t)
    else:
        if pat_regex.search(text):
            matched.append({'title': t, 'citation_count': cc_int})

total = sum(x['citation_count'] for x in matched)
matched_sorted = sorted(matched, key=lambda x: x['citation_count'], reverse=True)

result = {'total_citations_2020_for_CHI_papers': total, 'matched_count': len(matched_sorted), 'matched_papers': matched_sorted[:200], 'missing_doc_titles_count': len(missing_docs)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dhOgPAH5yYQRj271OIlkZkX7': 'file_storage/call_dhOgPAH5yYQRj271OIlkZkX7.json', 'var_call_O4nkGAb8V0cu2IJL0DJFErKf': 'file_storage/call_O4nkGAb8V0cu2IJL0DJFErKf.json', 'var_call_zHHPaGXfOotmAdBw2eAnxhQJ': {'total_citations_2020_for_CHI_papers': 0, 'papers': []}}

exec(code, env_args)
