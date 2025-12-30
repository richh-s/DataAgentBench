code = """import json
import re

# Load data
with open(locals()['var_function-call-6642322525338972320'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6642322525338973529'], 'r') as f:
    funding_data = json.load(f)

# Extract projects from docs
projects = []

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

extracted_projects = {} # Name -> {start_date, ...}

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    current_project = None
    
    for i, line in enumerate(lines):
        # Heuristic for project name: Next line is "Updates:" or "Project Description:"
        # The line itself should not be "Capital Improvement Projects..."
        
        is_header = False
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if "Updates:" in next_line or "Project Description:" in next_line:
                # Check if current line is valid project name
                if "Capital Improvement Projects" not in line and "Agenda Item" not in line:
                    current_project = line
                    is_header = True
        
        if current_project:
            # Look for Start Date
            # "Begin Construction:"
            if "Begin Construction:" in line or "Begin construction:" in line:
                # Extract value
                parts = line.split("onstruction:", 1)
                if len(parts) > 1:
                    val = parts[1].strip()
                    # Store
                    extracted_projects[current_project] = val

# Now filter for Spring 2022
spring_projects = []
for name, date_str in extracted_projects.items():
    if is_spring_2022(date_str):
        spring_projects.append(name)

# Helper to normalize names for matching
def normalize(name):
    return re.sub(r'\s+', ' ', name).strip().lower()

normalized_spring_projects = {normalize(n): n for n in spring_projects}

# Filter Funding
# Funding table has Project_Name. Join.
# Need to be careful about matching. Exact string match might fail due to minor diffs.
# But prompt says "matches the project names that can be extracted". Let's try exact or normalized match.

total_funding = 0
count = 0
matched_projects = []

for row in funding_data:
    p_name = row['Project_Name']
    p_norm = normalize(p_name)
    
    if p_norm in normalized_spring_projects:
        matched_projects.append(p_name)
        total_funding += float(row['Amount'])

# Deduplicate matched projects?
# The question asks "How many projects...". If a project has multiple funding sources, it appears multiple times in Funding table.
# Usually "How many projects" implies counting distinct projects.
# "Total funding" sums all funding.

unique_projects = set(matched_projects)

print("__RESULT__:")
print(json.dumps({
    "count": len(unique_projects),
    "total_funding": total_funding,
    "spring_projects_found": list(normalized_spring_projects.values()),
    "matched_projects_funding": matched_projects
}))"""

env_args = {'var_function-call-15062411839169597296': 'file_storage/function-call-15062411839169597296.json', 'var_function-call-15062411839169595261': ['Funding'], 'var_function-call-6642322525338973529': 'file_storage/function-call-6642322525338973529.json', 'var_function-call-6642322525338972320': 'file_storage/function-call-6642322525338972320.json'}

exec(code, env_args)
