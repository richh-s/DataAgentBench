code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding Data
funding_path = locals()['var_function-call-12717263916929775114']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Civic Docs
civic_path = locals()['var_function-call-12717263916929775677']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = "\n".join([d['text'] for d in civic_docs])

# Define keywords
keywords = ['emergency', 'fema', 'disaster', 'fire']

# Function to extract projects from text
def extract_projects(text):
    lines = text.split('\n')
    projects = []
    
    current_section = "Unknown"
    
    # regex for section headers
    # "Capital Improvement Projects (Design)"
    # "Capital Improvement Projects (Construction)"
    # "Capital Improvement Projects (Not Started)"
    
    section_map = {
        "Design": "design",
        "Construction": "construction",
        "Not Started": "not started"
    }
    
    # We need to iterate and maintain context
    # Use specific markers
    
    # Identify project blocks:
    # Look for line i containing "(cid:190) Updates:" or "(cid:190) Project Description:"
    # line i-1 (stripping whitespace) is the Project Name.
    # Note: Sometimes there are empty lines. Go back to first non-empty.
    
    # Also track sections.
    
    # Store line indices of project starts
    project_indices = []
    for i, line in enumerate(lines):
        if "(cid:190) Updates:" in line or "(cid:190) Project Description:" in line:
            # Find name
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                name = lines[j].strip()
                # Check if this name line is actually part of the marker or something else?
                # Usually it's the name.
                project_indices.append({'name': name, 'start_line': j, 'marker_line': i})
    
    # Sort by line index
    project_indices.sort(key=lambda x: x['start_line'])
    
    # Now iterate through projects and capture text until next project
    for k in range(len(project_indices)):
        p = project_indices[k]
        start = p['start_line']
        end = project_indices[k+1]['start_line'] if k < len(project_indices) - 1 else len(lines)
        
        # Extract block
        block_lines = lines[start:end]
        block_text = "\n".join(block_lines)
        
        # Determine section/status
        # Scan backwards from start for section header
        status = "unknown"
        # We can look at the lines before 'start'
        # To be efficient, let's just search the whole text for headers and their positions?
        # Better: iterate lines and update current_section.
        
        projects.append({
            'name': p['name'],
            'block': block_text,
            'status_context': 'unknown', # Will fill next
            'line_idx': start
        })

    # Determine status for each project based on headers
    # Headers: "Capital Improvement Projects (Design)", etc.
    header_indices = []
    for section_name, status_code in section_map.items():
        # Find all occurrences
        pattern = re.escape(f"Capital Improvement Projects ({section_name})")
        for match in re.finditer(pattern, text, re.IGNORECASE):
            # Map character index to line index?
            # Easier: Search in list of lines?
            pass
            
    # Let's iterate lines again to assign status to projects
    current_status = "unknown"
    p_idx = 0
    
    for i, line in enumerate(lines):
        # Check for headers
        lower_line = line.lower()
        if "capital improvement projects (design)" in lower_line:
            current_status = "design"
        elif "capital improvement projects (construction)" in lower_line:
            current_status = "construction"
        elif "capital improvement projects (not started)" in lower_line:
            current_status = "not started"
            
        # Check if we are at a project start
        if p_idx < len(projects) and projects[p_idx]['line_idx'] == i:
            projects[p_idx]['status_context'] = current_status
            p_idx += 1
            
    return projects

extracted_projects = extract_projects(full_text)

# Match with Funding and Filter
results = []
df_funding['Project_Name_Clean'] = df_funding['Project_Name'].astype(str).str.replace(r'\s*\(.*?\)\s*', '', regex=True).str.strip().str.lower()

for p in extracted_projects:
    p_name = p['name']
    p_text = p['block'].lower()
    p_status = p['status_context']
    
    # Check "Completed" in text
    if "construction was completed" in p_text:
        p_status = "completed"
    
    # Check relevance
    is_related = False
    
    # Check keywords in text or name
    for kw in keywords:
        if kw in p_name.lower() or kw in p_text:
            is_related = True
            break
            
    # Also matches against funding to see if funding has keywords?
    # Let's find funding matches first
    
    # Matching Logic:
    # Normalized name match
    p_name_clean = re.sub(r'\s*\(.*?\)\s*', '', p_name).strip().lower()
    
    # Find in funding df
    # Exact clean match
    matches = df_funding[df_funding['Project_Name_Clean'] == p_name_clean]
    
    # If no match, try string containment (fuzzy)
    if matches.empty:
        # Try if p_name_clean is in funding name or vice versa
        # This can be slow, but n is small
        matches = df_funding[df_funding['Project_Name_Clean'].apply(lambda x: x == p_name_clean or x in p_name_clean or p_name_clean in x)]
        
    if matches.empty:
        # If relevant by text but no funding, we might skip or include with None?
        # Query asks for "funding sources, amounts". If none, maybe exclude.
        # But let's assume we need funding info.
        funding_records = []
    else:
        funding_records = matches.to_dict('records')
        
    # Check if ANY funding record name has keywords (e.g. "(FEMA Project)")
    # Or if text has keywords
    
    if not is_related:
        # Check funding names
        for rec in funding_records:
            if any(kw in rec['Project_Name'].lower() for kw in keywords):
                is_related = True
                break
                
    if is_related and funding_records:
        for rec in funding_records:
            results.append({
                "Project_Name": rec['Project_Name'], # Use Funding Name for precision
                "Funding_Source": rec['Funding_Source'],
                "Amount": rec['Amount'],
                "Status": p_status
            })
            
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7885629070765766098': ['civic_docs'], 'var_function-call-7885629070765766627': ['Funding'], 'var_function-call-7885629070765767156': 'file_storage/function-call-7885629070765767156.json', 'var_function-call-7885629070765767685': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-12717263916929775114': 'file_storage/function-call-12717263916929775114.json', 'var_function-call-12717263916929775677': 'file_storage/function-call-12717263916929775677.json'}

exec(code, env_args)
