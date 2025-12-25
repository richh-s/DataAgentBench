code = """import json

# Load the state from the previous execute_python call (after processing AGMH)
with open(locals()['var_function-call-4021816663017577478'], 'r') as f:
    state = json.load(f)

company_symbols = state['company_symbols']
current_symbol_index = state['current_symbol_index']

if current_symbol_index < len(company_symbols):
    current_symbol = company_symbols[current_symbol_index]
    result = {"current_symbol": current_symbol, "current_symbol_index": current_symbol_index}
else:
    # All symbols processed, prepare final answer
    sorted_companies = sorted(state['volatility_counts'].items(), key=lambda item: item[1], reverse=True)
    top_5_companies = sorted_companies[:5]
    
    final_answer_lines = ["The 5 companies listed on the NASDAQ Capital Market with the highest number of days in 2019 where the intraday price range exceeded 20% of the low price are:"]
    for symbol, count in top_5_companies:
        company_name = state['company_info'].get(symbol, symbol)
        final_answer_lines.append(f"- {company_name} ({count} days)")
    
    result = {"status": "all_symbols_processed", "answer": "\n".join(final_answer_lines)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17697039676223139705': 'file_storage/function-call-17697039676223139705.json', 'var_function-call-7956518453806938118': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-4541980299049963873': 'file_storage/function-call-4541980299049963873.json', 'var_function-call-15727735854005665678': {'num_companies': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-3283387045808530877': {'current_symbol': 'AGMH', 'current_symbol_index': 0}, 'var_function-call-8146823205966599953': 'file_storage/function-call-8146823205966599953.json', 'var_function-call-788278587502682892': 'file_storage/function-call-788278587502682892.json', 'var_function-call-779338217959558487': {'num_companies': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-8334651670665658110': {'num_companies': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-16650692447863298889': 'file_storage/function-call-16650692447863298889.json', 'var_function-call-17217199204999239618': {'num_companies': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-18402343745024006056': 'file_storage/function-call-18402343745024006056.json', 'var_function-call-7289321450900091136': 'file_storage/function-call-7289321450900091136.json', 'var_function-call-59093121807540674': {'current_symbol': 'AGMH', 'current_symbol_index': 0}, 'var_function-call-2682483529085289976': 'file_storage/function-call-2682483529085289976.json', 'var_function-call-9869199768486787863': 'file_storage/function-call-9869199768486787863.json', 'var_function-call-7629036268135267362': {'current_symbol': 'ALACU', 'current_symbol_index': 1}, 'var_function-call-13911929991100615342': 'file_storage/function-call-13911929991100615342.json', 'var_function-call-10136401767547026427': 'file_storage/function-call-10136401767547026427.json', 'var_function-call-498208698970566735': 'file_storage/function-call-498208698970566735.json', 'var_function-call-11755190746480251269': 'file_storage/function-call-11755190746480251269.json', 'var_function-call-2723367954241804855': {'current_symbol': 'AGMH', 'current_symbol_index': 0}, 'var_function-call-16094845983882697556': 'file_storage/function-call-16094845983882697556.json', 'var_function-call-9562606935784239267': {'current_symbol': 'AGMH', 'current_symbol_index': 0}, 'var_function-call-6200540545529387738': 'file_storage/function-call-6200540545529387738.json', 'var_function-call-11707789698378722514': 'file_storage/function-call-11707789698378722514.json', 'var_function-call-14226077288603291857': {'current_symbol': 'ALACU', 'current_symbol_index': 1}, 'var_function-call-18099531297825121337': 'file_storage/function-call-18099531297825121337.json', 'var_function-call-5543433303352979326': 'file_storage/function-call-5543433303352979326.json', 'var_function-call-2847292459501809027': 'file_storage/function-call-2847292459501809027.json', 'var_function-call-3845224712035393308': 'file_storage/function-call-3845224712035393308.json', 'var_function-call-10510401776337203250': {'current_symbol': 'AGMH', 'current_symbol_index': 0}, 'var_function-call-1946539673515245398': 'file_storage/function-call-1946539673515245398.json', 'var_function-call-4021816663017577478': 'file_storage/function-call-4021816663017577478.json', 'var_function-call-6245642348061177362': {'current_symbol': 'ALACU', 'current_symbol_index': 1}, 'var_function-call-17241613189943637450': 'file_storage/function-call-17241613189943637450.json', 'var_function-call-18381665606881781523': 'file_storage/function-call-18381665606881781523.json', 'var_function-call-15665721516337034997': 'file_storage/function-call-15665721516337034997.json'}

exec(code, env_args)
