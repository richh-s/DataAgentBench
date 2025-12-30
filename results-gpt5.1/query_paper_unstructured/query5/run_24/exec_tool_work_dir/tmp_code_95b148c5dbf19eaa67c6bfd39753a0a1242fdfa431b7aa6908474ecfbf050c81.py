code = """import json, pandas as pd, os

# Load full citations result from JSON file
file_path = var_call_gQsijWfEdC5dVnJBUvaOjDtW
with open(file_path, 'r') as f:
    citations = json.load(f)

cit_df = pd.DataFrame(citations)
chi_files = pd.DataFrame(var_call_FRJA2IIUXx7MAtL1z1Y7aR1a)
chi_files['title'] = chi_files['filename'].str.replace('.txt', '', regex=False)

merged = cit_df.merge(chi_files[['title']], on='title', how='inner')

total_citations_chi_2020 = int(merged['total_citations'].astype(int).sum())

result = json.dumps({"total_citations_CHI_2020": total_citations_chi_2020})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_gQsijWfEdC5dVnJBUvaOjDtW': 'file_storage/call_gQsijWfEdC5dVnJBUvaOjDtW.json', 'var_call_FRJA2IIUXx7MAtL1z1Y7aR1a': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
