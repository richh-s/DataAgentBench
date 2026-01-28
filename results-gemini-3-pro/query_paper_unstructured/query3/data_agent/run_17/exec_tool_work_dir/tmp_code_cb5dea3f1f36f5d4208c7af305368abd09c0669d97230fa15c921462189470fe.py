code = """import json
import re

result_info = {}

try:
    with open('var_function-call-13071401018580020986', 'r') as f:
        papers = json.load(f)
    
    result_info['total_papers'] = len(papers)
    if papers:
        result_info['keys'] = list(papers[0].keys())
        
    count_empirical = 0
    for p in papers[:100]:
        if 'empirical' in p.get('text', '').lower():
            count_empirical += 1
    result_info['empirical_count_first_100'] = count_empirical
    
    years = []
    for p in papers[:10]:
        header = p.get('text', '')[:1000]
        # Look for Year: 2017, 2018, etc. 
        # Regex for 4 digits starting with 19 or 20
        match = re.search(r'\b(20\d{2})\b', header)
        if not match:
             match = re.search(r'\b(19\d{2})\b', header)
        
        y = match.group(1) if match else "Not found"
        years.append({'title': p.get('filename'), 'year': y})
    result_info['sample_years'] = years

except Exception as e:
    result_info['error'] = str(e)

print("__RESULT__:")
print(json.dumps(result_info))"""

env_args = {'var_function-call-6267193881023352391': 'file_storage/function-call-6267193881023352391.json', 'var_function-call-6267193881023352398': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-13071401018580018055': ['paper_docs'], 'var_function-call-13071401018580020986': 'file_storage/function-call-13071401018580020986.json'}

exec(code, env_args)
