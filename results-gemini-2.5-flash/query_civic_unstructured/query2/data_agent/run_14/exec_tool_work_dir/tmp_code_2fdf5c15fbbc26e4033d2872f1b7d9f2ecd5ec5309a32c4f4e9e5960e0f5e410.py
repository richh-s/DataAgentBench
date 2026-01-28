code = """import pandas as pd
import re
import json

funding_data = pd.read_json(locals()['var_function-call-15757902439040205744'])
civic_docs = pd.read_json(locals()['var_function-call-5129165909291944523'])

project_info = []

for index, row in civic_docs.iterrows():
    text = row['text']

    # Regex to find project details (Project_Name, topic, status, et)
    # This is a simplified regex and may need adjustment based on actual document structure
    # Looking for 'Project Name', 'topic', 'status', 'Complete Construction: YYYY', 'Complete Design: YYYY', 'Begin Construction: YYYY'
    # Project names are usually followed by (cid:190) Updates: or similar
    
    # Capital Improvement Projects (Design) / (Construction) / (Not Started)
    # Disaster Recovery Projects
    
    # A more robust approach would be to process text paragraph by paragraph and infer context.
    # For this task, I'll assume project name is followed by details in subsequent lines.

    # This pattern attempts to capture project names and their associated schedules/updates
    
    # First, try to capture explicit "Construction was completed X" or "Complete Construction: YYYY"
    # This captures the project name that appears before "Updates: Construction was completed..." or similar
    completed_pattern = re.compile(r'(?P<Project_Name>[A-Za-z0-9 _&/\\-]+(?: \\(FEMA Project\\))?(?: \\(CalJPIA Project\\))?(?: \\(CalOES Project\\))?)\n(?:\\(cid:190\\) Updates: Construction was completed, (?P<Month_Day_Year>[A-Za-z]+ \\d{4}))|(?:Complete Construction: (?P<Year_Complete>\\w+ \\d{4}|\\d{4}|Summer \\d{4}|Fall \\d{4}|Spring \\d{4}|Winter \\d{4}))')

    for match in completed_pattern.finditer(text):
        project_name = match.group('Project_Name').strip()
        
        # Check for explicit completion date first
        end_date = None
        if match.group('Month_Day_Year'):
            end_date = match.group('Month_Day_Year')
        elif match.group('Year_Complete'):
            end_date = match.group('Year_Complete')
        
        if end_date:
            # Check if "2022" is in the end date string
            if "2022" in end_date:
                # Check for "park" in the project name, or if "park" is explicitly mentioned in the text
                if re.search(r'park', project_name, re.IGNORECASE) or re.search(r'park', text, re.IGNORECASE):
                    project_info.append({'Project_Name': project_name, 'status': 'completed', 'et': end_date, 'topic': 'park'})

    # Try another pattern to find projects that are listed as "completed" in the document without explicit date in the same line.
    # This pattern looks for "Project_Name" and then checks for "status: completed" and "et: 2022" in the surrounding text.
    # This is more complex for a simple regex, so I will stick to explicitly looking for "completed" and "2022" in relation to a project.
    
    # More general pattern to find project names and then look for "completed" and "2022" in the text block associated with it.
    # This is a heuristic approach.
    project_block_pattern = re.compile(r'(?P<Project_Name>[A-Za-z0-9 _&/\\-]+(?: \\(FEMA Project\\))?(?: \\(CalJPIA Project\\))?(?: \\(CalOES Project\\))?)\n(.*?)(?=\n[A-Za-z0-9 _&/\\-]+(?: \\(FEMA Project\\))?(?: \\(CalJPIA Project\\))?(?: \\(CalOES Project\\))?|\Z)', re.DOTALL)

    for match in project_block_pattern.finditer(text):
        project_name = match.group('Project_Name').strip()
        project_block = match.group(2) # The content associated with the project

        if re.search(r'park', project_name, re.IGNORECASE) or re.search(r'park', project_block, re.IGNORECASE):
            if re.search(r'completed', project_block, re.IGNORECASE) and re.search(r'2022', project_block):
                # Now try to extract the specific completion date for 2022
                completed_date_match = re.search(r'(?:Complete Construction: (?P<Year_Complete_Block>\\w+ \\d{4}|\\d{4}|Summer \\d{4}|Fall \\d{4}|Spring \\d{4}|Winter \\d{4}))|(?:Construction was completed, (?P<Month_Day_Year_Block>[A-Za-z]+ \\d{4}))', project_block)
                if completed_date_match:
                    end_date = None
                    if completed_date_match.group('Month_Day_Year_Block'):
                        end_date = completed_date_match.group('Month_Day_Year_Block')
                    elif completed_date_match.group('Year_Complete_Block'):
                        end_date = completed_date_match.group('Year_Complete_Block')
                    
                    if end_date and "2022" in end_date:
                        project_info.append({'Project_Name': project_name, 'status': 'completed', 'et': end_date, 'topic': 'park'})


project_info_df = pd.DataFrame(project_info)

# Remove duplicates, as a project might be mentioned multiple times
project_info_df.drop_duplicates(subset=['Project_Name'], inplace=True)

# Merge with funding data
merged_df = pd.merge(funding_data, project_info_df, on='Project_Name', how='inner')

# Calculate total funding
total_funding = merged_df['Amount'].astype(int).sum()

print('__RESULT__:')
print(json.dumps(str(total_funding)))"""

env_args = {'var_function-call-15757902439040205744': 'file_storage/function-call-15757902439040205744.json', 'var_function-call-5129165909291944523': 'file_storage/function-call-5129165909291944523.json'}

exec(code, env_args)
