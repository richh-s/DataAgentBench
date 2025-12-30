code = """import json
import re

# Load papers
with open(locals()['var_function-call-8113430388473756974'], 'r') as f:
    papers = json.load(f)

# Inspect first paper end
text = papers[0]['text']
print("LAST 1000 chars:")
print(json.dumps(text[-1000:]))

# Regex for metadata
# Check if there is a block like "Contribution: ..."
match = re.search(r'Contribution\s*[:\-]\s*(.*)', text, re.IGNORECASE)
if match:
    print("Found Contribution Line:")
    print(match.group(0))
else:
    print("No 'Contribution:' line found.")
    
# Check for year in first 500 chars
year_match = re.search(r'\b(20\d{2})\b', text[:500])
if year_match:
    print(f"Year found: {year_match.group(1)}")

print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-3660777886062697260': ['paper_docs'], 'var_function-call-3660777886062696049': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6381855521960426930': 'file_storage/function-call-6381855521960426930.json', 'var_function-call-8113430388473756974': 'file_storage/function-call-8113430388473756974.json', 'var_function-call-2108608692273987200': 'file_storage/function-call-2108608692273987200.json'}

exec(code, env_args)
