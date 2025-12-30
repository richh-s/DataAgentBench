code = """import json

# Load citations
with open(locals()['var_function-call-5858360374360622472'], 'r') as f:
    citations_list = json.load(f)

# Load papers
with open(locals()['var_function-call-17448438011554741318'], 'r') as f:
    papers_list = json.load(f)

citation_map = {}
for c in citations_list:
    try:
        count = int(c['citation_count'])
        citation_map[c['title']] = count
    except ValueError:
        continue

acm_citations = []
for paper in papers_list:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    if 'ACM' in text[:5000]:
        if title in citation_map:
            acm_citations.append(citation_map[title])

print("__RESULT__:")
print(json.dumps({"count": len(acm_citations), "avg": sum(acm_citations)/len(acm_citations) if acm_citations else 0}))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158, 'var_function-call-3027916622841632543': 'file_storage/function-call-3027916622841632543.json', 'var_function-call-17448438011554741318': 'file_storage/function-call-17448438011554741318.json', 'var_function-call-6936084591521727754': 67.8, 'var_function-call-3893205258143355360': 0, 'var_function-call-9991689489332659929': True, 'var_function-call-13779047879887923666': True}

exec(code, env_args)
