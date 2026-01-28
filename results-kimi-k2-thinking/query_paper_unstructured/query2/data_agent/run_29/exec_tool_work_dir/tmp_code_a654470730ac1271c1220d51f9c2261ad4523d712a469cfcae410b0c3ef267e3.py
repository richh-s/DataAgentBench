code = """import json
import re

# Step 1: Read the 2018 citations
citations_2018_key = 'var_functions.query_db:5'
citations_2018 = locals()[citations_2018_key]

# Step 2: Read the paper documents
paper_docs_key = 'var_functions.query_db:2'
paper_docs = locals()[paper_docs_key]

# Check if they are file paths (strings ending with .json)
if isinstance(citations_2018, str) and citations_2018.endswith('.json'):
    with open(citations_2018, 'r') as f:
        citations_2018 = json.load(f)

if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

print(f"Number of 2018 citations: {len(citations_2018)}")
print(f"Number of paper documents: {len(paper_docs)}")

# Display sample data
print("Sample 2018 citations:")
for i, cit in enumerate(citations_2018[:3]):
    print(f"  {i}: {cit}")

print("Sample paper documents:")
for i, doc in enumerate(paper_docs[:2]):
    print(f"  {i}: {doc.get('filename', 'No filename')}")"""

env_args = {'var_functions.query_db:0': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
