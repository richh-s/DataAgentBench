code = """import json, re

# Read clinical data
clinical_file = open('/mnt/data/var_functions.query_db:52.json', 'r')
clinical_data = json.load(clinical_file)
clinical_file.close()

# Read CDH1 mutation data
cdh1_file = open('/mnt/data/var_functions.query_db:40.json', 'r')
cdh1_mutations = json.load(cdh1_file)
cdh1_file.close()

print('Clinical records:', len(clinical_data))
print('CDH1 mutations (PASS):', len(cdh1_mutations))

# Find female patients and extract histological types
female_patients = {}
for rec in clinical_data:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', '')
    if 'FEMALE' in desc:
        barcode_match = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
        if barcode_match:
            barcode = barcode_match.group(0)
            female_patients[barcode] = {'desc': desc, 'hist': hist}

print('Total female patients:', len(female_patients))

# Find bladder cancer patients
bladder_patients = {}
for barcode, info in female_patients.items():
    desc = info['desc']
    hist = info['hist']
    is_bladder = ('bladder' in desc.lower() or 'BRCA' in desc or 
                  'urothelial' in desc.lower() or 'Urothelial' in hist)
    if is_bladder:
        bladder_patients[barcode] = hist

print('Bladder cancer patients (female):', len(bladder_patients))

# Get CDH1 mutated patients
cdh1_patients = set(m['ParticipantBarcode'] for m in cdh1_mutations)

# Build contingency table
contingency = {}
for barcode, hist in bladder_patients.items():
    has_cdh1 = barcode in cdh1_patients
    if hist not in contingency:
        contingency[hist] = {'CDH1_mutated': 0, 'CDH1_wildtype': 0}
    if has_cdh1:
        contingency[hist]['CDH1_mutated'] += 1
    else:
        contingency[hist]['CDH1_wildtype'] += 1

# Filter out histological types with total <= 10
filtered_contingency = {}
for hist, counts in contingency.items():
    total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
    if total > 10:
        filtered_contingency[hist] = counts

print('Histological types with >10 patients:', len(filtered_contingency))
for hist, cnt in sorted(filtered_contingency.items(), key=lambda x: x[1]['CDH1_mutated'] + x[1]['CDH1_wildtype'], reverse=True):
    print('  ' + hist + ': mutated=' + str(cnt['CDH1_mutated']) + ', wildtype=' + str(cnt['CDH1_wildtype']))

result = {
    'total_bladder_patients': len(bladder_patients),
    'contingency_table': filtered_contingency
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
