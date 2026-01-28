code = """import json, re

# Load the large query results from storage paths
with open(var_call_NKVx9rUY0bmT41io0Fkwxbwl, 'r') as f:
    clinical_records = json.load(f)
with open(var_call_kyleW9un3A09OlpnHlF6ha38, 'r') as f:
    cdh1_records = json.load(f)

# Build set of ParticipantBarcode that have CDH1 mutations
cdh1_barcodes = set()
for r in cdh1_records:
    val = r.get('ParticipantBarcode')
    if val:
        cdh1_barcodes.add(val.strip())

# From clinical_records (BRCA-related), extract barcodes and histological types for alive patients
barcode_to_hist = {}

pattern = re.compile(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', re.IGNORECASE)
for rec in clinical_records:
    desc = (rec.get('Patient_description') or '').lower()
    # consider alive if 'alive' appears in description
    if 'alive' not in desc:
        continue
    m = pattern.search(rec.get('Patient_description') or '')
    if not m:
        continue
    barcode = m.group(1).upper()
    hist = rec.get('histological_type') or 'Unknown'
    barcode_to_hist[barcode] = hist

# Aggregate counts per histological_type
from collections import defaultdict
counts = defaultdict(lambda: {'alive_total':0, 'mutated_count':0})
for barcode, hist in barcode_to_hist.items():
    counts[hist]['alive_total'] += 1
    if barcode in cdh1_barcodes:
        counts[hist]['mutated_count'] += 1

# Compute percentages and prepare list
results = []
for hist, vals in counts.items():
    total = vals['alive_total']
    mutated = vals['mutated_count']
    pct = (mutated / total * 100) if total>0 else 0.0
    results.append({'histological_type': hist, 'alive_total': total, 'mutated_count': mutated, 'percentage': round(pct, 2)})

# Sort by percentage desc, then mutated_count desc, then alive_total desc
results_sorted = sorted(results, key=lambda x: (-x['percentage'], -x['mutated_count'], -x['alive_total']))

top3 = results_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_X1mWgs8c1YzTh86hW9T2T6fN': ['clinical_info'], 'var_call_1LcEKrlc1nKh4aTlfIDNbEGl': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_iecIGLeugM5PSJ9m5FW8qP2w': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_JBsV8sO2YAU8LLNqWY4CCaYh': [], 'var_call_maQzVSnKz7893oiHX0ty2qZQ': [], 'var_call_K3qDK3DW7wtiMDKvjbVcJTCB': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Hugo_Symbol': 'GLI3'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Hugo_Symbol': 'MUM1L1'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Hugo_Symbol': 'CSF2RA'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Hugo_Symbol': 'CMC4'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Hugo_Symbol': 'THADA'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Hugo_Symbol': 'OBSCN'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Hugo_Symbol': 'RIMS2'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Hugo_Symbol': 'TMEM53'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'CCDC102A'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'WNT7A'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'SIRT2'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'PRKAR2A'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'COPB2'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'FIP1L1'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'EMILIN2'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'TMEM79'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'TTN'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'KRT82'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Hugo_Symbol': 'KLHL38'}, {'ParticipantBarcode': 'TCGA-04-1336', 'Hugo_Symbol': 'PDE4DIP'}, {'ParticipantBarcode': 'TCGA-04-1336', 'Hugo_Symbol': 'LNX2'}, {'ParticipantBarcode': 'TCGA-04-1336', 'Hugo_Symbol': 'TP53'}, {'ParticipantBarcode': 'TCGA-04-1341', 'Hugo_Symbol': 'ITGAE'}, {'ParticipantBarcode': 'TCGA-04-1341', 'Hugo_Symbol': 'LRRK2'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'ZNF471'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'EPS8L3'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'CPSF1'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'SBP1'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'XAB2'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'CENPJ'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'ZFP36'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'CCND1'}, {'ParticipantBarcode': 'TCGA-04-1342', 'Hugo_Symbol': 'ARAP3'}, {'ParticipantBarcode': 'TCGA-04-1343', 'Hugo_Symbol': 'CCDC180'}, {'ParticipantBarcode': 'TCGA-04-1343', 'Hugo_Symbol': 'VWF'}, {'ParticipantBarcode': 'TCGA-04-1343', 'Hugo_Symbol': 'ATG9A'}, {'ParticipantBarcode': 'TCGA-04-1346', 'Hugo_Symbol': 'MTERFD2'}, {'ParticipantBarcode': 'TCGA-04-1346', 'Hugo_Symbol': 'CDH7'}, {'ParticipantBarcode': 'TCGA-04-1348', 'Hugo_Symbol': 'RANBP2'}, {'ParticipantBarcode': 'TCGA-04-1348', 'Hugo_Symbol': 'GCLM'}, {'ParticipantBarcode': 'TCGA-04-1348', 'Hugo_Symbol': 'MAP3K19'}, {'ParticipantBarcode': 'TCGA-04-1348', 'Hugo_Symbol': 'TP53'}, {'ParticipantBarcode': 'TCGA-04-1348', 'Hugo_Symbol': 'KIF21A'}, {'ParticipantBarcode': 'TCGA-04-1348', 'Hugo_Symbol': 'HIST1H3I'}, {'ParticipantBarcode': 'TCGA-04-1349', 'Hugo_Symbol': 'SART1'}, {'ParticipantBarcode': 'TCGA-04-1349', 'Hugo_Symbol': 'NADK'}, {'ParticipantBarcode': 'TCGA-04-1349', 'Hugo_Symbol': 'UBR1'}, {'ParticipantBarcode': 'TCGA-04-1356', 'Hugo_Symbol': 'TP53TG5'}, {'ParticipantBarcode': 'TCGA-04-1356', 'Hugo_Symbol': 'RAB14'}, {'ParticipantBarcode': 'TCGA-04-1356', 'Hugo_Symbol': 'MICAL3'}], 'var_call_W1dp3HbCEnTDEcxw6omPIOy2': 'file_storage/call_W1dp3HbCEnTDEcxw6omPIOy2.json', 'var_call_NKVx9rUY0bmT41io0Fkwxbwl': 'file_storage/call_NKVx9rUY0bmT41io0Fkwxbwl.json', 'var_call_kyleW9un3A09OlpnHlF6ha38': 'file_storage/call_kyleW9un3A09OlpnHlF6ha38.json'}

exec(code, env_args)
