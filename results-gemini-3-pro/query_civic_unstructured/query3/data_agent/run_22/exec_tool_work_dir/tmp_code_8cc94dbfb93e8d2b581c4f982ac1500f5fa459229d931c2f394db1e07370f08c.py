code = """import json
import pandas as pd
import re

# Load the data
with open(locals()['var_function-call-4228173855339130551'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-4228173855339128632'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Split text into sections based on headers like "Capital Improvement Projects (Design)"
    # We use a regex to find these headers and their positions
    # Pattern: Newline, Title, (Status)
    # The sample shows: "Capital Improvement Projects (Design)"
    
    # We'll normalize the text first to handle different newline chars if any, but regex handles \n
    
    # Find all matches of sections
    # Regex explanation:
    # \n? -> optional newline
    # (Capital Improvement Projects|Disaster Recovery Projects) -> Group 1: Type
    # \s+ -> whitespace
    # \((.*?)\) -> Group 2: Status (e.g. Design, Construction, Not Started)
    section_pattern = re.compile(r"(Capital Improvement Projects|Disaster Recovery Projects)\s*\((.*?)\)", re.IGNORECASE)
    
    matches = list(section_pattern.finditer(text))
    
    for i, match in enumerate(matches):
        p_type = match.group(1)
        p_status_header = match.group(2)
        
        start_idx = match.end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(text)
        
        section_text = text[start_idx:end_idx]
        
        # Now find projects within this section
        # Projects seem to be identified by a line (Project Name) followed by updates starting with (cid:190)
        # Regex:
        # \n(?P<name>[^\n]+)\n+\(cid:190\)\s*(Updates|Project Description)
        # Note: The name is captured.
        
        # We need to iterate through the section text to find these blocks
        # Let's verify the marker (cid:190). In the JSON string it might be unicode or escaped.
        # The preview shows "(cid:190)".
        
        # Let's split by the project name pattern
        # Be careful not to miss the first one if it doesn't start with \n (though usually does)
        
        # We can iterate by finding the marker "(cid:190)" and looking backwards for the name
        
        # Pattern:
        # (.*?)\n+\(cid:190\)
        # The group 1 would contain the name, but might also contain previous text.
        # However, names are usually on their own line.
        
        # Strategy: Find all occurrences of "(cid:190)" (which is a bullet point, likely unicode U+00BE if decoded, but here it seems to be the literal string "(cid:190)" in the preview text? 
        # Wait, the preview says `(cid:190)`. If it's a PDF extraction, cid:190 is a font mapping. 
        # Let's assume the string literal "(cid:190)" is in the text.
        
        # Split section_text by "\n(cid:190)" to find project blocks?
        # No, that splits inside a project (between updates and schedule).
        # We need to find the START of a project.
        # The start is the Name line.
        # The Name line is followed by `(cid:190) Updates:` or `(cid:190) Project Description:`
        
        proj_pattern = re.compile(r"\n\s*([^\n]+)\s*\n+\s*\(cid:190\)\s*(Updates|Project Description)", re.MULTILINE)
        
        project_matches = list(proj_pattern.finditer(section_text))
        
        for j, p_match in enumerate(project_matches):
            p_name = p_match.group(1).strip()
            
            p_start = p_match.start()
            p_end = project_matches[j+1].start() if j + 1 < len(project_matches) else len(section_text)
            
            p_text = section_text[p_start:p_end]
            
            # Determine Status
            # Default to header status
            status = p_status_header.lower()
            
            # Check for specific status overrides in text
            if "Construction was completed" in p_text:
                status = "completed"
            elif "Project is currently under construction" in p_text and status == "construction":
                # Keep as construction or map to hint?
                # Hint: "design", "completed", "not started".
                # If the user wants specific statuses, I should probably stick to the hint categories if possible.
                # But "under construction" is neither "design" nor "completed" nor "not started".
                # It's "active". The hint says: "Projects have three statuses: 'design' (in planning/design phase), 'completed' (finished), and 'not started'".
                # This implies "Construction" phase might be grouped under "design" (active) or maybe the hint is incomplete.
                # However, usually "Capital Improvement Projects (Construction)" implies active construction.
                # I'll just use the status I have (e.g. "construction") or map it if I can confirm.
                # Given I have to return "statuses", returning "Construction" is likely more accurate than "Design".
                # But to follow the hint strictly... maybe I should leave it as "construction" and let the user decide.
                pass
            
            # Check for keywords
            # Keywords: 'emergency' or 'FEMA'
            # Case insensitive
            combined_text = (p_name + " " + p_text).lower()
            if "emergency" in combined_text or "fema" in combined_text:
                extracted_projects.append({
                    "Project_Name": p_name,
                    "status": status,
                    "extracted_topic": "emergency/FEMA", # Placeholder
                    "raw_text": p_text # for debugging if needed
                })

# Convert to DataFrame
extracted_df = pd.DataFrame(extracted_projects)

# Join with Funding
# We need to match Project_Name.
# Let's do a merge.
# Strip whitespace from names in both.
if not extracted_df.empty:
    extracted_df['Project_Name'] = extracted_df['Project_Name'].str.strip()
    funding_df['Project_Name'] = funding_df['Project_Name'].str.strip()
    
    # Left join to extracted to keep the found projects
    result_df = pd.merge(extracted_df, funding_df, on="Project_Name", how="inner")
    
    final_result = result_df[['Project_Name', 'Funding_Source', 'Amount', 'status']].to_dict(orient='records')
else:
    final_result = []

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-9734910196601830303': 'file_storage/function-call-9734910196601830303.json', 'var_function-call-9734910196601828350': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-4228173855339130551': 'file_storage/function-call-4228173855339130551.json', 'var_function-call-4228173855339128632': 'file_storage/function-call-4228173855339128632.json'}

exec(code, env_args)
