code = """import json

with open(locals()['var_function-call-18120137010689516403'], 'r') as f:
    papers_data = json.load(f)

count_domain = 0
examples_domain = []

count_2016 = 0

for paper in papers_data:
    text = paper.get('text', '')
    
    if 'physical activity' in text.lower():
        count_domain += 1
        if len(examples_domain) < 5:
            examples_domain.append(text[:300])
            
    if '2016' in text[:1000]:
        count_2016 += 1

print("__RESULT__:")
print(json.dumps({
    "count_domain_physical_activity": count_domain,
    "count_year_2016_heuristic": count_2016,
    "examples": examples_domain
}))"""

env_args = {'var_function-call-12537067908498854148': ['paper_docs'], 'var_function-call-12537067908498856339': ['Citations', 'sqlite_sequence'], 'var_function-call-18120137010689517392': 'file_storage/function-call-18120137010689517392.json', 'var_function-call-18120137010689516403': 'file_storage/function-call-18120137010689516403.json', 'var_function-call-7739271670607473700': []}

exec(code, env_args)
