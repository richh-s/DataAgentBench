code = """import json, re

# Load data
funding = globals()['var_functions.query_db:42']
civic_path = globals()['var_functions.query_db:0']
civic_docs = json.load(open(civic_path))

# Process each funding record to add status and topic
final_results = []

for rec in funding:
    name = rec['Project_Name']
    
    # Default values
    status = 'Unknown'
    topics = []
    
    # Extract topics from name
    if 'emergency' in name.lower():
        topics.append('emergency warning')
    if 'FEMA' in name:
        topics.append('FEMA')
    if 'drain' in name.lower() or 'storm' in name.lower() or 'culvert' in name.lower():
        topics.append('drainage')
    if 'road' in name.lower():
        topics.append('road')
    if 'siren' in name.lower() or 'warning' in name.lower():
        topics.append('emergency warning')
    if 'park' in name.lower():
        topics.append('park')
    if 'bridge' in name.lower():
        topics.append('bridge')
    if 'irrigation' in name.lower():
        topics.append('irrigation')
    
    topic_str = ', '.join(topics) if topics else 'None'
    
    # Determine type
    ptype = 'disaster' if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name else 'capital'
    
    # Search for status in civic documents
    for doc in civic_docs:
        if name in doc['text']:
            text = doc['text'].lower()
            if 'design' in text:
                status = 'design'
                break
            if 'construction' in text:
                status = 'construction'
                break
            if 'completed' in text:
                status = 'completed'
                break
            if 'not started' in text:
                status = 'not started'
                break
    
    final_results.append({
        'Project_Name': name,
        'Funding_Source': rec['Funding_Source'],
        'Amount': int(rec['Amount']),
        'Status': status,
        'Type': ptype,
        'Topic': topic_str
    })

# Sort by amount
final_results.sort(key=lambda x: x['Amount'], reverse=True)

answer = 'Emergency/FEMA Related Projects\n\n'
answer += ('%-50s | %-25s | %10s | %-12s | %-20s\n' % ('Project Name', 'Funding Source', 'Amount', 'Status', 'Topic'))
answer += ('-' * 130) + '\n'

for r in final_results:
    proj_name_short = r['Project_Name'][:45] + '...' if len(r['Project_Name']) > 45 else r['Project_Name']
    answer += ('%-50s | %-25s | $%8d | %-12s | %-20s\n' % (proj_name_short, r['Funding_Source'][:24], r['Amount'], r['Status'], r['Topic'][:19]))

answer += ('\nTotal projects found: %d' % len(final_results))

print('__RESULT__:') 
print(json.dumps(answer))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.query_db:42': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
