code = """import json
import re
import os

# List all tmp files sorted by size
tmp_files = [f for f in os.listdir('/tmp') if f.endswith('.json')]
file_info = []
for f in tmp_files:
    path = f'/tmp/{f}'
    size = os.path.getsize(path)
    file_info.append((f, size, path))

# Sort by file size (largest first)
file_info.sort(key=lambda x: x[1], reverse=True)

print('All JSON files in /tmp (sorted by size):')
for i, (name, size, path) in enumerate(file_info, 1):
    print(f"{i}. {name} ({size} bytes)")

# The two largest files should be our clinical and mutation data
if len(file_info) >= 2:
    # Second largest is likely clinical data (breast patients)
    clinical_path = file_info[1][2]
    # Largest is likely mutation data (all CDH1 mutations)
    mutation_path = file_info[0][2]
    
    print(f'\\nUsing files:')
    print(f'Clinical: {file_info[1][0]} ({file_info[1][1]} bytes)')
    print(f'Mutation: {file_info[0][0]} ({file_info[0][1]} bytes)')
    
    # Load the data
    with open(clinical_path, 'r') as f:
        clinical_data = json.load(f)
    
    with open(mutation_path, 'r') as f:
        mutation_data = json.load(f)
    
    print(f'\\nRecords loaded:')
    print(f'Clinical: {len(clinical_data)}')
    print(f'Mutation: {len(mutation_data)}')
    
    # Find alive BRCA patients
    brca_patients = []
    for rec in clinical_data:
        desc = rec.get('Patient_description', '')
        if 'Breast' in desc and 'Alive' in desc:
            match = re.search(r'TCGA-\w{2}-\w{4}', desc)
            if match:
                brca_patients.append({
                    'barcode': match.group(0),
                    'histological_type': rec.get('histological_type', 'Unknown')
                })
    
    # Get CDH1 mutation barcodes
    cdh1_barcodes = set()
    for rec in mutation_data:
        if rec.get('Hugo_Symbol') == 'CDH1':
            cdh1_barcodes.add(rec['ParticipantBarcode'])
    
    # Calculate statistics
    hist_stats = {}
    for patient in brca_patients:
        h = patient['histological_type']
        if h not in hist_stats:
            hist_stats[h] = {'total': 0, 'mutated': 0}
        
        hist_stats[h]['total'] += 1
        if patient['barcode'] in cdh1_barcodes:
            hist_stats[h]['mutated'] += 1
    
    # Calculate percentages and get top 3
    results = []
    for h, stats in hist_stats.items():
        if stats['total'] >= 3:  # Minimum 3 patients
            pct = round(stats['mutated'] / stats['total'] * 100, 2)
            results.append({
                'histological_type': h,
                'percentage': pct,
                'total_patients': stats['total'],
                'mutated_patients': stats['mutated']
            })
    
    results.sort(key=lambda x: x['percentage'], reverse=True)
    top3 = results[:3]
    
    output = {
        'analysis_summary': {
            'total_alive_brca_patients': len(brca_patients),
            'total_cdh1_mutations_all_cancers': len(cdh1_barcodes),
        },
        'top_3_histological_types': top3
    }
else:
    output = {'error': 'Not enough data files found'}

print('\\n__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:18': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-X6-A8C2', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EE-A2GO', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-13-0889', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A6', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-A02K', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AG-3892', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-63-A5MM', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YK', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A7-A4SC', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-8370', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-CV-6937', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-A4NK', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FP-A8CX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G4-6586', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-GC-A3I6', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OD-A75X', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A09Z', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A2', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-55-A4DF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-5L-AAT0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-77-A5G1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A06L', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A18F', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A209', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-4188', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-4279', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-A44T', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0TE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-C8-A274', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D1-A103', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-A6EY', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-A748', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27V', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-AADA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-AADI', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DU-6392', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EO-A3AZ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G2-A3IE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-S3-A6ZG', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-VQ-A91K', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AO-A0J8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A6IX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0EX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A0GA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AN-A0FN', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-06-0210', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A5QM', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A2HC', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B6-A2IU', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A0C1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-8592', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-CN-6024', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-6522', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DU-6392', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FW-A3R5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G9-6365', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-IR-A3LH', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-JX-A3Q0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-WT-AB44', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-XX-A899', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-Z7-A8R5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EE-A2GT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-X6-A7WB', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AP-A056', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-2Y-A9H5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-3M-AB47', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-50-6590', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0EW', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A1G0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-A01R', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A2B8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A2FB', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A4ZE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A6IV', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A2HA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B5-A11G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B7-A5TI', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:38': {'error': 'Required files not found'}, 'var_functions.execute_python:52': {'error': 'Missing required data'}, 'var_functions.execute_python:56': {'error': 'Missing data', 'clinical': 0, 'mutation': 0}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.execute_python:78': {'error': 'Missing files - Clinical: None, Mutation: None'}, 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json', 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:94': 'file_storage/functions.query_db:94.json'}

exec(code, env_args)
