code = """import json
import re

with open(locals()['var_function-call-3050203900418415447'], 'r') as f:
    papers = json.load(f)

print("Total papers:", len(papers))

# Check for "empirical"
empirical_count = sum(1 for p in papers if 'empirical' in p.get('text', '').lower())
print("Papers with 'empirical':", empirical_count)

# Check years in first 5 papers
print("Sample Headers:")
for p in papers[:5]:
    text = p.get('text', '')[:300]
    print(f"--- {p['filename']} ---")
    print(text.replace('\n', ' '))
    
    # Test regex
    matches = re.findall(r'\b(20\d\d)\b', text)
    print("Years found:", matches)"""

env_args = {'var_function-call-7133362832000802960': 'file_storage/function-call-7133362832000802960.json', 'var_function-call-7133362832000806077': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-3665432082971907292': 'file_storage/function-call-3665432082971907292.json', 'var_function-call-3050203900418415447': 'file_storage/function-call-3050203900418415447.json', 'var_function-call-4351111685594668903': []}

exec(code, env_args)
