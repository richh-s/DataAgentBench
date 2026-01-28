code = """import json

# Load analyzed projects from the previous step result file
with open(locals()['var_function-call-7547475634007785108'], 'r') as f:
    projects = json.load(f)

# Load funding data
with open(locals()['var_function-call-15395128546112038851'], 'r') as f:
    funding = json.load(f)

# Create a lookup for funding
# Sum amounts by Project_Name (in case of duplicate entries, though unlikely for same ID)
funding_map = {}
for item in funding:
    name = item['Project_Name']
    amount = int(item['Amount'])
    if name in funding_map:
        funding_map[name] += amount
    else:
        funding_map[name] = amount

# Filter projects
target_projects = set()
for p in projects:
    name = p['name']
    start = p['start_date']
    is_disaster = p['is_disaster']
    
    # Fix disaster classification
    if "CalJPIA" in name or "CalJPIA" in str(p).upper(): # Check name or original text context logic
        is_disaster = True
        
    # Check criteria
    if is_disaster and "2022" in start:
        target_projects.add(name)

# Calculate total
total_funding = 0
matched_projects = []
for name in target_projects:
    if name in funding_map:
        total_funding += funding_map[name]
        matched_projects.append({"name": name, "amount": funding_map[name]})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-17928919016931246816': 'file_storage/function-call-17928919016931246816.json', 'var_function-call-17928919016931249021': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-8182209293978562195': 'file_storage/function-call-8182209293978562195.json', 'var_function-call-15395128546112038851': 'file_storage/function-call-15395128546112038851.json', 'var_function-call-7547475634007785108': 'file_storage/function-call-7547475634007785108.json'}

exec(code, env_args)
