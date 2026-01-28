code = """import json
import re

# Load papers
with open(locals()['var_function-call-8113430388473756974'], 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")

# Inspect first paper text for metadata patterns
sample_text = papers[0]['text']
print("First 1000 chars of paper 1:")
print(json.dumps(sample_text[:1000]))

# Check for "Contribution" in a few papers
print("\nScanning for 'Contribution' or similar keys in first 5 papers:")
for i, p in enumerate(papers[:5]):
    text = p.get('text', '')
    # Search for lines containing "Contribution"
    lines = text.split('\n')
    found = False
    for line in lines:
        if "contribution" in line.lower() and len(line) < 200:
            print(f"Paper {i} match: {json.dumps(line.strip())}")
            found = True
    if not found:
        print(f"Paper {i}: No short line with 'contribution' found.")

# Check for Year
print("\nScanning for Year in first 5 papers:")
for i, p in enumerate(papers[:5]):
    text = p.get('text', '')
    # Look for 4 digits
    matches = re.findall(r'\b(19|20)\d{2}\b', text[:1000])
    print(f"Paper {i} year candidates: {matches}")

print("__RESULT__:")
print("Inspection done")"""

env_args = {'var_function-call-3660777886062697260': ['paper_docs'], 'var_function-call-3660777886062696049': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6381855521960426930': 'file_storage/function-call-6381855521960426930.json', 'var_function-call-8113430388473756974': 'file_storage/function-call-8113430388473756974.json', 'var_function-call-2108608692273987200': 'file_storage/function-call-2108608692273987200.json'}

exec(code, env_args)
