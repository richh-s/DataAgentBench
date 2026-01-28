code = """import json, re

# Read clinical data (note: the file is at /mnt/data, not /tmp)
clinical_file = open('/mnt/data/var_functions.query_db:22.json', 'r')
clinical_data = json.load(clinical_file)
clinical_file.close()

# Read CDH1 mutation data
cdh1_file = open('/mnt/data/var_functions.query_db:40.json', 'r')
cdh1_mutations = json.load(cdh1_file)
cdh1_file.close()

print('Clinical records:', len(clinical_data))
print('CDH1 mutations (PASS):', len(cdh1_mutations))

# Extract female BRCA patients
female_brca = {}
for rec in clinical_data:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', '')
    
    # Check for female BRCA patients
    if 'FEMALE' in desc and ('BRCA' in desc or 'breast' in desc.lower()):
        m = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
        if m:
            barcode = m.group(0)
            female_brca[barcode] = hist

print('Female BRCA patients:', len(female_brca))

# Get CDH1 mutated patients
cdh1_patients = set(m['ParticipantBarcode'] for m in cdh1_mutations)
print('Total CDH1-mutated patients:', len(cdh1_patients))

# Find overlap: BRCA patients with CDH1 mutations
brca_with_cdh1 = female_brca.keys() & cdh1_patients
brca_without_cdh1 = female_brca.keys() - cdh1_patients

print('BRCA with CDH1 mutation:', len(brca_with_cdh1))
print('BRCA without CDH1 mutation:', len(brca_without_cdh1))

# Build contingency table: histological type vs CDH1 status
contingency_table = {}

for barcode in female_brca:
    hist = female_brca[barcode]
    has_cdh1 = barcode in cdh1_patients
    
    if hist not in contingency_table:
        contingency_table[hist] = {'CDH1_mutated': 0, 'CDH1_wildtype': 0}
    
    if has_cdh1:
        contingency_table[hist]['CDH1_mutated'] += 1
    else:
        contingency_table[hist]['CDH1_wildtype'] += 1

# Count histotype frequencies
hist_counts = {}
for hist in female_brca.values():
    hist_counts[hist] = hist_counts.get(hist, 0) + 1

print('\nHistological types (frequency):')
for hist, count in sorted(hist_counts.items(), key=lambda x: x[1], reverse=True):
    if count >= 5:  # Show types with at least 5 patients
        print(f'  {hist}: {count}')

result = {
    'female_brca_count': len(female_brca),
    'cdh1_mutated_in_brca': len(brca_with_cdh1),
    'contingency_table': contingency_table,
    'hist_distribution': hist_counts
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
