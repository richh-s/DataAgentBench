code = """import json, re

# Read the clinical data
with open('/tmp/var_functions.query_db:22.json', 'r') as f:
    clinical_data = json.load(f)

print('Total clinical records: ' + str(len(clinical_data)))

# Extract female BRCA patients
female_brca_patients = {}
all_histological_types = {}

for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', '')
    
    # Check if female
    if 'FEMALE' not in desc:
        continue
    
    # Check if breast cancer (BRCA)
    if 'BRCA' in desc or 'breast' in desc.lower() or 'Breast' in desc:
        # Extract barcode
        barcode_match = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
        if barcode_match:
            barcode = barcode_match.group(0)
            female_brca_patients[barcode] = {
                'histological_type': hist_type,
                'description': desc
            }
    
    # Count all histological types for reference
    if hist_type:
        all_histological_types[hist_type] = all_histological_types.get(hist_type, 0) + 1

print('Female BRCA patients found: ' + str(len(female_brca_patients)))
print('\nHistological types among female BRCA patients:')
hist_counter = {}
for patient in female_brca_patients.values():
    hist = patient['histological_type']
    hist_counter[hist] = hist_counter.get(hist, 0) + 1

for hist, count in sorted(hist_counter.items(), key=lambda x: x[1], reverse=True):
    print('  ' + hist + ': ' + str(count))

print('\nAll histological types in database (top 20):')
for hist, count in sorted(all_histological_types.items(), key=lambda x: x[1], reverse=True)[:20]:
    print('  ' + hist + ': ' + str(count))

# Save the female BRCA patient barcodes for next step
brca_barcodes = list(female_brca_patients.keys())
print('\nSample BRCA barcodes: ' + str(brca_barcodes[:10]))

# Store results
result = {
    'female_brca_patients': female_brca_patients,
    'brca_barcodes': brca_barcodes,
    'hist_type_counts': hist_counter
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}]}

exec(code, env_args)
