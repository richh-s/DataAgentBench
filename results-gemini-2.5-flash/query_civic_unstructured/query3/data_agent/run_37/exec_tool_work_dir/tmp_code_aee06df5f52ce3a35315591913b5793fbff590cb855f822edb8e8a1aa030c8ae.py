code = """import pandas as pd
import json
import re

# Load funding data
with open(locals()['var_function-call-14481153673372787681'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic documents data
with open(locals()['var_function-call-12785932103837883149'], 'r') as f:
    civic_docs_data = json.load(f)

project_details = []

# Keywords to identify relevant projects and their status
emergency_keywords = ['emergency', 'FEMA', 'disaster recovery', 'caloes', 'caljpia', 'warning sirens']
status_keywords = {
    'design': ['design', 'preliminary design'],
    'completed': ['completed', 'construction was completed', 'notice of completion filed'],
    'not started': ['not started', 'waiting for agreement', 'identified but not begun', 'preliminary design phase'],
    'under construction': ['under construction', 'begin construction']
}

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')
    current_project_name = None
    current_status = 'Unknown'
    current_topics = []

    for i, line in enumerate(lines):
        line = line.strip()

        # Identify project names. Project names often appear as a main heading or after specific markers.
        # Look for capitalized phrases that could be project names.
        # Heuristic: a line that is not too short, not a bullet point, and contains multiple words.
        if 10 < len(line) < 100 and not line.startswith(('(cid:', 'Page', 'Agenda Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:')):
            # Check if this line is likely a project name
            # We can use patterns like "Project Name (Suffix)" or just a standalone capitalized line
            potential_project_name_match = re.match(r'^(.*?)(?:\s*\((FEMA|CalOES|CalJPIA) Project\))?$', line, re.IGNORECASE)
            if potential_project_name_match:
                potential_project_name = potential_project_name_match.group(1).strip()
                # Check if it contains keywords related to emergency/FEMA, or is explicitly categorized as such
                is_relevant = False
                temp_topics = []
                for keyword in emergency_keywords:
                    if keyword in potential_project_name.lower():
                        is_relevant = True
                        temp_topics.append(keyword)
                
                # Also check in the next few lines for status or additional topic info
                context_window = 5 # Check next 5 lines for context
                context_text = ' '.join(lines[i+1 : i+1+context_window]).lower()
                for keyword in emergency_keywords:
                    if keyword in context_text:
                        is_relevant = True
                        temp_topics.append(keyword)
                
                # Try to infer status from context (e.g., "(Design)", "(Construction)", "Updates:", "Project Schedule:")
                inferred_status = 'Unknown'
                for status_key, patterns in status_keywords.items():
                    for pattern in patterns:
                        if pattern in line.lower() or pattern in context_text:
                            inferred_status = status_key
                            break
                    if inferred_status != 'Unknown':
                        break

                if is_relevant and potential_project_name not in [p['Project_Name'] for p in project_details]: # Avoid adding duplicates immediately
                    project_details.append({
                        'Project_Name': potential_project_name,
                        'status': inferred_status,
                        'topic': ', '.join(list(set(temp_topics))) # Use set to remove duplicate topics
                    })


# Convert to DataFrame
projects_df = pd.DataFrame(project_details)

# Ensure unique project names for merging, keeping the first status/topic found.
projects_df = projects_df.drop_duplicates(subset=['Project_Name'])

# Merge funding data with project details
# Use an outer merge to keep all funding projects and try to find matching details
merged_df = pd.merge(funding_df, projects_df, on='Project_Name', how='left')

# Filter for projects related to "emergency" or "FEMA" based on Project_Name or topic
# Fill NaN in 'topic' column with empty string for robust string operations
merged_df['topic'] = merged_df['topic'].fillna('')
merged_df['status'] = merged_df['status'].fillna('Unknown')

filtered_df = merged_df[
    merged_df['Project_Name'].str.contains('FEMA', case=False, na=False) |
    merged_df['Project_Name'].str.contains('emergency', case=False, na=False) |
    merged_df['topic'].str.contains('FEMA', case=False, na=False) |
    merged_df['topic'].str.contains('emergency', case=False, na=False) |
    merged_df['topic'].str.contains('disaster', case=False, na=False) |
    merged_df['Project_Name'].str.contains('CalOES', case=False, na=False) |
    merged_df['Project_Name'].str.contains('CalJPIA', case=False, na=False)
]

# Select and rename columns for the final output
final_result = filtered_df[['Project_Name', 'Funding_Source', 'Amount', 'status']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-14481153673372787681': 'file_storage/function-call-14481153673372787681.json', 'var_function-call-12785932103837883149': 'file_storage/function-call-12785932103837883149.json'}

exec(code, env_args)
