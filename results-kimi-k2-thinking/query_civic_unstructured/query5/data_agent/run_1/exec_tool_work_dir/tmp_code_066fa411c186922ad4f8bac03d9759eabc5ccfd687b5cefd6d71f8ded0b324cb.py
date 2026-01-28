code = """import json

docs_var = locals()['var_functions.query_db:32']
fund_var = locals()['var_functions.query_db:33']

if isinstance(docs_var, str) and docs_var.endswith('.json'):
    with open(docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(docs_var) if docs_var else []

if isinstance(fund_var, str) and fund_var.endswith('.json'):
    with open(fund_var, 'r') as f:
        funding = json.load(f)
else:
    funding = list(fund_var) if fund_var else []

funding_lookup = {}
for rec in funding:
    name = rec.get('Project_Name', '').strip()
    amount = int(rec.get('Amount', '0'))
    funding_lookup[name] = amount

eligible_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        if len(line) < 10:
            continue
        
        if 'Capital Improvement' in line or 'AGENDA' in line or 'Page ' in line:
            continue
        
        context_start = max(0, i-6)
        context_end = min(len(lines), i+8)
        context_lines = lines[context_start:context_end]
        context_text = ' '.join(context_lines)
        
        if '2022' in context_text:
            if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
                eligible_projects.add(line)
            else:
                for fund_name in funding_lookup.keys():
                    if '(FEMA' in fund_name or '(CalOES' in fund_name or '(CalJPIA' in fund_name:
                        if line in fund_name or fund_name in line:
                            eligible_projects.add(fund_name)
                            break

total = 0
results = []

for proj in eligible_projects:
    if proj in funding_lookup:
        amt = funding_lookup[proj]
        total += amt
        results.append({'name': proj, 'amount': amt})
    else:
        for fund in funding_lookup.keys():
            if proj in fund or fund in proj:
                amt = funding_lookup[fund]
                total += amt
                results.append({'name': fund, 'amount': amt})
                break

for fund in funding_lookup.keys():
    if '2022' in fund:
        has_marker = '(FEMA' in fund or '(CalOES' in fund or '(CalJPIA' in fund
        if has_marker:
            already = any(p['name'] == fund for p in results)
            if not already:
                amt = funding_lookup[fund]
                total += amt
                results.append({'name': fund, 'amount': amt})

output = {'total_funding': total, 'project_count': len(results), 'projects': results}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
