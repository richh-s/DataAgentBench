code = """import json, os

# List all tmp files
tmp_files = os.listdir('/tmp')
print('TMP files:')
for i, f in enumerate(tmp_files, 1):
    print(f"{i}. {f}")

# Check for clinical data file
clinical_files = []
cdh1_files = []

for f in tmp_files:
    try:
        with open(f'/tmp/{f}', 'r') as file:
            content = file.read(500)  # Read first 500 chars
            if 'Patient_description' in content and 'Breast' in content:
                clinical_files.append(f)
            elif 'ParticipantBarcode' in content and 'Hugo_Symbol' in content:
                cdh1_files.append(f)
    except:
        continue

print('\nClinical file candidates:', clinical_files)
print('CDH1 mutation file candidates:', cdh1_files)

# Process data if found
if clinical_files and cdh1_files:
    # Load clinical data
    with open(f'/tmp/{clinical_files[0]}', 'r') as f:
        clinical_data = json.load(f)
    
    # Load mutation data
    with open(f'/tmp/{cdh1_files[0]}', 'r') as f:
        mutation_data = json.load(f)
    
    print(f'\nClinical records: {len(clinical_data)}')
    print(f'Mutation records: {len(mutation_data)}')
    
    # Filter CDH1 mutations
    cdh1_barcodes = set()
    for record in mutation_data:
        if record.get('Hugo_Symbol') == 'CDH1':
            cdh1_barcodes.add(record['ParticipantBarcode'])
    
    print(f'CDH1 mutation participants: {len(cdh1_barcodes)}')
    
    # Extract barcodes from clinical descriptions and identify BRCA Alive patients
    results = []
    for record in clinical_data:
        desc = record['Patient_description']
        histo = record['histological_type']
        
        # Extract TCGA barcode
        import re
        match = re.search(r'TCGA-\w{2}-\w{4}', desc)
        if match:
            barcode = match.group(0)
            results.append({
                'barcode': barcode,
                'histological_type': histo,
                'has_cdh1': barcode in cdh1_barcodes
            })
    
    # Calculate statistics by histological type
    histo_dict = {}
    for r in results:
        h = r['histological_type']
        histo_dict[h] = histo_dict.get(h, {'total': 0, 'mutated': 0})
        histo_dict[h]['total'] += 1
        if r['has_cdh1']:
            histo_dict[h]['mutated'] += 1
    
    # Sort by mutation percentage
    histo_list = []
    for h, data in histo_dict.items():
        pct = (data['mutated'] / data['total'] * 100) if data['total'] > 0 else 0
        histo_list.append({
            'histological_type': h,
            'percentage': round(pct, 2),
            'total': data['total'],
            'mutated': data['mutated']
        })
    
    histo_list.sort(key=lambda x: x['percentage'], reverse=True)
    top3 = histo_list[:3]
    
    final_result = {'top_3_histological_types': top3}
    print('\nTop 3 results prepared')
    
    __RESULT__ = json.dumps(final_result)
else:
    __RESULT__ = json.dumps({'error': 'Files not found'})"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:18': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-X6-A8C2', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EE-A2GO', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-13-0889', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A6', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-A02K', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AG-3892', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-63-A5MM', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YK', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A7-A4SC', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-8370', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-CV-6937', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-A4NK', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FP-A8CX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G4-6586', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-GC-A3I6', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OD-A75X', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A09Z', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A2', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-55-A4DF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-5L-AAT0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-77-A5G1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A06L', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A18F', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A209', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-4188', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-4279', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-A44T', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0TE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-C8-A274', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D1-A103', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-A6EY', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-A748', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27V', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-AADA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-AADI', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DU-6392', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EO-A3AZ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G2-A3IE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-S3-A6ZG', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-VQ-A91K', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AO-A0J8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A6IX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0EX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A0GA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AN-A0FN', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-06-0210', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A5QM', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A2HC', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B6-A2IU', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A0C1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-8592', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-CN-6024', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-6522', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DU-6392', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FW-A3R5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G9-6365', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-IR-A3LH', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-JX-A3Q0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-WT-AB44', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-XX-A899', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-Z7-A8R5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EE-A2GT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-X6-A7WB', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AP-A056', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-2Y-A9H5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-3M-AB47', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-50-6590', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0EW', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A1G0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-A01R', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A2B8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A2FB', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A4ZE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A6IV', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A2HA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B5-A11G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B7-A5TI', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
