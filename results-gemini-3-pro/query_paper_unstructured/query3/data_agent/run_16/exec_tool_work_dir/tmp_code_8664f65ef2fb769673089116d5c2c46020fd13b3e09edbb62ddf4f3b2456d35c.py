code = """import json
import re

file_key = 'var_function-call-3366737603932088961'
result_info = {}

try:
    with open(locals()[file_key], 'r') as f:
        data = json.load(f)
    
    result_info['count'] = len(data)
    result_info['samples'] = []
    
    for i in range(min(5, len(data))):
        doc = data[i]
        text = doc.get('text', '')
        title = doc.get('filename', '')
        
        # Look for year
        year_match = re.search(r'\b(20\d{2})\b', text[:500])
        year = year_match.group(1) if year_match else None
        
        # Look for "contribution"
        contrib_idx = text.lower().find('contribution')
        contrib_context = text[contrib_idx:contrib_idx+100] if contrib_idx != -1 else None
        
        result_info['samples'].append({
            'title': title,
            'year_extracted': year,
            'contrib_context': contrib_context
        })

except Exception as e:
    result_info['error'] = str(e)

print("__RESULT__:")
print(json.dumps(result_info))"""

env_args = {'var_function-call-13973424374790880036': 'file_storage/function-call-13973424374790880036.json', 'var_function-call-13973424374790878367': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3366737603932088961': 'file_storage/function-call-3366737603932088961.json'}

exec(code, env_args)
