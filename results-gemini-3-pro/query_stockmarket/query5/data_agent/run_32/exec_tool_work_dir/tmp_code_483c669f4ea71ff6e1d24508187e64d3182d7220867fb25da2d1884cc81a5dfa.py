code = """import json

# Read the file from the previous step which contains the valid symbols
path = locals().get('var_function-call-16048660223325191044')
with open(path, 'r') as f:
    data = json.load(f)

valid_symbols = data['all_valid_symbols']

queries = []
for sym in valid_symbols:
    # Use double quotes for table names just in case
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM \"{sym}\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.20 * Low"
    queries.append(q)

final_query = " UNION ALL ".join(queries) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-17503537162949357124': 'file_storage/function-call-17503537162949357124.json', 'var_function-call-14793823752656914527': 'file_storage/function-call-14793823752656914527.json', 'var_function-call-16048660223325191044': {'total_nasdaq_cm': 86, 'valid_companies_count': 86, 'sample_valid': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}, {'Symbol': 'ANDA', 'Company Description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}], 'all_valid_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_function-call-14774891534332390183': [{'Date': '2018-04-18'}, {'Date': '2018-04-19'}, {'Date': '2018-04-20'}, {'Date': '2018-04-23'}, {'Date': '2018-04-24'}]}

exec(code, env_args)
