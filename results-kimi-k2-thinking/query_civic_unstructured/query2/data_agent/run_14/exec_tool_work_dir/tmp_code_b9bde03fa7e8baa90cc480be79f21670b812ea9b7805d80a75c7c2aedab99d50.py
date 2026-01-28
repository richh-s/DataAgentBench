code = """import json

# Load funding data
with open("var_functions.query_db:2", "r") as f:
    funding_data = json.load(f)

# Load civic documents  
with open("var_functions.query_db:4", "r") as f:
    civic_docs = json.load(f)

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Extract projects from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc["text"]
    lines = text.split("\n")
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        if any(skip in line for skip in ["PAGE", "AGENDA", "PUBLIC WORKS", "COMMISSION", "CITY OF"]):
            continue
            
        if line.isupper() and len(line) < 150:
            if current_project:
                # Check previous project
                proj_text = current_project["text"].lower()
                is_park = any(kw in proj_text for kw in ["park", "playground", "bluffs", "landon", "arbors", "benches", "walkway"])
                completed_2022 = ("completed" in proj_text or "completion" in proj_text) and "2022" in current_project["text"]
                if is_park and completed_2022:
                    park_projects_2022.append(current_project)
            
            current_project = {"name": line, "text": "", "amount": 0}
        elif current_project:
            current_project["text"] += line + "\n"
    
    # Check last project
    if current_project:
        proj_text = current_project["text"].lower()
        is_park = any(kw in proj_text for kw in ["park", "playground", "bluffs", "landon", "arbors", "benches", "walkway"])
        completed_2022 = ("completed" in proj_text or "completion" in proj_text) and "2022" in current_project["text"]
        if is_park and completed_2022:
            park_projects_2022.append(current_project)

print("\nPark projects completed in 2022:", len(park_projects_2022))
for p in park_projects_2022:
    print("-", p["name"])

# Match with funding
total_funding = 0
matches = []

# Index funding by lowercase name
funding_index = {}
for fund in funding_data:
    funding_index[fund["Project_Name"].lower()] = fund

for proj in park_projects_2022:
    proj_name_lower = proj["name"].lower()
    
    if proj_name_lower in funding_index:
        fund = funding_index[proj_name_lower]
        amount = int(fund["Amount"])
        total_funding += amount
        matches.append({
            "project": proj["name"],
            "funding_record": fund["Project_Name"],
            "amount": amount,
            "source": fund["Funding_Source"]
        })
        continue
    
    # Fuzzy match
    for fund_name_lower, fund in funding_index.items():
        if proj_name_lower in fund_name_lower or fund_name_lower in proj_name_lower:
            amount = int(fund["Amount"])
            total_funding += amount
            matches.append({
                "project": proj["name"],
                "funding_record": fund["Project_Name"],
                "amount": amount,
                "source": fund["Funding_Source"]
            })
            break

print("\nFunding matches found:", len(matches))
print("Total funding:", total_funding)

for m in matches:
    print(f"- {m['project']}: ${m['amount']:,} ({m['source']})")

# Additional check for park funding records
park_keywords = ["park", "bluffs", "playground", "landon", "arbors", "benches", "walkway", "shade structure"]
additional_park_funding = []

for fund in funding_data:
    proj_name = fund["Project_Name"].lower()
    if any(kw in proj_name for kw in park_keywords):
        additional_park_funding.append({
            "name": fund["Project_Name"],
            "amount": int(fund["Amount"]),
            "source": fund["Funding_Source"]
        })

additional_total = sum(p["amount"] for p in additional_park_funding)
print("\nAll park-related funding records:", len(additional_park_funding))
print("Total all park funding (not filtered by year):", additional_total)

# Return final result
result = {
    "park_projects_2022_count": len(park_projects_2022),
    "direct_funding_matches": len(matches),
    "total_funding_for_matches": total_funding,
    "all_park_funding_records": len(additional_park_funding),
    "total_all_park_funding": additional_total
}

print("__RESULT__:")
print(json.dumps(result))}"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
