code = """import json, re

clinical_file = var_functions.query_db:30
if isinstance(clinical_file, str):
    with open(clinical_file) as f: a_patients = json.load(f)
else: a_patients = clinical_file

cdh1_file = var_functions.query_db:42
if isinstance(cdh1_file, str):
    with open(cdh1_file) as f: c_muts = json.load(f)
else: c_muts = cdh1_file

print('Alive BRCA:', len(a_patients))
print('CDH1 mutations:', len(c_muts))

alive_dict = {}
for p in a_patients:
    m = re.search(r'(TCGA-\w{2}-\w{4})', p['Patient_description'])
    if m:
        b = m.group(1)
        alive_dict[b] = p['histological_type']

cdh1_set = set([x['ParticipantBarcode'] for x in c_muts])

print('Alive barcodes:', len(alive_dict))
print('CDH1 barcodes:', len(cdh1_set))

common = set(alive_dict.keys()) & cdh1_set
print('Common:', len(common))

result = json.dumps({
    'alive_count': len(alive_dict),
    'cdh1_count': len(cdh1_set),
    'common_count': len(common),
    'barcode_mapping': alive_dict,
    'cdh1_barcodes_list': list(cdh1_set)
})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'alive_barcodes': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'total_alive': 30}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-XF-A9T3'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
