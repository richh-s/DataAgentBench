code = """import json
import os
import re

# Check what files are actually in /tmp
tmp_files = [f for f in os.listdir('/tmp') if f.endswith('.json') and f.startswith('tmp')]
print('TMP JSON files:')
for f in tmp_files:
    file_path = f'/tmp/{f}'
    size = os.path.getsize(file_path)
    print(f'  {f} ({size} bytes)')

# Look for our specific query results
print('\nLooking for clinical and mutation data...')

# Clinical data - breast alive patients
clinical_file = None
for f in tmp_files:
    file_path = f'/tmp/{f}'
    try:
        with open(file_path, 'r') as reader:
            data = json.load(reader)
        if len(data) > 0 and 'Patient_description' in data[0]:
            # Check if this has breast cancer records
            breast_count = sum(1 for rec in data if 'Breast' in rec.get('Patient_description', ''))
            if breast_count > 0:
                clinical_file = file_path
                print(f'Found clinical data: {f} with {len(data)} records')
                break
    except:
        continue

# Mutation data - CDH1 mutations
mutation_file = None
for f in tmp_files:
    file_path = f'/tmp/{f}'
    try:
        with open(file_path, 'r') as reader:
            data = json.load(reader)
        if len(data) > 0 and 'ParticipantBarcode' in data[0]:
            cdh1_count = sum(1 for rec in data if rec.get('Hugo_Symbol') == 'CDH1')
            if cdh1_count > 0:
                mutation_file = file_path
                print(f'Found mutation data: {f} with {len(data)} records')
                break
    except:
        continue

print(f'\nClinical file: {clinical_file}')
print(f'Mutation file: {mutation_file}')
print('Done')"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:18': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-X6-A8C2', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EE-A2GO', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-13-0889', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A6', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-A02K', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AG-3892', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-63-A5MM', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YK', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A7-A4SC', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-8370', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-CV-6937', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-A4NK', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FP-A8CX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G4-6586', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-GC-A3I6', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OD-A75X', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A09Z', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A2', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-55-A4DF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-5L-AAT0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-77-A5G1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A06L', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A18F', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A209', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-4188', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-4279', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-A44T', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0TE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-C8-A274', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D1-A103', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-A6EY', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-A748', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27V', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-AADA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DD-AADI', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DU-6392', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EO-A3AZ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G2-A3IE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-S3-A6ZG', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-VQ-A91K', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AO-A0J8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A6IX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0EX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A0GA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AN-A0FN', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-06-0210', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A5QM', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A2HC', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B6-A2IU', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BH-A0C1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BR-8592', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-CN-6024', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D7-6522', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-DU-6392', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-FW-A3R5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-G9-6365', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-IR-A3LH', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-JX-A3Q0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-WT-AB44', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-XX-A899', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-Z7-A8R5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EE-A2GT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-X6-A7WB', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AP-A056', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-2Y-A9H5', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-3M-AB47', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-50-6590', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0EW', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A1G0', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-A01R', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A2B8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A2FB', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A4ZE', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AC-A6IV', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AX-A2HA', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B5-A11G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-B7-A5TI', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:38': {'error': 'Required files not found'}, 'var_functions.execute_python:52': {'error': 'Missing required data'}, 'var_functions.execute_python:56': {'error': 'Missing data', 'clinical': 0, 'mutation': 0}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
