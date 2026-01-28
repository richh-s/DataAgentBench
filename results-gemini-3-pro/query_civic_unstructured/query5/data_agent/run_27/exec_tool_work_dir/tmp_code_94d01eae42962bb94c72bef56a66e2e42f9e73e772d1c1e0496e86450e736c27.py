code = """import json
import pandas as pd
import re

# Load Funding Data
funding_path = locals()['var_function-call-9396770381544518491']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load Civic Docs
docs_path = locals()['var_function-call-9396770381544517930']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

extracted_projects = []

for doc in docs_data:
    text = doc['text']
    # Split text into lines
    lines = text.split('\n')
    
    current_project = None
    current_info = {}
    
    # Heuristic: Project names are often lines before "(cid:190) Updates:"
    # Or we can split by double newline blocks and look for patterns.
    # Let's iterate through lines to find project starts.
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check for project start signal
        # Based on preview: "Project Name" then next lines contain "(cid:190) Updates:"
        # Sometimes there's a blank line or two.
        
        if "(cid:190) Updates:" in line or "Updates:" in line:
            # The project name should be in the previous lines.
            # Look backwards for a non-empty line that looks like a title.
            # Titles are usually not "Capital Improvement Projects (Design)" which are headers.
            
            # Simple backtrack
            j = i - 1
            while j >= 0:
                prev_line = lines[j].strip()
                if prev_line and "Capital Improvement Projects" not in prev_line and "Page " not in prev_line:
                    # Potential project name
                    # Sometimes project name is split on two lines? 
                    # Let's assume one line for now or take the last non-empty line.
                    project_name = prev_line
                    
                    # Verify it's not a header
                    if "Status Report" in project_name or "Subject:" in project_name:
                        j -= 1
                        continue
                        
                    # Initialize new project found
                    # But first, save previous if exists
                    if current_project:
                        extracted_projects.append(current_info)
                    
                    current_project = project_name
                    current_info = {
                        "Project_Name": project_name,
                        "text_block": "",
                        "type": "unknown",
                        "dates": []
                    }
                    break
                j -= 1
        
        if current_project:
            current_info["text_block"] += line + "\n"
            
            # Extract dates
            # Look for "Begin Construction: <Date>"
            # Look for "Advertise: <Date>"
            # Look for "Start: <Date>"
            
            # Regex for date extraction (simple year/season)
            date_match = re.search(r'(Begin Construction|Advertise|Start Date)[:\s]+([A-Za-z0-9,\s]+)', line, re.IGNORECASE)
            if date_match:
                date_type = date_match.group(1)
                date_val = date_match.group(2).strip()
                current_info["dates"].append((date_type, date_val))

    # Append last
    if current_project:
        extracted_projects.append(current_info)

# Process extracted projects to identify 2022 starters and disaster types
final_list = []
for p in extracted_projects:
    name = p['Project_Name']
    text = p['text_block']
    dates = p['dates']
    
    # Determine Type
    is_disaster = False
    if "FEMA" in name or "CalOES" in name or "Disaster" in name:
        is_disaster = True
    # Check text keywords
    if "FEMA" in text or "CalOES" in text or "Woolsey" in text or "disaster" in text.lower():
        # "FEMA" in text is a strong indicator, but let's be careful.
        # The prompt says "Disaster project names often include suffixes...".
        # Let's rely on name/suffix primarily, or explicit "Disaster" keywords in description.
        # Let's stick to name checks first, and maybe refine if count is low.
        pass

    # Determine Start Date
    started_2022 = False
    start_date_str = ""
    
    # Check explicitly extracted dates
    for dtype, dval in dates:
        if "2022" in dval:
            # Check if it's a "Begin" or "Advertise"
            if "Begin Construction" in dtype or "Advertise" in dtype:
                started_2022 = True
                start_date_str = dval
                break
    
    # If no explicit "Project Schedule" date found, check "Updates" text for "began" or similar?
    # The preview showed "Construction was completed November 2022". This implies start < 2022.
    # So we strictly look for "Begin ... 2022".
    
    final_list.append({
        "extracted_name": name,
        "is_disaster": is_disaster,
        "started_2022": started_2022,
        "dates": dates,
        "raw_text_preview": text[:200]
    })

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-9396770381544518491': 'file_storage/function-call-9396770381544518491.json', 'var_function-call-9396770381544517930': 'file_storage/function-call-9396770381544517930.json'}

exec(code, env_args)
