code = """import json
import re

# Load funding data
with open('var_function-call-1424370091685766711.json', 'r') as f:
    funding_records = json.load(f)

# Filter funding for > 50,000
high_funding_projects = {}
for r in funding_records:
    try:
        amount = float(r['Amount'])
        if amount > 50000:
            high_funding_projects[r['Project_Name'].strip()] = amount
    except ValueError:
        continue

# Load civic docs
with open('var_function-call-10286396622452696184.json', 'r') as f:
    docs = json.load(f)

capital_design_projects = set()

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        # The text in preview shows: "Capital Improvement Projects (Design)"
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
        
        # Stop if we hit another section
        # The next section in preview is "Capital Improvement Projects (Construction)"
        # Or "Capital Improvement Projects (Not Started)" or "Disaster Recovery Projects"
        if "Capital Improvement Projects (" in line and "Design" not in line:
            in_design_section = False
        if "Disaster Recovery Projects" in line:
            in_design_section = False
            
        if in_design_section:
            # Heuristic to identify project names:
            # - Not a bullet point (special chars are often decoded or represented uniquely)
            # - The preview shows (cid:190) and (cid:131). These might be bullets.
            # - Lines starting with "Page", "Agenda Item", "updates:", "schedule:", etc. are not names.
            
            # Skip bullet points and metadata
            if line.startswith("(cid:") or line.startswith("Page ") or line.startswith("Agenda Item") or \
               line.lower().startswith("prepared by") or line.lower().startswith("approved by") or \
               line.lower().startswith("date prepared") or line.lower().startswith("meeting date") or \
               line.lower().startswith("subject:") or line.lower().startswith("recommended action:") or \
               line.lower().startswith("discussion:"):
                continue
                
            # If line contains "Updates:" or "Schedule:" it's likely part of the details
            if "Updates:" in line or "Schedule:" in line:
                continue
            
            # Assume it's a project name if it looks like a title
            # In the preview: "2022 Morning View Resurfacing & Storm Drain Improvements"
            # It comes before the updates.
            # Also need to handle multi-line names if any, but let's assume single line for now.
            # Sometimes headers appear like "Item 4.B."
            if line.startswith("Item") or line.startswith("To:") or line.startswith("From:"):
                continue
            
            # Specific clean up
            project_name = line.strip()
            # If the line is just a year or very short, might be noise.
            if len(project_name) < 5:
                continue
                
            capital_design_projects.add(project_name)

# Now check intersection
matching_projects = []
for p in capital_design_projects:
    # Try exact match or match with stripped spaces
    if p in high_funding_projects:
        matching_projects.append(p)
    else:
        # The prompt mentions "Project names can be joined...".
        # Sometimes there are minor differences. 
        # But let's check the exact matches first.
        pass

print("__RESULT__:")
print(json.dumps({"matches": matching_projects, "extracted_candidates": list(capital_design_projects)}))"""

env_args = {'var_function-call-1424370091685766711': 'file_storage/function-call-1424370091685766711.json', 'var_function-call-10286396622452696184': 'file_storage/function-call-10286396622452696184.json'}

exec(code, env_args)
