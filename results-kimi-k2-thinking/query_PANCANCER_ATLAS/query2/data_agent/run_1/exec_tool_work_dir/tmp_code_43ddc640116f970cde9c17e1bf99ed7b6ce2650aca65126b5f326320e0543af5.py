code = """import json
import pandas as pd
import re
import os

# The data is stored in a variable, let's check what's in the storage
print('Checking storage keys:', list(locals().keys()))

# Let's get the actual data - the previous query result is stored as a file path
# We need to read the file to get the data
if 'var_functions.query_db:20' in locals():
    file_path = locals()['var_functions.query_db:20']
    print('File path from storage:', file_path)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            clinical_data = json.load(f)
    else:
        print('File does not exist, let\'s try a different approach')
        clinical_data = []
else:
    print('No data found in storage')
    clinical_data = []

if clinical_data:
    df_clinical = pd.DataFrame(clinical_data)
    print('Number of records:', len(df_clinical))
    
    def extract_barcode(description):
        if not description:
            return None
        match = re.search(r'(TCGA-\d{2}-\d{4})', description)
        return match.group(1) if match else None
    
    def extract_cancer_type(description):
        if not description:
            return None
        match = re.search(r'In the ([^,]+?) dataset', description)
        if match:
            return match.group(1).strip()
        match = re.search(r'diagnosed with ([^,.]+)', description)
        return match.group(1).strip() if match else None
    
    def extract_vital_status(description):
        if not description:
            return None
        if 'vital status: Alive' in description or 'vital status = Alive' in description:
            return 'Alive'
        elif 'vital status: Dead' in description or 'vital status = Dead' in description:
            return 'Dead'
        return None
    
    df_clinical['barcode'] = df_clinical['Patient_description'].apply(extract_barcode)
    df_clinical['cancer_type'] = df_clinical['Patient_description'].apply(extract_cancer_type)
    df_clinical['vital_status'] = df_clinical['Patient_description'].apply(extract_vital_status)
    
    print('Total samples:', len(df_clinical))
    print('Samples with valid barcodes:', df_clinical['barcode'].notna().sum())
    
    # Filter BRCA samples
    brca_df = df_clinical[
        (df_clinical['cancer_type'].str.contains('BRCA', case=False, na=False)) |
        (df_clinical['cancer_type'].str.contains('Bladder', case=False, na=False)) |
        (df_clinical['cancer_type'].str.contains('Urothelial', case=False, na=False)) |
        (df_clinical['cancer_type'].str.contains('Breast', case=False, na=False))
    ]
    
    print('BRCA-related samples:', len(brca_df))
    
    # Filter for alive patients
    brca_alive = brca_df[brca_df['vital_status'] == 'Alive']
    print('Alive BRCA samples:', len(brca_alive))
    
    if not brca_alive.empty:
        print('Sample BRCA alive data:')
        print(brca_alive[['barcode', 'cancer_type', 'vital_status', 'histological_type']].head())
    
    result = {
        'brca_samples_total': int(len(brca_df)),
        'brca_alive': int(len(brca_alive)),
        'has_data': True
    }
else:
    result = {'has_data': False, 'message': 'No clinical data found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:15': [{'barcode': 'None', 'cancer_type': 'None', 'histological_type': 'None'}, {'barcode': 'None', 'cancer_type': 'UQ', 'histological_type': 'Other  specify'}, {'barcode': 'TCGA-60-2720', 'cancer_type': ' corresponds to a FEMALE patient diagnosed with Lung squamous cell carcinoma', 'histological_type': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)'}, {'barcode': 'TCGA-55-7281', 'cancer_type': 'ab', 'histological_type': 'Lung Adenocarcinoma- Not Otherwise Specified (NOS)'}, {'barcode': 'None', 'cancer_type': 'AAKG', 'histological_type': 'Non-Seminoma; Embryonal Carcinoma'}, {'barcode': 'TCGA-94-7943', 'cancer_type': ' corresponds to a MALE patient diagnosed with Lung squamous cell carcinoma', 'histological_type': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)'}, {'barcode': 'None', 'cancer_type': 'IM', 'histological_type': 'Other  specify'}, {'barcode': 'None', 'cancer_type': 'PL', 'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'barcode': 'None', 'cancer_type': 'YO', 'histological_type': 'None'}, {'barcode': 'TCGA-60-2708', 'cancer_type': 'In the Lung squamous cell carcinoma dataset', 'histological_type': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)'}, {'barcode': 'None', 'cancer_type': 'AAMF', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'barcode': 'None', 'cancer_type': 'AADJ', 'histological_type': 'Hepatocellular Carcinoma'}, {'barcode': 'TCGA-95-8494', 'cancer_type': 'None', 'histological_type': 'Lung Adenocarcinoma- Not Otherwise Specified (NOS)'}, {'barcode': 'None', 'cancer_type': 'a', 'histological_type': 'Kidney Chromophobe'}, {'barcode': 'None', 'cancer_type': 'cac is a MALE case of Brain lower grade glioma', 'histological_type': 'Oligoastrocytoma'}, {'barcode': 'None', 'cancer_type': 'c', 'histological_type': 'Endometrioid endometrial adenocarcinoma'}, {'barcode': 'None', 'cancer_type': 'FR', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'barcode': 'None', 'cancer_type': 'BCF is a MALE case of Esophageal carcinoma', 'histological_type': 'Esophagus Adenocarcinoma  NOS'}, {'barcode': 'None', 'cancer_type': 'MALE', 'histological_type': 'Thymoma; Type B2'}, {'barcode': 'None', 'cancer_type': 'None', 'histological_type': 'Kidney Chromophobe'}], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
