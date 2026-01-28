code = """import json
import re
from collections import defaultdict

# Load the civic docs data from the file
civic_docs_path = locals()['var_functions.query_db:8']
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:8']

print(f"Number of civic documents: {len(civic_docs)}")

# Let's examine the structure of the first document
first_doc = civic_docs[0]
print(f"\nFirst document keys: {list(first_doc.keys())}")
print(f"First document filename: {first_doc.get('filename')}")
print(f"First document text preview (first 500 chars):\n{first_doc.get('text', '')[:500]}")

# Let's look for patterns that might indicate project information
# Based on the preview, projects seem to be listed with their names and details
text = first_doc.get('text', '')

# Try to extract project information using regex patterns
# Look for patterns like project names followed by status/schedule info
project_patterns = [
    r'([A-Z][a-zA-Z\s\&\-]+?(?:Project|Improvements|Repairs|Structure|System|Plan|Facility|Study)\b)',
    r'([A-Z][a-zA-Z\s\&\-]+?(?:\(FEMA[\w\s/]*\)))',
    r'([A-Z][a-zA-Z\s\&\-]+?(?:\(CalJPIA[\w\s/]*\)))',
    r'([A-Z][a-zA-Z\s\&\-]+?(?:\(CalOES[\w\s/]*\)))'
]

found_projects = []
for pattern in project_patterns:
    matches = re.findall(pattern, text)
    found_projects.extend(matches)

print(f"\nPotential projects found in first document: {list(set(found_projects))[:20]}")"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
