code = """import json
import re

# Load papers
try:
    with open('var_function-call-13071401018580020986', 'r') as f:
        papers = json.load(f)
except Exception as e:
    print(e)
    papers = []

print("Total papers: " + str(len(papers)))

# Check keys
if len(papers) > 0:
    print("Keys: " + str(list(papers[0].keys())))

# Check for 'empirical'
count = 0
for p in papers[:100]:
    if 'empirical' in p.get('text', '').lower():
        count += 1
print("Papers with 'empirical' in first 100: " + str(count))

# Test Year
print("Year extraction test:")
for p in papers[:5]:
    header = p.get('text', '')[:1000]
    match = re.search(r'\b(20\d{2})\b', header)
    year = match.group(1) if match else "Not found"
    print("Title: " + str(p.get('filename')) + ", Year: " + str(year))

print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-6267193881023352391': 'file_storage/function-call-6267193881023352391.json', 'var_function-call-6267193881023352398': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-13071401018580018055': ['paper_docs'], 'var_function-call-13071401018580020986': 'file_storage/function-call-13071401018580020986.json'}

exec(code, env_args)
