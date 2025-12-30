code = """import json
import re

citations_file = locals()['var_function-call-332096647494284469']
papers_file = locals()['var_function-call-9719230712903826217']

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

stats = {}
stats['total_citations'] = len(citations_data)
stats['total_papers'] = len(papers_data)

# Check years
years = {'2014': 0, '2015': 0, '2016': 0, '2017': 0}
for p in papers_data:
    text = p.get('text', '')
    for y in years:
        if y in text[:1000]: # Check header
            years[y] += 1

stats['years_in_header'] = years

# Check "physical activity"
pa_count = 0
for p in papers_data:
    if "physical activity" in p.get('text', '').lower():
        pa_count += 1
stats['pa_count'] = pa_count

# Check overlap
paper_titles = set(p['filename'].replace('.txt', '') for p in papers_data)
citation_titles = set(c['title'] for c in citations_data)
stats['common_titles'] = len(paper_titles.intersection(citation_titles))
stats['sample_paper_titles'] = list(paper_titles)[:3]
stats['sample_citation_titles'] = list(citation_titles)[:3]

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-332096647494284469': 'file_storage/function-call-332096647494284469.json', 'var_function-call-332096647494285302': 'file_storage/function-call-332096647494285302.json', 'var_function-call-9719230712903826217': 'file_storage/function-call-9719230712903826217.json', 'var_function-call-9839691519987756055': [], 'var_function-call-7088723840574718985': []}

exec(code, env_args)
