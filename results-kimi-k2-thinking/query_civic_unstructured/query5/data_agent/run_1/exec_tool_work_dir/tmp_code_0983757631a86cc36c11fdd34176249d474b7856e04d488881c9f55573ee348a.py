code = """import json

# Load data from storage
civic_docs_result = locals()['var_functions.query_db:32']
funding_result = locals()['var_functions.query_db:33']

# Parse civic documents
civic_docs = []
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(civic_docs_result) if civic_docs_result else []

# Parse funding records
funding_records = []
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = list(funding_result) if funding_result else []

# Build funding lookup table
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '').strip()
    amount_str = rec.get('Amount', '0')
    amount = int(amount_str) if amount_str else 0
    funding_lookup[name] = amount

# Identify disaster projects that started in 2022
total_funding = 0
matched_projects = []

# First, look for projects explicitly mentioned with 2022 dates in civic documents
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if not text:
        continue
    
    # Check for 2022 dates in the text
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip non-project lines
            if not line or len(line) < 5:
                continue
            
            skip_terms = ['Capital Improvement', 'Disaster Recovery', 'RECOMMENDED ACTION', 'AGENDA', 'Item', 'To:', 'From:', 'Subject:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Page ']
            should_skip = False
            for term in skip_terms:
                if term in line:
                    should_skip = True
                    break
            if should_skip:
                continue
            
            # Check if this is a disaster project
            is_disaster = False
            if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
                is_disaster = True
            
            # Or check if it matches a disaster funding project
            if not is_disaster:
                for funding_name in funding_lookup.keys():
                    if '(FEMA' in funding_name or '(CalOES' in funding_name or '(CalJPIA' in funding_name:
                        if line in funding_name or funding_name in line:
                            line = funding_name
                            is_disaster = True
                            break
            
            # Check if 2022 appears near this project name
            if is_disaster:
                context_start = max(0, i-3)
                context_end = min(len(lines), i+4)
                for context_line in lines[context_start:context_end]:
                    if '2022' in context_line:
                        # Found a disaster project with 2022 date
                        project_name = line.strip()[:200]
                        
                        # Get funding amount
                        if project_name in funding_lookup:
                            amount = funding_lookup[project_name]
                            total_funding += amount
                            matched_projects.append({'name': project_name, 'amount': amount})
                        else:
                            # Try partial match
                            for funding_name in funding_lookup.keys():
                                if project_name in funding_name or funding_name in project_name:
                                    amount = funding_lookup[funding_name]
                                    total_funding += amount
                                    matched_projects.append({'name': funding_name, 'amount': amount})
                                    break
                        break

# Also include disaster funding records that have 2022 in the name
for funding_name in funding_lookup.keys():
    if '2022' in funding_name:
        # Check if disaster-related
        if '(FEMA' in funding_name or '(CalOES' in funding_name or '(CalJPIA' in funding_name:
            # Check if not already included
            already_included = False
            for proj in matched_projects:
                if proj['name'] == funding_name:
                    already_included = True
                    break
            
            if not already_included:
                amount = funding_lookup[funding_name]
                total_funding += amount
                matched_projects.append({'name': funding_name, 'amount': amount})

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
