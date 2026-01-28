code = """import json
import re
from collections import defaultdict

# Load clinical data for alive BRCA patients
clinical_file = locals()['var_functions.query_db:14']
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Load CDH1 mutation data
mutation_file = locals()['var_functions.query_db:22']
with open(mutation_file, 'r') as f:
    mutation_data = json.load(f)

# Extract barcodes with CDH1 mutations (unique)
cdh1_barcodes = set()
for mut in mutation_data:
    if isinstance(mut, dict) and 'ParticipantBarcode' in mut:
        cdh1_barcodes.add(mut['ParticipantBarcode'])

# Build totals and mutated counts per histological type
total_per_hist = defaultdict(int)
mutated_per_hist = defaultdict(int)

pattern = re.compile(r"TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}")

for rec in clinical_data:
    desc = rec.get('Patient_description', '')
    hist_type = rec.get('histological_type')
    if not hist_type:
        continue
    # Try to find barcode
    m = pattern.search(desc)
    if not m:
        continue
    barcode = m.group(0)  # e.g., TCGA-AC-A5EH
    total_per_hist[hist_type] += 1
    if barcode in cdh1_barcodes:
        mutated_per_hist[hist_type] += 1

# Compute percentages and sort
results = []
for ht in total_per_hist.keys():
    total = total_per_hist[ht]
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

# Sort descending by percentage
results.sort(key=lambda x: x['percentage'], reverse=True)

# Get top 3
top3 = results[:3]

# Return JSON
print('__RESULT__:')
print(json.dumps(top3))"""

env_args = {'var_functions.query_db:0': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}], 'var_functions.query_db:2': [{'column_name': 'Patient_description'}, {'column_name': 'patient_id'}, {'column_name': 'patient_death_reason'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'person_neoplasm_cancer_status': 'TUMOR FREE'}, {'person_neoplasm_cancer_status': 'WITH TUMOR'}, {'person_neoplasm_cancer_status': '[Discrepancy]'}, {'person_neoplasm_cancer_status': '[Unknown]'}, {'person_neoplasm_cancer_status': 'None'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'count': 39, 'sample': ['f', 'i']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
