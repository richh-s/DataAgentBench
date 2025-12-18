code = """import pandas as pd
import json

# Load results from previous steps
clinical_processed_data = locals()['var_function-call-9726461708806369647']
cdh1_mutations = locals()['var_function-call-10637093304524372400']

# Create DataFrame for histological types and participant barcodes
df_hist_types = pd.DataFrame(clinical_processed_data['histological_types'])

# Create DataFrame for CDH1 mutations
df_cdh1_mutations = pd.DataFrame(cdh1_mutations)

# Mark patients with CDH1 mutations
df_hist_types['CDH1_mutated'] = df_hist_types['ParticipantBarcode'].isin(df_cdh1_mutations['ParticipantBarcode'])

# Calculate total patients per histological type
total_patients_per_hist_type = df_hist_types.groupby('histological_type')['ParticipantBarcode'].nunique().reset_index()
total_patients_per_hist_type.rename(columns={'ParticipantBarcode': 'TotalPatients'}, inplace=True)

# Calculate patients with CDH1 mutations per histological type
cdh1_mutated_patients_per_hist_type = df_hist_types[df_hist_types['CDH1_mutated']]
cdh1_mutated_patients_per_hist_type = cdh1_mutated_patients_per_hist_type.groupby('histological_type')['ParticipantBarcode'].nunique().reset_index()
cdh1_mutated_patients_per_hist_type.rename(columns={'ParticipantBarcode': 'CDH1MutatedPatients'}, inplace=True)

# Merge the two counts
merged_counts = pd.merge(total_patients_per_hist_type, cdh1_mutated_patients_per_hist_type, on='histological_type', how='left')
merged_counts['CDH1MutatedPatients'] = merged_counts['CDH1MutatedPatients'].fillna(0).astype(int)

# Calculate percentage of CDH1 mutations
merged_counts['MutationPercentage'] = (merged_counts['CDH1MutatedPatients'] / merged_counts['TotalPatients']) * 100

# Sort by percentage and get top 3
top_3_hist_types = merged_counts.sort_values(by='MutationPercentage', ascending=False).head(3)

print("__RESULT__:")
print(top_3_hist_types.to_json(orient='records'))"""

env_args = {'var_function-call-4641508794214492565': ['clinical_info'], 'var_function-call-14341548236009829069': 'file_storage/function-call-14341548236009829069.json', 'var_function-call-9726461708806369647': {'participants': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'histological_types': [{'ParticipantBarcode': 'TCGA-GD-A3OQ', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-GV-A3QI', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-BT-A42F', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-K4-A6FZ', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-ZF-A9RF', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-DK-A6AV', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-GD-A6C6', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-GU-A766', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-E7-A8O7', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-GC-A4ZW', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-G2-A2EK', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-GV-A3JZ', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-UY-A9PH', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-UY-A78O', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-DK-A1AC', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-C4-A0F6', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-KQ-A41O', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-4Z-AA7M', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-UY-A78L', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-S5-AA26', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-XF-A9T3', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-E7-A678', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-FT-A61P', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-K4-A3WV', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-GD-A3OP', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-G2-A3VY', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-FD-A5C1', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-E7-A5KF', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-DK-A2I1', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'ParticipantBarcode': 'TCGA-H4-A2HO', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}]}, 'var_function-call-10637093304524372400': [{'ParticipantBarcode': 'TCGA-XF-A9T3', 'Hugo_Symbol': 'CDH1'}]}

exec(code, env_args)
