code = """import json

# Load funding data with Amount > 50000
funding_file = var_functions.query_db:60
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding map: project name -> amount
funding_map = {}
for item in funding_records:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_map[project_name] = amount

# Extract design status capital projects from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lowercase_text = text.lower()
    
    # Look for capital improvement projects in design phase
    if 'capital improvement projects' in lowercase_text and 'design' in lowercase_text:
        # Split into lines and examine each
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty or very short lines
            if len(line) < 5:
                continue
            # Skip headers, page numbers, etc.
            if line.startswith('Page') or line.startswith('Item'):
                continue
            if 'Schedule:' in line or 'Updates:' in line or 'Project Description:' in line:
                continue
            if line.startswith('202') or line.startswith('20-'):
                continue
            # Skip lines with common non-project terms
            skip_terms = ['staff is', 'city will', 'consultant', 'project is', 'recommended action', 'discussion:']
            if any(term in line.lower() for term in skip_terms):
                continue
                
            # Check if this project has design status in its context
            line_pos = text.find(line)
            if line_pos >= 0:
                # Look ahead in text for status
                lookahead_end = min(line_pos + 400, len(text))
                context = text[line_pos:lookahead_end]
                if 'Design' in context:
                    clean_name = line.replace('•', '').replace('○', '').strip()
                    if 8 < len(clean_name) < 200:
                        design_projects.add(clean_name)

# Count matches: design projects with funding > 50000
count = 0
matched_list = []

for design_proj in design_projects:
    for funded_name, amount in funding_map.items():
        if amount > 50000:
            # Check for name similarity (substring match)
            d_lower = design_proj.lower()
            f_lower = funded_name.lower()
            
            # Check if one name is contained in the other
            if (d_lower in f_lower) or (f_lower in d_lower):
                # Additional check: length similarity
                if abs(len(design_proj) - len(funded_name)) < 40:
                    count += 1
                    matched_list.append({
                        'project': design_proj,
                        'funded_as': funded_name,
                        'amount': amount
                    })
                    break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
