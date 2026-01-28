code = """import json

# Load results
civic_docs_result = locals()['var_functions.query_db:46']
funding_result = locals()['var_functions.query_db:47']

# Parse data safely
def safe_load_data(result_var):
    if isinstance(result_var, str) and result_var.endswith('.json'):
        with open(result_var, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return list(result_var) if result_var else []

civic_docs = safe_load_data(civic_docs_result)
funding = safe_load_data(funding_result)

# Build funding lookup
funding_lookup = {}
for rec in funding:
    name = rec.get('Project_Name', '')
    if name:
        amount = int(rec.get('Amount', 0))
        funding_lookup[name] = amount

# Find disaster projects with 2022
total_funding = 0
matched_projects = []

# First pass: look for projects with 2022 in their name from funding
for name, amount in funding_lookup.items():
    if '2022' in name and any(m in name for m in ['(FEMA', '(CalOES', '(CalJPIA']):
        total_funding += amount
        matched_projects.append({'name': name, 'amount': amount})

# Second pass: analyze civic documents
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for disaster projects and 2022 dates
    if '2022' in text and any(m in text for m in ['(FEMA', '(CalOES', '(CalJPIA']):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip metadata lines
            if any(skip in line for skip in ['Capital Improvement', 'Disaster Recovery', 'AGENDA', 'Page', 'Prepared by:', 'Approved by:']):
                continue
            
            # Look for disaster project names
            if any(m in line for m in ['(FEMA', '(CalOES', '(CalJPIA']):
                # Check if 2022 appears nearby
                context_start = max(0, i-3)
                context_end = min(len(lines), i+4)
                has_2022 = False
                for ctx in lines[context_start:context_end]:
                    if '2022' in ctx:
                        has_2022 = True
                        break
                
                if has_2022 and line not in [p['name'] for p in matched_projects]:
                    # Find funding
                    if line in funding_lookup:
                        total_funding += funding_lookup[line]
                        matched_projects.append({'name': line, 'amount': funding_lookup[line]})
                    else:
                        # Try partial match
                        for fund_name in funding_lookup.keys():
                            if line in fund_name or fund_name in line:
                                if fund_name not in [p['name'] for p in matched_projects]:
                                    total_funding += funding_lookup[fund_name]
                                    matched_projects.append({'name': fund_name, 'amount': funding_lookup[fund_name]})
                                break

result = {'total_funding': total_funding, 'project_count': len(matched_projects), 'projects': matched_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:47': 'file_storage/functions.query_db:47.json'}

exec(code, env_args)
