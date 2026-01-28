code = """import json
import re
from collections import defaultdict

# Load clinical and mutation data from storage keys
with open(var_call_Pbx4SYqV0OzKQz2OHwZ7AqtX, 'r') as f:
    clinical = json.load(f)
with open(var_call_GnCsnGCkzNr26PIyWINLOInk, 'r') as f:
    mutations = json.load(f)

# Build set of patient barcodes that have CDH1 mutations
mut_barcodes = set()
for m in mutations:
    pb = m.get('ParticipantBarcode')
    if pb:
        mut_barcodes.add(pb.strip())

# Process clinical records: filter Breast patients who are Alive
breast_alive = []
for rec in clinical:
    desc = rec.get('Patient_description','')
    if not desc:
        continue
    if 'breast' in desc.lower() and 'alive' in desc.lower():
        # extract TCGA barcode
        m = re.search(r'(TCGA-[A-Za-z0-9-]+)', desc)
        barcode = m.group(1) if m else None
        # fallback: try to construct from patient_id if looks like last segment
        if not barcode:
            pid = rec.get('patient_id') or rec.get('patient') or rec.get('patient_id')
            if pid:
                pid = str(pid)
                # try to find any TCGA-... in desc first; if not, attempt to find pattern prefix in desc
                m2 = re.search(r'(TCGA-[A-Za-z0-9-]+)', desc)
                if m2:
                    barcode = m2.group(1)
        breast_alive.append({'patient_id': rec.get('patient_id'), 'barcode': barcode, 'histological_type': rec.get('histological_type')})

# Aggregate totals and mutated counts by histological_type
totals = defaultdict(set)  # hist -> set of barcodes
mut_counts = defaultdict(set)
for r in breast_alive:
    hist = r.get('histological_type') or 'Unknown'
    bc = r.get('barcode')
    # Use barcode if available, else use patient_id prefixed to ensure uniqueness
    if not bc or bc.strip()=='' or not bc.startswith('TCGA'):
        # try to build from patient_id by searching any TCGA in desc? but we don't have desc here
        # fallback to patient_id
        bc = 'PID-' + str(r.get('patient_id'))
    totals[hist].add(bc)
    if bc in mut_barcodes:
        mut_counts[hist].add(bc)

# Prepare results: compute percentage
results = []
for hist, barcodes in totals.items():
    total = len(barcodes)
    mutated = len(mut_counts.get(hist, set()))
    pct = (mutated / total * 100) if total>0 else 0.0
    results.append({'histological_type': hist, 'total_alive_patients': total, 'mutated_patients': mutated, 'mutation_percentage': round(pct,4)})

# Sort by percentage desc, then by mutated count desc
results_sorted = sorted(results, key=lambda x: (-x['mutation_percentage'], -x['mutated_patients']))

top3 = results_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_xLGvMiQkGuR9NeCE9sfREf7q': ['clinical_info'], 'var_call_X7I7sxtKpzs4csfdvFBqSgk4': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_ysZTmiZFslLAwz5xuT5bLsP9': 'file_storage/call_ysZTmiZFslLAwz5xuT5bLsP9.json', 'var_call_GwccanqqWFT3gIsqtMJ7j6PT': [], 'var_call_xxjBYG7pR1kfTJfItrWqPjYn': {'columns': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'num_rows_preview': 50, 'breast_matches_count_preview': 0, 'brca_matches_count_preview': 0, 'breast_samples_preview': [], 'brca_samples_preview': []}, 'var_call_Pbx4SYqV0OzKQz2OHwZ7AqtX': 'file_storage/call_Pbx4SYqV0OzKQz2OHwZ7AqtX.json', 'var_call_GnCsnGCkzNr26PIyWINLOInk': 'file_storage/call_GnCsnGCkzNr26PIyWINLOInk.json'}

exec(code, env_args)
