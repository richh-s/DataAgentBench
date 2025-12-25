code = """import json

# Load valid symbols
with open(locals()['var_function-call-14196940699141511923'], 'r') as f:
    valid_symbols = json.load(f)

parts = []
for sym in valid_symbols:
    # Construct subquery using concatenation
    part = "SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    parts.append(part)

full_query = " UNION ALL ".join(parts)
final_query = "SELECT Symbol, Days FROM (" + full_query + ") ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-2569984885001255549': 'file_storage/function-call-2569984885001255549.json', 'var_function-call-2569984885001253606': 'file_storage/function-call-2569984885001253606.json', 'var_function-call-14196940699141511923': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-6163067840660889135': [{'Date': '2018-04-18', 'Open': '5.75', 'High': '7.5', 'Low': '5.010000228881836', 'Close': '6.300000190734863', 'Adj Close': '6.300000190734863', 'Volume': '291800'}]}

exec(code, env_args)
