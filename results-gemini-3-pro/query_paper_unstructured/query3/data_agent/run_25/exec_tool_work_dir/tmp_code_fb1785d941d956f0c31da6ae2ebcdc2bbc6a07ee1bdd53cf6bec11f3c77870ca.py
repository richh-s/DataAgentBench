code = """import json
import re

with open(locals()['var_function-call-15606477523093127544'], 'r') as f:
    docs = json.load(f)

debug_info = []
for doc in docs:
    text = doc['text']
    title = doc['filename'].replace('.txt', '')
    header = text[:1000]
    years = re.findall(r"20\d{2}", header)
    year = int(years[0]) if years else 0
    debug_info.append({"title": title, "year": year})

print("__RESULT__:")
print(json.dumps({"count": len(docs), "samples": debug_info}))"""

env_args = {'var_function-call-4403390195297864469': 'file_storage/function-call-4403390195297864469.json', 'var_function-call-5079307557547688021': ['paper_docs'], 'var_function-call-3097430276196367090': 'file_storage/function-call-3097430276196367090.json', 'var_function-call-5206321841837773326': {'has_empirical': False, 'has_survey': True, 'has_interview': True, 'has_study': True}, 'var_function-call-3687296208506163854': [], 'var_function-call-5857355116469077971': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-4539730163481461020': 'file_storage/function-call-4539730163481461020.json', 'var_function-call-10637637580937536300': {'total_docs': 5, 'docs_after_2016': 0, 'docs_after_2016_with_empirical': 0, 'docs_after_2016_with_study': 0, 'examples_empirical': []}, 'var_function-call-15606477523093127544': 'file_storage/function-call-15606477523093127544.json', 'var_function-call-6095849557644838005': []}

exec(code, env_args)
