code = """import json

file_path = locals()['var_function-call-11399838663012174565']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_info = {}
debug_info['total_papers'] = len(papers)

if len(papers) > 0:
    debug_info['first_paper_filename'] = papers[0].get('filename')
    debug_info['first_paper_text_start'] = papers[0].get('text')[:300]

pa_count = 0
y2016_count = 0
intersection_count = 0

for p in papers:
    text = p.get('text', '')
    has_pa = 'physical activity' in text.lower()
    has_2016 = '2016' in text[:3000]
    
    if has_pa: pa_count += 1
    if has_2016: y2016_count += 1
    if has_pa and has_2016: intersection_count += 1

debug_info['pa_count'] = pa_count
debug_info['y2016_count'] = y2016_count
debug_info['intersection_count'] = intersection_count

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-2366143788913111129': ['paper_docs'], 'var_function-call-2366143788913114632': ['Citations', 'sqlite_sequence'], 'var_function-call-17599226762723281444': 'file_storage/function-call-17599226762723281444.json', 'var_function-call-11399838663012174565': 'file_storage/function-call-11399838663012174565.json', 'var_function-call-6378129950907540898': [], 'var_function-call-1573942914296370840': 'Debug Info Printed'}

exec(code, env_args)
