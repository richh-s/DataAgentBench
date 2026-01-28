code = """import json, re

print('Loading data files...', flush=True)

# Read clinical data
with open('/mnt/data/var_functions.query_db:52.json', 'r') as f:
    clinical_data = json.load(f)

# Read CDH1 mutation data  
with open('/mnt/data/var_functions.query_db:40.json', 'r') as f:
    cdh1_mutations = json.load(f)

print('Clinical records: %d' % len(clinical_data))
print('CDH1 mutations (PASS filter): %d' % len(cdh1_mutations))

# Store patient barcode to histological type mapping
patient_histotype = {}
female_bladder_patients = []

for rec in clinical_data:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', '')
    
    # Check for female bladder cancer patients
    if 'FEMALE' in desc:
        # Extract barcode
        m = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
        if m:
            barcode = m.group(0)
            patient_histotype[barcode] = hist
            
            # Check bladder cancer indicators
            bladder_indicators = ['bladder', 'BRCA', 'urothelial']
            desc_lower = desc.lower()
            hist_lower = hist.lower()
            
            if any(indicator in desc_lower or indicator in hist_lower for indicator in bladder_indicators):
                female_bladder_patients.append(barcode)

print('Female bladder cancer patients: %d' % len(female_bladder_patients))

# Get CDH1 mutated patients
cdh1_patients = set(m['ParticipantBarcode'] for m in cdh1_mutations)
print('CDH1-mutated patients in database: %d' % len(cdh1_patients))

# Build contingency table
contingency = {}
for barcode in female_bladder_patients:
    hist = patient_histotype.get(barcode, '')
    if not hist:  # Skip if no histological type
        continue
        
    has_cdh1 = 1 if barcode in cdh1_patients else 0
    
    if hist not in contingency:
        contingency[hist] = {'CDH1_mutated': 0, 'CDH1_wildtype': 0}
    
    if has_cdh1:
        contingency[hist]['CDH1_mutated'] += 1
    else:
        contingency[hist]['CDH1_wildtype'] += 1

print('Unique histological types: %d' % len(contingency))

# Filter categories with marginal totals <= 10
filtered_contingency = {}
for hist, counts in contingency.items():
    total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
    if total > 10:
        filtered_contingency[hist] = counts
        print('Type: %s, Total: %d, CDH1+: %d, CDH1-: %d' % 
              (hist, total, counts['CDH1_mutated'], counts['CDH1_wildtype']))

print('Filtered histological types (total>10): %d' % len(filtered_contingency))

result = {
    'bladder_patients': len(female_bladder_patients),
    'valid_histotypes': len(filtered_contingency),
    'contingency_table': filtered_contingency
}

print('
__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
