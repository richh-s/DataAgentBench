code = """import json
import os

# Load funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_file = var_functions.query_db:1
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

# Create map of project names to amounts
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Find projects that are capital projects in design status
design_projects = []

for doc in civic_docs_data:
    if 'text' not in doc:
        continue
    
    text = doc['text']
    
    # Check if this document contains design phase capital projects
    if 'Capital Improvement Projects (Design)' in text:
        # Find where the design section starts
        design_start = text.find('Capital Improvement Projects (Design)')
        section_text = text[design_start:]
        
        # Find where the next section starts to isolate the design section
        next_section_starts = [
            section_text.find('Capital Improvement Projects (Construction)'),
            section_text.find('Capital Improvement Projects (Not Started)'),
            section_text.find('Disaster Recovery Projects')
        ]
        
        # Filter out -1 values (not found)
        next_section_starts = [pos for pos in next_section_starts if pos > 0]
        
        if next_section_starts:
            section_end = min(next_section_starts)
            design_section = section_text[:section_end]
        else:
            design_section = section_text
        
        # Look for project names (assuming they're lines that don't start with special chars)
        for line in design_section.split('\n'):
            line = line.strip()
            
            if not line:
                continue
                
            is_heading = False
            heading_markers = ['Capital Improvement', 'Design:', 'Construction:', 'Updates:', 'Schedule:', 'Project Description:']
            for marker in heading_markers:
                if marker in line:
                    is_heading = True
                    break
            
            if is_heading:
                continue
                
            # Skip lines with markers that indicate notes, not project names
            if line.startswith('(') or line.startswith('-') or line.startswith('•'):
                continue
                
            # Check if this line is a project name we have funding for
            if line in funding_map and funding_map[line] > 50000:
                design_projects.append(line)

# Remove duplicates
unique_design_projects = list(set(design_projects))

# Create result
result = {
    'count': len(unique_design_projects),
    'projects': unique_design_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
