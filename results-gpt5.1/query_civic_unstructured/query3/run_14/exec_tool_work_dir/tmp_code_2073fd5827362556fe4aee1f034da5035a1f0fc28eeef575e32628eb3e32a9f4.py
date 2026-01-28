code = """import json, re
from pathlib import Path

# Load full funding table
with open(var_call_Cepcv0I6L3jedfyQJRNtBCY7, 'r') as f:
    funding = json.load(f)

# Filter projects with 'FEMA' or 'emergency' in name (case-insensitive)
pattern = re.compile(r'(fema|emergency)', re.I)
filtered = [
    {
        'Project_Name': row['Project_Name'],
        'Funding_Source': row['Funding_Source'],
        'Amount': int(row['Amount']) if isinstance(row['Amount'], str) and row['Amount'].isdigit() else row['Amount']
    }
    for row in funding
    if pattern.search(row['Project_Name'])
]

result = json.dumps(filtered)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_Cepcv0I6L3jedfyQJRNtBCY7': 'file_storage/call_Cepcv0I6L3jedfyQJRNtBCY7.json', 'var_call_6fkm4Vim8c3iYTNWbif0rDsd': 'file_storage/call_6fkm4Vim8c3iYTNWbif0rDsd.json', 'var_call_qjyG82mJI1WUVKnZiuWmM6nn': ['civic_docs'], 'var_call_pL6y4mZ8d7bTL4FD6WjlaUNb': ['Funding']}

exec(code, env_args)
