code = """import json
import pandas as pd

# Load funding data
funding_data = pd.read_json(locals()['var_function-call-8349484065091426871'])
project_names = set(funding_data['Project_Name'].str.strip().tolist())

# Load doc text
with open(locals()['var_function-call-3235961165398988678'], 'r') as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check if line is a project name
        # We check if the line matches one of the known project names
        # Sometimes there might be minor differences, but let's try exact match first
        if line_clean in project_names:
            current_project = line_clean
        else:
            # Maybe the project name in text is slightly different or has extra chars?
            # But let's assume the text headers match the DB names for now based on the hints.
            # "The Project_Name in the Funding SQLite table matches the project names that can be extracted from the civic documents"
            pass

        if current_project:
            # Look for start date
            # Patterns: "Begin Construction:", "Start Date:", "st:"
            if "Begin Construction:" in line_clean or "Start Date:" in line_clean:
                parts = line_clean.split(':')
                if len(parts) > 1:
                    date_str = parts[1].strip()
                    extracted_projects.append({
                        "Project_Name": current_project,
                        "st": date_str
                    })
                    # Reset current project to avoid assigning same date to multiple if duplicates exist (though unlikely in this flow)
                    # Actually, a project might have multiple schedule lines? 
                    # "Begin Construction" usually appears once per project block.
                    # Keep current_project active until a new one is found.

# Convert to DF
df_extracted = pd.DataFrame(extracted_projects)

print("__RESULT__:")
print(df_extracted.to_json(orient='records'))"""

env_args = {'var_function-call-3235961165398988678': 'file_storage/function-call-3235961165398988678.json', 'var_function-call-8349484065091426871': 'file_storage/function-call-8349484065091426871.json'}

exec(code, env_args)
