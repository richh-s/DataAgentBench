code = """import json

# Load citations
with open(locals()['var_function-call-5858360374360622472'], 'r') as f:
    citations_list = json.load(f)

# Load papers
with open(locals()['var_function-call-17448438011554741318'], 'r') as f:
    papers_list = json.load(f)

citation_map = {c['title']: int(c['citation_count']) for c in citations_list}

acm_titles = []
for paper in papers_list:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    if 'ACM' in text[:5000]:
        acm_titles.append(title)

print("__RESULT__:")
print(json.dumps(acm_titles))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158, 'var_function-call-3027916622841632543': 'file_storage/function-call-3027916622841632543.json', 'var_function-call-17448438011554741318': 'file_storage/function-call-17448438011554741318.json', 'var_function-call-6936084591521727754': 67.8, 'var_function-call-3893205258143355360': 0, 'var_function-call-9991689489332659929': True, 'var_function-call-13779047879887923666': True, 'var_function-call-8236464070197401554': {'count': 5, 'avg': 67.8}}

exec(code, env_args)
