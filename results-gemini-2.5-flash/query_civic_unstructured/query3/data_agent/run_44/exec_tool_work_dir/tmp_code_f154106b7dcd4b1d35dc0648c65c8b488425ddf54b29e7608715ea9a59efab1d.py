code = """import json
import pandas as pd

# Load the extracted project information
projects_data = locals()['var_function-call-3709741721618593721']
df_projects = pd.DataFrame(projects_data)

# Clean the Project_Name in df_projects to remove extra text like '(cid:131)' and trim spaces
df_projects['Project_Name'] = df_projects['Project_Name'].apply(lambda x: x.split('(cid:131)')[-1].strip() if x else x)
# Remove the 'details' column as it is no longer needed
df_projects = df_projects.drop(columns=['details'])

# Load the funding data
with open(locals()['var_function-call-12343138372542381145'], 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Clean the Project_Name in df_funding to handle potential inconsistencies if any, although less likely here
df_funding['Project_Name'] = df_funding['Project_Name'].str.strip()

# Merge the two dataframes on 'Project_Name'
# Using an outer merge to see all projects, then filter for those with funding and relevant topics
merged_df = pd.merge(df_projects, df_funding, on='Project_Name', how='inner')

# Filter for projects related to 'emergency' or 'FEMA' based on the topic column from the civic docs
# This should already be filtered by the previous python step, but good to double check or re-confirm
filtered_merged_df = merged_df[
    merged_df['topic'].str.contains('emergency', case=False, na=False) | 
    merged_df['topic'].str.contains('FEMA', case=False, na=False)
]

# Select the required columns: Project_Name, Funding_Source, Amount, and Status
final_result = filtered_merged_df[['Project_Name', 'Funding_Source', 'Amount', 'status']]

# Convert to a list of dictionaries for JSON output
result_list = final_result.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-5052213206219168496': 'file_storage/function-call-5052213206219168496.json', 'var_function-call-3709741721618593721': [{'Project_Name': '(cid:131) The project consultant has started the design of this project.', 'status': 'not started', 'type': 'capital', 'details': ['', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Storm Drain Master Plan (FEMA Project)', '', 'Page 5 of 8', '', 'Agenda Item # 4.A.', '', '', '', '', '', '', '', '', '', '', '(cid:190) Project Description: This project will be funded through a grant from FEMA'], 'topic': 'FEMA'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'status': 'not started', 'type': 'capital', 'details': ['', '(cid:190) Project Description: This project has been cancelled as it could not get FEMA', ''], 'topic': 'FEMA'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'status': 'not started', 'type': 'capital', 'details': ['', '(cid:190) Project Description: An Emergency Warning Siren system will improve the', 'City’s ability to alert the community by providing mechanisms to alert', 'residents in areas without power and those who live in neighborhoods with', 'poor cell service. Phase One of the project included a sound study to', 'determine the optimal number and locations of individual sirens, power and', 'infrastructure requirements, and siren sound range. The City has been', '', 'Page 7 of 8', '', 'Agenda Item # 4.A.', '', '', '', '', '', '', '', 'awarded a FEMA Hazard Mitigation grant to fund the design, engineering and', 'environmental compliance needed for a shovel ready project. Phase Two of'], 'topic': 'emergency, FEMA'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'status': 'not started', 'type': 'capital', 'details': ['', '(cid:190) Project Description: This project will be funded through a grant from FEMA'], 'topic': 'FEMA'}, {'Project_Name': 'a plan that includes the evaluation of a siren system and possible locations.', 'status': 'not started', 'type': 'capital', 'details': ['', '(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Dependent upon final grant approval from FEMA', '', 'Page 6 of 6', '', 'Agenda Item # 4.A.', '', '', '', '', '', '', '', '', '', ''], 'topic': 'FEMA'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'status': 'not started', 'type': 'capital', 'details': ['', '(cid:190) Project Description: This project will be funded through a grant from FEMA'], 'topic': 'FEMA'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'status': 'not started', 'type': 'capital', 'details': ['', '(cid:190) Project Description: This project will be funded through a grant from FEMA'], 'topic': 'FEMA'}], 'var_function-call-12343138372542381145': 'file_storage/function-call-12343138372542381145.json'}

exec(code, env_args)
