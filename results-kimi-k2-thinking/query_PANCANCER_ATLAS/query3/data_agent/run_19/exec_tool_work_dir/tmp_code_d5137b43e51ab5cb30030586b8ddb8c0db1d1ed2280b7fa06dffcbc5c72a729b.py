code = """import json
import pandas as pd
import scipy.stats as stats
import re

# Read the clinical data file
with open('var_functions.query_db_50', 'r') as f:
    clinical_data = json.load(f)

# Read the mutation data file  
with open('var_functions.query_db_52', 'r') as f:
    mutation_data = json.load(f)

# Create DataFrames
df_clinical = pd.DataFrame(clinical_data)
df_mutations = pd.DataFrame(mutation_data)

# Extract patient barcodes from clinical data
df_clinical['patient_barcode'] = df_clinical['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)')

# Get CDH1 mutated patients
cdh1_mutated = set(df_mutations['ParticipantBarcode'].unique())

# Add CDH1 mutation status
df_clinical['cdh1_mutated'] = df_clinical['patient_barcode'].isin(cdh1_mutated)

# Create contingency table
table = pd.crosstab(df_clinical['histological_type'], df_clinical['cdh1_mutated'])

# Calculate marginal totals (row and column sums)
row_totals = table.sum(axis=1)
col_totals = table.sum(axis=0)
grand_total = table.sum().sum()

# Identify categories to exclude (marginal totals <= 10)
exclude_categories = row_totals[row_totals <= 10].index.tolist()

# Filter table to exclude low-frequency categories
filtered_table = table.loc[~table.index.isin(exclude_categories)]

# Recalculate marginal totals for filtered table
filtered_row_totals = filtered_table.sum(axis=1)
filtered_col_totals = filtered_table.sum(axis=0)
filtered_grand_total = filtered_table.sum().sum()

# Calculate expected frequencies
expected = pd.DataFrame(index=filtered_table.index, columns=filtered_table.columns)
for i in filtered_table.index:
    for j in filtered_table.columns:
        expected.loc[i, j] = (filtered_row_totals[i] * filtered_col_totals[j]) / filtered_grand_total

# Calculate chi-square statistic
chi2 = 0
for i in filtered_table.index:
    for j in filtered_table.columns:
        observed = filtered_table.loc[i, j]
        expected_val = expected.loc[i, j]
        if expected_val > 0:
            chi2 += ((observed - expected_val) ** 2) / expected_val

# Get degrees of freedom
degrees_of_freedom = (len(filtered_table.index) - 1) * (len(filtered_table.columns) - 1)

# Format output
filtered_table_dict = filtered_table.to_dict()
filtered_table_dict['row_totals'] = filtered_row_totals.to_dict()
filtered_table_dict['col_totals'] = filtered_col_totals.to_dict()
filtered_table_dict['grand_total'] = int(filtered_grand_total)

print('__RESULT__:')
print(json.dumps({
    'original_table': table.to_dict(),
    'filtered_table': filtered_table_dict,
    'excluded_categories': exclude_categories,
    'chi_square_statistic': float(chi2),
    'degrees_of_freedom': int(degrees_of_freedom),
    'total_patients_analyzed': int(filtered_grand_total),
    'cdh1_mutated_patients': int(filtered_col_totals.get(True, 0)),
    'cdh1_wildtype_patients': int(filtered_col_totals.get(False, 0))
}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:9': [], 'var_functions.query_db:8': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead."}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.'}, {'Patient_description': 'Case 1db60f09-7f5a-4f21-8003-06a6abc781db, linked to barcode TCGA-29-1694, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-WR-A838 (UUID B8023162-5E82-40E6-AD8C-8ACF81821F01) is recorded as a FEMALE with vital status: Dead.'}, {'Patient_description': "Patient TCGA-31-1955, registered under UUID cce34351-1700-405b-818f-a598f63a33e8, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Patient TCGA-32-4209 (MALE, UUID 5438322c-9db0-4974-ba01-801020559f97) is enrolled in the study of Glioblastoma multiforme. Vital status: Dead.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-29-1696 (UUID 8a98a6e6-b763-4824-858b-fd2738e6c9a3) is recorded as a FEMALE with vital status: Dead.'}, {'Patient_description': 'Record 40635bf3-d8ba-4833-b623-547e55e5d07e refers to patient TCGA-29-2425, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 05019013-7ea5-4905-ac79-901146ba2ee2, linked to barcode TCGA-29-1688, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': 'Record 13319c20-02f6-4b5f-b24f-3d8f4084094c refers to patient TCGA-25-1318, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 79fd602b-3e8e-4353-aa78-4f5f170b607d refers to patient TCGA-25-1328, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'The individual with barcode TCGA-57-1584 and UUID ed21615c-0de3-421c-9e8d-8996026c4431 is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Alive.'}], 'var_functions.query_db:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:32': {'available_vars': ['var_functions.query_db:10', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.query_db:18', 'var_functions.query_db:2', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:24', 'var_functions.query_db:8']}, 'var_functions.execute_python:36': {'clinical_file': 'var_functions.query_db_24', 'mutation_file': 'var_functions.query_db_22', 'clinical_exists': False, 'mutation_exists': False, 'pwd': '/workspace'}, 'var_functions.execute_python:40': {'all_relevant_keys': ['var_functions.query_db:2', 'var_functions.query_db:9', 'var_functions.query_db:8', 'var_functions.query_db:10', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.query_db:18', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:24'], 'clinical_keys': [], 'mutation_keys': [], 'sample_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5', 'var_functions.query_db:9', 'var_functions.query_db:8', 'var_functions.query_db:10', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.query_db:18', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:24', 'var_functions.execute_python:32', 'var_functions.execute_python:36', '__builtins__', 'json']}, 'var_functions.execute_python:44': {'clinical_var_type': "<class 'NoneType'>", 'mutation_var_type': "<class 'NoneType'>", 'clinical_var_exists': False, 'mutation_var_exists': False, 'keys_in_globals': ['var_functions.query_db:2', 'var_functions.query_db:9', 'var_functions.query_db:8', 'var_functions.query_db:10', 'var_functions.query_db:12']}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
