code = """import json
import re
from collections import Counter

# Initialize variables
brca_alive_patients = []
cdh1_mutation_patients = []

# Access BRCA alive patients data
try:
    # Try to get from the variable directly
    if 'var_functions.query_db:30' in locals():
        data1 = locals()['var_functions.query_db:30']
        if isinstance(data1, str) and data1.endswith('.json'):
            with open(data1, 'r') as f:
                brca_alive_patients = json.load(f)
        elif isinstance(data1, list):
            brca_alive_patients = data1
        print(f"Loaded BRCA alive patients: {len(brca_alive_patients)}")
    else:
        print("BRCA alive patients data not found in locals")
except Exception as e:
    print(f"Error loading BRCA data: {e}")

# Access CDH1 mutation patients data
try:
    if 'var_functions.query_db:44' in locals():
        data2 = locals()['var_functions.query_db:44']
        if isinstance(data2, str) and data2.endswith('.json'):
            with open(data2, 'r') as f:
                cdh1_mutation_patients = json.load(f)
        elif isinstance(data2, list):
            cdh1_mutation_patients = data2
        print(f"Loaded CDH1 mutation patients: {len(cdh1_mutation_patients)}")
    else:
        print("CDH1 mutation patients data not found in locals")
except Exception as e:
    print(f"Error loading CDH1 data: {e}")

# Debug info
print(f"BRCA data type: {type(brca_alive_patients)}")
print(f"CDH1 data type: {type(cdh1_mutation_patients)}")

if brca_alive_patients and cdh1_mutation_patients:
    # Extract BRCA alive patients barcodes and histology
    brca_alive_histology = {}
    brca_alive_barcodes = set()
    
    for record in brca_alive_patients:
        if isinstance(record, dict):
            patient_desc = record.get('Patient_description', '')
            hist_type = record.get('histological_type', '')
            
            # Extract barcode
            barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', patient_desc)
            if barcode_match:
                barcode = barcode_match.group(1)
                brca_alive_barcodes.add(barcode)
                brca_alive_histology[barcode] = hist_type
    
    print(f"Total BRCA alive patients: {len(brca_alive_barcodes)}")
    
    # Extract CDH1 mutation patient barcodes
    cdh1_patient_barcodes = set()
    for record in cdh1_mutation_patients:
        if isinstance(record, dict) and 'ParticipantBarcode' in record:
            cdh1_patient_barcodes.add(record['ParticipantBarcode'])
    
    print(f"Total CDH1 mutation patients: {len(cdh1_patient_barcodes)}")
    
    # Find intersection
    cdh1_brca_alive = cdh1_patient_barcodes.intersection(brca_alive_barcodes)
    print(f"CDH1 mutated BRCA alive patients: {len(cdh1_brca_alive)}")
    
    # Count by histology
    cdh1_histology_counts = Counter()
    for barcode in cdh1_brca_alive:
        hist_type = brca_alive_histology.get(barcode, 'Unknown')
        cdh1_histology_counts[hist_type] += 1
    
    # Total by histology
    total_by_histology = Counter(brca_alive_histology.values())
    
    # Calculate percentages
    histology_percentages = {}
    for hist_type, total_count in total_by_histology.items():
        cdh1_count = cdh1_histology_counts[hist_type]
        if total_count > 0:
            percentage = (cdh1_count / total_count) * 100
            histology_percentages[hist_type] = {
                'percentage': percentage,
                'cdh1_count': cdh1_count,
                'total_count': total_count
            }
    
    # Get top 3
    top_3 = sorted(histology_percentages.items(), 
                   key=lambda x: x[1]['percentage'], 
                   reverse=True)[:3]
    
    print("\nTop 3 histological types by CDH1 mutation percentage:")
    for i, (hist_type, data) in enumerate(top_3, 1):
        print(f"  {i}. {hist_type}: {data['percentage']:.2f}% "
              f"({data['cdh1_count']}/{data['total_count']} patients)")
    
    result = {
        'top_3': [(h, d['percentage'], d['cdh1_count'], d['total_count']) 
                  for h, d in top_3],
        'summary': {
            'total_brca_alive': len(brca_alive_barcodes),
            'cdh1_mutated_brca_alive': len(cdh1_brca_alive)
        }
    }
    
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print("Data not loaded properly")
    print('__RESULT__:')
    print(json.dumps({'error': 'Data loading failed'}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:7': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_rows': '10761'}], 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Tumor_SampleBarcode': 'TCGA-A8-A091-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A091-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A091-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A091-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E243K', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.727G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Tumor_SampleBarcode': 'TCGA-A8-A0A1-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A1-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A1-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A1-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q307Hfs*2', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.921_955delAGATCCTGAGCTCCCTGACAAAAATATGTTCACCA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Tumor_SampleBarcode': 'TCGA-A8-A0A9-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A9-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A9-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A9-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q503*', 'Variant_Classification': 'Nonsense_Mutation', 'HGVSc': 'c.1507C>T', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Tumor_SampleBarcode': 'TCGA-AA-3821-01A', 'Tumor_AliquotBarcode': 'TCGA-AA-3821-01A-01W-0995-10', 'Normal_SampleBarcode': 'TCGA-AA-3821-10A', 'Normal_AliquotBarcode': 'TCGA-AA-3821-10A-01W-0995-10', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V365I', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1093G>A', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Tumor_SampleBarcode': 'TCGA-A2-A0YL-01A', 'Tumor_AliquotBarcode': 'TCGA-A2-A0YL-01A-21D-A10G-09', 'Normal_SampleBarcode': 'TCGA-A2-A0YL-10A', 'Normal_AliquotBarcode': 'TCGA-A2-A0YL-10A-01D-A10G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.1090_1100delACAGTCACTGA', 'CENTERS': 'INDELOCATOR*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Tumor_SampleBarcode': 'TCGA-AR-A1AT-01A', 'Tumor_AliquotBarcode': 'TCGA-AR-A1AT-01A-11D-A12Q-09', 'Normal_SampleBarcode': 'TCGA-AR-A1AT-10A', 'Normal_AliquotBarcode': 'TCGA-AR-A1AT-10A-01D-A12Q-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.N315Ifs*41', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.944delA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Tumor_SampleBarcode': 'TCGA-BS-A0U8-01A', 'Tumor_AliquotBarcode': 'TCGA-BS-A0U8-01A-11D-A10B-09', 'Normal_SampleBarcode': 'TCGA-BS-A0U8-10A', 'Normal_AliquotBarcode': 'TCGA-BS-A0U8-10A-01D-A10B-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.A824V', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.2471C>T', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Tumor_SampleBarcode': 'TCGA-D8-A27G-01A', 'Tumor_AliquotBarcode': 'TCGA-D8-A27G-01A-11D-A16D-09', 'Normal_SampleBarcode': 'TCGA-D8-A27G-10A', 'Normal_AliquotBarcode': 'TCGA-D8-A27G-10A-01D-A16D-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.G169Rfs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.504dupA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Tumor_SampleBarcode': 'TCGA-E6-A1LX-01A', 'Tumor_AliquotBarcode': 'TCGA-E6-A1LX-01A-11D-A14G-09', 'Normal_SampleBarcode': 'TCGA-E6-A1LX-10A', 'Normal_AliquotBarcode': 'TCGA-E6-A1LX-10A-01D-A14G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R598Q', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1793G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Tumor_SampleBarcode': 'TCGA-EJ-7782-01A', 'Tumor_AliquotBarcode': 'TCGA-EJ-7782-01A-11D-2114-08', 'Normal_SampleBarcode': 'TCGA-EJ-7782-10A', 'Normal_AliquotBarcode': 'TCGA-EJ-7782-10A-01D-2114-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.L249V', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.745T>G', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'PASS'}], 'var_functions.query_db:20': [], 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'brca_count': '0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
