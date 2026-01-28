code = """import json
import re

# Load the data from both sources
with open('var_functions.query_db:18', 'r') as f:
    civic_docs = json.load(f)

with open('var_functions.query_db:24', 'r') as f:
    funding_data = json.load(f)

print('Loaded ' + str(len(civic_docs)) + ' civic documents')
print('Loaded ' + str(len(funding_data)) + ' funding records')

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check if document contains emergency or FEMA keywords
    lower_text = text.lower()
    has_emergency = 'emergency' in lower_text
    has_fema = 'fema' in lower_text
    
    if has_emergency or has_fema:
        # Find project sections - look for project names followed by (cid:190)
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for potential project names (not too short, not headers)
            if len(line) > 10 and not line.startswith('(') and not line.endswith(':'):
                # Check if next line contains (cid:190) indicating a project
                if i + 1 < len(lines) and '(cid:190)' in lines[i+1]:
                    project_name = line
                    
                    # Skip category headers
                    if any(x in project_name for x in ['Capital Improvement', 'Disaster Recovery', 'Public Works', 'Agenda Report', 'RECOMMENDED ACTION', 'To:', 'Prepared by:', 'Approved by:', 'Subject:']):
                        continue
                    
                    # Determine status from context
                    status = 'not started'
                    snippet = ' '.join(lines[i:i+15])  # Look at next 15 lines for context
                    
                    if 'under construction' in snippet.lower():
                        status = 'construction'
                    elif 'design' in snippet.lower() and ('complete' in snippet.lower() or 'completed' in snippet.lower()):
                        # Special case for "Complete Design"
                        pass
                    elif 'design' in snippet.lower():
                        status = 'design'
                    elif 'complete' in snippet.lower() or 'completed' in snippet.lower():
                        status = 'completed'
                    
                    # Build topic list
                    topic_list = []
                    if has_fema:
                        topic_list.append('FEMA')
                    if has_emergency:
                        topic_list.append('emergency')
                    
                    # Determine type
                    project_type = 'disaster' if has_fema else 'capital'
                    
                    projects.append({
                        'Project_Name': project_name,
                        'topic': ','.join(topic_list),
                        'type': project_type,
                        'status': status,
                        'source_file': filename
                    })

print('Extracted ' + str(len(projects)) + ' emergency/FEMA related projects from documents')

# Show first few extracted projects
for i, proj in enumerate(projects[:10]):
    print('Project ' + str(i) + ': ' + proj['Project_Name'] + ' (status: ' + proj['status'] + ')')

# Convert funding data to dict for easy lookup by project name
funding_dict = {}
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    if proj_name not in funding_dict:
        funding_dict[proj_name] = []
    funding_dict[proj_name].append({
        'Funding_Source': fund.get('Funding_Source', ''),
        'Amount': int(fund.get('Amount', 0)) if fund.get('Amount') else 0
    })

print('Funding dict has ' + str(len(funding_dict)) + ' unique project names')

# Merge projects with funding data
merged_results = []

for project in projects:
    proj_name = project['Project_Name']
    # Try exact match first
    if proj_name in funding_dict:
        for fund in funding_dict[proj_name]:
            merged_results.append({
                'Project_Name': proj_name,
                'Funding_Source': fund['Funding_Source'],
                'Amount': fund['Amount'],
                'Status': project['status'],
                'Topic': project['topic'],
                'Type': project['type'],
                'Source_File': project['source_file']
            })
    else:
        # Try fuzzy matching - check if project name contains or is contained in funded project names
        matched = False
        for funded_name in funding_dict.keys():
            if proj_name in funded_name or funded_name in proj_name:
                # Found a match
                for fund in funding_dict[funded_name]:
                    merged_results.append({
                        'Project_Name': proj_name + ' (matched to: ' + funded_name + ')',
                        'Funding_Source': fund['Funding_Source'],
                        'Amount': fund['Amount'],
                        'Status': project['status'],
                        'Topic': project['topic'],
                        'Type': project['type'],
                        'Source_File': project['source_file']
                    })
                matched = True
                break
        
        if not matched:
            # No funding found
            merged_results.append({
                'Project_Name': proj_name,
                'Funding_Source': 'Not found',
                'Amount': 0,
                'Status': project['status'],
                'Topic': project['topic'],
                'Type': project['type'],
                'Source_File': project['source_file']
            })

print('Merged results count: ' + str(len(merged_results)))

# Filter to only include projects with actual funding
funded_projects = [r for r in merged_results if r['Funding_Source'] != 'Not found']
print('Projects with funding: ' + str(len(funded_projects)))

# Output results
result_str = json.dumps(funded_projects, ensure_ascii=False, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'name': 'Funding'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
