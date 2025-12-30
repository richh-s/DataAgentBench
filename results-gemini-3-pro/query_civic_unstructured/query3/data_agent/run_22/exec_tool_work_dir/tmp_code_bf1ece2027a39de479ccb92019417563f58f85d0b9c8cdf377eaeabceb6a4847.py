code = """import json
import pandas as pd

with open(locals()['var_function-call-4228173855339130551'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-4228173855339128632'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
# Ensure clean names
funding_df['Project_Name'] = funding_df['Project_Name'].str.strip()

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Identify sections
    # We look for lines containing "Capital Improvement Projects (" or "Disaster Recovery Projects ("
    lines = text.split('\n')
    sections = []
    current_status = None
    section_start_line = 0
    
    # Simple state machine to identify sections
    for i, line in enumerate(lines):
        line = line.strip()
        if ("Capital Improvement Projects (" in line or "Disaster Recovery Projects (" in line) and line.endswith(")"):
            # New section
            # Extract status from parens
            # e.g. "Capital Improvement Projects (Design)" -> "Design"
            start_paren = line.rfind('(')
            end_paren = line.rfind(')')
            if start_paren != -1 and end_paren != -1:
                status = line[start_paren+1:end_paren].lower()
                sections.append({'status': status, 'start_line': i})
    
    # Process each section
    for idx, section in enumerate(sections):
        status = section['status']
        start = section['start_line'] + 1
        end = sections[idx+1]['start_line'] if idx + 1 < len(sections) else len(lines)
        
        # Get lines for this section
        section_lines = lines[start:end]
        section_text = "\n".join(section_lines)
        
        # Split by (cid:190)
        # Note: (cid:190) might be attached to text or space
        # We replace (cid:190) with a unique marker to split safely
        token = "||SPLIT_TOKEN||"
        section_text_clean = section_text.replace("(cid:190)", token)
        
        parts = section_text_clean.split(token)
        
        # parts[0] contains the first project name at the end
        # parts[1] contains details for first project, and potentially next name at end
        
        for p_idx in range(1, len(parts)):
            # The name of this project is at the end of parts[p_idx-1]
            prev_part = parts[p_idx-1]
            current_part = parts[p_idx]
            
            # Extract Name
            # The prev_part ends with the name. 
            # We split prev_part by newlines and take the last non-empty line
            prev_lines = [l.strip() for l in prev_part.split('\n') if l.strip()]
            if not prev_lines:
                continue
            project_name = prev_lines[-1]
            
            # Extract Body
            # The current_part starts with "Updates:" or "Project Description:" and contains the body.
            # It also contains the NEXT project name at the end, but we don't care about the next name for the current body 
            # (except to exclude it? No, the next name is part of the next iteration's prev_part).
            # Wait, if current_part has the next name at the end, that next name is part of the body text we extract?
            # Yes. We should try to exclude it if possible.
            # But "emergency" keyword might be in the description, not the name.
            # If the next name is appended, it might trigger a false positive if the next name has "emergency".
            # However, typically names are short.
            # Let's assume the body is the main text.
            
            project_text = current_part
            
            # Check for Status Override in text
            final_status = status
            if "Construction was completed" in project_text:
                final_status = "completed"
            
            # Check keywords
            combined = (project_name + " " + project_text).lower()
            if "emergency" in combined or "fema" in combined:
                extracted_projects.append({
                    "Project_Name": project_name,
                    "status": final_status
                })

# Deduplicate extracted projects if needed (same project in multiple docs?)
# Assuming one doc for now based on sample.

extracted_df = pd.DataFrame(extracted_projects)

if not extracted_df.empty:
    # Clean names
    extracted_df['Project_Name'] = extracted_df['Project_Name'].str.strip()
    
    # Merge with Funding
    # We do an inner join? Or Left join? 
    # Query asks for "project names, funding sources, amounts, and statuses".
    # This implies we need funding info. So inner join with funding table.
    
    merged = pd.merge(extracted_df, funding_df, on='Project_Name', how='inner')
    
    # Select columns
    result = merged[['Project_Name', 'Funding_Source', 'Amount', 'status']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9734910196601830303': 'file_storage/function-call-9734910196601830303.json', 'var_function-call-9734910196601828350': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-4228173855339130551': 'file_storage/function-call-4228173855339130551.json', 'var_function-call-4228173855339128632': 'file_storage/function-call-4228173855339128632.json'}

exec(code, env_args)
