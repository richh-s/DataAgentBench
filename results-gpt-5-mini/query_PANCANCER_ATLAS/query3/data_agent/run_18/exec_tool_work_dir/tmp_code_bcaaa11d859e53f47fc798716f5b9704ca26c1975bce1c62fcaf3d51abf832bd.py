code = """import json
import re
import pandas as pd

clinical_path = var_call_kPrfeGwjv27evuhf8zWlxOMt
mut_path = var_call_nXCvAMkLLW60oJJ9Zt0HntiR

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(mut_path, 'r') as f:
    mutations = json.load(f)

clin_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Extract ParticipantBarcode from Patient_description
def extract_barcode(desc):
    if not desc:
        return None
    m = re.search(r'TCGA-[A-Za-z0-9-]+', desc)
    return m.group(0) if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Filter for female and Breast invasive carcinoma cohort
clin_df = clin_df[clin_df['Patient_description'].str.contains('FEMALE', case=False, na=False)]
clin_df = clin_df[clin_df['ParticipantBarcode'].notna()]
clin_df = clin_df[clin_df['histological_type'].notna()]

# Drop duplicates by ParticipantBarcode keeping first
unique_clin = clin_df.drop_duplicates(subset=['ParticipantBarcode']).copy()

# Normalize barcodes: some mutation barcodes may differ in format; we'll try matching by prefix TCGA-XX-YYYY
# Get set of mutation ParticipantBarcode values
mut_set = set(mut_df['ParticipantBarcode'].unique())

# Function to match clinical barcode to mutation barcodes by exact match or by replacing last segment if needed

def match_barcode(clin_barcode):
    if clin_barcode in mut_set:
        return clin_barcode
    # Sometimes clinical has TCGA-XX-YYYY where YYYY shorter/longer; try match by first two parts
    parts = clin_barcode.split('-')
    if len(parts) >= 3:
        prefix = '-'.join(parts[:2])
        # find any mutation barcode that startswith prefix
        for m in mut_set:
            if m.startswith(prefix+'-'):
                return m
    return None

unique_clin['MutationBarcodeMatched'] = unique_clin['ParticipantBarcode'].apply(match_barcode)
unique_clin['CDH1_mutated'] = unique_clin['MutationBarcodeMatched'].notna()

contingency = unique_clin.groupby(['histological_type', 'CDH1_mutated']).size().unstack(fill_value=0)
if True not in contingency.columns:
    contingency[True] = 0
if False not in contingency.columns:
    contingency[False] = 0
contingency = contingency[[True, False]].rename(columns={True: 'Mutated', False: 'Not_Mutated'})
contingency['Row_Total'] = contingency['Mutated'] + contingency['Not_Mutated']

included = contingency[contingency['Row_Total'] > 10].copy()

# Compute chi-square
grand_total = included['Row_Total'].sum()
col_totals = [included['Mutated'].sum(), included['Not_Mutated'].sum()]
chi2 = 0.0
for idx, row in included.iterrows():
    row_total = row['Row_Total']
    for j, col in enumerate(['Mutated', 'Not_Mutated']):
        O = row[col]
        E = (row_total * col_totals[j]) / grand_total if grand_total>0 else 0
        if E>0:
            chi2 += (O - E)**2 / E

r = included.shape[0]
df = (r-1)*(2-1) if r>0 else 0

included_histos = []
for idx, row in included.iterrows():
    included_histos.append({'histological_type': idx, 'Mutated': int(row['Mutated']), 'Not_Mutated': int(row['Not_Mutated']), 'Row_Total': int(row['Row_Total'])})

result = {
    'chi2': chi2,
    'degrees_of_freedom': df,
    'grand_total': int(grand_total),
    'column_totals': {'Mutated': int(col_totals[0]), 'Not_Mutated': int(col_totals[1])},
    'included_histologies': included_histos,
    'excluded_histology_count': int(contingency.shape[0] - included.shape[0])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EZConpLNNtTMuMHqwpFGCPmZ': ['clinical_info'], 'var_call_4Bo1zPhpt8F051RJTIEiJptH': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_eZ2gRyyrwAfUjcUJlM6Vbk5s': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_adNAHTxP5f0V2biww0rq8Qci': 'file_storage/call_adNAHTxP5f0V2biww0rq8Qci.json', 'var_call_ZCOG8WZGyXMcorybiEOoCO4m': [], 'var_call_U1Fil0FI5kei2c3BCsbICuQd': 'file_storage/call_U1Fil0FI5kei2c3BCsbICuQd.json', 'var_call_kPrfeGwjv27evuhf8zWlxOMt': 'file_storage/call_kPrfeGwjv27evuhf8zWlxOMt.json', 'var_call_nXCvAMkLLW60oJJ9Zt0HntiR': 'file_storage/call_nXCvAMkLLW60oJJ9Zt0HntiR.json', 'var_call_j97ieRM1DWC8xoBVwH4olaNl': {'clinical_len': 1074, 'mutation_len': 261, 'clinical_first3': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_id': 'A5EH'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_id': 'A7SZ'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_id': 'A0FY'}], 'mutation_first3': [{'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.N315Ifs*41', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.A824V', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}], 'clinical_columns_sample': ['Patient_description', 'histological_type', 'patient_id'], 'mutation_columns_sample': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER']}}

exec(code, env_args)
