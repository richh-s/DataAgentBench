code = """import json

# Load trading data
path_data = locals()['var_function-call-16426001998038706086']
with open(path_data, 'r') as f:
    trading_data = json.load(f)

# Load symbol info for names
path_info = locals()['var_function-call-12504970688043942614']
with open(path_info, 'r') as f:
    stock_info_list = json.load(f)

# Create mapping
symbol_to_name = {}
for item in stock_info_list:
    symbol_to_name[item['Symbol']] = item['Company Description']

# Count volatile days
counts = {}

for row in trading_data:
    sym = row['Symbol']
    try:
        high = float(row['High'])
        low = float(row['Low'])
    except (ValueError, TypeError):
        continue
        
    if low > 0:
        if (high - low) > 0.20 * low:
            counts[sym] = counts.get(sym, 0) + 1

# Sort and get top 5
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_counts[:5]

result_names = []
for sym, count in top_5:
    name = symbol_to_name.get(sym, sym)
    # The user asks for company names. The description usually starts with the name.
    # I will return the full description or extract the name if it looks like "Name is..."
    # But the instruction says "list the company names please".
    # Looking at the mapping: "AGM Group Holdings Inc. specializes..."
    # I'll try to extract the name, usually up to the first verb or just return the full description if unsure.
    # Actually, returning the full string from "Company Description" is probably safest as it contains the name.
    # But I can try to be cleaner.
    # Let's just return the description as is, or maybe just the first sentence?
    # Let's print the top 5 with their counts to debug, but for the final result, just the list.
    result_names.append(name)

print("__RESULT__:")
print(json.dumps(result_names))"""

env_args = {'var_function-call-7329624428160398946': ['stockinfo'], 'var_function-call-12504970688043942614': 'file_storage/function-call-12504970688043942614.json', 'var_function-call-8220860292931182157': 86, 'var_function-call-4470108010213238886': 'file_storage/function-call-4470108010213238886.json', 'var_function-call-9191686510936429403': 'file_storage/function-call-9191686510936429403.json', 'var_function-call-7472186252339293938': 'SELECT \'AGMH\' as Symbol, High, Low FROM "AGMH" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'ALACU\' as Symbol, High, Low FROM "ALACU" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'AMHC\' as Symbol, High, Low FROM "AMHC" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'ANDA\' as Symbol, High, Low FROM "ANDA" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'APEX\' as Symbol, High, Low FROM "APEX" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'BCLI\' as Symbol, High, Low FROM "BCLI" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'BHAT\' as Symbol, High, Low FROM "BHAT" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'BIOC\' as Symbol, High, Low FROM "BIOC" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'BKYI\' as Symbol, High, Low FROM "BKYI" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'BLFS\' as Symbol, High, Low FROM "BLFS" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'BOSC\' as Symbol, High, Low FROM "BOSC" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'BOTJ\' as Symbol, High, Low FROM "BOTJ" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'BWEN\' as Symbol, High, Low FROM "BWEN" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CBAT\' as Symbol, High, Low FROM "CBAT" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CCCL\' as Symbol, High, Low FROM "CCCL" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CDMOP\' as Symbol, High, Low FROM "CDMOP" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CEMI\' as Symbol, High, Low FROM "CEMI" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CFBK\' as Symbol, High, Low FROM "CFBK" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CFFA\' as Symbol, High, Low FROM "CFFA" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CLRB\' as Symbol, High, Low FROM "CLRB" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CORV\' as Symbol, High, Low FROM "CORV" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CPAAU\' as Symbol, High, Low FROM "CPAAU" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CPAH\' as Symbol, High, Low FROM "CPAH" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CUBA\' as Symbol, High, Low FROM "CUBA" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'CVV\' as Symbol, High, Low FROM "CVV" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'DZSI\' as Symbol, High, Low FROM "DZSI" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'ELSE\' as Symbol, High, Low FROM "ELSE" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'EXPC\' as Symbol, High, Low FROM "EXPC" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'EYEG\' as Symbol, High, Low FROM "EYEG" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'FAMI\' as Symbol, High, Low FROM "FAMI" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'FNCB\' as Symbol, High, Low FROM "FNCB" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'FSBW\' as Symbol, High, Low FROM "FSBW" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'FTFT\' as Symbol, High, Low FROM "FTFT" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'GDYN\' as Symbol, High, Low FROM "GDYN" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'GLG\' as Symbol, High, Low FROM "GLG" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'GRNVU\' as Symbol, High, Low FROM "GRNVU" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'GTEC\' as Symbol, High, Low FROM "GTEC" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'HCCOU\' as Symbol, High, Low FROM "HCCOU" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'HNNA\' as Symbol, High, Low FROM "HNNA" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'HQI\' as Symbol, High, Low FROM "HQI" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'HRTX\' as Symbol, High, Low FROM "HRTX" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'IDEX\' as Symbol, High, Low FROM "IDEX" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'IGIC\' as Symbol, High, Low FROM "IGIC" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'IOTS\' as Symbol, High, Low FROM "IOTS" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'ISNS\' as Symbol, High, Low FROM "ISNS" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'ITI\' as Symbol, High, Low FROM "ITI" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'LACQ\' as Symbol, High, Low FROM "LACQ" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'MBCN\' as Symbol, High, Low FROM "MBCN" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'MBNKP\' as Symbol, High, Low FROM "MBNKP" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'MCEP\' as Symbol, High, Low FROM "MCEP" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'MLND\' as Symbol, High, Low FROM "MLND" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'MMAC\' as Symbol, High, Low FROM "MMAC" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'MNCLU\' as Symbol, High, Low FROM "MNCLU" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'MNPR\' as Symbol, High, Low FROM "MNPR" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'NVEE\' as Symbol, High, Low FROM "NVEE" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'NXTD\' as Symbol, High, Low FROM "NXTD" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'OPOF\' as Symbol, High, Low FROM "OPOF" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'OPTT\' as Symbol, High, Low FROM "OPTT" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'ORGO\' as Symbol, High, Low FROM "ORGO" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'ORSNU\' as Symbol, High, Low FROM "ORSNU" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'OTEL\' as Symbol, High, Low FROM "OTEL" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'PBFS\' as Symbol, High, Low FROM "PBFS" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'PBTS\' as Symbol, High, Low FROM "PBTS" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'PCSB\' as Symbol, High, Low FROM "PCSB" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'PECK\' as Symbol, High, Low FROM "PECK" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'PEIX\' as Symbol, High, Low FROM "PEIX" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'PFIE\' as Symbol, High, Low FROM "PFIE" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'PLIN\' as Symbol, High, Low FROM "PLIN" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'POPE\' as Symbol, High, Low FROM "POPE" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'QRHC\' as Symbol, High, Low FROM "QRHC" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'SES\' as Symbol, High, Low FROM "SES" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'SHSP\' as Symbol, High, Low FROM "SHSP" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'SNSS\' as Symbol, High, Low FROM "SNSS" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'SSNT\' as Symbol, High, Low FROM "SSNT" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'STKS\' as Symbol, High, Low FROM "STKS" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'TGLS\' as Symbol, High, Low FROM "TGLS" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'TMSR\' as Symbol, High, Low FROM "TMSR" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'VERB\' as Symbol, High, Low FROM "VERB" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'VMD\' as Symbol, High, Low FROM "VMD" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'VRRM\' as Symbol, High, Low FROM "VRRM" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'VTIQW\' as Symbol, High, Low FROM "VTIQW" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'VVPR\' as Symbol, High, Low FROM "VVPR" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'WHLM\' as Symbol, High, Low FROM "WHLM" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'WHLR\' as Symbol, High, Low FROM "WHLR" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'XBIOW\' as Symbol, High, Low FROM "XBIOW" WHERE Date LIKE \'2019%\' UNION ALL SELECT \'XPEL\' as Symbol, High, Low FROM "XPEL" WHERE Date LIKE \'2019%\'', 'var_function-call-16426001998038706086': 'file_storage/function-call-16426001998038706086.json'}

exec(code, env_args)
