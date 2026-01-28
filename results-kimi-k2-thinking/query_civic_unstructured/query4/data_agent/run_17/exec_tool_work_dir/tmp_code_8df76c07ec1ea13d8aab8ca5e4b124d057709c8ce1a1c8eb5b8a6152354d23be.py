code = """import json

# Load files
civic_docs = json.load(open(locals()['var_functions.query_db:5']))
funding = json.load(open(locals()['var_functions.query_db:20']))

# Build funding lookup
totals = {}
for f in funding:
    name = f['Project_Name']
    amt = int(f['Amount'])
    totals[name] = totals.get(name, 0) + amt

# Extract projects with 2022 start from civic docs
names = set()
scheduled_start = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip irrelevant lines
        if not line or len(line) > 100 or line.isupper():
            continue
        if any(x in line for x in ['To:', 'From:', 'Subject:', 'Date:', 'Page', 'Projects (', 'Updates:', 'Schedule:']):
            continue
        
        # Check if this is a project name (not too long, proper case)
        words = line.split()
        if len(words) >= 2 and len(words) <= 15:
            # Check context for 2022 dates
            context = ' '.join(lines[max(0,i-5):min(len(lines),i+15)])
            if '2022' in context:
                # Check if it's Spring
                if any(s in context.lower() for s in ['spring', 'march', 'april', 'may']):
                    names.add(line)
                # Or check if project name itself starts with 2022
                elif line.startswith('2022'):
                    # Check if it's Morning View or other Spring indicators
                    if 'Morning View' in line or 'Spring' in context:
                        names.add(line)

# Find funding matches
matches = {}
for name in names:
    name_lower = name.lower()
    for fund in totals:
        fund_lower = fund.lower()
        # Match if similar
        if name_lower in fund_lower or fund_lower in name_lower:
            score = len(set(name_lower.split()) & set(fund_lower.split()))
            if score >= 2 or len(name.split()) <= 3:
                matches[name] = totals[fund]
                break

output = {
    'count': len(matches),
    'funding': sum(matches.values()),
    'projects': matches
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'num_civic_docs': 5, 'num_funding_records': 500}}

exec(code, env_args)
