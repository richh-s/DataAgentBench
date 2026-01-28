code = """import json
import math
import pandas as pd

# Load data from storage
clinical_file = locals().get('var_functions.query_db:10')
molecular_file = locals().get('var_functions.query_db:18')

if not clinical_file or not molecular_file:
    print('__RESULT__:')
    print(json.dumps({'error': 'File paths not found in storage'}))
else:
    # Load clinical data (LGG patients)
    with open(clinical_file, 'r') as f:
        clinical_data = json.load(f)
    
    # Load IGF2 expression data
    with open(molecular_file, 'r') as f:
        molecular_data = json.load(f)
    
    # Create clinical dataframe
    lgg_patients = []
    import re
    for record in clinical_data:
        if 'histological_type' not in record:
            continue
        histology = record['histological_type']
        # Skip histology enclosed in square brackets
        if histology.startswith('[') and histology.endswith(']'):
            continue
        
        # Parse patient barcode from Patient_description
        desc = record.get('Patient_description', '')
        barcode_match = re.search(r'TCGA-[A-Z0-9]+-[A-Z0-9]+', desc)
        if barcode_match:
            barcode = barcode_match.group(0)
            lgg_patients.append({
                'ParticipantBarcode': barcode,
                'histological_type': histology
            })
    
    clinical_df = pd.DataFrame(lgg_patients)
    
    # Create molecular dataframe
    molecular_df = pd.DataFrame(molecular_data)
    
    # Convert normalized_count to numeric
    molecular_df['normalized_count'] = pd.to_numeric(molecular_df['normalized_count'], errors='coerce')
    
    # Filter for valid expression values
    molecular_df = molecular_df.dropna(subset=['normalized_count'])
    molecular_df = molecular_df[molecular_df['normalized_count'] >= 0]
    
    # Join datasets on ParticipantBarcode
    merged_df = clinical_df.merge(molecular_df, on='ParticipantBarcode', how='inner')
    
    # Compute log10(n + 1) transformation and group by histology
    merged_df['log10_expression'] = merged_df['normalized_count'].apply(lambda x: math.log10(x + 1))
    
    # Group by histological type and compute mean
    results = merged_df.groupby('histological_type')['log10_expression'].agg(['count', 'mean']).reset_index()
    results = results.round({'mean': 4, 'count': 0})
    
    result_dict = results.to_dict('records')
    
    print('__RESULT__:')
    print(json.dumps(result_dict, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'patient_count': 544, 'unique_histologies': ['Paraganglioma; Extra-adrenal Pheochromocytoma', 'Oligoastrocytoma', 'Oligodendroglioma', 'Paraganglioma', 'Astrocytoma'], 'sample_patients': [{'ParticipantBarcode': 'TCGA-RY-A83X', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-FG-A60K', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XH', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XE', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XC', 'histological_type': 'Oligoastrocytoma'}]}, 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'SampleBarcode': 'TCGA-A8-A082-01A', 'AliquotBarcode': 'TCGA-A8-A082-01A-11R-A00Z-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'SampleBarcode': 'TCGA-B5-A3FA-01A', 'AliquotBarcode': 'TCGA-B5-A3FA-01A-11R-A19W-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'SampleBarcode': 'TCGA-BH-A1EX-01A', 'AliquotBarcode': 'TCGA-BH-A1EX-01A-11R-A13Q-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'SampleBarcode': 'TCGA-BT-A20O-01A', 'AliquotBarcode': 'TCGA-BT-A20O-01A-21R-A14Y-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'SampleBarcode': 'TCGA-CD-5799-01A', 'AliquotBarcode': 'TCGA-CD-5799-01A-11R-1602-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '3936.02070028943'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
