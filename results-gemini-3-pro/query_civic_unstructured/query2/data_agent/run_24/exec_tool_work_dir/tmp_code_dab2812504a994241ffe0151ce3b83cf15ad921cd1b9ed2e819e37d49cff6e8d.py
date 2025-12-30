code = """import json
import re
import pandas as pd

# Load funding data
with open(locals()['var_function-call-10729501578572278771'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load civic docs
with open(locals()['var_function-call-14279954887626903002'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # The text contains project sections.
    # Looking at the sample, projects seem to be headers followed by "(cid:190)" (which is likely a bullet point character like -> or similar, rendered oddly).
    # Let's try to split by project blocks.
    
    # Heuristic: Find lines that look like project titles.
    # Usually followed by "(cid:190) Updates:" or "(cid:190) Project Description:"
    
    lines = text.split('\n')
    current_project = {}
    buffer_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for start of a section marker
        if "(cid:190)" in line:
            # The previous non-empty line(s) probably constitute the project name.
            # We need to capture the project name from the buffer.
            if not current_project:
                # This is the first time we see a marker for a potential project
                # Walk back in buffer to find the name
                name_parts = []
                for prev_line in reversed(buffer_lines):
                    if not prev_line: continue
                    # Stop if we hit a date line or something generic like "Capital Improvement Projects (Design)"
                    if "Capital Improvement Projects" in prev_line: break
                    if "Agenda Item" in prev_line: break
                    if "Page " in prev_line: break
                    
                    name_parts.insert(0, prev_line)
                    # Assuming project name is usually 1 or 2 lines.
                    if len(name_parts) >= 2: break
                
                if name_parts:
                    project_name = " ".join(name_parts).strip()
                    # Clean up common garbage
                    if project_name:
                        current_project = {'Project_Name': project_name, 'text_lines': [line]}
            else:
                # We are already in a project, just add the line
                current_project['text_lines'].append(line)
        else:
            # If we have a current project, check if we are starting a NEW project
            # This is hard because headers look like text.
            # However, if we hit a known big header like "Capital Improvement Projects...", we reset.
            if "Capital Improvement Projects" in line:
                if current_project:
                    extracted_projects.append(current_project)
                    current_project = {}
            
            # If we are currently collecting a project, add to its lines
            if current_project:
                current_project['text_lines'].append(line)
            
            buffer_lines.append(line)

    # Add the last project
    if current_project:
        extracted_projects.append(current_project)

# Now process the extracted projects to find details
final_projects = []
for p in extracted_projects:
    name = p['Project_Name']
    full_text = " ".join(p['text_lines'])
    
    # Topic detection
    topics = []
    keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]
    lower_text = (name + " " + full_text).lower()
    for kw in keywords:
        if kw in lower_text:
            topics.append(kw)
    
    # Status and Date detection
    status = "unknown"
    et = None
    
    # Look for "completed"
    if "completed" in lower_text or "complete construction" in lower_text:
        # Try to find the date associated with completion
        # Patterns: "completed <Month> <Year>", "Complete Construction: <Month> <Year>"
        
        # Regex for date: Month Year (e.g., November 2022)
        date_match = re.search(r'(?:completed|Complete Construction:?)\D{0,10}(\w+\s+\d{4})', full_text, re.IGNORECASE)
        if date_match:
            et = date_match.group(1)
            status = "completed"
    
    final_projects.append({
        "Project_Name": name,
        "topics": topics,
        "status": status,
        "et": et,
        "raw_text": full_text
    })

# Filter for the query
# Query: park-related projects completed in 2022
target_projects = []
for p in final_projects:
    is_park = "park" in p['topics']
    is_completed = p['status'] == "completed"
    
    in_2022 = False
    if p['et']:
        if "2022" in p['et']:
            in_2022 = True
    
    if is_park and is_completed and in_2022:
        target_projects.append(p)

# Convert to DataFrame for merging
target_df = pd.DataFrame(target_projects)

# We need to fuzzy match or exact match Project_Name with funding_df
# Let's try to normalize names
def normalize(s):
    return " ".join(s.lower().split())

if not target_df.empty:
    target_df['normalized_name'] = target_df['Project_Name'].apply(normalize)
    funding_df['normalized_name'] = funding_df['Project_Name'].apply(normalize)
    
    # Merge
    merged = pd.merge(target_df, funding_df, on='normalized_name', how='inner')
    
    total_funding = merged['Amount'].sum()
    
    # Debug info
    debug_info = merged[['Project_Name_x', 'Project_Name_y', 'Amount', 'et']].to_dict(orient='records')
else:
    total_funding = 0
    debug_info = []

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": debug_info, "extracted_count": len(final_projects)}))"""

env_args = {'var_function-call-10729501578572278771': 'file_storage/function-call-10729501578572278771.json', 'var_function-call-14279954887626903002': 'file_storage/function-call-14279954887626903002.json'}

exec(code, env_args)
