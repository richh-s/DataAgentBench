code = """import json
import re

# Load funding data with Amount > 50000
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_file = var_functions.query_db:6
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for sections with projects
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Look for capital projects in design phase
        # Pattern: project name followed by status indicators
        
        # Check if this line looks like a project name
        # Ignore common non-project lines
        ignore_patterns = [
            'Updates:', 'Schedule:', 'Advertise:', 'Begin', 'Complete', 'Project Description:',
            'Recommended Action', 'Staff is', 'City will', 'City submitted', 'City has',
            'Consultant', 'Project is', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:',
            'Meeting date:', 'Subject:', 'Public Works', 'Commission', 'Agenda', 'Item',
            'Page', 'Discussion:', 'RECOMMENDED ACTION:', 'DISCUSSION:'
        ]
        
        should_ignore = any(pattern.lower() in line.lower() for pattern in ignore_patterns)
        
        if not should_ignore and len(line) > 10 and 'Capital Improvement Projects' not in line:
            # Check if this project has design status
            # Look ahead in the next few lines for status
            status = None
            look_ahead = min(i + 5, len(lines))
            
            for j in range(i, look_ahead):
                context_line = lines[j].strip().lower()
                if 'design' in context_line:
                    status = 'design'
                    break
                elif 'construction' in context_line:
                    status = 'construction'
                    break
                elif 'not started' in context_line:
                    status = 'not started'
                    break
                elif 'complete' in context_line or 'completed' in context_line:
                    status = 'completed'
                    break
            
            # If status found and no ignore patterns, add project
            if status == 'design':
                # Clean project name
                proj_name = line
                # Remove common suffixes/prefixes
                proj_name = proj_name.replace('• ', '').replace('○ ', '').strip()
                
                # Only add if it seems like a real project name
                if (len(proj_name) < 150 and 
                    not proj_name.startswith('202') and 
                    not proj_name.startswith('Page') and
                    'Funding' not in proj_name and
                    'Agreement' not in proj_name):
                    
                    projects.append({
                        'Project_Name': proj_name,
                        'status': 'design',
                        'type': 'capital'
                    })
        
        i += 1

# Remove duplicates by project name
unique_projects = {}
for p in projects:
    name = p['Project_Name']
    if name not in unique_projects and len(name) > 5:
        unique_projects[name] = p

# Filter funding data to dictionary for faster lookup
funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Match projects with funding
matched_count = 0
matched_details = []

for proj_name in unique_projects.keys():
    # Direct match
    if proj_name in funding_dict and funding_dict[proj_name] > 50000:
        matched_count += 1
        matched_details.append({
            'Project_Name': proj_name,
            'Amount': funding_dict[proj_name]
        })
    else:
        # Try to find partial matches
        for funded_name, amount in funding_dict.items():
            if amount > 50000:
                # Check for substring matches
                proj_lower = proj_name.lower()
                funded_lower = funded_name.lower()
                
                # Check if they are similar (one contains the other)
                if (proj_lower in funded_lower or funded_lower in proj_lower):
                    # Additional check: they should be reasonably similar in length
                    length_diff = abs(len(proj_name) - len(funded_name))
                    if length_diff < 40:  # Allow some difference for suffixes
                        matched_count += 1
                        matched_details.append({
                            'Project_Name': proj_name,
                            'Amount': amount,
                            'Matched_With': funded_name
                        })
                        break

# Create result
result = {
    'count': matched_count,
    'projects': sorted(matched_details, key=lambda x: x['Amount'], reverse=True)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
