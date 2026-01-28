code = """import json
import re

result_info = {}

# Get file paths
path_papers = locals()['var_function-call-13071401018580020986']
path_citations = locals()['var_function-call-6267193881023352391']

try:
    with open(path_papers, 'r') as f:
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
    for p in papers[:5]:
        header = p.get('text', '')[:1000]
        match = re.search(r'\b(20\d{2})\b', header)
        y = match.group(1) if match else "Not found"
        years.append({'title': p.get('filename'), 'year': y})
    result_info['sample_years'] = years

    # Check Citations
    with open(path_citations, 'r') as f:
        citations = json.load(f)
    result_info['total_citations_records'] = len(citations)
    result_info['sample_citations'] = citations[:5]

except Exception as e:
    result_info['error'] = str(e)

print("__RESULT__:")
print(json.dumps(result_info))"""

env_args = {'var_function-call-6267193881023352391': 'file_storage/function-call-6267193881023352391.json', 'var_function-call-6267193881023352398': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-13071401018580018055': ['paper_docs'], 'var_function-call-13071401018580020986': 'file_storage/function-call-13071401018580020986.json', 'var_function-call-5244719068911348439': {'error': "[Errno 2] No such file or directory: 'var_function-call-13071401018580020986'"}}

exec(code, env_args)
