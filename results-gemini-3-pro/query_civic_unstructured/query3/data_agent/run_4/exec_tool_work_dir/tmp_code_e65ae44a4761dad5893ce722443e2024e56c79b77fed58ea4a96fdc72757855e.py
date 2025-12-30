code = """import json
import pandas as pd
import re
import datetime

# Load Funding Data
with open(locals()['var_function-call-17289363314070391295'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-14887521830663367550'], 'r') as f:
    civic_docs = json.load(f)

# Helper to extract date from filename
def extract_date(filename):
    # format: malibucity_agenda_03222023-2060.txt -> 03-22-2023
    # pattern: \d{8} or \d{2}\d{2}\d{4}
    match = re.search(r'(\d{2})(\d{2})(\d{4})', filename)
    if match:
        return datetime.datetime(int(match.group(3)), int(match.group(1)), int(match.group(2)))
    return datetime.datetime.min

# Sort docs by date descending
civic_docs.sort(key=lambda x: extract_date(x['filename']), reverse=True)

# Define regex for headers
# Headers seen in preview: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"
# Maybe "Disaster Recovery Projects" too?
header_pattern = re.compile(r'(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started|Completed)\)', re.IGNORECASE)

relevant_projects = []

for index, row in funding_df.iterrows():
    project_name = row['Project_Name']
    funding_source = row['Funding_Source']
    amount = row['Amount']
    
    # Check relevance by name
    name_relevant = False
    if 'FEMA' in project_name.upper() or 'EMERGENCY' in project_name.upper():
        name_relevant = True
        
    status = "Unknown"
    is_relevant_in_text = False
    
    # Normalize project name for search
    norm_project_name = " ".join(project_name.split())
    
    # Search in docs (starting from latest)
    for doc in civic_docs:
        text = doc['text']
        # Normalize text slightly? removing excessive newlines might help matching, but sections rely on structure.
        # Let's keep structure but handle finding the project name.
        
        if norm_project_name.lower() in " ".join(text.split()).lower():
            # Found the project in this doc
            
            # 1. Determine Status
            # Find all header matches
            matches = list(header_pattern.finditer(text))
            
            # Find the position of the project name
            # We use a normalized version of text for finding index? No, need original indices.
            # Simple approach: Search in original text (assuming exact spacing match or close enough)
            # If not exact match, try ignoring whitespace.
            
            # Let's try to find the start index of the project name in the text
            # This is tricky if whitespace differs.
            # Strategy: Split text into lines. Check if project name is in a line.
            
            lines = text.split('\n')
            current_status = "Unknown"
            
            # Iterate lines to find headers and project
            found_in_doc = False
            for line in lines:
                # Check for header
                h_match = header_pattern.search(line)
                if h_match:
                    # e.g. "Capital Improvement Projects (Design)" -> group 2 is "Design"
                    current_status = h_match.group(2).lower()
                    # map to standardized status
                    if "design" in current_status: current_status = "design"
                    elif "construction" in current_status: current_status = "construction"
                    elif "not started" in current_status: current_status = "not started"
                    elif "completed" in current_status: current_status = "completed"
                
                # Check for project name
                # normalize line and project name
                if norm_project_name.lower() in " ".join(line.split()).lower():
                    # Found project under current_status
                    status = current_status
                    found_in_doc = True
                    
                    # Check for relevance in this block/line or general context?
                    # The query implies finding projects "related to".
                    # If I found it here, let's look at the surrounding text for keywords?
                    # Or just simpler: if "FEMA" or "Emergency" is in the name, it's relevant.
                    # If not, scan the whole text of this update for "FEMA"/"Emergency"? 
                    # The text for a project continues until the next project name or header.
                    # This is hard to parse perfectly without more logic.
                    
                    # Heuristic: Check the line itself and maybe subsequent lines until empty line?
                    # Let's just check the whole doc text for keywords if we are unsure? No, that's too broad.
                    # Let's check if "FEMA" or "Emergency" appears in the `text` of the document *near* the project name?
                    # Simpler: The user provided HINT: "topic field contains...".
                    # If we can't parse topic, we search for keywords in the project name or check if the project is a "Disaster Recovery Project" (which implies Emergency/FEMA).
                    
                    # If header was "Disaster Recovery Projects...", then it's relevant.
                    if h_match and "Disaster" in h_match.group(1):
                        is_relevant_in_text = True
                    
                    # Also check keywords in the line
                    if "fema" in line.lower() or "emergency" in line.lower():
                        is_relevant_in_text = True
                        
                    break # Found the project in the latest doc
            
            if found_in_doc:
                # Check keywords in the whole text if not yet relevant? 
                # No, that risks false positives. 
                # Let's rely on:
                # 1. Name match
                # 2. Status header containing "Disaster" (if valid)
                # 3. Keywords in the line containing project name.
                
                # If still not relevant, maybe check strict proximity?
                # For now, let's assume if name doesn't match and line doesn't match, we rely on Name check.
                # But wait, "projects related to 'emergency' or 'FEMA'".
                # If the description *below* the name mentions FEMA, I should count it.
                # Parsing the description block:
                # Starts at project name line, ends at next project name line or double newline?
                # Let's try to grab a window of text (e.g., 500 chars) after the name.
                
                start_idx = text.lower().find(project_name.lower())
                if start_idx == -1:
                     # Try normalized
                     start_idx = (" ".join(text.split()).lower()).find(norm_project_name.lower())
                     # If we matched in normalized, we can't easily index into original.
                     # Skip context check if exact match fails, fallback to name/line check.
                     pass
                else:
                    context = text[start_idx:start_idx+1000]
                    if "fema" in context.lower() or "emergency" in context.lower():
                        is_relevant_in_text = True
                
                break # Stop searching docs, we found the latest status.

    if name_relevant or is_relevant_in_text:
        relevant_projects.append({
            "Project_Name": project_name,
            "Funding_Source": funding_source,
            "Amount": amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(relevant_projects))"""

env_args = {'var_function-call-14887521830663364851': ['civic_docs'], 'var_function-call-14887521830663367550': 'file_storage/function-call-14887521830663367550.json', 'var_function-call-17289363314070391640': ['Funding'], 'var_function-call-17289363314070391295': 'file_storage/function-call-17289363314070391295.json'}

exec(code, env_args)
