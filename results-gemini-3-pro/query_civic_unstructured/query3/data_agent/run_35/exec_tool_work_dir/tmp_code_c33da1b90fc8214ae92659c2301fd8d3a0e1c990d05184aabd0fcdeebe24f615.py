code = """import json
import sqlite3
import re
import pandas as pd

# Load Funding
with open('var_function-call-7750960758477245626.json', 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

def clean_name(name):
    # Remove suffixes
    name = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA|FEMA/CalOES).*?\)$', '', name)
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
    
    # Split sections
    # Regex: (Capital Improvement Projects \((?:Design|Construction|Not Started)\))
    # Escaped for JSON: \\( ... \\)
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
            # Split projects
            # Regex: \n(?=[^\n]+\n\(cid:190\))
            # Escaped: \\n(?=[^\\n]+\\n\\(cid:190\\))
            sub_blocks = re.split(r'\n(?=[^\n]+\n\(cid:190\))', part)
            
            for block in sub_blocks:
                block = block.strip()
                if not block: continue
                
                lines = block.split('\n')
                is_project = False
                if len(lines) > 1 and '(cid:190)' in lines[1]:
                    is_project = True
                
                if not is_project: continue
                
                raw_name = lines[0].strip()
                project_name = clean_name(raw_name)
                project_text = block
                
                status = current_status
                if status == "construction":
                    if "Construction was completed" in project_text or "Notice of completion" in project_text:
                        status = "completed"
                
                topics = []
                search_text = (raw_name + " " + project_text).lower()
                for kw in keywords_list:
                    if kw.lower() in search_text:
                        topics.append(kw)
                if "emergency warning" in search_text:
                    topics.append("emergency")
                
                extracted_projects.append({
                    "Base_Name": project_name,
                    "status": status,
                    "topics": topics,
                    "full_text": project_text
                })

df_extracted = pd.DataFrame(extracted_projects)

# Join
merged = pd.merge(df_funding, df_extracted, on='Base_Name', how='inner')

# Filter
def is_relevant(row):
    text_content = (str(row['Project_Name']) + " " + str(row['full_text']) + " " + str(row['topics'])).lower()
    if 'emergency' in text_content or 'fema' in text_content:
        return True
    return False

filtered = merged[merged.apply(is_relevant, axis=1)].copy()

result = filtered[['Project_Name', 'Funding_Source', 'Amount', 'status']]
result = result.drop_duplicates()

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-10239882962867119811': ['civic_docs'], 'var_function-call-10239882962867121006': ['Funding'], 'var_function-call-7750960758477245626': 'file_storage/function-call-7750960758477245626.json', 'var_function-call-7750960758477242945': 'file_storage/function-call-7750960758477242945.json', 'var_function-call-3106554336237263291': 'file_storage/function-call-3106554336237263291.json'}

exec(code, env_args)
