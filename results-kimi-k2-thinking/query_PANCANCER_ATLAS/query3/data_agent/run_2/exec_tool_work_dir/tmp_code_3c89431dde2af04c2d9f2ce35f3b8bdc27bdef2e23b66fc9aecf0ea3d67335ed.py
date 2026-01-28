code = """import json, re, math

# Load bladder cancer clinical data
with open('/mnt/data/var_functions.query_db:64.json', 'r') as f:
    bladder_clinical = json.load(f)

# Load CDH1 mutation data
with open('/mnt/data/var_functions.query_db:40.json', 'r') as f:
    cdh1_mutations = json.load(f)

print('Bladder cancer clinical records: ' + str(len(bladder_clinical)))
print('CDH1 mutations (PASS): ' + str(len(cdh1_mutations)))

# Get CDH1 mutated patients
cdh1_patients = set(m['ParticipantBarcode'] for m in cdh1_mutations)

# Extract female bladder cancer patients
female_bladder = {}
for rec in bladder_clinical:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', '')
    
    if 'FEMALE' in desc:
        m = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
        if m:
            barcode = m.group(0)
            female_bladder[barcode] = hist

print('Female bladder patients: ' + str(len(female_bladder)))

# Build contingency table: histological type vs CDH1 mutation status
contingency = {}
for barcode, hist in female_bladder.items():
    if not hist or hist == 'None':
        continue
    has_cdh1 = barcode in cdh1_patients
    
    if hist not in contingency:
        contingency[hist] = {'CDH1_mutated': 0, 'CDH1_wildtype': 0}
    
    if has_cdh1:
        contingency[hist]['CDH1_mutated'] += 1
    else:
        contingency[hist]['CDH1_wildtype'] += 1

# Filter categories with marginal totals > 10
filtered = {}
for hist, counts in contingency.items():
    total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
    if total > 10:
        filtered[hist] = counts
        print(hist + ': total=' + str(total) + ', mut=' + str(counts['CDH1_mutated']) + ', wt=' + str(counts['CDH1_wildtype']))

print('Filtered histological types: ' + str(len(filtered)))

# Calculate chi-square statistic
grand_total = sum(c['CDH1_mutated'] + c['CDH1_wildtype'] for c in filtered.values())
total_mutated = sum(c['CDH1_mutated'] for c in filtered.values())
total_wildtype = sum(c['CDH1_wildtype'] for c in filtered.values())

print('Grand total: ' + str(grand_total))
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

print('Chi-square statistic: ' + str(round(chi_square,4)))

result = {
    'chi_square_statistic': chi_square,
    'filtered_contingency_table': filtered,
    'total_patients': grand_total
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
