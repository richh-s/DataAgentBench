code = """import json
import re

# Load the result from query_db
with open(locals()['var_function-call-7732815880617685738'], 'r') as f:
    papers = json.load(f)

filtered_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' not in text.lower():
        continue
        
    # Check year
    # Look for 2016 in the first 1000 characters
    header_text = text[:1000]
    
    # Heuristic: Look for 2016, or '16 followed by a non-digit or end of line, or specific venue patterns
    # But strict "2016" is usually good enough for headers like "CHI 2016" or "September 2016"
    if '2016' in header_text:
        filtered_titles.append(title)
    elif "'16" in header_text:
        # Check if it looks like a year abbreviation (e.g. CHI '16)
        # Avoid matches like "user'16" (though unlikely in header)
        if re.search(r"\b'16\b", header_text) or re.search(r" \d{2}, '16", header_text):
            filtered_titles.append(title)

print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-12176732640452715958': 'file_storage/function-call-12176732640452715958.json', 'var_function-call-9822203806490735992': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7732815880617685738': 'file_storage/function-call-7732815880617685738.json'}

exec(code, env_args)
