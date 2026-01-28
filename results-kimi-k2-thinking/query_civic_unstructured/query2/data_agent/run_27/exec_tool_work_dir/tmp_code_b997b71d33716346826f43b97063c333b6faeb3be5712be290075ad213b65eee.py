code = """import json, re, os

# Get the stored file paths
civic_docs_json = locals()['var_functions.query_db:16']
funding_json = locals()['var_functions.query_db:17']

# Process the civic documents text file
civic_docs_text = open(civic_docs_json).read()
civic_docs = json.loads(civic_docs_text)

# Process the funding data text file  
funding_text = open(funding_json).read()
funding_data = json.loads(funding_text)

print("Successfully loaded {} civic documents and {} funding records".format(len(civic_docs), len(funding_data)))

# Find park projects completed in 2022
park_projects_2022 = []

# Combine all text from all documents
all_document_text = ""
for doc in civic_docs:
    all_document_text += doc["text"] + "\n"

# Look for park projects with completion in 2022
lines = all_document_text.split("\n")

for i in range(len(lines)):
    line = lines[i].strip()
    if not line or line.startswith("("):
        continue
        
    # Check if line mentions completion in 2022
    if "2022" in line and ("completed" in line.lower() or "completion" in line.lower()):
        # Look backwards for project name
        project_name = None
        for j in range(i-1, max(0, i-10), -1):
            prev_line = lines[j].strip()
            if prev_line and not prev_line.startswith("(") and len(prev_line) > 5:
                # Clean project name
                clean_name = prev_line.replace("•", "").replace("◦", "").strip()
                clean_name = re.sub(r"^[A-Z]\.?\s+", "", clean_name)
                
                # Check if it's a reasonable project name
                if clean_name and "Update" not in clean_name and "Schedule" not in clean_name:
                    project_name = clean_name
                    break
        
        if project_name and ("park" in project_name.lower() or "playground" in project_name.lower()):
            if project_name not in park_projects_2022:
                park_projects_2022.append(project_name)

print("Found {} unique park projects completed in 2022".format(len(park_projects_2022)))
for proj in park_projects_2022:
    print("- {}".format(proj))

# Calculate total funding
total_funding = 0
matched_projects = []

for park_name in park_projects_2022:
    park_simple = park_name.lower().replace(" ", "").replace("-", "")
    
    for fund in funding_data:
        fund_name = fund["Project_Name"]
        fund_simple = fund_name.lower().replace(" ", "").replace("-", "")
        amount = int(fund["Amount"])
        
        # Check for name match
        if park_simple in fund_simple or fund_simple in park_simple:
            total_funding += amount
            matched_projects.append({
                "park_project": park_name,
                "funding_record": fund_name,
                "amount": amount
            })
            break

print("\nTotal funding for park-related projects completed in 2022: ${:,}".format(total_funding))

result = {
    "total_funding_dollars": total_funding,
    "number_of_projects": len(park_projects_2022),
    "matched_funding_details": matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
