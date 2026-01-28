code = """import json

# Load funding data
with open('var_function-call-396539203064907425', 'r') as f:
    funding_data = json.load(f)

# Extract project names with amount > 50000
# The SQL query "SELECT Project_Name, Amount FROM Funding WHERE Amount > 50000" was used.
funded_projects = {item['Project_Name'].strip() for item in funding_data}

# Load civic docs
with open('var_function-call-13579578021652581201', 'r') as f:
    docs = json.load(f)

design_capital_projects = set()

for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    
    in_design_section = False
    
    for line in lines:
        line_stripped = line.strip()
        
        if not line_stripped:
            continue
        
        # Check for section headers
        # Use simple string matching. The sample shows exact headers.
        if line_stripped == "Capital Improvement Projects (Design)":
            in_design_section = True
            continue
        
        if in_design_section:
            # Check for end of section
            if "Capital Improvement Projects (Construction)" in line_stripped or \
               "Capital Improvement Projects (Not Started)" in line_stripped or \
               "Disaster Recovery Projects" in line_stripped:
                in_design_section = False
                continue
            
            # Skip known non-project lines
            # Bullet points in PDF extraction often show as (cid:190) or (cid:131)
            if line_stripped.startswith("(cid:") or \
               line_stripped.startswith("Updates:") or \
               line_stripped.startswith("Project Schedule:") or \
               line_stripped.startswith("Estimated Schedule:") or \
               line_stripped.startswith("Complete Design:") or \
               line_stripped.startswith("Advertise:") or \
               line_stripped.startswith("Begin Construction:") or \
               line_stripped.startswith("Final Design:") or \
               line_stripped.startswith("Page") or \
               line_stripped.startswith("Agenda Item") or \
               line_stripped.startswith("To:") or \
               line_stripped.startswith("Prepared by:") or \
               line_stripped.startswith("Approved by:") or \
               line_stripped.startswith("Subject:") or \
               line_stripped.startswith("RECOMMENDED ACTION:") or \
               line_stripped.startswith("DISCUSSION:") or \
               line_stripped.startswith("Date prepared:") or \
               line_stripped.startswith("Meeting date:"):
                continue
            
            # Heuristic: Project names in this list are usually Title Case or start with Year
            # "2022 Morning View..."
            # "PCH Median..."
            # Filter out random short strings or noise?
            if len(line_stripped) < 5:
                continue
            
            # Assume it's a project name
            design_capital_projects.add(line_stripped)

# Find intersection
matching_projects = design_capital_projects.intersection(funded_projects)

print("__RESULT__:")
print(json.dumps(len(matching_projects)))"""

env_args = {'var_function-call-396539203064907425': 'file_storage/function-call-396539203064907425.json', 'var_function-call-396539203064906594': 'file_storage/function-call-396539203064906594.json', 'var_function-call-13579578021652581201': 'file_storage/function-call-13579578021652581201.json'}

exec(code, env_args)
