code = """import json

with open(locals()['var_function-call-3535475471263660703'], 'r') as f:
    papers = json.load(f)

pa_papers = []
for p in papers:
    if "physical activity" in p['text'].lower():
        pa_papers.append({
            "filename": p['filename'],
            "header": p['text'][:300]
        })

print("__RESULT__:")
print(json.dumps(pa_papers))"""

env_args = {'var_function-call-3353327849135623283': ['paper_docs'], 'var_function-call-3353327849135620318': ['Citations', 'sqlite_sequence'], 'var_function-call-869967969559808981': 'file_storage/function-call-869967969559808981.json', 'var_function-call-869967969559806992': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3535475471263660703': 'file_storage/function-call-3535475471263660703.json', 'var_function-call-3656629748920796517': 'file_storage/function-call-3656629748920796517.json', 'var_function-call-8186264000082721214': [], 'var_function-call-5808988951641865091': {'count_physical_activity_anywhere': 4, 'count_2016_in_header': 0, 'sample_pa_paper_header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'sample_2016_paper_header': 'None'}}

exec(code, env_args)
