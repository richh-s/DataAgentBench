code = """import json
import re
import pandas as pd

# Load data from storage
with open(locals()['var_function-call-18142847645302743990'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-15935162301044067236'], 'r') as f:
    funding_records = json.load(f)

projects_extracted = []

# Regex for (cid:190) like markers. \d{3} matches three digits.
# It's inside a raw string, so no need for \\ for the backslashes in the regex itself.
CID_MARKER = r'\(cid:\d{3}\)'

# Define keywords for status and topics
status_keywords = {
    'completed': ['completed', 'notice of completion', 'finished'],
    'construction': ['construction', 'under construction', 'begin construction', 'out to bid'],
    'design': ['design', 'preliminary design', 'FEMA/CalOES approval', 'consultant to finalize the design plans', 'in planning/design phase'],
    'not started': ['not started', 'identified in the .* Study', 'waiting for the agreement', 'not yet begun']
}
topic_keywords = ['emergency', 'FEMA', 'disaster', 'CalOES']

# Project name pattern: starts with a capital letter, followed by common project name chars, ending with 'Project' or 'Plan'
# Project name characters can include A-Z, a-z, 0-9, space, hyphen, ampersand, comma, dot, single quote, and square brackets.
# Escape single quote within the raw string using \'
project_name_char_set = r'[A-Za-z0-9 \-&,.\'\[\]()]*?' # Updated to allow more characters and make it non-greedy
project_name_pattern = re.compile(r'(' + project_name_char_set + r'(?:Project|Plan))')

for doc in civic_docs:
    text = doc['text']

    # Use a broader pattern to find potential project blocks including their descriptions and updates
    # This pattern tries to capture a project name and its associated descriptive text.
    # It assumes project names are typically followed by (cid:190) Updates/Schedule/Description.
    # The outer group captures the whole block for context.
    project_block_regex = re.compile(
        r'('  # Start capturing the entire project block
        r'(' + project_name_char_set + r'(?:Project|Plan))' # Project Name (group 1)
        r'\n\n'
        r'(?:' + CID_MARKER + r'\s*(?:Updates:|Project Schedule:|Project Description:))' # Marker and type
        r'\n*(.*?)' # Details (group 2) - non-greedy to stop before next project or section end
        r'(?=\n\n' + project_name_char_set + r'(?:Project|Plan)|\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects|\n\nPage \d+ of \d+|$)'
        r')'
        , re.DOTALL
    )

    for match in project_block_regex.finditer(text):
        # Use groups from the broader match
        project_name = match.group(1).strip() # Project name itself
        details = match.group(2).strip() if match.group(2) else '' # Associated details
        full_context = match.group(0) # Full captured block for more context if needed

        is_relevant = False
        for keyword in topic_keywords:
            if re.search(keyword, project_name, re.IGNORECASE) or re.search(keyword, details, re.IGNORECASE):
                is_relevant = True
                break
        
        if is_relevant:
            current_status = "unknown"
            for status_type, keywords in status_keywords.items():
                if any(re.search(keyword, details, re.IGNORECASE) for keyword in keywords):
                    current_status = status_type
                    break
            
            current_topic = "general"
            if re.search(r'Disaster Recovery', full_context, re.IGNORECASE) or "FEMA Project" in project_name or re.search(r'CalOES', project_name + details, re.IGNORECASE):
                current_topic = "disaster/FEMA/emergency"
            elif re.search(r'emergency', project_name + details, re.IGNORECASE):
                current_topic = "emergency"
            elif re.search(r'FEMA', project_name + details, re.IGNORECASE):
                current_topic = "FEMA"
            
            projects_extracted.append({"Project_Name": project_name, "status": current_status, "topic": current_topic})

    # Handle specific projects explicitly mentioned in hints, ensuring no duplicates
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
