code = """import json
import pandas as pd

# Read the full civic docs result
with open(var_call_M5WB5deY7REsm7gEQ2IqlM4Q, 'r') as f:
    civic_docs = json.load(f)

# Read the full funding result
with open(var_call_Rp5VVDEy0XKOcKG6atWrw8IL, 'r') as f:
    funding = json.load(f)

# Park-related projects keywords to match
park_keywords = ['park']

# Helper function to filter relevant park-related project names that were completed in 2022 based on documents
completed_2022_projects = set()
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if '2022' in text and 'completed' in text:
        # Split into possible lines or sentences to find project names
        lines = text.split('\n')
        for idx, line in enumerate(lines):
            # Look for lines with park and completed and 2022
            if ('park' in line) and (('completed' in line) or ('construction was completed' in line and '2022' in line)):
                # Try to extract project name
                # Project name can sometimes be before a colon or in heading lines
                if ':' in line:
                    project_name = line.split(':')[0].strip()
                else:
                    # Look for previous line if it's not the project name
                    project_name = line.strip()
                if len(project_name) > 4:
                    completed_2022_projects.add(project_name)
            # Look for specific named completions in context for parks
            if 'construction was completed' in line and '2022' in line:
                # Try preceding lines for park wording
                for offset in range(1,4):
                    if idx-offset >= 0 and 'park' in lines[idx-offset]:
                        potential_name = lines[idx-offset].replace(':', '').strip()
                        if len(potential_name) > 4:
                            completed_2022_projects.add(potential_name)

# Normalize to lower for matching against funding database
completed_2022_projects_lower = {p.lower() for p in completed_2022_projects}

# Prepare funding dataframe
funding_df = pd.DataFrame(funding)

# Normalize project names for comparison
def normalize(s):
    return s.lower().replace('project', '').replace('repairs', '').replace('upgrade', '').replace(':', '').replace('-', '').replace('structure', '').replace('walkway', '').replace('shade', '').replace('bluffs', '').strip()

funding_df['proj_name_norm'] = funding_df['Project_Name'].astype(str).str.lower().apply(normalize)

# Try matching funding rows against detected completed projects
matched_rows = funding_df[funding_df['proj_name_norm'].apply(lambda x: any(n in x for n in completed_2022_projects_lower))]

# If not enough matches, also check for contains 'park' and completed in project name
if matched_rows.empty:
    matched_rows = funding_df[funding_df['Project_Name'].str.lower().str.contains('park') & funding_df['Project_Name'].str.lower().str.contains('repair|shade|walkway|playground|structure|renovation|slope')]

# Filter only those that plausibly relate to 2022
likely_2022_names = ['2022', 'completed', 'november 2022', 'december 2022']
def plausible_2022(row):
    name = row['Project_Name'].lower()
    return any(k in name for k in likely_2022_names)
matched_rows_2022 = matched_rows[matched_rows.apply(plausible_2022, axis=1)]

# Also keep known matches from document parsing (for which we know were completed in 2022)
for p in completed_2022_projects:
    matched_rows_2022 = pd.concat([
        matched_rows_2022,
        funding_df[funding_df['proj_name_norm'].str.contains(normalize(p))]
    ]).drop_duplicates()

# Total amount
total_funding = matched_rows_2022['Amount'].astype(float).sum()

print('__RESULT__:')
print(json.dumps(int(total_funding)))"""

env_args = {'var_call_M5WB5deY7REsm7gEQ2IqlM4Q': 'file_storage/call_M5WB5deY7REsm7gEQ2IqlM4Q.json', 'var_call_Rp5VVDEy0XKOcKG6atWrw8IL': 'file_storage/call_Rp5VVDEy0XKOcKG6atWrw8IL.json'}

exec(code, env_args)
