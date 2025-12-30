code = """import json

with open(locals()['var_function-call-15052837677645358985'], 'r') as f:
    citations_2020 = json.load(f)

paper_titles = [item['title'] for item in citations_2020]

__RESULT__:
print(json.dumps(paper_titles))"""

env_args = {'var_function-call-15052837677645358985': 'file_storage/function-call-15052837677645358985.json'}

exec(code, env_args)
