code = """import json, re
# load clinical LGG results
p_clin = var_call_u9ZXvr3twvoIiW6DiOxtlulr
with open(p_clin, 'r') as f:
    clin = json.load(f)
# load IGF2 expression rows
p_igf = var_call_gWUyr7BlMGzeKlhet6OTBFZf
with open(p_igf, 'r') as f:
    igf = json.load(f)

# build mapping from participant barcode to histological_type from clinical
barcode_to_hist = {}
pattern = re.compile(r'(TCGA-[A-Za-z0-9]+-[A-Za-z0-9]+)', re.IGNORECASE)
for row in clin:
    pd = row.get('Patient_description','')
    m = pattern.search(pd)
    if not m:
        # also try to find token like TCGA-XX-XXXX within patient_id maybe
        continue
    bc = m.group(1).upper()
    hist = row.get('histological_type')
    if hist is None:
        continue
    hist_strip = hist.strip()
    # exclude histologies enclosed in square brackets
    if hist_strip.startswith('[') and hist_strip.endswith(']'):
        continue
    # Only keep if not enclosed; if multiple entries for same barcode, prefer non-empty hist
    if bc not in barcode_to_hist and hist_strip:
        barcode_to_hist[bc] = hist_strip

# Now process IGF2 rows, filter to those with participant in barcode_to_hist and valid numeric normalized_count
from math import log10
values_by_hist = {}
for row in igf:
    part = row.get('ParticipantBarcode')
    if not part:
        continue
    part_up = part.strip().upper()
    # sometimes ParticipantBarcode includes full like TCGA-AB-2908, good
    if part_up not in barcode_to_hist:
        continue
    nc = row.get('normalized_count')
    # handle numeric strings
    try:
        nc_f = float(nc)
    except Exception:
        continue
    if nc_f < 0:
        continue
    # compute log10(nc+1)
    val = log10(nc_f + 1.0)
    hist = barcode_to_hist[part_up]
    values_by_hist.setdefault(hist, []).append(val)

# compute means
import statistics
result = {}
for hist, vals in values_by_hist.items():
    if len(vals) == 0:
        continue
    meanv = statistics.mean(vals)
    # format with at least 4 decimal places
    result[hist] = float(f"{meanv:.4f}")

# Sort keys for deterministic output
result_sorted = {k: result[k] for k in sorted(result.keys())}
print("__RESULT__:")
print(json.dumps(result_sorted))"""

env_args = {'var_call_LbgPtZExvwJtrs4UATQNVFpu': ['clinical_info'], 'var_call_xnzj4OKSQf9x5TcVu1yCPXI7': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_nhNStC2SRmzpwyGyn7MgSIVB': 'file_storage/call_nhNStC2SRmzpwyGyn7MgSIVB.json', 'var_call_COJl6LlFAfQv84wGi8aKSnV0': {'columns_sample': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'tumor_tissue_site_unique_sample': ['Ovary'], 'diagnosis_sample': ['None'], 'patient_description_samples': ['In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.']}, 'var_call_gWUyr7BlMGzeKlhet6OTBFZf': 'file_storage/call_gWUyr7BlMGzeKlhet6OTBFZf.json', 'var_call_9atGTUuE9zeX0dAIxIBvA4Ws': 'file_storage/call_9atGTUuE9zeX0dAIxIBvA4Ws.json', 'var_call_u9ZXvr3twvoIiW6DiOxtlulr': 'file_storage/call_u9ZXvr3twvoIiW6DiOxtlulr.json'}

exec(code, env_args)
