code = """import json, re

# Read clinical data (note: file is at /mnt/data, not /tmp)
clinical_file = open('/mnt/data/var_functions.query_db:52.json', 'r')
clinical_data = json.load(clinical_file)
clinical_file.close()

# Read CDH1 mutation data
cdh1_file = open('/mnt/data/var_functions.query_db:40.json', 'r')
cdh1_mutations = json.load(cdh1_file)
cdh1_file.close()

print('Clinical records:', len(clinical_data))
print('CDH1 mutations (PASS):', len(cdh1_mutations))

# Find female patients with various cancer types
female_patients = {}
for rec in clinical_data:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', '')
    
    # Check for female patients
    if 'FEMALE' in desc:
        # Extract barcode
        barcode_match = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
        if barcode_match:
            barcode = barcode_match.group(0)
            female_patients[barcode] = {
                'description': desc,
                'histological_type': hist
            }

print('Total female patients:', len(female_patients))

# Look for bladder cancer patients
bladder_patients = {}
for barcode, info in female_patients.items():
    desc = info['description']
    hist = info['histological_type']
    
    # Check for bladder cancer mentions
    if ('bladder' in desc.lower() or 'BRCA' in desc or 
        'urothelial' in desc.lower() or 'Urothelial' in hist):
        bladder_patients[barcode] = hist

print('Bladder cancer patients (female):', len(bladder_patients))

# Get CDH1 mutated patients
cdh1_patients = set(m['ParticipantBarcode'] for m in cdh1_mutations)

# Find bladder patients with and without CDH1 mutations
bladder_with_cdh1 = bladder_patients.keys() & cdh1_patients
bladder_without_cdh1 = bladder_patients.keys() - cdh1_patients

print('Bladder patients with CDH1 mutation:', len(bladder_with_cdh1))
print('Bladder patients without CDH1 mutation:', len(bladder_without_cdh1))

# Show some examples
print('\nSample bladder cancer patient descriptions:')
count = 0
for barcode, hist in list(bladder_patients.items())[:10]:
    desc = female_patients[barcode]['description']
    has_cdh1 = barcode in cdh1_patients
    print(f'  {barcode}: {hist}')
    print(f'    CDH1 mutated: {has_cdh1}')
    print(f'    Desc: {desc[:120]}...')
    print()
    count += 1
    if count >= 5:
        break

result = {
    'female_bladder_count': len(bladder_patients),
    'cdh1_mutated_in_bladder': len(bladder_with_cdh1),
    'bladder_patients': list(bladder_patients.keys())
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
