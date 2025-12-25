code = """import json, pandas as pd
cdh1_file = var_call_KTH0WrCvkBRCClTw96td4gjV
cdh1 = pd.read_json(cdh1_file)
clin_file = var_call_9w5yAQKc9uF3pKSPWKRbIabC
clin = pd.read_json(clin_file)
clin['ParticipantBarcode'] = clin['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
merged = clin.merge(cdh1[['ParticipantBarcode']].drop_duplicates(), on='ParticipantBarcode', how='left', indicator=True)
merged['CDH1_mutated'] = merged['_merge'].eq('both')
stats = merged.groupby('histological_type').agg(total=('ParticipantBarcode','nunique'), mutated=('CDH1_mutated','sum'))
stats = stats[stats['total']>0]
stats['percent_mutated'] = stats['mutated'] / stats['total'] * 100
stats = stats.sort_values('percent_mutated', ascending=False).head(3)
result = stats.reset_index().to_dict(orient='records')
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_KTH0WrCvkBRCClTw96td4gjV': 'file_storage/call_KTH0WrCvkBRCClTw96td4gjV.json', 'var_call_aWS6YxB35awxI10om6EqGR9S': ['clinical_info'], 'var_call_2uaVinCqplTHK1d70f5fUiCO': 'file_storage/call_2uaVinCqplTHK1d70f5fUiCO.json', 'var_call_GfjHSHrUiWPlYOspKv8VULaZ': [], 'var_call_9w5yAQKc9uF3pKSPWKRbIabC': 'file_storage/call_9w5yAQKc9uF3pKSPWKRbIabC.json'}

exec(code, env_args)
