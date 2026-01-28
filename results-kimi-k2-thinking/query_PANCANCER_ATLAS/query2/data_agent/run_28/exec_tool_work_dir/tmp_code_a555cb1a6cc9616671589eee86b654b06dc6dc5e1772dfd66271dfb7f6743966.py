code = """import json, re

# Access stored data
clinical_path = var_functions.query_db:30
cdh1_path = var_functions.query_db:42

# Load alive BRCA clinical data
with open(clinical_path) as f:
    alive_patients = json.load(f)

# Load CDH1 mutation data  
with open(cdh1_path) as f:
    cdh1_muts = json.load(f)

print('Alive BRCA patients:', len(alive_patients))
print('Total CDH1 mutations:', len(cdh1_muts))

# Map alive BRCA barcode to histological type
alive_map = {}
for p in alive_patients:
    m = re.search(r'(TCGA-\w{2}-\w{4})', p['Patient_description'])
    if m:
        alive_map[m.group(1)] = p['histological_type']

# Get set of all CDH1 mutated barcodes
cdh1_set = set([x['ParticipantBarcode'] for x in cdh1_muts])

print('Alive BRCA barcodes:', len(alive_map))
print('CDH1 mutation barcodes:', len(cdh1_set))

# Find common patients (alive BRCA with CDH1 mutations)
common = set(alive_map.keys()) & cdh1_set
print('Alive BRCA with CDH1 mutations:', len(common))

result = json.dumps({
    'alive_count': len(alive_map),
    'cdh1_count': len(cdh1_set),
    'common_count': len(common),
    'alive_map': alive_map,
    'common_barcodes': list(common)
})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'alive_barcodes': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'total_alive': 30}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-XF-A9T3'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
