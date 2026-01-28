code = """import json

# Load the list of available tables from stocktrade_database
trade_tables_result = locals()['var_functions.list_db:18']

if isinstance(trade_tables_result, str) and trade_tables_result.endswith('.json'):
    with open(trade_tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = trade_tables_result

# Load NASDAQ Capital Market stocks
stockinfo_result = locals()['var_functions.query_db:6']

if isinstance(stockinfo_result, str) and stockinfo_result.endswith('.json'):
    with open(stockinfo_result, 'r') as f:
        nasdaq_cap_data = json.load(f)
else:
    nasdaq_cap_data = stockinfo_result

# Get intersection of NASDAQ Capital stocks and available tables
nasdaq_symbols = [item['Symbol'] for item in nasdaq_cap_data]
available_nasdaq_stocks = set(nasdaq_symbols).intersection(set(all_tables))

print("__RESULT__:")
print(json.dumps({
    "nasdaq_cap_count": len(nasdaq_symbols),
    "available_in_trade_db": len(available_nasdaq_stocks),
    "first_10_available": list(available_nasdaq_stocks)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:4': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:12': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}], 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.execute_python:14': {'symbol_mapping': {'AGMH': 'AGM Group Holdings Inc.', 'ALACU': 'Alberton Acquisition Corporation', 'AMHC': 'Amplitude Healthcare Acquisition Corporation', 'ANDA': 'Andina Acquisition Corp. III', 'APEX': 'Apex Global Brands Inc.', 'BCLI': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine', 'BHAT': 'Blue Hat Interactive Entertainment Technology', 'BIOC': 'Biocept', 'BKYI': 'BIO-key International', 'BLFS': 'BioLife Solutions', 'BOSC': 'B.O.S. Better Online Solutions', 'BOTJ': 'Bank of the James Financial Group', 'BWEN': 'Broadwind Energy', 'CBAT': 'CBAK Energy Technology', 'CCCL': 'China Ceramics Co.', 'CDMOP': 'Avid Bioservices', 'CEMI': 'Chembio Diagnostics', 'CFBK': 'Central Federal Corporation', 'CFFA': 'CF Finance Acquisition Corp.', 'CLRB': 'Cellectar Biosciences', 'CORV': 'Correvio Pharma Corp.', 'CPAAU': 'Conyers Park II Acquisition Corp.', 'CPAH': 'CounterPath Corporation', 'CUBA': 'The Herzfeld Caribbean Basin Fund', 'CVV': 'CVD Equipment Corporation', 'DZSI': 'DASAN Zhone Solutions', 'ELSE': 'Electro-Sensors', 'EXPC': 'Experience Investment Corp.', 'EYEG': 'Eyegate Pharmaceuticals', 'FAMI': 'Farmmi', 'FNCB': 'FNCB Bancorp Inc.', 'FSBW': 'FS Bancorp', 'FTFT': 'Future FinTech Group Inc.', 'GDYN': 'Grid Dynamics Holdings', 'GLG': 'TD Holdings', 'GRNVU': 'GreenVision Acquisition Corp', 'GTEC': 'Greenland Technologies Holding Corporation', 'HCCOU': 'Healthcare Merger Corp.', 'HNNA': 'Hennessy Advisors', 'HQI': 'HireQuest', 'HRTX': 'Heron Therapeutics', 'IDEX': 'Ideanomics', 'IGIC': 'International General Insurance Holdings Ltd.', 'IOTS': 'Adesto Technologies Corporation', 'ISNS': 'Image Sensing Systems', 'ITI': 'Iteris', 'LACQ': 'Leisure Acquisition Corp.', 'MBCN': 'Middlefield Banc Corp.', 'MBNKP': 'Medallion Bank offers specialized financial services', 'MCEP': 'Mid-Con Energy Partners', 'MLND': 'Millendo Therapeutics', 'MMAC': 'MMA Capital Holdings', 'MNCLU': 'Monocle Acquisition Corporation', 'MNPR': 'Monopar Therapeutics Inc. is dedicated to developing innovative treatments for life-threatening diseases', 'NVEE': 'NV5 Global', 'NXTD': 'NXT-ID Inc.', 'OPOF': 'Old Point Financial Corporation', 'OPTT': 'Ocean Power Technologies', 'ORGO': 'Organogenesis Holdings Inc.', 'ORSNU': 'Orisun Acquisition Corp.', 'OTEL': 'Otelco Inc.', 'PBFS': 'Pioneer Bancorp', 'PBTS': 'Powerbridge Technologies Co.', 'PCSB': 'PCSB Financial Corporation', 'PECK': 'The Peck Company Holdings', 'PEIX': 'Pacific Ethanol', 'PFIE': 'Profire Energy', 'PLIN': 'China Xiangtai Food Co.', 'POPE': 'Pope Resources - Limited Partnership is dedicated to managing timberland and real estate', 'QRHC': 'Quest Resource Holding Corporation', 'SES': 'Synthesis Energy Systems', 'SHSP': 'SharpSpring', 'SNSS': 'Sunesis Pharmaceuticals', 'SSNT': 'SilverSun Technologies', 'STKS': 'The ONE Group Hospitality', 'TGLS': 'Tecnoglass Inc.', 'TMSR': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials', 'VERB': 'Verb Technology Company', 'VMD': 'Viemed Healthcare', 'VRRM': 'Verra Mobility Corporation', 'VTIQW': 'VectoIQ Acquisition Corp.', 'VVPR': 'VivoPower International PLC', 'WHLM': 'Wilhelmina International', 'WHLR': 'Wheeler Real Estate Investment Trust', 'XBIOW': 'Xenetic Biosciences', 'XPEL': 'XPEL'}, 'count': 86}, 'var_functions.execute_python:16': {'sample': {'AGMH': 'AGM Group Holdings Inc.', 'ALACU': 'Alberton Acquisition Corporation', 'AMHC': 'Amplitude Healthcare Acquisition Corporation', 'ANDA': 'Andina Acquisition Corp. III', 'APEX': 'Apex Global Brands Inc.'}, 'total': 86}, 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json'}

exec(code, env_args)
