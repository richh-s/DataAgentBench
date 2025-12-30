code = """import json
import re
import pandas as pd

def extract_design_capital_projects(text):
    projects = []
    # Find the section for 'Capital Improvement Projects (Design)'
    # Using re.escape for the literal strings to ensure proper regex interpretation
    design_section_start_match = re.search(re.escape('Capital Improvement Projects (Design)'), text)

    if design_section_start_match:
        start_index = design_section_start_match.end()
        
        end_markers = [
            re.escape('Capital Improvement Projects (Construction)'),
            re.escape('Capital Improvement Projects (Not Started)'),
            re.escape('Disaster Recovery Projects'),
            re.escape('RECOMMENDED ACTION:')
        ]
        
        design_section_end_index = len(text)
        for marker in end_markers:
            marker_match = re.search(marker, text[start_index:])
            if marker_match:
                # Adjust the index relative to the full text
                current_end_index = start_index + marker_match.start()
                if current_end_index < design_section_end_index:
                    design_section_end_index = current_end_index
        
        design_section = text[start_index:design_section_end_index]
        
        # Extract project names within this section
        # Project names typically appear as standalone lines after bullets or without explicit prefixes.
        # Let's refine the project name extraction: lines starting with a capital letter, are not updates/schedule, and not bullet points.
        project_name_candidates = re.findall(r'^[A-Z].*$', design_section, re.MULTILINE)
        
        for candidate in project_name_candidates:
            clean_name = candidate.strip()
            # Filter out lines that are clearly not project names (e.g., updates, schedules, just 'Page X of Y')
            if not any(keyword in clean_name for keyword in ['Updates:', 'Project Schedule:', 'Page', 'Agenda Item #']):
                # Further clean any (cid:xx) artifacts, though the text processing might have already done this
                clean_name = re.sub(r'\\(cid:\\d+\\) ', '', clean_name).strip()
                if clean_name and len(clean_name) > 5: # Basic length filter to avoid very short non-project lines
                    projects.append({'Project_Name': clean_name, 'type': 'capital', 'status': 'design'})
    return projects

# Load the full text data from the file path
with open(locals()['var_function-call-4307287955121684053'], 'r') as f:
    civic_docs = json.load(f)

all_capital_design_projects = []
for doc in civic_docs:
    all_capital_design_projects.extend(extract_design_capital_projects(doc['text']))

# Filter for unique projects as some might be mentioned in multiple documents or sections
unique_capital_design_projects = []
project_names_seen = set()
for project in all_capital_design_projects:
    if project['Project_Name'] not in project_names_seen:
        unique_capital_design_projects.append(project)
        project_names_seen.add(project['Project_Name'])

# Load funding data
with open(locals()['var_function-call-6712936743636236687'], 'r') as f:
    funding_data = json.load(f)

# Create DataFrames
df_projects = pd.DataFrame(unique_capital_design_projects)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Merge dataframes
merged_df = pd.merge(df_projects, df_funding, on='Project_Name', how='inner')

# Filter for funding greater than $50,000 (already done in SQL query, but good to double check or if logic changes)
# merged_df = merged_df[merged_df['Amount'] > 50000]

# Get the count
project_count = len(merged_df)

print("__RESULT__:")
print(json.dumps(project_count))"""

env_args = {'var_function-call-3903943541476756532': ['civic_docs'], 'var_function-call-4307287955121684053': 'file_storage/function-call-4307287955121684053.json', 'var_function-call-6712936743636236687': 'file_storage/function-call-6712936743636236687.json'}

exec(code, env_args)
