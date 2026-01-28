code = """import json
import re

# Read the clinical data file
file_path = var_functions.query_db:22
with open(file_path, 'r') as f:
    clinical_data = json.load(f)

print('Total records in clinical database:', len(clinical_data))

# Look for BRCA (breast cancer) patients who are alive
brca_alive_patients = []
total_alive = 0

for record in clinical_data:
    patient_desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', '')
    days_to_death = record.get('days_to_death')
    
    # Check vital status (alive)
    is_alive = days_to_death in [None, 'None', '[Not Applicable]', 'nan', '']
    if is_alive:
        total_alive += 1
    
    # Check for breast cancer (BRCA or breast)
    is_brca = False
    if re.search(r'\bBRCA\b', patient_desc):
        is_brca = True
    if re.search(r'\bbreast\b', patient_desc, re.IGNORECASE):
        is_brca = True
    if re.search(r'\bbreast\b', hist_type, re.IGNORECASE):
        is_brca = True
        
    if is_brca and is_alive:
        brca_alive_patients.append({
            'Patient_description': patient_desc,
            'histological_type': hist_type
        })

print('Total BRCA patients who are alive:', len(brca_alive_patients))
print('Total alive patients in database:', total_alive)

result = {
    'total_brca_alive': len(brca_alive_patients),
    'total_alive': total_alive
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': 'test', 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5', 'var_functions.query_db:8', 'var_functions.query_db:11', 'var_functions.execute_python:18'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
