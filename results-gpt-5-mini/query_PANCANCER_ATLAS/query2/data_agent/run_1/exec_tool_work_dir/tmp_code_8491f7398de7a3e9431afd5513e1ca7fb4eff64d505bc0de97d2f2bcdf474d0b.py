code = """import pandas as pd
import json
import re

# Load clinical data (alive breast patients) and mutation participant list from storage paths
clin_path = var_call_6dGHOGbWvf9WYd1EYF4mU3gt
mut_path = var_call_g8XXopK4ayg7VPjkVgRyleeH

df_clin = pd.read_json(clin_path)
df_mut = pd.read_json(mut_path)

# Extract TCGA barcode from Patient_description
barcode_re = re.compile(r'(TCGA-[A-Za-z0-9-]+)')

def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = barcode_re.search(s)
    return m.group(1).upper() if m else None

if 'Patient_description' not in df_clin.columns:
    raise ValueError('Expected Patient_description column in clinical data')

df_clin['barcode'] = df_clin['Patient_description'].apply(extract_barcode)
# Drop rows without a barcode
df_clin = df_clin.dropna(subset=['barcode']).copy()

# Normalize histological_type
if 'histological_type' not in df_clin.columns:
    df_clin['histological_type'] = 'Unknown'
else:
    df_clin['histological_type'] = df_clin['histological_type'].fillna('Unknown')

# Get set of ParticipantBarcodes with CDH1 mutation
if 'ParticipantBarcode' in df_mut.columns:
    cdh1_barcodes = set(df_mut['ParticipantBarcode'].dropna().astype(str).str.upper().unique())
else:
    # If the mutation file structure is list of dicts, convert
    try:
        df_mut2 = pd.DataFrame(var_call_g8XXopK4ayg7VPjkVgRyleeH)
        cdh1_barcodes = set(df_mut2['ParticipantBarcode'].dropna().astype(str).str.upper().unique())
    except Exception:
        cdh1_barcodes = set()

# For each histological type, compute total alive patients and number with CDH1 mutation
group = df_clin.groupby('histological_type').agg(total_patients=('barcode','nunique'))

# compute mutated counts
mut_counts = df_clin[['histological_type','barcode']].drop_duplicates()
mut_counts['has_cdh1'] = mut_counts['barcode'].isin(cdh1_barcodes)
mut_counts = mut_counts.groupby('histological_type').agg(mutated_patients=('has_cdh1','sum'))

# Merge
summary = group.join(mut_counts, how='left').fillna(0)
summary['mutated_patients'] = summary['mutated_patients'].astype(int)
summary['percentage_mutated'] = summary.apply(lambda r: (r['mutated_patients']/r['total_patients']*100) if r['total_patients']>0 else 0, axis=1)

# Sort and pick top 3 by percentage then by mutated count then by total
summary = summary.reset_index()
summary = summary.sort_values(by=['percentage_mutated','mutated_patients','total_patients'], ascending=[False,False,True])

top3 = summary.head(3)

# Prepare result
result = []
for _, row in top3.iterrows():
    result.append({
        'histological_type': row['histological_type'],
        'total_alive_patients': int(row['total_patients']),
        'cdh1_mutated_patients': int(row['mutated_patients']),
        'percentage_mutated': round(float(row['percentage_mutated']), 2)
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_35jtY24Pu27UwqdO1GjTfEL7': ['clinical_info'], 'var_call_PCxSQFtmKPHSsnFd7e4E2rb2': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Dfn433WKTJPlCi0TSn23l5yu': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_RNQK8rZpsv0zbm6HEOvBAdYL': [], 'var_call_tqH6kMaifUYemHHXE3vJ3h0k': 'file_storage/call_tqH6kMaifUYemHHXE3vJ3h0k.json', 'var_call_gpgajEg8Sm00uP0hozdbJXgX': 'file_storage/call_gpgajEg8Sm00uP0hozdbJXgX.json', 'var_call_NfJ9zqIUeCzgLB6en1LJ8u04': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Tumor_SampleBarcode': 'TCGA-A8-A091-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Tumor_SampleBarcode': 'TCGA-A8-A0A1-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Tumor_SampleBarcode': 'TCGA-A8-A0A9-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Tumor_SampleBarcode': 'TCGA-AA-3821-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Tumor_SampleBarcode': 'TCGA-A2-A0YL-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Tumor_SampleBarcode': 'TCGA-AR-A1AT-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Tumor_SampleBarcode': 'TCGA-BS-A0U8-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Tumor_SampleBarcode': 'TCGA-D8-A27G-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Tumor_SampleBarcode': 'TCGA-E6-A1LX-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Tumor_SampleBarcode': 'TCGA-EJ-7782-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Tumor_SampleBarcode': 'TCGA-FI-A2D5-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Tumor_SampleBarcode': 'TCGA-G4-6628-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Tumor_SampleBarcode': 'TCGA-GI-A2C8-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Tumor_SampleBarcode': 'TCGA-VQ-A8PX-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-X6-A8C2', 'Tumor_SampleBarcode': 'TCGA-X6-A8C2-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-EE-A2GO', 'Tumor_SampleBarcode': 'TCGA-EE-A2GO-06A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Splice_Site'}, {'ParticipantBarcode': 'TCGA-13-0889', 'Tumor_SampleBarcode': 'TCGA-13-0889-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-A8-A0A6', 'Tumor_SampleBarcode': 'TCGA-A8-A0A6-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Splice_Site'}, {'ParticipantBarcode': 'TCGA-AA-A02K', 'Tumor_SampleBarcode': 'TCGA-AA-A02K-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-AG-3892', 'Tumor_SampleBarcode': 'TCGA-AG-3892-01A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}], 'var_call_6dGHOGbWvf9WYd1EYF4mU3gt': 'file_storage/call_6dGHOGbWvf9WYd1EYF4mU3gt.json', 'var_call_g8XXopK4ayg7VPjkVgRyleeH': 'file_storage/call_g8XXopK4ayg7VPjkVgRyleeH.json'}

exec(code, env_args)
