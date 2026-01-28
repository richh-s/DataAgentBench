code = """import json
import re

papers_path = locals()['var_function-call-13085037572156381968']
with open(papers_path, 'r') as f:
    papers = json.load(f)

debug_info = []
for p in papers[:10]:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    header = text[:1000]
    years = re.findall(r'\b(20[1-2][0-9])\b', header)
    pub_year = int(years[0]) if years else None
    has_empirical = "empirical" in text.lower()
    
    debug_info.append({
        "title": title,
        "year": pub_year,
        "has_empirical": has_empirical,
        "header_snippet": header[:100]
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-7886853940146991682': 'file_storage/function-call-7886853940146991682.json', 'var_function-call-14846085348849016055': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13085037572156381968': 'file_storage/function-call-13085037572156381968.json', 'var_function-call-1254515193280365466': [{'COUNT(*)': '1405'}], 'var_function-call-13580482470423784099': 'file_storage/function-call-13580482470423784099.json', 'var_function-call-5769832818917747020': []}

exec(code, env_args)
