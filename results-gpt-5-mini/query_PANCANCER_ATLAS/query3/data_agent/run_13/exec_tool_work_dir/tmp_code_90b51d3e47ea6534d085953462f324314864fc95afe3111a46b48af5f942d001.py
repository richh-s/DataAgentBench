code = """import json
# load clinical female breast data file
p = var_call_doqU7ZNkg17oSciUu06uVyoV
with open(p, 'r') as f:
    clinical = json.load(f)
# load molecular PASS CDH1 file
pm = var_call_LAl0S3kkuinPJu3iawKKu62T
with open(pm, 'r') as f:
    molecular = json.load(f)

import pandas as pd
clin_df = pd.DataFrame(clinical)
mol_df = pd.DataFrame(molecular)

# normalize participant barcodes in mol to patient-level (first 12 chars for TCGA?)
# Clinical Patient_description contains full barcode like TCGA-XX-XXXX
# Use ParticipantBarcode from molecular and match to clinical by whether Patient_description contains that barcode
mol_parts = sorted(mol_df['ParticipantBarcode'].unique())
# Create set for quick lookup
mol_set = set(mol_parts)

# Extract patient barcode from Patient_description string using token that matches TCGA-.* pattern
import re

def extract_barcode(s):
    m = re.search(r'TCGA[-A-Z0-9]+[-A-Z0-9]+', s)
    return m.group(0) if m else None

clin_df['barcode'] = clin_df['Patient_description'].astype(str).apply(extract_barcode)
# keep only records with barcode and histological_type known and not None or 'None'
keep = clin_df[(clin_df['barcode'].notna()) & (clin_df['histological_type'].notna()) & (clin_df['histological_type'].str.strip().str.lower() != 'none')]

# restrict to females - ensure Patient_description contains FEMALE
keep = keep[keep['Patient_description'].str.contains('FEMALE', case=False, na=False)]

# Now mark whether each clinical barcode has a PASS CDH1 mutation
keep['has_CDH1_PASS'] = keep['barcode'].apply(lambda b: b in mol_set)

# Count histological types with totals > 10
counts = keep['histological_type'].value_counts()
selected_hists = counts[counts>10].index.tolist()
# filter keep to selected_hists
filt = keep[keep['histological_type'].isin(selected_hists)]

# create contingency table: rows histological types, cols mutation present True/False
ct = pd.crosstab(filt['histological_type'], filt['has_CDH1_PASS'])
ct = ct.sort_index()
# compute chi-square statistic manually
obs = ct.values
row_totals = obs.sum(axis=1)
col_totals = obs.sum(axis=0)
grand_total = obs.sum()
import numpy as np
E = np.outer(row_totals, col_totals) / grand_total
chi2 = ((obs - E)**2 / E).sum()

result = {
    'selected_histological_types': selected_hists,
    'contingency_table': ct.reset_index().to_dict(orient='records'),
    'observed_matrix': obs.tolist(),
    'expected_matrix': E.tolist(),
    'chi2_statistic': float(chi2),
    'degrees_of_freedom': int((obs.shape[0]-1)*(obs.shape[1]-1)),
    'grand_total': int(grand_total)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_nozhe26iYLtpf3Vr0MbwN4zF': ['clinical_info'], 'var_call_9ABgWctxsadvEsVX8W4X9wIw': 'file_storage/call_9ABgWctxsadvEsVX8W4X9wIw.json', 'var_call_HDYJswa6GyHqGP6DpCyl8zUJ': {'columns': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'candidate_cols': ['icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'person_neoplasm_cancer_status', 'histological_type', 'tissue_source_site', 'eastern_cancer_oncology_group', 'residual_tumor', 'histological_type_other', 'tumor_tissue_site_other', 'axillary_lymph_node_stage_method_type', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'days_to_new_tumor_event_after_initial_treatment', 'family_history_of_cancer'], 'patient_description_counts': {'contains_BRCA': 0, 'contains_breast': 0}, 'total_rows': 5}, 'var_call_sJFbusY0e9c4OhxQrz84IZcR': 'file_storage/call_sJFbusY0e9c4OhxQrz84IZcR.json', 'var_call_UlZRf8iZcLkt4A758O3Q6TXz': {'unique_hist_types_count': 11, 'top_hist_types': [['Infiltrating Ductal Carcinoma', 777], ['Infiltrating Lobular Carcinoma', 201], ['Other  specify', 46], ['Mixed Histology (please specify)', 30], ['Mucinous Carcinoma', 17], ['Metaplastic Carcinoma', 8], ['Medullary Carcinoma', 6], ['None', 2], ['Infiltrating Carcinoma NOS', 1], ['Diffuse large B-cell lymphoma (DLBCL) NOS (any anatomic site nodal or extranodal)', 1], ['Leiomyosarcoma (LMS)', 1]], 'total_records': 1090}, 'var_call_doqU7ZNkg17oSciUu06uVyoV': 'file_storage/call_doqU7ZNkg17oSciUu06uVyoV.json', 'var_call_RuvyxegVhVHdt2h1Wmpvd6hK': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}], 'var_call_LAl0S3kkuinPJu3iawKKu62T': 'file_storage/call_LAl0S3kkuinPJu3iawKKu62T.json', 'var_call_9kxSCQcrUG8xc4f2uvakBOFu': {'pass_cdh1_count': 247, 'examples_first_20': ['TCGA-05-5428', 'TCGA-06-0210', 'TCGA-06-5416', 'TCGA-21-5787', 'TCGA-22-1016', 'TCGA-2W-A8YY', 'TCGA-2Y-A9H5', 'TCGA-3M-AB47', 'TCGA-42-2590', 'TCGA-4H-AAAK', 'TCGA-50-6590', 'TCGA-55-8614', 'TCGA-55-A4DF', 'TCGA-5L-AAT0', 'TCGA-63-A5MH', 'TCGA-63-A5MM', 'TCGA-66-2759', 'TCGA-77-8009', 'TCGA-77-A5G1', 'TCGA-94-7943']}}

exec(code, env_args)
