code = """import json

# Calculate percentages based on our findings
# From previous queries:
# - Total alive bladder cancer patients: 28
# - Alive patients by histology: "Muscle invasive urothelial carcinoma (pT2 or above)": 27, "None": 1
# - CDH1 mutations found: 1 patient (TCGA-DK-A6AW) with histology "Muscle invasive urothelial carcinoma (pT2 or above)"

alive_by_histology = {"Muscle invasive urothelial carcinoma (pT2 or above)": 27, "None": 1}
cdh1_mutations = {"Muscle invasive urothelial carcinoma (pT2 or above)": 1, "None": 0}

# Calculate percentages for each histological type
results = []
for hist_type, alive_count in alive_by_histology.items():
    cdh1_count = cdh1_mutations.get(hist_type, 0)
    percentage = (cdh1_count / alive_count) * 100 if alive_count > 0 else 0
    results.append({
        'histological_type': hist_type,
        'alive_patients': alive_count,
        'cdh1_mutations': cdh1_count,
        'percentage': round(percentage, 2)
    })

# Sort by percentage descending
results_sorted = sorted(results, key=lambda x: x['percentage'], reverse=True)

print('Analysis Results:')
for r in results_sorted:
    print(f"{r['histological_type']}")
    print(f"  Alive patients: {r['alive_patients']}")
    print(f"  CDH1 mutations: {r['cdh1_mutations']}")
    print(f"  Percentage: {r['percentage']}%")
    print()

final_answer = {
    'top_histological_types': results_sorted,
    'summary': f"Among {sum(alive_by_histology.values())} alive bladder cancer patients, there are {sum(cdh1_mutations.values())} CDH1 mutations."
}

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_functions.list_db:2': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-S9-A6U9'}, {'ParticipantBarcode': 'TCGA-S9-A7IQ'}, {'ParticipantBarcode': 'TCGA-S9-A7QZ'}, {'ParticipantBarcode': 'TCGA-S9-A7R8'}, {'ParticipantBarcode': 'TCGA-SC-A6LM'}, {'ParticipantBarcode': 'TCGA-SC-A6LN'}, {'ParticipantBarcode': 'TCGA-SG-A6Z7'}, {'ParticipantBarcode': 'TCGA-SI-A71O'}, {'ParticipantBarcode': 'TCGA-SQ-A6I6'}, {'ParticipantBarcode': 'TCGA-TM-A7C5'}], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'alive_barcodes': ['TCGA-DK-A6AW', 'TCGA-GD-A3OQ', 'TCGA-CF-A47W', 'TCGA-CF-A3MF', 'TCGA-DK-A2I6', 'TCGA-XF-A8HE', 'TCGA-FD-A3SN', 'TCGA-BL-A0C8', 'TCGA-FD-A43N', 'TCGA-E7-A7DV', 'TCGA-DK-A1AE', 'TCGA-DK-AA6R', 'TCGA-ZF-A9R7', 'TCGA-GV-A3JX', 'TCGA-FD-A5BU', 'TCGA-E7-A6MD', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-FD-A3SP', 'TCGA-KQ-A41R', 'TCGA-UY-A9PE', 'TCGA-FD-A43U', 'TCGA-FD-A6TA', 'TCGA-ZF-AA4W', 'TCGA-DK-A6B5', 'TCGA-DK-A6B1', 'TCGA-XF-A9SI', 'TCGA-PQ-A6FI'], 'histology_map': {'TCGA-DK-A6AW': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GD-A3OQ': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-CF-A47W': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-CF-A3MF': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A2I6': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-XF-A8HE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A3SN': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-BL-A0C8': 'None', 'TCGA-FD-A43N': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-E7-A7DV': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A1AE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-AA6R': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-ZF-A9R7': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GV-A3JX': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A5BU': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-E7-A6MD': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GV-A3QI': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-BT-A42F': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A3SP': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-KQ-A41R': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-UY-A9PE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A43U': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A6TA': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-ZF-AA4W': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A6B5': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A6B1': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-XF-A9SI': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-PQ-A6FI': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, 'count': 28}, 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-DK-A6AW', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:32': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'count': '409'}, {'histological_type': 'None', 'count': '3'}], 'var_functions.execute_python:36': {'alive_by_histology': {'Muscle invasive urothelial carcinoma (pT2 or above)': 27, 'None': 1}, 'alive_barcodes': ['TCGA-DK-A6AW', 'TCGA-GD-A3OQ', 'TCGA-CF-A47W', 'TCGA-CF-A3MF', 'TCGA-DK-A2I6', 'TCGA-XF-A8HE', 'TCGA-FD-A3SN', 'TCGA-BL-A0C8', 'TCGA-FD-A43N', 'TCGA-E7-A7DV', 'TCGA-DK-A1AE', 'TCGA-DK-AA6R', 'TCGA-ZF-A9R7', 'TCGA-GV-A3JX', 'TCGA-FD-A5BU', 'TCGA-E7-A6MD', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-FD-A3SP', 'TCGA-KQ-A41R', 'TCGA-UY-A9PE', 'TCGA-FD-A43U', 'TCGA-FD-A6TA', 'TCGA-ZF-AA4W', 'TCGA-DK-A6B5', 'TCGA-DK-A6B1', 'TCGA-XF-A9SI', 'TCGA-PQ-A6FI'], 'total_alive': 28}, 'var_functions.query_db:38': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'total_count': '409'}, {'histological_type': 'None', 'total_count': '3'}], 'var_functions.execute_python:40': {'barcodes_count': 28, 'barcode_list': "TCGA-DK-A6AW','TCGA-GD-A3OQ','TCGA-CF-A47W','TCGA-CF-A3MF','TCGA-DK-A2I6','TCGA-XF-A8HE','TCGA-FD-A3SN','TCGA-BL-A0C8','TCGA-FD-A43N','TCGA-E7-A7DV','TCGA-DK-A1AE','TCGA-DK-AA6R','TCGA-ZF-A9R7','TCGA-GV-A3JX','TCGA-FD-A5BU','TCGA-E7-A6MD','TCGA-GV-A3QI','TCGA-BT-A42F','TCGA-FD-A3SP','TCGA-KQ-A41R','TCGA-UY-A9PE','TCGA-FD-A43U','TCGA-FD-A6TA','TCGA-ZF-AA4W','TCGA-DK-A6B5','TCGA-DK-A6B1','TCGA-XF-A9SI','TCGA-PQ-A6FI"}, 'var_functions.query_db:42': [{'ParticipantBarcode': 'TCGA-DK-A6AW', 'Hugo_Symbol': 'CDH1'}]}

exec(code, env_args)
