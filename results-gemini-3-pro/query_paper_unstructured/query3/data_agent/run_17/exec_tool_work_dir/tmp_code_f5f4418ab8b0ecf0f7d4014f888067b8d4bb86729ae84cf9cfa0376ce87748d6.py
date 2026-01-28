code = """import json
import re

# Load data
path_papers = locals()['var_function-call-13071401018580020986']
path_citations = locals()['var_function-call-12503289098151716023']

with open(path_papers, 'r') as f:
    papers = json.load(f)

with open(path_citations, 'r') as f:
    citations_list = json.load(f)

# Build citations map
citation_sums = {}
for c in citations_list:
    t = c['title']
    count = int(c['citation_count'])
    citation_sums[t] = citation_sums.get(t, 0) + count

# Process papers
results = []
debug_info = []

for p in papers:
    filename = p['filename']
    title = filename.replace('.txt', '')
    text = p['text']
    
    # Extract Year
    # Look for 20xx in first 1000 chars
    years = re.findall(r'\b(20\d{2})\b', text[:2000])
    # Filter reasonable years for publication (e.g. 2010-2025)
    valid_years = [int(y) for y in years if 2000 <= int(y) <= 2030]
    
    if valid_years:
        # Assume the first mention is the pub year (often in header)
        pub_year = valid_years[0]
    else:
        pub_year = 0
    
    # Check Contribution: "empirical"
    # Also check if "empirical" is in text
    is_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        'title': title,
        'year': pub_year,
        'is_empirical': is_empirical
    })
    
    if pub_year > 2016 and is_empirical:
        count = citation_sums.get(title, 0)
        results.append({'title': title, 'citation_count': count})

print("__RESULT__:")
print(json.dumps(results))
# We also verify debug info by printing it (but only return results in JSON)
# print(json.dumps(debug_info)) # Commented out to match print format rules"""

env_args = {'var_function-call-6267193881023352391': 'file_storage/function-call-6267193881023352391.json', 'var_function-call-6267193881023352398': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-13071401018580018055': ['paper_docs'], 'var_function-call-13071401018580020986': 'file_storage/function-call-13071401018580020986.json', 'var_function-call-5244719068911348439': {'error': "[Errno 2] No such file or directory: 'var_function-call-13071401018580020986'"}, 'var_function-call-9288955964106777218': 'file_storage/function-call-9288955964106777218.json', 'var_function-call-12503289098151716023': 'file_storage/function-call-12503289098151716023.json'}

exec(code, env_args)
