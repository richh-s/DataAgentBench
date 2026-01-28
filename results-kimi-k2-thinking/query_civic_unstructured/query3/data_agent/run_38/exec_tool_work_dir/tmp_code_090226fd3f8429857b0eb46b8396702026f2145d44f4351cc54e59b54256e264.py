code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:32']
funding_path = locals()['var_functions.query_db:34']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Build funding lookup: normalized project name -> list of (source, amount)
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    source = rec.get('Funding_Source', 'Unknown')
    amount = int(rec.get('Amount', 0))
    funding_lookup.setdefault(name, []).append((source, amount))

# Process civic docs to extract emergency/FEMA projects
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    has_fema = 'fema' in lower_text
    has_emergency = 'emergency' in lower_text
    if not (has_fema or has_emergency):
        continue
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10:
            continue
        # Skip header-like lines
        if any(header in line for header in ['Capital Improvement', 'Disaster Recovery', 'Agenda Report', 'Public Works Commission', 'To:', 'Prepared by:', 'Subject:']):
            continue
        # Check if next line contains (cid:190) indicating a project entry
        if idx + 1 < len(lines) and '(cid:190)' in lines[idx+1]:
            proj_name = line
            # Determine status based on following context
            status = 'not started'
            context = ' '.join(lines[idx:idx+15]).lower()
            if 'under construction' in context:
                status = 'construction'
            elif 'design' in context:
                # 'Complete Design' still counts as design phase
                status = 'design'
            elif 'complete' in context or 'completed' in context:
                # Ensure not 'Complete Design'
                if 'complete design' not in context:
                    status = 'completed'
            # Build topics list
            topics = []
            if has_fema:
                topics.append('FEMA')
            if has_emergency:
                topics.append('emergency')
            # Determine type
            project_type = 'disaster' if has_fema else 'capital'
            projects.append({
                'Project_Name': proj_name,
                'topics': ','.join(topics),
                'type': project_type,
                'status': status
            })

# Merge with funding data
results = []
for proj in projects:
    name = proj['Project_Name']
    matched = False
    # Direct match
    if name in funding_lookup:
        for source, amount in funding_lookup[name]:
            results.append([name, source, amount, proj['status'], proj['topics'], proj['type']])
        matched = True
    else:
        # Fuzzy containment match
        for funded_name in funding_lookup:
            if name in funded_name or funded_name in name:
                for source, amount in funding_lookup[funded_name]:
                    results.append([name, source, amount, proj['status'], proj['topics'], proj['type']])
                matched = True
                break
    if not matched:
        results.append([name, 'No funding record', 0, proj['status'], proj['topics'], proj['type']])

# Format results as plain text list
output_lines = []
for row in results:
    proj_name, source, amount, status, topics, typ = row
    output_lines.append(f"Project: {proj_name}")
    output_lines.append(f"  Funding Source: {source}")
    output_lines.append(f"  Amount: ${amount:,}")
    output_lines.append(f"  Status: {status}")
    output_lines.append(f"  Topics: {topics}")
    output_lines.append(f"  Type: {typ}")
    output_lines.append('')

final_answer = '\n'.join(output_lines)
print('__RESULT__:')
print(final_answer)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'name': 'Funding'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
