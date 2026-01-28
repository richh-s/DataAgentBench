code = """import json, re, math

# Load bladder cancer clinical data
bladder_file = '/mnt/data/var_functions.query_db:64.json'
print('Loading bladder cancer data...')
with open(bladder_file, 'r') as f:
    bladder_clinical = json.load(f)

# Load CDH1 mutation data
cdh1_file = '/mnt/data/var_functions.query_db:40.json'
print('Loading CDH1 mutation data...')
with open(cdh1_file, 'r') as f:
    cdh1_mutations = json.load(f)

print('Bladder cancer records: ' + str(len(bladder_clinical)))
print('CDH1 mutations: ' + str(len(cdh1_mutations)))

# Extract female bladder cancer patients and their histological types
female_bladder = {}
cdh1_patients = set(m['ParticipantBarcode'] for m in cdh1_mutations)

for rec in bladder_clinical:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', '')
    
    # Check for female patients
    if 'FEMALE' in desc:
        # Extract barcode
        m = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
        if m:
            barcode = m.group(0)
            female_bladder[barcode] = hist

print('Female bladder patients: ' + str(len(female_bladder)))

# Build contingency table: histological type vs CDH1 mutation status
contingency = {}
for barcode, hist in female_bladder.items():
    # Skip missing or None histological types
    if not hist or hist == 'None':
        continue
        
    has_cdh1 = barcode in cdh1_patients
    
    if hist not in contingency:
        contingency[hist] = {'CDH1_mutated': 0, 'CDH1_wildtype': 0}
    
    if has_cdh1:
        contingency[hist]['CDH1_mutated'] += 1
    else:
        contingency[hist]['CDH1_wildtype'] += 1

# Show all histological types before filtering
print('\nAll histological types:')
for hist, counts in sorted(contingency.items(), key=lambda x: x[1]['CDH1_mutated'] + x[1]['CDH1_wildtype'], reverse=True):
    total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
    print(hist + ': total=' + str(total) + ', CDH1_mut=' + str(counts['CDH1_mutated']) + ', CDH1_wt=' + str(counts['CDH1_wildtype']))

# Filter out categories with marginal totals <= 10
filtered = {}
for hist, counts in contingency.items():
    total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
    if total > 10:
        filtered[hist] = counts

print('\nFiltered histological types (total > 10):')
for hist, counts in filtered.items():
    total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
    print(hist + ': total=' + str(total))

print('\nNumber of filtered categories: ' + str(len(filtered)))

# If we have multiple categories, calculate chi-square
if len(filtered) >= 2:
    # Calculate chi-square statistic
    grand_total = sum(c['CDH1_mutated'] + c['CDH1_wildtype'] for c in filtered.values())
    total_mutated = sum(c['CDH1_mutated'] for c in filtered.values())
    total_wildtype = sum(c['CDH1_wildtype'] for c in filtered.values())
    
    print('\nGrand total: ' + str(grand_total))
    print('Total CDH1 mutated: ' + str(total_mutated))
    print('Total CDH1 wildtype: ' + str(total_wildtype))
    
    chi_square = 0.0
    for hist, obs in filtered.items():
        row_total = obs['CDH1_mutated'] + obs['CDH1_wildtype']
        expected_mutated = (row_total * total_mutated) / grand_total
        expected_wildtype = (row_total * total_wildtype) / grand_total
        
        chi_square += ((obs['CDH1_mutated'] - expected_mutated) ** 2) / expected_mutated
        chi_square += ((obs['CDH1_wildtype'] - expected_wildtype) ** 2) / expected_wildtype
        
        print(hist + ': O=(' + str(obs['CDH1_mutated']) + ',' + str(obs['CDH1_wildtype']) + '), E=(' + str(round(expected_mutated,2)) + ',' + str(round(expected_wildtype,2)) + ')')
    
    print('\nChi-square statistic: ' + str(round(chi_square,4)))
else:
    print('\nInsufficient categories for chi-square test (need at least 2 categories with >10 patients each)')
    chi_square = 0.0

result = {
    'chi_square_statistic': chi_square,
    'filtered_contingency_table': filtered,
    'total_patients_analyzed': sum(c['CDH1_mutated'] + c['CDH1_wildtype'] for c in filtered.values()),
    'total_female_bladder_patients': len(female_bladder)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.list_db:76': ['clinical_info'], 'var_functions.list_db:80': ['clinical_info'], 'var_functions.query_db:82': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:84': [], 'var_functions.execute_python:96': {'chi_square_statistic': 0.0, 'contingency_table': {'Muscle invasive urothelial carcinoma (pT2 or above)': {'CDH1_mutated': 3, 'CDH1_wildtype': 47}}, 'total_patients': 50}}

exec(code, env_args)
