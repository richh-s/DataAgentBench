code = """import json
import re
from collections import Counter

# Load the data from the files
brca_file = 'var_functions.query_db:56'
cdh1_file = 'var_functions.query_db:44'

# Read BRCA alive patients
with open(brca_file, 'r') as f:
    brca_data = f.read()
    brca_patients = json.loads(brca_data)

print(f'BRCA alive patients count: {len(brca_patients)}')

# Read CDH1 mutation patients  
with open(cdh1_file, 'r') as f:
    cdh1_data = f.read()
    cdh1_patients = json.loads(cdh1_data)

print(f'CDH1 mutation patients count: {len(cdh1_patients)}')

# Extract BRCA patient barcodes and histology
brca_barcodes = set()
brca_histology_map = {}

for patient in brca_patients:
    desc = patient.get('Patient_description', '')
    hist = patient.get('histological_type', 'Unknown')
    
    # Extract barcode
    match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if match:
        barcode = match.group(1)
        brca_barcodes.add(barcode)
        brca_histology_map[barcode] = hist

print(f'BRCA unique patients: {len(brca_barcodes)}')

# Extract CDH1 mutation barcodes
cdh1_barcodes = set()
for patient in cdh1_patients:
    barcode = patient.get('ParticipantBarcode', '')
    if barcode:
        cdh1_barcodes.add(barcode)

print(f'CDH1 mutation patients: {len(cdh1_barcodes)}')

# Find intersection - patients who are both BRCA alive and have CDH1 mutations
common_barcodes = brca_barcodes.intersection(cdh1_barcodes)
print(f'BRCA alive + CDH1 mutation: {len(common_barcodes)}')

# Count by histology for all BRCA alive patients
total_by_histology = Counter(brca_histology_map.values())

# Count by histology for CDH1 mutated BRCA alive patients
cdh1_by_histology = Counter()
for barcode in common_barcodes:
    hist_type = brca_histology_map.get(barcode, 'Unknown')
    cdh1_by_histology[hist_type] += 1

print(f'\nTotal BRCA patients by histology (top 10):')
for hist, count in total_by_histology.most_common(10):
    print(f'  {hist}: {count}')

print(f'\nCDH1 mutated BRCA patients by histology:')
for hist, count in cdh1_by_histology.most_common():
    total = total_by_histology.get(hist, 0)
    if total > 0:
        pct = (count / total) * 100
        print(f'  {hist}: {count}/{total} ({pct:.2f}%)')

# Calculate percentages for histology types with at least 3 patients
results = []
for hist_type, total_count in total_by_histology.items():
    if total_count >= 3:  # Minimum threshold
        cdh1_count = cdh1_by_histology.get(hist_type, 0)
        percentage = (cdh1_count / total_count) * 100
        results.append({
            'histological_type': hist_type,
            'percentage': round(percentage, 2),
            'cdh1_mutated_count': cdh1_count,
            'total_count': total_count
        })

# Sort by percentage descending
results_sorted = sorted(results, key=lambda x: x['percentage'], reverse=True)

print(f'\nTop histological types by CDH1 mutation percentage:')
for i, item in enumerate(results_sorted[:5], 1):
    print(f"  {i}. {item['histological_type']}: {item['percentage']}% "
          f"({item['cdh1_mutated_count']}/{item['total_count']} patients)")

top_3 = results_sorted[:3]

output = {
    'top_3_histological_types': top_3,
    'statistics': {
        'total_brca_alive_patients': len(brca_barcodes),
        'total_cdh1_mutated_brca_alive': len(common_barcodes),
        'histological_types_analyzed': len(total_by_histology)
    }
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:7': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_rows': '10761'}], 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Tumor_SampleBarcode': 'TCGA-A8-A091-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A091-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A091-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A091-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E243K', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.727G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Tumor_SampleBarcode': 'TCGA-A8-A0A1-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A1-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A1-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A1-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q307Hfs*2', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.921_955delAGATCCTGAGCTCCCTGACAAAAATATGTTCACCA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Tumor_SampleBarcode': 'TCGA-A8-A0A9-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A9-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A9-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A9-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q503*', 'Variant_Classification': 'Nonsense_Mutation', 'HGVSc': 'c.1507C>T', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Tumor_SampleBarcode': 'TCGA-AA-3821-01A', 'Tumor_AliquotBarcode': 'TCGA-AA-3821-01A-01W-0995-10', 'Normal_SampleBarcode': 'TCGA-AA-3821-10A', 'Normal_AliquotBarcode': 'TCGA-AA-3821-10A-01W-0995-10', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V365I', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1093G>A', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Tumor_SampleBarcode': 'TCGA-A2-A0YL-01A', 'Tumor_AliquotBarcode': 'TCGA-A2-A0YL-01A-21D-A10G-09', 'Normal_SampleBarcode': 'TCGA-A2-A0YL-10A', 'Normal_AliquotBarcode': 'TCGA-A2-A0YL-10A-01D-A10G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.1090_1100delACAGTCACTGA', 'CENTERS': 'INDELOCATOR*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Tumor_SampleBarcode': 'TCGA-AR-A1AT-01A', 'Tumor_AliquotBarcode': 'TCGA-AR-A1AT-01A-11D-A12Q-09', 'Normal_SampleBarcode': 'TCGA-AR-A1AT-10A', 'Normal_AliquotBarcode': 'TCGA-AR-A1AT-10A-01D-A12Q-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.N315Ifs*41', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.944delA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Tumor_SampleBarcode': 'TCGA-BS-A0U8-01A', 'Tumor_AliquotBarcode': 'TCGA-BS-A0U8-01A-11D-A10B-09', 'Normal_SampleBarcode': 'TCGA-BS-A0U8-10A', 'Normal_AliquotBarcode': 'TCGA-BS-A0U8-10A-01D-A10B-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.A824V', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.2471C>T', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Tumor_SampleBarcode': 'TCGA-D8-A27G-01A', 'Tumor_AliquotBarcode': 'TCGA-D8-A27G-01A-11D-A16D-09', 'Normal_SampleBarcode': 'TCGA-D8-A27G-10A', 'Normal_AliquotBarcode': 'TCGA-D8-A27G-10A-01D-A16D-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.G169Rfs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.504dupA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Tumor_SampleBarcode': 'TCGA-E6-A1LX-01A', 'Tumor_AliquotBarcode': 'TCGA-E6-A1LX-01A-11D-A14G-09', 'Normal_SampleBarcode': 'TCGA-E6-A1LX-10A', 'Normal_AliquotBarcode': 'TCGA-E6-A1LX-10A-01D-A14G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R598Q', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1793G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Tumor_SampleBarcode': 'TCGA-EJ-7782-01A', 'Tumor_AliquotBarcode': 'TCGA-EJ-7782-01A-11D-2114-08', 'Normal_SampleBarcode': 'TCGA-EJ-7782-10A', 'Normal_AliquotBarcode': 'TCGA-EJ-7782-10A-01D-2114-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.L249V', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.745T>G', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}], 'var_functions.query_db:20': [], 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'brca_count': '0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
