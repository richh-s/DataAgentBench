code = """import json

papers_path = locals()['var_function-call-16274009200495380828']
with open(papers_path, 'r') as f:
    papers = json.load(f)

sample_titles = [
    "Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection",
    "Sundroid: Solar Radiation Awareness with Smartphones",
    "Technologies for Everyday Life Reflection: Illustrating a Design Space"
]

found_headers = []
for p in papers:
    title = p.get('filename', '').replace('.txt', '')
    if title in sample_titles:
        header = p.get('text', '')[:500]
        found_headers.append({"title": title, "header": header})

print("__RESULT__:")
print(json.dumps(found_headers))"""

env_args = {'var_function-call-16274009200495380828': 'file_storage/function-call-16274009200495380828.json', 'var_function-call-12939429308500753230': 'file_storage/function-call-12939429308500753230.json', 'var_function-call-13758046956340935094': 0}

exec(code, env_args)
