code = """import json
import re

# Load papers
with open('var_function-call-13071401018580020986', 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")

# Check keys
print("Keys in first 5 papers:")
for p in papers[:5]:
    print(list(p.keys()))

# Check for 'empirical' in text
print("\nChecking for 'empirical' in first 100 papers...")
count_empirical = 0
for p in papers[:100]:
    if 'empirical' in p.get('text', '').lower():
        count_empirical += 1
print(f"Papers with 'empirical' in text (first 100): {count_empirical}")

# Test Year Extraction
print("\nTesting Year Extraction (first 5):")
for p in papers[:5]:
    # Look in first 1000 chars
    header = p.get('text', '')[:1000]
    match = re.search(r'\b(20\d{2})\b', header)
    year = match.group(1) if match else "Not found"
    print(f"Title: {p.get('filename')}, Extracted Year: {year}")

print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-6267193881023352391': 'file_storage/function-call-6267193881023352391.json', 'var_function-call-6267193881023352398': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-13071401018580018055': ['paper_docs'], 'var_function-call-13071401018580020986': 'file_storage/function-call-13071401018580020986.json'}

exec(code, env_args)
