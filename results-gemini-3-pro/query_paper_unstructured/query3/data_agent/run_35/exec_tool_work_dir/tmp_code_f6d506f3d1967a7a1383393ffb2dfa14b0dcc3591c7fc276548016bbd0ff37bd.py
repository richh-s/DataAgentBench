code = """import json
import re

with open(locals()['var_function-call-17398262827870080224'], 'r') as f:
    papers = json.load(f)

results = []
for p in papers:
    text = p['text']
    filename = p['filename']
    
    contrib_lines = [line.strip() for line in text.split('\\n') if 'contribution' in line.lower()]
    
    keywords = {
        'empirical': 'empirical' in text.lower(),
        'artifact': 'artifact' in text.lower(),
        'theoretical': 'theoretical' in text.lower(),
        'survey': 'survey' in text.lower(),
        'methodological': 'methodological' in text.lower()
    }
    
    results.append({
        'filename': filename,
        'contrib_lines_sample': contrib_lines[:3],
        'keywords': keywords,
        'first_lines': text[:200]
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8084430773459944096': 'file_storage/function-call-8084430773459944096.json', 'var_function-call-46270617840207883': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17398262827870080224': 'file_storage/function-call-17398262827870080224.json'}

exec(code, env_args)
