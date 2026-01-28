code = """import json
import pandas as pd

# Load data from previous steps
projects_from_docs = locals()['var_function-call-631145647031076741']
with open(locals()['var_function-call-13657466020950844419'], 'r') as f:
    funding_data = json.load(f)

# Convert to pandas DataFrames
df_projects = pd.DataFrame(projects_from_docs)
df_funding = pd.DataFrame(funding_data)

# Merge the two DataFrames on Project_Name
merged_df = pd.merge(df_projects, df_funding, on='Project_Name', how='inner')

# Filter for projects related to 'emergency' or 'FEMA' in the topic or project name
# The filtering by topic is already done during the extraction from civic_docs_database, so just need to ensure the project name is also checked.
filtered_df = merged_df[merged_df['topic'].str.contains('emergency|FEMA|disaster|emergency warning') | merged_df['Project_Name'].str.contains('emergency|FEMA', case=False)]

# Select and rename columns for the final output
final_output = filtered_df[['Project_Name', 'Funding_Source', 'Amount', 'status']]

# Convert to a list of dictionaries (JSON serializable format)
result_json = final_output.to_json(orient='records')

print('__RESULT__:')
print(result_json)"""

env_args = {'var_function-call-13297758767889787610': 'file_storage/function-call-13297758767889787610.json', 'var_function-call-631145647031076741': [{'Project_Name': 'Report', 'topic': 'disaster', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'topic': 'FEMA, road', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Outdoor Warning Signs', 'topic': 'emergency warning', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'topic': 'emergency warning', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'topic': 'FEMA, road', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'topic': 'FEMA, park', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'topic': 'FEMA, drainage, fire, storm drain', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'topic': 'FEMA, fire, guardrail', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'topic': 'FEMA, fire, road', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'topic': 'FEMA', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'topic': 'FEMA, road, storm drain', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'topic': 'FEMA, fire, road, storm drain', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'topic': 'FEMA, emergency, emergency warning', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES', 'topic': 'FEMA, road', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Project)', 'topic': 'FEMA', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'topic': 'FEMA, park', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'topic': 'FEMA, drainage, park', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'topic': 'FEMA, fire, guardrail', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'topic': 'FEMA, fire, road', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'topic': 'FEMA, road, storm drain', 'type': 'capital', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'topic': 'FEMA, fire, road, storm drain', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'topic': 'FEMA, drainage, fire, road, storm drain', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'topic': 'FEMA, fire, emergency warning', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'topic': 'FEMA, road', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'topic': 'FEMA, fire, emergency warning', 'type': 'capital', 'status': 'design'}], 'var_function-call-13657466020950844419': 'file_storage/function-call-13657466020950844419.json'}

exec(code, env_args)
