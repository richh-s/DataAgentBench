code = """import json
import re
from collections import defaultdict

# Load clinical BRCA records
with open(var_call_7Ipuk5pdB78CNv3PUjhUfrol, 'r') as f:
    clinical = json.load(f)

# Load mutation participant barcodes for CDH1
# var_call_TLLt3TF3iA35ULjsNu38pr0m is a file path
with open(var_call_TLLt3TF3iA35ULjsNu38pr0m, 'r') as f:
    mut_participants = json.load(f)

mut_set = set()
for r in mut_participants:
    v = r.get('ParticipantBarcode')
    if v:
        mut_set.add(v.strip())

# Map patient barcode to histological_type for alive BRCA patients
barcode_hist = {}
for rec in clinical:
    pd = rec.get('Patient_description','')
    hist = rec.get('histological_type')
    # Only consider records that indicate Alive
    if not pd or 'alive' not in pd.lower():
        continue
    # extract TCGA barcode
    m = re.search(r'(TCGA-[A-Za-z0-9-]+)', pd)
    if not m:
        continue
    barcode = m.group(1).strip()
    # normalize: some barcodes in mutation list may have different segment counts; keep as-is
    if barcode not in barcode_hist:
        # treat missing hist as string 'None'
        barcode_hist[barcode] = hist if hist is not None else 'None'

# Aggregate counts per histology
total_counts = defaultdict(int)
mut_counts = defaultdict(int)
for barcode, hist in barcode_hist.items():
    total_counts[hist] += 1
    if barcode in mut_set:
        mut_counts[hist] += 1

# Prepare results
results = []
for hist, total in total_counts.items():
    mutated = mut_counts.get(hist, 0)
    pct = (mutated/total*100) if total>0 else 0.0
    results.append({'histological_type': hist, 'total_alive': total, 'mutated_count': mutated, 'mutation_percentage': round(pct,4)})

# Sort by percentage desc, then mutated_count desc, then total_alive desc
results_sorted = sorted(results, key=lambda x: (-x['mutation_percentage'], -x['mutated_count'], -x['total_alive']))

top3 = results_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_CRDwydC65votVpGrOrFj3I3v': ['clinical_info'], 'var_call_OAY479d5tFKUQEry0wxt8xzE': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_DxfJNSPJbCAWTpiUdXPqS3RS': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_5QKWfjYZU4IAnbhpso35RjNS': 'file_storage/call_5QKWfjYZU4IAnbhpso35RjNS.json', 'var_call_VcTJfAn6qGSOb7fIWH2ucOOI': 'file_storage/call_VcTJfAn6qGSOb7fIWH2ucOOI.json', 'var_call_7Ipuk5pdB78CNv3PUjhUfrol': 'file_storage/call_7Ipuk5pdB78CNv3PUjhUfrol.json', 'var_call_TLLt3TF3iA35ULjsNu38pr0m': 'file_storage/call_TLLt3TF3iA35ULjsNu38pr0m.json'}

exec(code, env_args)
