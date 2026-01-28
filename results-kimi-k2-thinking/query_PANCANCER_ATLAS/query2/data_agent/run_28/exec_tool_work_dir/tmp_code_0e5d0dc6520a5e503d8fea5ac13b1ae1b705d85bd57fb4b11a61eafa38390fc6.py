code = """import json, re

# Load clinical data for alive BRCA patients
clinical_path = var_functions.query_db:64
if isinstance(clinical_path, str):
    with open(clinical_path) as f:
        alive_patients = json.load(f)
else:
    alive_patients = clinical_path

print("Alive BRCA patients:", len(alive_patients))

# Map barcode to histological type for alive BRCA patients
barcode_histology = {}
for patient in alive_patients:
    desc = patient['Patient_description']
    hist_type = patient['histological_type']
    
    # Extract barcode
    m = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if m:
        barcode = m.group(1)
        barcode_histology[barcode] = hist_type

print("Barcodes extracted:", len(barcode_histology))

# Get list of all CDH1 mutated barcodes from molecular database
# Need to query this
cdh1_barcodes_all = set()
cdh1_path = var_functions.query_db:42
if isinstance(cdh1_path, str):
    with open(cdh1_path) as f:
        cdh1_mutations = json.load(f)
    cdh1_barcodes_all = set([m['ParticipantBarcode'] for m in cdh1_mutations])
    print("CDH1 mutations total:", len(cdh1_barcodes_all))
else:
    cdh1_mutations = cdh1_path
    cdh1_barcodes_all = set([m['ParticipantBarcode'] for m in cdh1_mutations])
    print("CDH1 mutations total:", len(cdh1_barcodes_all))

# Find intersection - alive BRCA patients with CDH1 mutations
alive_brca_barcodes = set(barcode_histology.keys())
common_barcodes = alive_brca_barcodes & cdh1_barcodes_all
print("Alive BRCA with CDH1 mutations:", len(common_barcodes))

# Count by histological type
histology_stats = {}
for barcode, hist_type in barcode_histology.items():
    if hist_type not in histology_stats:
        histology_stats[hist_type] = {'total': 0, 'cdh1': 0}
    
    histology_stats[hist_type]['total'] += 1
    if barcode in common_barcodes:
        histology_stats[hist_type]['cdh1'] += 1

# Calculate percentages
for hist, stats in histology_stats.items():
    stats['percentage'] = (stats['cdh1'] / stats['total'] * 100) if stats['total'] > 0 else 0

# Sort by percentage and get top 3
sorted_hists = sorted(histology_stats.items(), key=lambda x: x[1]['percentage'], reverse=True)

print("\nTop 3 histological types by CDH1 mutation percentage:")
for i, (hist, stats) in enumerate(sorted_hists[:3], 1):
    print(f"{i}. {hist}")
    print(f"   {stats['percentage']:.1f}% ({stats['cdh1']}/{stats['total']} patients)")

result = json.dumps(sorted_hists[:3])
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'alive_barcodes': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'total_alive': 30}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-XF-A9T3'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
