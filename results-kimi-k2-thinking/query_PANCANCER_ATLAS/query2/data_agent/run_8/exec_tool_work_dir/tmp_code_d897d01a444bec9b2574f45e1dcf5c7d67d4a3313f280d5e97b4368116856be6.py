code = """import json
import re
from collections import defaultdict

# Load mutation data file
cdh1_file = locals()['var_functions.query_db:22']
with open(cdh1_file, 'r') as f:
    cdh1_data = json.load(f)

# Load clinical data file (all BRCA patients)
clinical_file = locals()['var_functions.query_db:28']
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Extract CDH1-mutated participants (barcodes)
cdh1_participants = set()
for row in cdh1_data:
    if isinstance(row, dict) and 'ParticipantBarcode' in row:
        cdh1_participants.add(row['ParticipantBarcode'])

# Filter to only alive BRCA patients and get histological types
# Pattern to extract barcode from Patient_description
pattern = re.compile(r"TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}")

total_per_hist = defaultdict(int)
mutated_per_hist = defaultdict(int)

for rec in clinical_data:
    desc = rec.get('Patient_description', '')
    hist_type = rec.get('histological_type', '')
    
    if not hist_type:
        continue
    
    # Check if patient is alive: days_to_death should be "[Not Applicable]" or similar
    # The description says "Alive" for alive patients
    if 'Alive' not in desc:
        continue
    
    # Find barcode
    m = pattern.search(desc)
    if not m:
        continue
    
    barcode = m.group(0)
    total_per_hist[hist_type] += 1
    
    if barcode in cdh1_participants:
        mutated_per_hist[hist_type] += 1

# Compute percentages
results = []
for ht, total in total_per_hist.items():
    if total == 0:
        continue
    mutated = mutated_per_hist.get(ht, 0)
    perc = (mutated / total) * 100
    results.append({
        'histological_type': ht,
        'total_patients': total,
        'cdh1_mutated_patients': mutated,
        'percentage': round(perc, 2)
    })

# Sort by percentage desc
results.sort(key=lambda x: x['percentage'], reverse=True)

# Top 3
top3 = results[:3]

print('__RESULT__:')
print(json.dumps(top3, indent=2))"""

env_args = {'var_functions.query_db:0': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}], 'var_functions.query_db:2': [{'column_name': 'Patient_description'}, {'column_name': 'patient_id'}, {'column_name': 'patient_death_reason'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'person_neoplasm_cancer_status': 'TUMOR FREE'}, {'person_neoplasm_cancer_status': 'WITH TUMOR'}, {'person_neoplasm_cancer_status': '[Discrepancy]'}, {'person_neoplasm_cancer_status': '[Unknown]'}, {'person_neoplasm_cancer_status': 'None'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'count': 39, 'sample': ['f', 'i']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': [{'histological_type': 'Infiltrating Lobular Carcinoma', 'total_patients': 178, 'cdh1_mutated_patients': 90, 'percentage': 50.56}, {'histological_type': 'Mixed Histology (please specify)', 'total_patients': 24, 'cdh1_mutated_patients': 4, 'percentage': 16.67}, {'histological_type': 'Other  specify', 'total_patients': 36, 'cdh1_mutated_patients': 3, 'percentage': 8.33}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
