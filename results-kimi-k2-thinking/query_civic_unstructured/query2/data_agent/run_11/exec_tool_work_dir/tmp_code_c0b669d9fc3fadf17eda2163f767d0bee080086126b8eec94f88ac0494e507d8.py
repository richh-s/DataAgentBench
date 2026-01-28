code = """import json

# Load civic documents
civic_docs = json.load(open("/tmp/tmpu9m4oj6r.json"))
# Load funding data
funding = json.load(open("/tmp/tmpg3x0v1j7.json"))

print("Loaded civic_docs:", len(civic_docs))
print("Loaded funding:", len(funding))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get("text", "")
    lines = text.split("\n")
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for project names containing Park
        if "Park" in line and len(line) > 10:
            # Skip headers
            if "Subject" in line or "Page" in line or "Item" in line:
                continue
            if line.startswith("("):
                continue
                
            # Check next lines for completion in 2022
            next_part = " ".join(lines[i:i+15])
            if "completed" in next_part.lower() and "2022" in next_part:
                park_projects.append(line)

unique_projects = list(set(park_projects))

# Match with funding
total_funding = 0
funding_matches = []

for proj in unique_projects:
    for rec in funding:
        name = rec.get("Project_Name", "")
        if proj.lower() in name.lower():
            amount = int(rec.get("Amount", 0))
            total_funding += amount
            funding_matches.append([proj, name, amount])

result = {
    "project_count": len(unique_projects),
    "total_funding": total_funding,
    "projects": unique_projects,
    "matches": funding_matches
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
