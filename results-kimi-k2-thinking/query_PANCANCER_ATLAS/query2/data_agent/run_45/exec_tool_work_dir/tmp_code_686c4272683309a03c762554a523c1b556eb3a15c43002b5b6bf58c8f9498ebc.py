code = """import pandas as pd, json, os

# Load clinical data
tmp_dir = '/tmp'
files = os.listdir(tmp_dir)

# Find clinical data file
clinical_file = None
for f in files:
    if f.endswith('.json') and ('clinical' in f or f.startswith('tmp')):
        clinical_file = os.path.join(tmp_dir, f)
        break

if clinical_file:
    with open(clinical_file, 'r', encoding='utf-8') as f:
        clinical_data = json.load(f)
    print('Clinical data loaded:', len(clinical_data))
    
    # Filter alive breast cancer patients
    brca_alive = []
    for row in clinical_data:
        desc = row.get('Patient_description', '')
        if 'Breast' in desc and 'Alive' in desc:
            brca_alive.append({
                'patient_description': desc,
                'histological_type': row.get('histological_type', 'Unknown')
            })
    
    print('Alive BRCA patients:', len(brca_alive))
    
    # Get mutation data
    cdh1_participants = set()
    for f in files:
        f_path = os.path.join(tmp_dir, f)
        try:
            with open(f_path, 'r', encoding='utf-8') as reader:
                data = json.load(reader)
                # Check if this is mutation data with ParticipantBarcode and Hugo_Symbol
                if isinstance(data, list) and len(data) > 0:
                    first = data[0]
                    if 'ParticipantBarcode' in first and 'Hugo_Symbol' in first:
                        for record in data:
                            if record.get('Hugo_Symbol') == 'CDH1':
                                cdh1_participants.add(record['ParticipantBarcode'])
                        print('CDH1 participants:', len(cdh1_participants))
                        break
        except:
            continue
    
    # Match CDH1 mutations with BRCA alive patients
    if brca_alive and cdh1_participants:
        # Extract participant barcodes from patient descriptions
        for patient in brca_alive:
            desc = patient['patient_description']
            # Find TCGA barcode in description
            if 'TCGA-' in desc:
                barcode = desc.split('TCGA-')[1].split(' ')[0]
                patient['barcode'] = 'TCGA-' + barcode
        
        # Check which patients have CDH1 mutation
        results = []
        for patient in brca_alive:
            if 'barcode' in patient:
                patient['has_cdh1_mutation'] = patient['barcode'] in cdh1_participants
                results.append(patient)
        
        # Calculate mutation percentage by histological type
        hist_summary = {}
        for patient in results:
            hist = patient['histological_type']
            if hist not in hist_summary:
                hist_summary[hist] = {'total': 0, 'mutated': 0}
            hist_summary[hist]['total'] += 1
            if patient['has_cdh1_mutation']:
                hist_summary[hist]['mutated'] += 1
        
        # Calculate percentages
        hist_percentages = []
        for hist, counts in hist_summary.items():
            pct = (counts['mutated'] / counts['total']) * 100 if counts['total'] > 0 else 0
            hist_percentages.append({'histological_type': hist, 'percentage': pct, 'total_patients': counts['total'], 'mutated_patients': counts['mutated']})
        
        # Sort by percentage and get top 3
        hist_percentages.sort(key=lambda x: x['percentage'], reverse=True)
        top3 = hist_percentages[:3]
        
        print('\nTop 3 Histological Types:')
        result_json = {'top_3_histological_types': top3}
        
        __RESULT__ = json.dumps(result_json)
    else:
        print('Insufficient data')
        __RESULT__ = json.dumps({'error': 'Insufficient data'})
else:
    print('Clinical data file not found')
    __RESULT__ = json.dumps({'error': 'Clinical data file not found'})"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:18': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-X6-A8C2', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EE-A2GO', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-13-0889', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A6', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-A02K', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AG-3892', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-63-A5MM', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YK', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A7-A4SC', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-8370', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-CV-6937', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-A4NK', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FP-A8CX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G4-6586', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-GC-A3I6', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OD-A75X', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A09Z', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A2', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-55-A4DF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-5L-AAT0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-77-A5G1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A06L', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A18F', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A209', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-4188', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-4279', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-A44T', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0TE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-C8-A274', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D1-A103', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-A6EY', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-A748', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27V', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-AADA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-AADI', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DU-6392', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EO-A3AZ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G2-A3IE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-S3-A6ZG', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-VQ-A91K', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AO-A0J8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A6IX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0EX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A0GA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AN-A0FN', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-06-0210', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A5QM', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A2HC', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B6-A2IU', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A0C1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-8592', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-CN-6024', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-6522', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DU-6392', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FW-A3R5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G9-6365', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-IR-A3LH', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-JX-A3Q0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-WT-AB44', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-XX-A899', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-Z7-A8R5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EE-A2GT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-X6-A7WB', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AP-A056', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-2Y-A9H5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-3M-AB47', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-50-6590', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0EW', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A1G0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-A01R', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A2B8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A2FB', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A4ZE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A6IV', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A2HA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B5-A11G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B7-A5TI', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
