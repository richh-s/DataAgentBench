code = """import json
import re
import pandas as pd

# Load data from storage
with open(locals()['var_function-call-18142847645302743990'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-15935162301044067236'], 'r') as f:
    funding_records = json.load(f)

projects_extracted = []

# Regex for (cid:190) like markers.
# This pattern needs to be consistent with how it appears in the text.
CID_MARKER = r'\(cid:\d{3}\)'

# Define keywords for status and topics
status_keywords = {
    'completed': ['completed', 'notice of completion', 'finished'],
    'construction': ['construction', 'under construction', 'begin construction', 'out to bid'],
    'design': ['design', 'preliminary design', 'FEMA/CalOES approval', 'consultant to finalize the design plans', 'in planning/design phase'],
    'not started': ['not started', 'identified in the .* Study', 'waiting for the agreement', 'not yet begun']
}
topic_keywords = ['emergency', 'FEMA', 'disaster', 'CalOES']

for doc in civic_docs:
    text = doc['text']

    # Combined pattern to find project names and their immediate descriptive text
    # This pattern attempts to capture the project name and the text following it up to the next project or section boundary.
    # Using single quotes for string literals to avoid issues with triple quotes.
    # Escaping backslashes in regex properly for single-quoted strings.
    project_capture_pattern = re.compile(
        r'([A-Z][a-zA-Z0-9 \\-&,.''()\[\]]+? (?:Project|Plan))' # Project Name
        r'\n\n' # Two newlines after project name are common
        r'(?:' + CID_MARKER + r'\s*(?:Updates:|Project Schedule:|Project Description:))' # Optional marker + type of detail
        r'\n*(.*?)' # Non-greedy capture of details until next boundary (Group 2)
        r'(?=\n\n[A-Z][a-zA-Z0-9 \\-&,.''()\[\]]+? (?:Project|Plan)|\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects|\n\nPage \d+ of \d+|$)'
        , re.DOTALL
    )

    for match in project_capture_pattern.finditer(text):
        project_name = match.group(1).strip()
        details = match.group(2).strip() if match.group(2) else ''
        full_context = project_name + ' ' + details # Combine for keyword search

        is_relevant = False
        for keyword in topic_keywords:
            if re.search(keyword, full_context, re.IGNORECASE):
                is_relevant = True
                break
        
        if is_relevant:
            current_status = "unknown"
            for status_type, keywords in status_keywords.items():
                if any(re.search(keyword, full_context, re.IGNORECASE) for keyword in keywords):
                    current_status = status_type
                    break
            
            current_topic = "general"
            if re.search(r'Disaster Recovery', full_context, re.IGNORECASE) or "FEMA Project" in project_name or re.search(r'CalOES', full_context, re.IGNORECASE):
                current_topic = "disaster/FEMA/emergency"
            elif re.search(r'emergency', full_context, re.IGNORECASE):
                current_topic = "emergency"
            elif re.search(r'FEMA', full_context, re.IGNORECASE):
                current_topic = "FEMA"
            
            projects_extracted.append({"Project_Name": project_name, "status": current_status, "topic": current_topic})

    # Specific project checks (ensure these don't create duplicates if already caught)
    # Outdoor Warning Signs
    if re.search(r'Outdoor Warning Signs', text) and re.search(r'emergency', text, re.IGNORECASE):
        if not any(p['Project_Name'] == "Outdoor Warning Signs" for p in projects_extracted):
            projects_extracted.append({"Project_Name": "Outdoor Warning Signs", "status": "design", "topic": "emergency"})

    # Latigo Canyon Road Retaining Wall Repair Project
    if re.search(r'Latigo Canyon Road Retaining Wall Repair Project', text) and re.search(r'FEMA/CalOES approval', text):
        if not any(p['Project_Name'] == "Latigo Canyon Road Retaining Wall Repair Project" for p in projects_extracted):
            projects_extracted.append({"Project_Name": "Latigo Canyon Road Retaining Wall Repair Project", "status": "design", "topic": "FEMA"})

    # City Traffic Signals Backup Power (Specific pattern for this project)
    traffic_signals_match = re.search(
        r'City Traffic Signals Backup Power\n\n' + CID_MARKER + r' Project Description:(.*?)\n\n'
        + CID_MARKER + r' Updates:(.*?)\n\n' + CID_MARKER + r' Project Schedule:(.*?)(?=\n\n.+?$)'
        , text, re.DOTALL)
    if traffic_signals_match:
        description = traffic_signals_match.group(1)
        updates = traffic_signals_match.group(2)
        if re.search(r'emergency', description + updates, re.IGNORECASE):
            if not any(p['Project_Name'] == "City Traffic Signals Backup Power" for p in projects_extracted):
                projects_extracted.append({"Project_Name": "City Traffic Signals Backup Power", "status": "preliminary design", "topic": "emergency"})

# Convert to DataFrame for easier merging and deduplication
df_projects = pd.DataFrame(projects_extracted)
# Drop duplicates based on Project_Name and topic/status for robustness
df_projects.drop_duplicates(subset=['Project_Name', 'status', 'topic'], inplace=True)

# Load funding data into DataFrame
df_funding = pd.DataFrame(funding_records)

# Merge the two DataFrames on Project_Name
merged_df = pd.merge(df_projects, df_funding, on='Project_Name', how='left')

# Final filter to ensure all projects are related to 'emergency' or 'FEMA' keywords either in name or extracted topic
final_projects = merged_df[
    merged_df['Project_Name'].str.contains('emergency|FEMA|CalOES|Disaster', case=False, na=False) |
    (merged_df['topic'].notna() & merged_df['topic'].str.contains('emergency|FEMA|disaster', case=False, na=False))
].to_dict(orient='records')

# Select and reorder columns for the final output
result = []
for project in final_projects:
    result.append({
        "Project_Name": project.get('Project_Name'),
        "Funding_Source": project.get('Funding_Source'),
        "Amount": project.get('Amount'),
        "status": project.get('status')
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16338752333912652679': ['civic_docs'], 'var_function-call-2241076992410809533': 'file_storage/function-call-2241076992410809533.json', 'var_function-call-15935162301044067236': 'file_storage/function-call-15935162301044067236.json', 'var_function-call-18142847645302743990': 'file_storage/function-call-18142847645302743990.json'}

exec(code, env_args)
