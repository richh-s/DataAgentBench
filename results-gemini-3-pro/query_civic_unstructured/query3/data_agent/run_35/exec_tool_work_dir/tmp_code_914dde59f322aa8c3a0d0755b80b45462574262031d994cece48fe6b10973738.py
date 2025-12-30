code = """import json
import sqlite3
import re
import pandas as pd

# Load Funding Data
# The funding data is in a file, but I can query it directly using pandas if I had the connection, 
# but I have the result in a file from previous turn. 
# Wait, I have the result of `SELECT * FROM Funding` in `var_function-call-7750960758477245626`.
# I should read that file.

with open('var_function-call-7750960758477245626.json', 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Load Civic Docs
# The result is in `var_function-call-3106554336237263291.json`.
with open('var_function-call-3106554336237263291.json', 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

# Define keywords for topic extraction
keywords_list = ["park", "road", "FEMA", "fire", "emergency", "warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]

for doc in civic_docs:
    text = doc['text']
    
    # Identify Sections
    # We split by the known headers.
    # Note: Regex split might be easier.
    
    # Normalize text newlines
    text = text.replace('\r\n', '\n')
    
    # Regex to find sections. 
    # Sections start with "Capital Improvement Projects (Design)" etc.
    # The text before the first section is intro.
    
    sections = re.split(r'(Capital Improvement Projects \((?:Design|Construction|Not Started)\))', text)
    
    current_status = None
    
    # specific handling because split returns [preamble, header1, body1, header2, body2...]
    for i in range(len(sections)):
        part = sections[i].strip()
        if "Capital Improvement Projects" in part:
            if "(Design)" in part:
                current_status = "design"
            elif "(Construction)" in part:
                current_status = "construction" # Will refine later
            elif "(Not Started)" in part:
                current_status = "not started"
        else:
            if current_status:
                # This part is the body of the section
                # Split into projects
                # Projects seem to be separated by project names which are followed by `(cid:190)` bullet points.
                # A good split might be lookahead for `\n\n.+?\n\n\(cid:190\)`.
                # But project names might not have double newlines.
                # Let's try splitting by the pattern that marks the START of a project block.
                # The start of a block is the Project Name. The Project Name is followed by `(cid:190)`.
                # So we can split by `\n(?=[^\n]+\n\(cid:190\))`.
                
                # Let's find all project starts
                # Pattern: A line of text (Project Name), followed immediately by a line starting with `(cid:190)`.
                # Note: The text in preview shows `(cid:190)` as literal characters.
                
                project_blocks = re.split(r'\n(?=.*\n\(cid:190\))', part)
                
                for block in project_blocks:
                    block = block.strip()
                    if not block:
                        continue
                        
                    # Extract Name
                    lines = block.split('\n')
                    # The first line should be the name (if we split correctly)
                    # However, split might leave some trailing newlines or the name might be the last line of previous chunk?
                    # No, regex split `(?=...)` keeps the delimiter.
                    # So the block starts with the Name.
                    
                    project_name = lines[0].strip()
                    if not project_name:
                         if len(lines) > 1: project_name = lines[1].strip()
                    
                    # Clean up project name (sometimes page numbers or garbage might be there?)
                    # The preview shows clear names.
                    
                    # Extract Text for topic/status analysis
                    project_text = block
                    
                    # Refine Status
                    status = current_status
                    if status == "construction":
                        if "Construction was completed" in project_text or "Notice of completion" in project_text:
                            status = "completed"
                    
                    # Determine Topic
                    topics = []
                    # check for keywords in name and text
                    content_to_search = (project_name + " " + project_text).lower()
                    
                    for kw in keywords_list:
                        if kw.lower() in content_to_search:
                            topics.append(kw)
                    
                    # Check for "FEMA" specifically case-sensitive? No, "FEMA" is in keywords list.
                    
                    # Check for emergency/FEMA related
                    # Query: related to 'emergency' or 'FEMA'
                    is_related = False
                    if "emergency" in topics or "FEMA" in topics or "fema" in content_to_search or "emergency" in content_to_search:
                        is_related = True
                    
                    # Also check for "Disaster Recovery" in context?
                    
                    if is_related:
                        extracted_projects.append({
                            "Project_Name": project_name,
                            "status": status,
                            "topics": topics,
                            "full_text_snippet": project_text[:200]
                        })

# Convert to DF
df_extracted = pd.DataFrame(extracted_projects)

# Merge with Funding
# We need to match Project_Name. 
# Let's do a merge.
# But first check if extracted names match Funding names.
# Funding names might have (FEMA Project) suffixes which might not be in the extracted name if the name line didn't include it.
# Wait, looking at preview: "Latigo Canyon Road Retaining Wall Repair Project" in text.
# In funding: "Latigo Canyon Road Retaining Wall Repair Project".
# "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)".
# The text name might be clean, or might have suffixes.
# Let's clean the extracted name and funding name to facilitate join?
# Or just try exact join first.

merged = pd.merge(df_funding, df_extracted, on='Project_Name', how='inner')

# If exact match fails for some, we might need fuzzy or substring match.
# Let's check how many we got.

# Filter for emergency/FEMA
# We already filtered extracted projects? Yes, `is_related` check.
# But we need to make sure the funding record is also relevant (it shares the name).

result = merged[['Project_Name', 'Funding_Source', 'Amount', 'status']]

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-10239882962867119811': ['civic_docs'], 'var_function-call-10239882962867121006': ['Funding'], 'var_function-call-7750960758477245626': 'file_storage/function-call-7750960758477245626.json', 'var_function-call-7750960758477242945': 'file_storage/function-call-7750960758477242945.json', 'var_function-call-3106554336237263291': 'file_storage/function-call-3106554336237263291.json'}

exec(code, env_args)
