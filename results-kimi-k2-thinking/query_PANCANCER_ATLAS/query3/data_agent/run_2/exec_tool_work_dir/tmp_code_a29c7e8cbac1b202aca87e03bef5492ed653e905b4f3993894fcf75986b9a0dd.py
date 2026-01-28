code = """import json, re

# Load the bladder cancer clinical data
bladder_clinical_file = open('/mnt/data/var_functions.query_db:64.json', 'r')
bladder_clinical = json.load(bladder_clinical_file)
bladder_clinical_file.close()

# Load CDH1 mutation data
cdh1_file = open('/mnt/data/var_functions.query_db:40.json', 'r')
cdh1_mutations = json.load(cdh1_file)
cdh1_file.close()

print('Bladder cancer clinical records:', len(bladder_clinical))
print('CDH1 mutations (PASS):', len(cdh1_mutations))

# Extract female BRCA (bladder) patients
female_bladder_patients = {}
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
            female_bladder_patients[barcode] = hist

print('Female bladder patients:', len(female_bladder_patients))

# Build contingency table: histological type vs CDH1 mutation status
contingency_table = {}
for barcode, hist in female_bladder_patients.items():
    # Skip missing histological types
    if not hist or hist == 'None':
        continue
        
    has_cdh1 = barcode in cdh1_patients
    
    if hist not in contingency_table:
        contingency_table[hist] = {'CDH1_mutated': 0, 'CDH1_wildtype': 0}
    
    if has_cdh1:
        contingency_table[hist]['CDH1_mutated'] += 1
    else:
        contingency_table[hist]['CDH1_wildtype'] += 1

# Filter out categories with marginal totals <= 10
filtered_table = {}
for hist, counts in contingency_table.items():
    total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
    if total > 10:
        filtered_table[hist] = counts
        print(f"{hist}: total={total}, CDH1_mutated={counts['CDH1_mutated']}, CDH1_wildtype={counts['CDH1_wildtype']}")

print('\nFiltered histological types:', len(filtered_table))

# Calculate chi-square statistic
import math

# Calculate totals
grand_total = sum(counts['CDH1_mutated'] + counts['CDH1_wildtype'] for counts in filtered_table.values())
total_mutated = sum(counts['CDH1_mutated'] for counts in filtered_table.values())
total_wildtype = sum(counts['CDH1_wildtype'] for counts in filtered_table.values())

print(f'Grand total: {grand_total}')
print(f'Total CDH1 mutated: {total_mutated}')
print(f'Total CDH1 wildtype: {total_wildtype}')

# Calculate chi-square
chi_square = 0
for hist, observed in filtered_table.items():
    row_total = observed['CDH1_mutated'] + observed['CDH1_wildtype']
    
    # Expected values
    expected_mutated = (row_total * total_mutated) / grand_total
    expected_wildtype = (row_total * total_wildtype) / grand_total
    
    # Chi-square contributions
    chi_square += ((observed['CDH1_mutated'] - expected_mutated) ** 2) / expected_mutated
    chi_square += ((observed['CDH1_wildtype'] - expected_wildtype) ** 2) / expected_wildtype
    
    print(f"{hist}: O=({observed['CDH1_mutated']},{observed['CDH1_wildtype']}), E=({expected_mutated:.2f},{expected_wildtype:.2f})")

print(f'\nChi-square statistic: {chi_square:.4f}')

result = {
    'chi_square_statistic': chi_square,
    'filtered_table': filtered_table,
    'total_patients': grand_total
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
