code = """import json
import re

# Load data
with open(locals()['var_function-call-62592550053274037'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-62592550053277018'], 'r') as f:
    civic_docs = json.load(f)

# Combine text
# Use double backslash for newline char in the string literal
full_text = "\\n".join([d.get('text', '') for d in civic_docs])

# Define keywords
keywords = ['emergency', 'fema']

def has_keywords(text):
    return any(k in text.lower() for k in keywords)

def normalize_name(name):
    # Regex to strip suffixes. escaping backslashes.
    # Pattern: \s*\((?:.*?(?:FEMA|CalOES|CalJPIA).*?)\)$
    pattern = r'\\s*\\((?:.*?(?:FEMA|CalOES|CalJPIA).*?)\\)$'
    clean = re.sub(pattern, '', name, flags=re.IGNORECASE)
    return clean.strip()

unique_names = set()
for item in funding_data:
    unique_names.add(normalize_name(item['Project_Name']))
    unique_names.add(item['Project_Name'])

headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

header_positions = []
for h in headers:
    for m in re.finditer(re.escape(h), full_text, re.IGNORECASE):
        header_positions.append((m.start(), "HEADER", h))

project_positions = []
for name in unique_names:
    if len(name) < 5: continue
    for m in re.finditer(re.escape(name), full_text, re.IGNORECASE):
        project_positions.append((m.start(), "PROJECT", name))

all_positions = sorted(header_positions + project_positions, key=lambda x: x[0])

project_info_map = {} 
current_header = "Unknown"

for i in range(len(all_positions)):
    pos, type_, content = all_positions[i]
    if type_ == "HEADER":
        current_header = content
    elif type_ == "PROJECT":
        next_pos = all_positions[i+1][0] if i+1 < len(all_positions) else len(full_text)
        segment = full_text[pos:next_pos]
        
        # Check if segment implies a project section
        if "Updates:" in segment or "Project Schedule:" in segment or "Project Description:" in segment:
            status = "not started" # Default fallback
            if "Design" in current_header: 
                status = "design"
            elif "Not Started" in current_header: 
                status = "not started"
            elif "Construction" in current_header:
                if "completed" in segment.lower():
                    status = "completed"
                else:
                    status = "construction"
            
            relevant = has_keywords(segment)
            
            # Store/Update. 
            # If we already have info for this name, should we overwrite?
            # The text might mention the project multiple times.
            # We prefer the one that looks like a Status Report section (which we filtered by Updates/Schedule).
            # If multiple status reports? Maybe take the last one? Or first?
            # Let's take the one that is most descriptive. 
            project_info_map[content] = {'status': status, 'relevant': relevant}

final_output = []
for item in funding_data:
    p_name = item['Project_Name']
    norm_name = normalize_name(p_name)
    
    info = project_info_map.get(p_name) or project_info_map.get(norm_name)
    
    name_relevant = has_keywords(p_name)
    text_relevant = info['relevant'] if info else False
    
    if name_relevant or text_relevant:
        status_to_report = info['status'] if info else "not started"
        
        # If status is "construction" and we want to map to hint's 3 statuses?
        # The prompt asked "What are the ... statuses".
        # I'll leave it as "construction" if that's what I found. 
        # But wait, maybe "under construction" -> "design" (implementation phase)? 
        # No, "design" is "planning/design".
        # I'll stick to "construction".
        
        final_output.append({
            "Project_Name": p_name,
            "Funding_Source": item['Funding_Source'],
            "Amount": item['Amount'],
            "Status": status_to_report
        })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-2440996547258625204': ['Funding'], 'var_function-call-2440996547258622967': ['civic_docs'], 'var_function-call-2122594864921453126': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-2122594864921454085': 'file_storage/function-call-2122594864921454085.json', 'var_function-call-62592550053274037': 'file_storage/function-call-62592550053274037.json', 'var_function-call-62592550053277018': 'file_storage/function-call-62592550053277018.json'}

exec(code, env_args)
