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
    match = re.search(r'(\d{2})(\d{2})(\d{4})', filename)
    if match:
        return datetime.datetime(int(match.group(3)), int(match.group(1)), int(match.group(2)))
    return datetime.datetime.min

# Sort docs by date descending
civic_docs.sort(key=lambda x: extract_date(x['filename']), reverse=True)

# Define regex for headers
# Matches: "Capital Improvement Projects (Design)", "Disaster Recovery Projects (Construction)", etc.
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
        
    status = "not started" # Default if not found? Or "Unknown"? Prompt implies "not started" is a valid status. Let's use "not started" as default or "Unknown".
    # Actually, if I don't find it, I can't confirm it's "not started". But let's assume "Unknown" initially.
    status = "not started" 
    
    found_in_doc = False
    is_relevant_in_text = False
    
    # Normalize project name for search
    norm_project_name = " ".join(project_name.split())
    
    # Search in docs (starting from latest)
    for doc in civic_docs:
        text = doc['text']
        
        # Check if project name exists in text (case insensitive)
        if norm_project_name.lower() in " ".join(text.split()).lower():
            
            # Determine Status by parsing lines
            lines = text.split('\n')
            current_section_status = None
            
            for line in lines:
                # Check for header
                h_match = header_pattern.search(line)
                if h_match:
                    # Capture status from group 2
                    s_str = h_match.group(2).lower()
                    if "design" in s_str: current_section_status = "design"
                    elif "construction" in s_str: current_section_status = "completed" if "completed" in s_str else "completed" if "complete" in s_str else "construction" # Wait, Construction header means "In Construction"? Usually.
                    # The headers are "(Design)", "(Construction)", "(Not Started)".
                    # "Construction" implies "under construction".
                    # "Completed" isn't a header in the preview, but "Construction was completed" is in text.
                    # Wait, looking at preview: "Capital Improvement Projects (Construction)" -> List of active construction projects.
                    # Then there are entries like "Bluffs Park Shade Structure ... Updates: Construction was completed...".
                    # So even under "Construction" section, it might be completed.
                    # But the headers classify them.
                    # Let's map headers to: "design", "construction" (or "in progress"?), "not started".
                    # The prompt says statuses: "design", "completed", "not started".
                    # So "(Construction)" header probably maps to... well, usually "under construction".
                    # But if the text says "completed", it overrides.
                    
                    if "design" in s_str: current_section_status = "design"
                    elif "construction" in s_str: current_section_status = "construction" # Will refine later
                    elif "not started" in s_str: current_section_status = "not started"
                
                # Check if this line contains the project name
                if norm_project_name.lower() in " ".join(line.split()).lower():
                    # Found the project line
                    if current_section_status:
                        status = current_section_status
                    
                    # Check for "completed" in the project description/updates if status is construction?
                    # We need to look ahead in lines until next project/header.
                    # This is complex in a loop.
                    # Let's simple check: if line or next few lines say "Construction was completed" or similar.
                    # We will do a context check.
                    found_in_doc = True
                    
                    # Context check for relevance and completion
                    # Get surrounding text (e.g., this line + 500 chars)
                    # Use full text find
                    start_idx = text.lower().find(project_name.lower())
                    if start_idx == -1:
                        # try fuzzy or simple approach
                        start_idx = text.lower().find(norm_project_name.lower())
                        
                    if start_idx != -1:
                        context = text[start_idx:start_idx+800] # Check 800 chars forward
                        
                        # Check relevance
                        if "fema" in context.lower() or "emergency" in context.lower():
                            is_relevant_in_text = True
                        
                        # Check status override
                        if "construction was completed" in context.lower() or "project was completed" in context.lower() or "notice of completion" in context.lower():
                            status = "completed"
                            
                    break
            
            if found_in_doc:
                break
    
    # If the project wasn't found in docs, but name is relevant, we keep it with status "not started" (or "Unknown").
    # If found, use the found status.
    
    if name_relevant or is_relevant_in_text:
        # Map "construction" to "completed" if needed? No, user said "design", "completed", "not started".
        # If I have "construction", I should probably map it to "design" or "not started" or "completed"?
        # Usually "Construction" is distinct. But if I must match the 3 statuses:
        # "design" (in planning/design phase)
        # "completed" (finished)
        # "not started" (identified but not begun)
        # Where does "under construction" fit? 
        # Maybe the prompt implies "construction" is NOT a target status, or I should output "construction" if valid?
        # The prompt says: 'Projects have three statuses: "design" ..., "completed" ..., and "not started" ...'
        # It doesn't mention "construction" as a status in the description of types, but the preview shows "(Construction)".
        # Wait, if the prompt explicitly lists 3 statuses, I should try to map to them.
        # But "under construction" is definitely not "design" (planning) nor "not started". Is it "completed"? No.
        # Maybe I should just output "construction" if that's what it is. The prompt list might be non-exhaustive or referring to specific categories.
        # Let's keep "construction" if that's what I found, or maybe map to "design" if interpreted as "in progress"? 
        # No, "design" is "planning/design phase". Construction is execution.
        # I will output the status I found (e.g. "construction"). If strict adherence is required:
        # Maybe "design" covers "in progress"? Unlikely.
        # I'll stick to what I extract, but prioritize "completed" if completion text found.
        
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
