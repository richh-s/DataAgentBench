code = """import json

file_path = locals()['var_function-call-11196622143221928567']
with open(file_path, 'r') as f:
    papers = json.load(f)

# Debug: Print headers of first 5 papers
headers = []
for p in papers[:5]:
    headers.append(p['text'][:200])

# Debug: Check if any paper has "2016" in first 1000 chars
count_2016 = 0
for p in papers:
    if '2016' in p['text'][:1000]:
        count_2016 += 1

# Debug: Check if any paper has "physical activity"
count_pa = 0
for p in papers:
    if 'physical activity' in p['text'].lower():
        count_pa += 1

print("__RESULT__:")
print(json.dumps({
    "sample_headers": headers,
    "count_2016_in_header": count_2016,
    "count_pa": count_pa,
    "total_papers": len(papers)
}))"""

env_args = {'var_function-call-16083049299143672043': 'file_storage/function-call-16083049299143672043.json', 'var_function-call-6689175005249734094': ['Citations', 'sqlite_sequence'], 'var_function-call-11808017164042867885': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11196622143221928567': 'file_storage/function-call-11196622143221928567.json', 'var_function-call-9561131013778660731': []}

exec(code, env_args)
