code = """import json
import re
import pandas as pd

clinical_path = var_call_oPulsjm7P2SbmIoKcEWexjgg
with open(clinical_path, 'r') as f:
    clinical = json.load(f)
mut_list = var_call_JGbpnxgDQXAZPBhIa36ynwUX

rows = []
for rec in clinical:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', None)
    if not hist or hist in ['[Not Applicable]', 'None', '']:
        continue
    m = re.search(r'(TCGA-[A-Za-z0-9-]+)', desc)
    if not m:
        continue
    barcode = m.group(1)
    rows.append({'ParticipantBarcode': barcode, 'histological_type': hist.strip()})

if not rows:
    result = {'error': 'No clinical BRCA female patients with known histological_type found.'}
    out = json.dumps(result)
    print('__RESULT__:')
    print(out)
else:
    df = pd.DataFrame(rows)
    df = df.drop_duplicates(subset=['ParticipantBarcode']).reset_index(drop=True)

    mutated_set = set([d['ParticipantBarcode'] for d in mut_list if d.get('ParticipantBarcode')])

    df['CDH1_mutated'] = df['ParticipantBarcode'].apply(lambda x: x in mutated_set)
    # map to strings to avoid boolean column naming issues
    df['mut_status'] = df['CDH1_mutated'].map({True: 'Mutated', False: 'Not_mutated'})

    ct = pd.crosstab(df['histological_type'], df['mut_status'])
    # Ensure both columns exist
    for col in ['Mutated', 'Not_mutated']:
        if col not in ct.columns:
            ct[col] = 0
    ct = ct[['Mutated', 'Not_mutated']]

    row_totals = ct.sum(axis=1)
    removed = row_totals[row_totals <= 10].index.tolist()
    ct_filtered = ct.loc[row_totals > 10]

    if ct_filtered.shape[0] < 2:
        result = {
            'error': 'Not enough histological categories with >10 cases to perform chi-square after filtering.',
            'removed_categories': removed,
            'remaining_categories_count': int(ct_filtered.shape[0])
        }
        out = json.dumps(result)
        print('__RESULT__:')
        print(out)
    else:
        grand_total = int(ct_filtered.values.sum())
        col_totals = ct_filtered.sum(axis=0)
        chi2 = 0.0
        expected = {}
        for row_idx in ct_filtered.index:
            expected[row_idx] = {}
            rtotal = float(row_totals[row_idx])
            for col in ['Mutated', 'Not_mutated']:
                O = float(ct_filtered.at[row_idx, col])
                E = (rtotal * float(col_totals[col])) / grand_total
                expected[row_idx][col] = E
                if E > 0:
                    chi2 += (O - E) ** 2 / E
        dfree = (ct_filtered.shape[0] - 1) * (2 - 1)

        result = {
            'chi_square': chi2,
            'degrees_of_freedom': int(dfree),
            'grand_total': grand_total,
            'contingency_table_filtered': ct_filtered.reset_index().to_dict(orient='records'),
            'expected_counts': expected,
            'removed_categories': removed
        }
        out = json.dumps(result)
        print('__RESULT__:')
        print(out)"""

env_args = {'var_call_8YNnlPJQ3MX5OXgAUoFGva04': ['clinical_info'], 'var_call_W0s91zSe0F2aWdjZjTijeo7u': 'file_storage/call_W0s91zSe0F2aWdjZjTijeo7u.json', 'var_call_XEcdYnf78bCIV99czYhHqDFI': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_NoatGM4sxRB5tivXDDox0HtL': 'file_storage/call_NoatGM4sxRB5tivXDDox0HtL.json', 'var_call_xP6JELmgW5CNxUCBZbjyM6jN': [], 'var_call_oPulsjm7P2SbmIoKcEWexjgg': 'file_storage/call_oPulsjm7P2SbmIoKcEWexjgg.json', 'var_call_JGbpnxgDQXAZPBhIa36ynwUX': [{'ParticipantBarcode': 'TCGA-B9-A8YI'}, {'ParticipantBarcode': 'TCGA-D8-A27G'}, {'ParticipantBarcode': 'TCGA-BH-A0HP'}, {'ParticipantBarcode': 'TCGA-A2-A25A'}, {'ParticipantBarcode': 'TCGA-LL-A9Q3'}, {'ParticipantBarcode': 'TCGA-A2-A0CK'}, {'ParticipantBarcode': 'TCGA-E2-A1L8'}, {'ParticipantBarcode': 'TCGA-A2-A4S2'}, {'ParticipantBarcode': 'TCGA-A7-A425'}, {'ParticipantBarcode': 'TCGA-BS-A0UV'}, {'ParticipantBarcode': 'TCGA-CD-A4MG'}, {'ParticipantBarcode': 'TCGA-AC-A2FO'}, {'ParticipantBarcode': 'TCGA-B6-A0X7'}, {'ParticipantBarcode': 'TCGA-22-1016'}, {'ParticipantBarcode': 'TCGA-FP-A8CX'}, {'ParticipantBarcode': 'TCGA-BR-A44T'}, {'ParticipantBarcode': 'TCGA-06-5416'}, {'ParticipantBarcode': 'TCGA-B5-A11U'}, {'ParticipantBarcode': 'TCGA-LL-A6FP'}, {'ParticipantBarcode': 'TCGA-A7-A4SC'}, {'ParticipantBarcode': 'TCGA-VQ-A91K'}, {'ParticipantBarcode': 'TCGA-FW-A3R5'}, {'ParticipantBarcode': 'TCGA-JX-A3Q0'}, {'ParticipantBarcode': 'TCGA-AC-A2FB'}, {'ParticipantBarcode': 'TCGA-P6-A5OH'}, {'ParticipantBarcode': 'TCGA-DK-AA6Q'}, {'ParticipantBarcode': 'TCGA-AX-A2HD'}, {'ParticipantBarcode': 'TCGA-B5-A11F'}, {'ParticipantBarcode': 'TCGA-PG-A917'}, {'ParticipantBarcode': 'TCGA-2W-A8YY'}, {'ParticipantBarcode': 'TCGA-EO-A22X'}, {'ParticipantBarcode': 'TCGA-NC-A5HD'}, {'ParticipantBarcode': 'TCGA-B6-A40B'}, {'ParticipantBarcode': 'TCGA-AR-A24X'}, {'ParticipantBarcode': 'TCGA-BR-8364'}, {'ParticipantBarcode': 'TCGA-77-A5G1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4'}, {'ParticipantBarcode': 'TCGA-A5-A1OF'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ'}, {'ParticipantBarcode': 'TCGA-CA-6717'}, {'ParticipantBarcode': 'TCGA-CG-4474'}, {'ParticipantBarcode': 'TCGA-BF-A3DL'}, {'ParticipantBarcode': 'TCGA-G9-6365'}, {'ParticipantBarcode': 'TCGA-WT-AB44'}, {'ParticipantBarcode': 'TCGA-E1-A7YJ'}, {'ParticipantBarcode': 'TCGA-AC-A2FF'}, {'ParticipantBarcode': 'TCGA-AP-A0LM'}, {'ParticipantBarcode': 'TCGA-D7-6518'}, {'ParticipantBarcode': 'TCGA-BR-A453'}, {'ParticipantBarcode': 'TCGA-EE-A29E'}, {'ParticipantBarcode': 'TCGA-E9-A5FK'}, {'ParticipantBarcode': 'TCGA-F1-6874'}, {'ParticipantBarcode': 'TCGA-F5-6814'}, {'ParticipantBarcode': 'TCGA-66-2759'}, {'ParticipantBarcode': 'TCGA-B0-5692'}, {'ParticipantBarcode': 'TCGA-BR-A4J9'}, {'ParticipantBarcode': 'TCGA-GC-A3I6'}, {'ParticipantBarcode': 'TCGA-BH-A0E9'}, {'ParticipantBarcode': 'TCGA-EE-A2A6'}, {'ParticipantBarcode': 'TCGA-AR-A5QM'}, {'ParticipantBarcode': 'TCGA-3M-AB47'}, {'ParticipantBarcode': 'TCGA-A2-A1G0'}, {'ParticipantBarcode': 'TCGA-AC-A2B8'}, {'ParticipantBarcode': 'TCGA-A2-A0SY'}, {'ParticipantBarcode': 'TCGA-D7-8574'}, {'ParticipantBarcode': 'TCGA-BR-6803'}, {'ParticipantBarcode': 'TCGA-DD-AAE3'}, {'ParticipantBarcode': 'TCGA-A6-5661'}, {'ParticipantBarcode': 'TCGA-E9-A2JT'}, {'ParticipantBarcode': 'TCGA-LD-A66U'}, {'ParticipantBarcode': 'TCGA-EO-A22U'}, {'ParticipantBarcode': 'TCGA-R5-A804'}, {'ParticipantBarcode': 'TCGA-BH-A209'}, {'ParticipantBarcode': 'TCGA-BR-4188'}, {'ParticipantBarcode': 'TCGA-D7-A748'}, {'ParticipantBarcode': 'TCGA-VQ-A924'}, {'ParticipantBarcode': 'TCGA-BH-AB28'}, {'ParticipantBarcode': 'TCGA-AH-6544'}, {'ParticipantBarcode': 'TCGA-BH-A0C1'}, {'ParticipantBarcode': 'TCGA-50-6590'}, {'ParticipantBarcode': 'TCGA-A2-A0EW'}, {'ParticipantBarcode': 'TCGA-CC-5260'}, {'ParticipantBarcode': 'TCGA-AC-A5XS'}, {'ParticipantBarcode': 'TCGA-EW-A1J5'}, {'ParticipantBarcode': 'TCGA-AC-A8OS'}, {'ParticipantBarcode': 'TCGA-95-7567'}, {'ParticipantBarcode': 'TCGA-OL-A66K'}, {'ParticipantBarcode': 'TCGA-BS-A0U8'}, {'ParticipantBarcode': 'TCGA-42-2590'}, {'ParticipantBarcode': 'TCGA-IN-7808'}, {'ParticipantBarcode': 'TCGA-DD-A4NK'}, {'ParticipantBarcode': 'TCGA-IR-A3LH'}, {'ParticipantBarcode': 'TCGA-AC-A4ZE'}, {'ParticipantBarcode': 'TCGA-AC-A6IV'}, {'ParticipantBarcode': 'TCGA-AX-A0J0'}, {'ParticipantBarcode': 'TCGA-E9-A3X8'}, {'ParticipantBarcode': 'TCGA-PE-A5DD'}, {'ParticipantBarcode': 'TCGA-QF-A5YS'}, {'ParticipantBarcode': 'TCGA-BR-6452'}, {'ParticipantBarcode': 'TCGA-EW-A6SC'}, {'ParticipantBarcode': 'TCGA-AO-A128'}, {'ParticipantBarcode': 'TCGA-VQ-A8PO'}, {'ParticipantBarcode': 'TCGA-DF-A2KV'}, {'ParticipantBarcode': 'TCGA-A2-A0YK'}, {'ParticipantBarcode': 'TCGA-BR-8370'}, {'ParticipantBarcode': 'TCGA-B6-A2IU'}, {'ParticipantBarcode': 'TCGA-CN-6024'}, {'ParticipantBarcode': 'TCGA-C8-A1HO'}, {'ParticipantBarcode': 'TCGA-21-5787'}, {'ParticipantBarcode': 'TCGA-A2-A0CR'}, {'ParticipantBarcode': 'TCGA-DK-A6AW'}, {'ParticipantBarcode': 'TCGA-F4-6570'}, {'ParticipantBarcode': 'TCGA-BR-A4QM'}, {'ParticipantBarcode': 'TCGA-FI-A2D0'}, {'ParticipantBarcode': 'TCGA-FI-A2D5'}, {'ParticipantBarcode': 'TCGA-DD-AADI'}, {'ParticipantBarcode': 'TCGA-B5-A1MW'}, {'ParticipantBarcode': 'TCGA-XF-A9SX'}, {'ParticipantBarcode': 'TCGA-S3-A6ZG'}, {'ParticipantBarcode': 'TCGA-BR-8592'}, {'ParticipantBarcode': 'TCGA-77-8009'}, {'ParticipantBarcode': 'TCGA-AX-A1CE'}, {'ParticipantBarcode': 'TCGA-E2-A576'}, {'ParticipantBarcode': 'TCGA-KQ-A41S'}, {'ParticipantBarcode': 'TCGA-LL-A50Y'}, {'ParticipantBarcode': 'TCGA-BR-8058'}, {'ParticipantBarcode': 'TCGA-C4-A0F0'}, {'ParticipantBarcode': 'TCGA-EY-A5W2'}, {'ParticipantBarcode': 'TCGA-GM-A4E0'}, {'ParticipantBarcode': 'TCGA-EW-A423'}, {'ParticipantBarcode': 'TCGA-CD-5813'}, {'ParticipantBarcode': 'TCGA-AR-A1AT'}, {'ParticipantBarcode': 'TCGA-D1-A103'}, {'ParticipantBarcode': 'TCGA-DU-6392'}, {'ParticipantBarcode': 'TCGA-BH-A18P'}, {'ParticipantBarcode': 'TCGA-Z7-A8R5'}, {'ParticipantBarcode': 'TCGA-GM-A2DD'}, {'ParticipantBarcode': 'TCGA-BH-A28Q'}, {'ParticipantBarcode': 'TCGA-A2-A1FV'}, {'ParticipantBarcode': 'TCGA-GM-A2DO'}, {'ParticipantBarcode': 'TCGA-EB-A5UM'}, {'ParticipantBarcode': 'TCGA-XF-A9T3'}, {'ParticipantBarcode': 'TCGA-X6-A8C2'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ'}, {'ParticipantBarcode': 'TCGA-G2-A3IE'}, {'ParticipantBarcode': 'TCGA-D8-A3Z6'}, {'ParticipantBarcode': 'TCGA-BR-4187'}, {'ParticipantBarcode': 'TCGA-D7-8572'}, {'ParticipantBarcode': 'TCGA-C8-A3M7'}, {'ParticipantBarcode': 'TCGA-CK-6747'}, {'ParticipantBarcode': 'TCGA-EY-A548'}, {'ParticipantBarcode': 'TCGA-A2-A0YL'}, {'ParticipantBarcode': 'TCGA-EJ-7782'}, {'ParticipantBarcode': 'TCGA-G4-6628'}, {'ParticipantBarcode': 'TCGA-G4-6586'}, {'ParticipantBarcode': 'TCGA-BS-A0TE'}, {'ParticipantBarcode': 'TCGA-DD-AADA'}, {'ParticipantBarcode': 'TCGA-BB-A5HY'}, {'ParticipantBarcode': 'TCGA-IB-7651'}, {'ParticipantBarcode': 'TCGA-RP-A694'}, {'ParticipantBarcode': 'TCGA-AR-A2LE'}, {'ParticipantBarcode': 'TCGA-HQ-A2OF'}, {'ParticipantBarcode': 'TCGA-LD-A74U'}, {'ParticipantBarcode': 'TCGA-A1-A0SE'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX'}, {'ParticipantBarcode': 'TCGA-CV-6937'}, {'ParticipantBarcode': 'TCGA-D7-6522'}, {'ParticipantBarcode': 'TCGA-2Y-A9H5'}, {'ParticipantBarcode': 'TCGA-CD-5799'}, {'ParticipantBarcode': 'TCGA-B6-A0IH'}, {'ParticipantBarcode': 'TCGA-FP-8210'}, {'ParticipantBarcode': 'TCGA-A2-A0YD'}, {'ParticipantBarcode': 'TCGA-W8-A86G'}, {'ParticipantBarcode': 'TCGA-BH-A18F'}, {'ParticipantBarcode': 'TCGA-D7-A4YU'}, {'ParticipantBarcode': 'TCGA-H4-A2HQ'}, {'ParticipantBarcode': 'TCGA-MX-A5UG'}, {'ParticipantBarcode': 'TCGA-FS-A1ZK'}, {'ParticipantBarcode': 'TCGA-XX-A89A'}, {'ParticipantBarcode': 'TCGA-AR-A2LK'}, {'ParticipantBarcode': 'TCGA-63-A5MM'}, {'ParticipantBarcode': 'TCGA-06-0210'}, {'ParticipantBarcode': 'TCGA-AA-A01R'}, {'ParticipantBarcode': 'TCGA-SJ-A6ZI'}, {'ParticipantBarcode': 'TCGA-A7-A5ZX'}, {'ParticipantBarcode': 'TCGA-E2-A10F'}, {'ParticipantBarcode': 'TCGA-AD-6964'}, {'ParticipantBarcode': 'TCGA-EB-A3XC'}, {'ParticipantBarcode': 'TCGA-LD-A7W6'}, {'ParticipantBarcode': 'TCGA-E6-A1LX'}, {'ParticipantBarcode': 'TCGA-B5-A11G'}, {'ParticipantBarcode': 'TCGA-PE-A5DE'}, {'ParticipantBarcode': 'TCGA-4H-AAAK'}, {'ParticipantBarcode': 'TCGA-HT-A617'}, {'ParticipantBarcode': 'TCGA-BR-8686'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ'}, {'ParticipantBarcode': 'TCGA-05-5428'}, {'ParticipantBarcode': 'TCGA-D8-A1XO'}, {'ParticipantBarcode': 'TCGA-D8-A1Y1'}, {'ParticipantBarcode': 'TCGA-AC-A2FG'}, {'ParticipantBarcode': 'TCGA-AR-A2LN'}, {'ParticipantBarcode': 'TCGA-F4-6856'}, {'ParticipantBarcode': 'TCGA-GI-A2C8'}, {'ParticipantBarcode': 'TCGA-OD-A75X'}, {'ParticipantBarcode': 'TCGA-55-A4DF'}, {'ParticipantBarcode': 'TCGA-5L-AAT0'}, {'ParticipantBarcode': 'TCGA-AX-A06L'}, {'ParticipantBarcode': 'TCGA-C8-A274'}, {'ParticipantBarcode': 'TCGA-BH-A8FY'}, {'ParticipantBarcode': 'TCGA-EO-A22R'}, {'ParticipantBarcode': 'TCGA-AC-A3OD'}, {'ParticipantBarcode': 'TCGA-A2-A0T6'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ'}, {'ParticipantBarcode': 'TCGA-AR-A1AL'}, {'ParticipantBarcode': 'TCGA-XX-A899'}, {'ParticipantBarcode': 'TCGA-AX-A2HA'}, {'ParticipantBarcode': 'TCGA-D8-A27I'}, {'ParticipantBarcode': 'TCGA-B5-A0JY'}, {'ParticipantBarcode': 'TCGA-B6-A40C'}, {'ParticipantBarcode': 'TCGA-DK-A1AG'}, {'ParticipantBarcode': 'TCGA-AC-A6IX'}, {'ParticipantBarcode': 'TCGA-E2-A1IJ'}, {'ParticipantBarcode': 'TCGA-B5-A11E'}, {'ParticipantBarcode': 'TCGA-BR-4279'}, {'ParticipantBarcode': 'TCGA-CR-7370'}, {'ParticipantBarcode': 'TCGA-OL-A66N'}, {'ParticipantBarcode': 'TCGA-63-A5MH'}, {'ParticipantBarcode': 'TCGA-BR-A4IV'}, {'ParticipantBarcode': 'TCGA-GM-A5PX'}, {'ParticipantBarcode': 'TCGA-XF-AAN0'}, {'ParticipantBarcode': 'TCGA-A5-A0VO'}, {'ParticipantBarcode': 'TCGA-BR-8677'}, {'ParticipantBarcode': 'TCGA-BR-4292'}, {'ParticipantBarcode': 'TCGA-D7-A6EY'}, {'ParticipantBarcode': 'TCGA-D8-A27V'}, {'ParticipantBarcode': 'TCGA-B7-A5TI'}, {'ParticipantBarcode': 'TCGA-94-7943'}, {'ParticipantBarcode': 'TCGA-GM-A5PV'}, {'ParticipantBarcode': 'TCGA-AA-A00N'}, {'ParticipantBarcode': 'TCGA-BR-6566'}, {'ParticipantBarcode': 'TCGA-EO-A3AZ'}, {'ParticipantBarcode': 'TCGA-AX-A2HC'}, {'ParticipantBarcode': 'TCGA-55-8614'}, {'ParticipantBarcode': 'TCGA-E2-A1IH'}, {'ParticipantBarcode': 'TCGA-D5-6928'}, {'ParticipantBarcode': 'TCGA-E9-A6HE'}, {'ParticipantBarcode': 'TCGA-AC-A3YI'}]}

exec(code, env_args)
