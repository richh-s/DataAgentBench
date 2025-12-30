code = """import json
import pandas as pd

# Load funding data
funding_path = locals()['var_function-call-12949068118131678804']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
# Convert Amount to int
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Create a lookup dict {Project_Name: Amount}. Handle duplicates by summing if any (though unlikely for same name).
funding_lookup = funding_df.groupby('Project_Name')['Amount'].sum().to_dict()

# Load civic docs
docs_path = locals()['var_function-call-12949068118131677021']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Helper to categorize and parse
disaster_keywords = ['fema', 'caloes', 'woolsey', 'disaster', 'fire', 'emergency']
results = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = "Unknown"
    current_project = None
    project_buffer = [] # Store lines for current project to parse details later
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for Headers
        # Headers in preview: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", etc.
        # Also maybe "Disaster Recovery Projects"
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            current_section = line
            # Reset current project
            if current_project:
                results.append({'name': current_project, 'section': current_section_saved, 'text': "\n".join(project_buffer)})
                current_project = None
                project_buffer = []
            current_section_saved = current_section
            continue
            
        # Identify Project Name
        # Logic: If line is followed by "(cid:190) Updates:" or similar indicator, it's a project name.
        # Or if it matches a name in funding_lookup.
        
        # Look ahead for "Updates:"
        is_new_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if "Updates:" in next_line or "Project Description:" in next_line:
                is_new_project = True
        
        if is_new_project:
            # Save previous project
            if current_project:
                results.append({'name': current_project, 'section': current_section_saved, 'text': "\n".join(project_buffer)})
            
            current_project = line
            project_buffer = []
            # Use current_section_saved from when the section started
            # But wait, current_section matches the *current* line's section. 
            # If I just hit a header, current_section matches that.
            # If I haven't hit a header yet, it's Unknown.
        else:
            if current_project:
                project_buffer.append(line)

    # Add last project
    if current_project:
        results.append({'name': current_project, 'section': current_section, 'text': "\n".join(project_buffer)})

print(f"__RESULT__:")
print(json.dumps(results[:5])) # Print preview of extracted projects"""

env_args = {'var_function-call-12949068118131678804': 'file_storage/function-call-12949068118131678804.json', 'var_function-call-12949068118131677021': 'file_storage/function-call-12949068118131677021.json'}

exec(code, env_args)
