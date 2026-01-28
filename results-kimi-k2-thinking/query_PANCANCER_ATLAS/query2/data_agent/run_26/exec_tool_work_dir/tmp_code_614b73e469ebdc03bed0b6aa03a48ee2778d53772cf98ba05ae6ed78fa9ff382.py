code = """import json
import re

# Load clinical data to get all alive BRCA patients
clinical_file = 'test1.json'  # This should be the actual file path
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Count alive patients by histological type
histology_counts = {}
for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', 'Unknown')
    
    # Find TCGA barcode pattern
    bc_match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if bc_match:
        # Check if patient is alive
        if 'vital status' in desc.lower() and 'alive' in desc.lower():
            histology_counts[hist_type] = histology_counts.get(hist_type, 0) + 1

print('Alive patients by histology:', histology_counts)

# From the previous query, we know CDH1 mutations in alive patients
# TCGA-DK-A6AW had CDH1 mutation and has histology "Muscle invasive urothelial carcinoma (pT2 or above)"

# Count CDH1 mutations by histological type
cdh1_mutations = {'Muscle invasive urothelial carcinoma (pT2 or above)': 1, 'None': 0, 'Unknown': 0}

# Calculate percentages
percentages = []
for hist_type, total_count in histology_counts.items():
    if total_count > 0:
        cdh1_count = cdh1_mutations.get(hist_type, 0)
        percentage = (cdh1_count / total_count) * 100
        percentages.append({
            'histological_type': hist_type,
            'total_patients': total_count,
            'cdh1_mutations': cdh1_count,
            'percentage': round(percentage, 2)
        })

# Sort by percentage and get top 3
percentages_sorted = sorted(percentages, key=lambda x: x['percentage'], reverse=True)
top_3 = percentages_sorted[:3]

print('Top 3 histological types by CDH1 mutation percentage:')
for item in top_3:
    print(f"{item['histological_type']}: {item['percentage']}% ({item['cdh1_mutations']}/{item['total_patients']})")

result = {
    'top_3_histological_types': top_3,
    'total_alive_patients': sum(histology_counts.values())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:2': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-S9-A6U9'}, {'ParticipantBarcode': 'TCGA-S9-A7IQ'}, {'ParticipantBarcode': 'TCGA-S9-A7QZ'}, {'ParticipantBarcode': 'TCGA-S9-A7R8'}, {'ParticipantBarcode': 'TCGA-SC-A6LM'}, {'ParticipantBarcode': 'TCGA-SC-A6LN'}, {'ParticipantBarcode': 'TCGA-SG-A6Z7'}, {'ParticipantBarcode': 'TCGA-SI-A71O'}, {'ParticipantBarcode': 'TCGA-SQ-A6I6'}, {'ParticipantBarcode': 'TCGA-TM-A7C5'}], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'alive_barcodes': ['TCGA-DK-A6AW', 'TCGA-GD-A3OQ', 'TCGA-CF-A47W', 'TCGA-CF-A3MF', 'TCGA-DK-A2I6', 'TCGA-XF-A8HE', 'TCGA-FD-A3SN', 'TCGA-BL-A0C8', 'TCGA-FD-A43N', 'TCGA-E7-A7DV', 'TCGA-DK-A1AE', 'TCGA-DK-AA6R', 'TCGA-ZF-A9R7', 'TCGA-GV-A3JX', 'TCGA-FD-A5BU', 'TCGA-E7-A6MD', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-FD-A3SP', 'TCGA-KQ-A41R', 'TCGA-UY-A9PE', 'TCGA-FD-A43U', 'TCGA-FD-A6TA', 'TCGA-ZF-AA4W', 'TCGA-DK-A6B5', 'TCGA-DK-A6B1', 'TCGA-XF-A9SI', 'TCGA-PQ-A6FI'], 'histology_map': {'TCGA-DK-A6AW': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GD-A3OQ': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-CF-A47W': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-CF-A3MF': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A2I6': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-XF-A8HE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A3SN': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-BL-A0C8': 'None', 'TCGA-FD-A43N': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-E7-A7DV': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A1AE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-AA6R': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-ZF-A9R7': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GV-A3JX': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A5BU': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-E7-A6MD': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GV-A3QI': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-BT-A42F': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A3SP': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-KQ-A41R': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-UY-A9PE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A43U': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A6TA': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-ZF-AA4W': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A6B5': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A6B1': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-XF-A9SI': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-PQ-A6FI': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, 'count': 28}, 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-DK-A6AW', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:32': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'count': '409'}, {'histological_type': 'None', 'count': '3'}]}

exec(code, env_args)
