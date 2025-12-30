code = """import json
import re

# Load data
with open(locals()['var_function-call-6642322525338972320'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6642322525338973529'], 'r') as f:
    funding_data = json.load(f)

# Extract projects from docs
extracted_projects = {} # Name -> date_str

# Spring 2022 keywords
spring_2022_patterns = [
    r"spring\s*,?\s*2022",
    r"march\s*,?\s*2022",
    r"april\s*,?\s*2022",
    r"may\s*,?\s*2022",
    r"03/2022", r"04/2022", r"05/2022",
    r"03-2022", r"04-2022", r"05-2022"
]

def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower()
    for pattern in spring_2022_patterns:
        if re.search(pattern, date_str):
            return True
    return False

for doc in civic_docs:
    text = doc['text']
    # Use double backslash for newline in the string passed to python
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    current_project = None
    
    for i, line in enumerate(lines):
        # Heuristic for project name: Next line is "Updates:" or "Project Description:"
        is_header = False
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if "Updates:" in next_line or "Project Description:" in next_line:
                # Check if current line is valid project name
                # Exclude lines that are likely section headers
                if "Capital Improvement Projects" not in line and "Agenda Item" not in line and "Page" not in line:
                    current_project = line
                    is_header = True
        
        if current_project:
            # Look for Start Date
            # "Begin Construction:"
            # Check lower case
            line_lower = line.lower()
            if "begin construction:" in line_lower:
                # Extract value
                parts = line.split("onstruction:", 1)
                if len(parts) > 1:
                    val = parts[1].strip()
                    extracted_projects[current_project] = val

# Now filter for Spring 2022
spring_projects = []
for name, date_str in extracted_projects.items():
    if is_spring_2022(date_str):
        spring_projects.append(name)

# Normalize names for matching
def normalize(name):
    return re.sub(r'\s+', ' ', name).strip().lower()

normalized_spring_projects = {normalize(n): n for n in spring_projects}

# Filter Funding
total_funding = 0
matched_projects_set = set()

for row in funding_data:
    p_name = row['Project_Name']
    p_norm = normalize(p_name)
    
    if p_norm in normalized_spring_projects:
        matched_projects_set.add(p_name)
        total_funding += float(row['Amount'])

print("__RESULT__:")
print(json.dumps({
    "count": len(matched_projects_set),
    "total_funding": total_funding,
    "spring_projects_found": spring_projects,
    "debug_extracted": extracted_projects
}))"""

env_args = {'var_function-call-15062411839169597296': 'file_storage/function-call-15062411839169597296.json', 'var_function-call-15062411839169595261': ['Funding'], 'var_function-call-6642322525338973529': 'file_storage/function-call-6642322525338973529.json', 'var_function-call-6642322525338972320': 'file_storage/function-call-6642322525338972320.json'}

exec(code, env_args)
