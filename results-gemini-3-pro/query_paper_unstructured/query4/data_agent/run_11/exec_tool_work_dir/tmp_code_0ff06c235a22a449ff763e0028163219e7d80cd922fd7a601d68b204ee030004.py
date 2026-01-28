code = """import json

with open(locals()['var_function-call-3535475471263660703'], 'r') as f:
    papers = json.load(f)

pa_papers = []
year_2016_papers = []

for p in papers:
    text = p.get('text', '')
    if "physical activity" in text.lower():
        pa_papers.append(p)
    
    # Check for 2016 in top 1000 chars
    if "2016" in text[:1000]:
        year_2016_papers.append(p)

print("__RESULT__:")
debug_info = {
    "count_physical_activity_anywhere": len(pa_papers),
    "count_2016_in_header": len(year_2016_papers),
    "sample_pa_paper_header": pa_papers[0]['text'][:300] if pa_papers else "None",
    "sample_2016_paper_header": year_2016_papers[0]['text'][:300] if year_2016_papers else "None"
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-3353327849135623283': ['paper_docs'], 'var_function-call-3353327849135620318': ['Citations', 'sqlite_sequence'], 'var_function-call-869967969559808981': 'file_storage/function-call-869967969559808981.json', 'var_function-call-869967969559806992': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3535475471263660703': 'file_storage/function-call-3535475471263660703.json', 'var_function-call-3656629748920796517': 'file_storage/function-call-3656629748920796517.json', 'var_function-call-8186264000082721214': []}

exec(code, env_args)
