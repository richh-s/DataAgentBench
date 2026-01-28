code = """import json
import re

# Load funding data
with open('file_storage/execute_python_2/query_db_2.json', 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open('file_storage/execute_python_5/query_db_5.json', 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_records)} funding records and {len(civic_docs)} civic documents")

# Step 1: Identify high-funded projects
high_funded = {}
for rec in funding_records:
    amt = int(rec.get('Amount', 0))
    if amt > 50000:
        high_funded[rec.get('Project_Name', '').lower()] = {
            'name': rec.get('Project_Name'),
            'amount': amt
        }

print(f"Projects with >$50k funding: {len(high_funded)}")

# Step 2: Find capital design projects in civic documents
all_text = ""
for doc in civic_docs:
    all_text += " " + doc.get('text', '')

# Search for patterns
capital_design_funded = []
text_lower = all_text.lower()

for project_key in high_funded:
    if project_key in text_lower:
        # Find context
        idx = text_lower.find(project_key)
        context = text_lower[max(0, idx-200):idx+300]
        
        # Check for capital and design
        if "capital" in context and "design" in context:
            capital_design_funded.append({
                "project": high_funded[project_key]['name'],
                "funding": high_funded[project_key]['amount']
            })

print(f"Capital design projects with >$50k funding: {len(capital_design_funded)}")

result = {
    "count": len(capital_design_funded),
    "projects": capital_design_funded[:3]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
