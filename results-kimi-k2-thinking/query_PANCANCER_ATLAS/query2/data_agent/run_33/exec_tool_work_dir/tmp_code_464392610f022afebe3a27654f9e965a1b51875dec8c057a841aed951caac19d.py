code = """import json
import re

# Read the clinical data file
file_path = var_functions.query_db:11
with open(file_path, 'r') as f:
    clinical_data = json.load(f)

# Look for BRCA or bladder cancer patients
brca_patients = []
for record in clinical_data:
    patient_desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', '')
    
    # Check for BRCA, bladder, or breast mentions
    if re.search(r'\bBRCA\b', patient_desc, re.IGNORECASE) or \
       re.search(r'\bbladder\b', patient_desc, re.IGNORECASE) or \
       re.search(r'\bbreast\b', patient_desc, re.IGNORECASE) or \
       re.search(r'\bbladder\b', hist_type, re.IGNORECASE) or \
       re.search(r'\bbreast\b', hist_type, re.IGNORECASE):
        
        # Check vital status (alive)
        days_to_death = record.get('days_to_death')
        is_alive = days_to_death in [None, 'None', '[Not Applicable]', 'nan', '']
        
        brca_patients.append({
            'Patient_description': patient_desc,
            'histological_type': hist_type,
            'is_alive': is_alive,
            'days_to_death': days_to_death
        })

print('__RESULT__:')
print(json.dumps({
    'total_brca_like': len(brca_patients),
    'alive_brca': sum(1 for p in brca_patients if p['is_alive']),
    'sample_records': brca_patients[:10]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
