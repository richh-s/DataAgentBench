code = """import json
# load IGF2 expression data
path = var_call_TerQ9q1rcX8NasuGrMc02pyx
with open(path, 'r', encoding='utf-8') as f:
    expr = json.load(f)

# load LGG patient mapping from previous clinical execute_python result
path2 = var_call_W9uHS9co0uAsnSyoXaQL0SvB
with open(path2, 'r', encoding='utf-8') as f:
    clinical_map = json.load(f)

# Build mapping from patient barcode (first 3 fields of TCGA code) to histology
# Expression ParticipantBarcode seems to have formats like TCGA-XX-1234 or TCGA-XX-1234-01A
# We'll normalize both by taking first 3 dash fields e.g., TCGA-XX-1234
import re

lgg_map = clinical_map['mapping']
# create simpler mapping: for keys like TCGA-AB-1234-01A convert to TCGA-AB-1234
simple_lgg = {}
for k,v in lgg_map.items():
    m = re.match(r'^(TCGA-[A-Z0-9]+-[A-Z0-9]+)', k)
    if m:
        simple = m.group(1)
        simple_lgg[simple] = v

# Now iterate expression records, select those where participant belongs to LGG simple map
import math
from collections import defaultdict
vals = defaultdict(list)
for r in expr:
    part = r.get('ParticipantBarcode')
    if not part:
        continue
    # normalize
    m = re.match(r'^(TCGA-[A-Z0-9]+-[A-Z0-9]+)', part.upper())
    if not m:
        continue
    simple = m.group(1)
    if simple not in simple_lgg:
        continue
    # get normalized_count
    try:
        nc = float(r.get('normalized_count'))
    except:
        continue
    # only include valid expression values (non-null, non-negative?) We'll include nc >=0
    if nc is None:
        continue
    if nc < 0:
        continue
    # compute log10(normalized_count + 1)
    val = math.log10(nc + 1)
    hist = simple_lgg[simple]
    vals[hist].append(val)

# compute averages with at least 4 decimal places
res = []
for hist, arr in vals.items():
    if len(arr)==0:
        continue
    avg = sum(arr)/len(arr)
    res.append({'histology': hist, 'n_samples': len(arr), 'avg_log10_IGF2': round(avg, 4)})

# sort by histology
res = sorted(res, key=lambda x: x['histology'])
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_pGHKpjl8l0XDfFjOk5wLOpvO': ['clinical_info'], 'var_call_DRS1NDLRTZqBYG3860IQDIlZ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_uG2bCohG0ZXUfS90nW1rtvIO': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_okCM9iP5pjpbT1GCWl7T1wFo': 'file_storage/call_okCM9iP5pjpbT1GCWl7T1wFo.json', 'var_call_JqcfvD05Y4Be4hcdEU4loPEw': 'file_storage/call_JqcfvD05Y4Be4hcdEU4loPEw.json', 'var_call_W9uHS9co0uAsnSyoXaQL0SvB': 'file_storage/call_W9uHS9co0uAsnSyoXaQL0SvB.json', 'var_call_TerQ9q1rcX8NasuGrMc02pyx': 'file_storage/call_TerQ9q1rcX8NasuGrMc02pyx.json'}

exec(code, env_args)
