code = """import json
import math

# Contingency table data from previous analysis
contingency_table = [
    [9, 757],   # Infiltrating Ductal Carcinoma: CDH1+, CDH1-
    [83, 118],  # Infiltrating Lobular Carcinoma: CDH1+, CDH1-
    [0, 17],    # Mucinous Carcinoma: CDH1+, CDH1-
    [4, 26]     # Mixed Histology: CDH1+, CDH1-
]

row_labels = [
    "Infiltrating Ductal Carcinoma",
    "Infiltrating Lobular Carcinoma", 
    "Mucinous Carcinoma",
    "Mixed Histology (please specify)"
]

# Calculate marginal totals
row_totals = [row[0] + row[1] for row in contingency_table]
col_totals = [
    sum([row[0] for row in contingency_table]),  # CDH1+ column
    sum([row[1] for row in contingency_table])   # CDH1- column
]

grand_total = sum(row_totals)

print("Contingency Table:")
print("=" * 60)
print(f"{'Histological Type':<45} {'CDH1+':<10} {'CDH1-':<10} {'Total':<10}")
print("-" * 60)
for i, label in enumerate(row_labels):
    print(f"{label:<45} {contingency_table[i][0]:<10} {contingency_table[i][1]:<10} {row_totals[i]:<10}")
print("-" * 60)
print(f"{'Column Totals':<45} {col_totals[0]:<10} {col_totals[1]:<10} {grand_total:<10}")
print()

# Calculate chi-square statistic
chi_square = 0
calculations = []

for i, row in enumerate(contingency_table):
    for j, observed in enumerate(row):
        # Expected value Eij = (row_total * col_total) / grand_total
        expected = (row_totals[i] * col_totals[j]) / grand_total
        
        # Chi-square contribution = (O - E)^2 / E
        contribution = (observed - expected)**2 / expected
        chi_square += contribution
        
        calculations.append({
            'row': row_labels[i],
            'column': 'CDH1+' if j == 0 else 'CDH1-',
            'observed': observed,
            'expected': round(expected, 2),
            'contribution': round(contribution, 4)
        })

# Print calculations table
print("Chi-square Calculation Details:")
print("=" * 80)
print(f"{'Histological Type':<35} {'Column':<10} {'Observed':<10} {'Expected':<10} {'(O-E)^2/E':<12}")
print("-" * 80)
for calc in calculations:
    print(f"{calc['row']:<35} {calc['column']:<10} {calc['observed']:<10} {calc['expected']:<10} {calc['contribution']:<12}")
print("-" * 80)
print(f"{'Chi-square statistic':<67} {round(chi_square, 4):<12}")
print()

# Determine degrees of freedom
df = (len(row_labels) - 1) * (len(contingency_table[0]) - 1)

# Critical value for chi-square at typical significance levels
alpha_0_05 = 7.815  # df=3, alpha=0.05
alpha_0_01 = 11.345  # df=3, alpha=0.01

print("Statistical Summary:")
print("=" * 40)
print(f"Degrees of freedom: {df}")
print(f"Chi-square value: {round(chi_square, 4)}")
print(f"Critical value (α=0.05): {alpha_0_05}")
print(f"Critical value (α=0.01): {alpha_0_01}")
print()

if chi_square > alpha_0_01:
    significance = "highly significant (p < 0.01)"
elif chi_square > alpha_0_05:
    significance = "significant (p < 0.05)"
else:
    significance = "not significant (p ≥ 0.05)"

print(f"Result: The association is {significance}")
print()

# Summary for return
result_summary = {
    "contingency_table": {
        "rows": row_labels,
        "columns": ["CDH1+", "CDH1-"],
        "data": contingency_table,
        "row_totals": row_totals,
        "column_totals": col_totals,
        "grand_total": grand_total
    },
    "chi_square_statistic": round(chi_square, 4),
    "degrees_of_freedom": df,
    "significance": significance,
    "p_value_range": "< 0.001" if chi_square > alpha_0_01 else ("< 0.05" if chi_square > alpha_0_05 else ">= 0.05")
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead."}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.'}, {'Patient_description': 'Case 1db60f09-7f5a-4f21-8003-06a6abc781db, linked to barcode TCGA-29-1694, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-WR-A838 (UUID B8023162-5E82-40E6-AD8C-8ACF81821F01) is recorded as a FEMALE with vital status: Dead.'}, {'Patient_description': "Patient TCGA-31-1955, registered under UUID cce34351-1700-405b-818f-a598f63a33e8, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Patient TCGA-32-4209 (MALE, UUID 5438322c-9db0-4974-ba01-801020559f97) is enrolled in the study of Glioblastoma multiforme. Vital status: Dead.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-29-1696 (UUID 8a98a6e6-b763-4824-858b-fd2738e6c9a3) is recorded as a FEMALE with vital status: Dead.'}, {'Patient_description': 'Record 40635bf3-d8ba-4833-b623-547e55e5d07e refers to patient TCGA-29-2425, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 05019013-7ea5-4905-ac79-901146ba2ee2, linked to barcode TCGA-29-1688, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': 'Record 13319c20-02f6-4b5f-b24f-3d8f4084094c refers to patient TCGA-25-1318, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 79fd602b-3e8e-4353-aa78-4f5f170b607d refers to patient TCGA-25-1328, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'The individual with barcode TCGA-57-1584 and UUID ed21615c-0de3-421c-9e8d-8996026c4431 is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Alive.'}], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Tumor_SampleBarcode': 'TCGA-A8-A091-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A091-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A091-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A091-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E243K', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.727G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Tumor_SampleBarcode': 'TCGA-A8-A0A1-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A1-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A1-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A1-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q307Hfs*2', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.921_955delAGATCCTGAGCTCCCTGACAAAAATATGTTCACCA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Tumor_SampleBarcode': 'TCGA-A8-A0A9-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A9-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A9-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A9-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q503*', 'Variant_Classification': 'Nonsense_Mutation', 'HGVSc': 'c.1507C>T', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Tumor_SampleBarcode': 'TCGA-AA-3821-01A', 'Tumor_AliquotBarcode': 'TCGA-AA-3821-01A-01W-0995-10', 'Normal_SampleBarcode': 'TCGA-AA-3821-10A', 'Normal_AliquotBarcode': 'TCGA-AA-3821-10A-01W-0995-10', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V365I', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1093G>A', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Tumor_SampleBarcode': 'TCGA-A2-A0YL-01A', 'Tumor_AliquotBarcode': 'TCGA-A2-A0YL-01A-21D-A10G-09', 'Normal_SampleBarcode': 'TCGA-A2-A0YL-10A', 'Normal_AliquotBarcode': 'TCGA-A2-A0YL-10A-01D-A10G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.1090_1100delACAGTCACTGA', 'CENTERS': 'INDELOCATOR*|PINDEL', 'FILTER': 'PASS'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.list_db:20': ['clinical_info'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:34': {'total_female_brca': 1029, 'histological_counts': {'Infiltrating Ductal Carcinoma': 766, 'Infiltrating Lobular Carcinoma': 201, 'Metaplastic Carcinoma': 8, 'Infiltrating Carcinoma NOS': 1, 'Mucinous Carcinoma': 17, 'Medullary Carcinoma': 6, 'Mixed Histology (please specify)': 30}, 'cdh1_mutation_barcodes': 1}, 'var_functions.execute_python:38': {'total_unique_patients': 1029, 'sample_patients': ['TCGA-5L-AAT0', 'TCGA-AC-A8OR', 'TCGA-BH-AB28', 'TCGA-A8-A06Q', 'TCGA-GI-A2C9']}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:44': {'total_patients': 1029, 'hist_type_counts': {'Infiltrating Ductal Carcinoma': 766, 'Infiltrating Lobular Carcinoma': 201, 'Metaplastic Carcinoma': 8, 'Infiltrating Carcinoma NOS': 1, 'Mucinous Carcinoma': 17, 'Medullary Carcinoma': 6, 'Mixed Histology (please specify)': 30}, 'cdh1_mutations': 97}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': {'total_female_brca': 1029, 'histological_counts': {'Infiltrating Ductal Carcinoma': 766, 'Infiltrating Lobular Carcinoma': 201, 'Metaplastic Carcinoma': 8, 'Infiltrating Carcinoma NOS': 1, 'Mucinous Carcinoma': 17, 'Medullary Carcinoma': 6, 'Mixed Histology (please specify)': 30}, 'cdh1_brca_mutations': 97}, 'var_functions.execute_python:52': {'excluded_categories': ['Metaplastic Carcinoma', 'Infiltrating Carcinoma NOS', 'Medullary Carcinoma'], 'included_categories': ['Infiltrating Ductal Carcinoma', 'Infiltrating Lobular Carcinoma', 'Mucinous Carcinoma', 'Mixed Histology (please specify)'], 'contingency_table': [[9, 757], [83, 118], [0, 17], [4, 26]], 'row_labels': ['Infiltrating Ductal Carcinoma', 'Infiltrating Lobular Carcinoma', 'Mucinous Carcinoma', 'Mixed Histology (please specify)']}}

exec(code, env_args)
