code = """import json
import sqlite3
import re
import pandas as pd

# Load Funding
with open('var_function-call-7750960758477245626.json', 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Create Base_Name for joining
def clean_name(name):
    # Remove specific suffixes
    name = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA|FEMA/CalOES).*?\)$', '', name)
    # Remove generic (FEMA) or (CalOES) if just that
    name = re.sub(r'\s*\((?:FEMA|CalOES)\)$', '', name)
    return name.strip()

df_funding['Base_Name'] = df_funding['Project_Name'].apply(clean_name)

# Load Docs
with open('var_function-call-3106554336237263291.json', 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []
keywords_list = ["park", "road", "FEMA", "fire", "emergency", "warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]

for doc in civic_docs:
    text = doc['text']
    text = text.replace('\r\n', '\n')
    
    # Split by sections
    # Using simple string find/split because regex split with capture groups can be messy if not careful
    # But regex is robust for variations.
    # I'll use regex but escape carefully.
    
    # Sections: Capital Improvement Projects (Design), (Construction), (Not Started)
    # Pattern: Capital Improvement Projects \((?:Design|Construction|Not Started)\)
    
    sections = re.split(r'(Capital Improvement Projects \((?:Design|Construction|Not Started)\))', text)
    
    current_status = "unknown"
    
    for i in range(len(sections)):
        part = sections[i].strip()
        if not part: continue
        
        if "Capital Improvement Projects" in part:
            if "(Design)" in part:
                current_status = "design"
            elif "(Construction)" in part:
                current_status = "construction"
            elif "(Not Started)" in part:
                current_status = "not started"
        else:
            # Body
            # Split by Project Name. 
            # Project names are lines followed by a line starting with (cid:190)
            # We can split by `\n(?=.*\n\(cid:190\))`
            
            blocks = re.split(r'\n(?=[^\n]+\n\(cid:190\))', part)
            # Actually, this split assumes the project name is the LAST line of the previous block?
            # No, `(?=...)` is a lookahead. 
            # `re.split(pattern, string)` splits string by pattern.
            # If pattern is `\n`, it splits at newlines.
            # We want to split BEFORE the project name line.
            # The project name line is identified by: `Line\n(cid:190)`
            # So the delimiter is the newline BEFORE `Line\n(cid:190)`.
            # Regex: `\n(?=[^\n]+\n\(cid:190\))`
            
            # Note: The first block might contain garbage if the section didn't start cleanly.
            
            # Let's try to iterate through matches instead of split
            # Find all occurrences of `\n(Project Name)\n(cid:190)`? 
            # But the project name can be anything.
            
            # Let's iterate over blocks.
            # If I split by `\n(?=[^\n]+\n\(cid:190\))`, the first element is the text BEFORE the first project.
            # The subsequent elements start with the Project Name.
            
            sub_blocks = re.split(r'\n(?=[^\n]+\n\(cid:190\))', part)
            
            for b_idx, block in enumerate(sub_blocks):
                # The first block (index 0) usually contains the section header text or empty.
                # UNLESS the first project starts immediately?
                # Check if block starts with a project structure.
                # Project structure: `Name\n(cid:190)...`
                
                block = block.strip()
                if not block: continue
                
                lines = block.split('\n')
                # Check if second line is (cid:190)
                is_project = False
                if len(lines) > 1 and '(cid:190)' in lines[1]:
                    is_project = True
                
                if not is_project:
                    # Maybe it's index 0 and it's just preamble. Skip.
                    continue
                
                project_name = lines[0].strip()
                project_text = block
                
                # Check status override
                status = current_status
                if status == "construction":
                    if "Construction was completed" in project_text or "Notice of completion" in project_text:
                        status = "completed"
                
                # Check Topics
                topics = []
                search_text = (project_name + " " + project_text).lower()
                for kw in keywords_list:
                    if kw.lower() in search_text:
                        topics.append(kw)
                if "emergency warning" in search_text:
                    topics.append("emergency") # Treat as emergency
                
                extracted_projects.append({
                    "Base_Name": project_name, # Assuming text name matches Base_Name
                    "status": status,
                    "topics": topics,
                    "full_text": project_text
                })

df_extracted = pd.DataFrame(extracted_projects)

# Join
# Join df_funding on Base_Name matching df_extracted['Base_Name']
# But names might not be identical. Let's try exact match first.
merged = pd.merge(df_funding, df_extracted, on='Base_Name', how='inner')

# Filter
# Keep if Project_Name (Funding) has "emergency" or "FEMA"
# OR topics has "emergency" or "FEMA"
# OR full_text has "emergency" or "FEMA" (covered by topics usually, but let's be safe)

def is_relevant(row):
    text_content = (str(row['Project_Name']) + " " + str(row['full_text']) + " " + str(row['topics'])).lower()
    if 'emergency' in text_content or 'fema' in text_content:
        return True
    return False

filtered = merged[merged.apply(is_relevant, axis=1)].copy()

result = filtered[['Project_Name', 'Funding_Source', 'Amount', 'status']]
# Remove duplicates if any
result = result.drop_duplicates()

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-10239882962867119811': ['civic_docs'], 'var_function-call-10239882962867121006': ['Funding'], 'var_function-call-7750960758477245626': 'file_storage/function-call-7750960758477245626.json', 'var_function-call-7750960758477242945': 'file_storage/function-call-7750960758477242945.json', 'var_function-call-3106554336237263291': 'file_storage/function-call-3106554336237263291.json'}

exec(code, env_args)
