code = """import json
import pandas as pd

# Load data from stored results
civic_docs_path = locals()["var_functions.query_db:2"]
funding_path = locals()["var_functions.query_db:5"]

with open(civic_docs_path, "r") as f:
    civic_docs = json.load(f)

with open(funding_path, "r") as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df["Amount"] = pd.to_numeric(funding_df["Amount"], errors="coerce")

# Identify park projects completed in 2022 from the civic docs
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get("text", "")
    lines = text.split("\n")
    
    project_block = []
    for line in lines:
        line = line.strip()
        if line:
            project_block.append(line)
            # Look for completion patterns with 2022 and park
            lower_block = " ".join(project_block).lower()
            if ("completed" in lower_block and "2022" in lower_block and 
                "park" in lower_block):
                # Find the project name line (usually the first non-indented line)
                for block_line in project_block:
                    if (len(block_line) < 100 and 
                        not block_line.startswith("(") and 
                        not block_line.startswith("•")):
                        project_name = block_line
                        if project_name not in park_projects_2022:
                            park_projects_2022.append(project_name)
                        break
                project_block = []

# Remove duplicates and empty strings
park_projects_2022 = [p for p in park_projects_2022 if p]

# Match with funding data by creating a lookup
total_funding = 0
matched_projects = []

# Normalize project names for matching
def normalize_name(name):
    return name.lower().replace("project", "").strip()

funding_lookup = {}
for idx, row in funding_df.iterrows():
    funding_name = normalize_name(row["Project_Name"])
    funding_lookup[funding_name] = row["Amount"]

# Check each park project against funding data
for park_project in park_projects_2022:
    park_norm = normalize_name(park_project)
    
    # Direct match
    if park_norm in funding_lookup:
        total_funding += funding_lookup[park_norm]
        matched_projects.append(park_project)
        
    # Partial match - check each word
    else:
        park_words = set(park_norm.split())
        for funding_name, amount in funding_lookup.items():
            funding_words = set(funding_name.split())
            # Match if they share at least 2 significant words
            common_words = park_words & funding_words
            if len(common_words) >= 2 and len(list(common_words)[0]) > 3:
                total_funding += amount
                matched_projects.append(park_project + " -> " + funding_name)
                break

print("__RESULT__:")
print(json.dumps({
    "total_funding": int(total_funding),
    "matches": matched_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
