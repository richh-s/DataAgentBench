code = """import json
import re

debug_info = {}

try:
    with open(locals()['var_function-call-8113430388473756974'], 'r') as f:
        papers = json.load(f)
        
    debug_info['count'] = len(papers)
    if papers:
        p = papers[0]
        text = p.get('text', '')
        debug_info['first_paper_len'] = len(text)
        debug_info['last_1000'] = text[-1000:]
        debug_info['first_500'] = text[:500]
        
        # Check for Contribution pattern
        c_match = re.search(r'Contribution\s*[:\-]\s*(.*)', text, re.IGNORECASE)
        if c_match:
            debug_info['contribution_match'] = c_match.group(0)
        else:
            debug_info['contribution_match'] = "Not found"
            
        # Check for year
        y_match = re.search(r'\b(20\d{2})\b', text[:500])
        if y_match:
            debug_info['year_match'] = y_match.group(1)
        else:
            debug_info['year_match'] = "Not found"

except Exception as e:
    debug_info['error'] = str(e)

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-3660777886062697260': ['paper_docs'], 'var_function-call-3660777886062696049': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6381855521960426930': 'file_storage/function-call-6381855521960426930.json', 'var_function-call-8113430388473756974': 'file_storage/function-call-8113430388473756974.json', 'var_function-call-2108608692273987200': 'file_storage/function-call-2108608692273987200.json'}

exec(code, env_args)
