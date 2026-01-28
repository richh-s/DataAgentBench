code = """import json

# Load the NASDAQ Capital Market stocks
stockinfo_result = locals()['var_functions.query_db:6']

if isinstance(stockinfo_result, str) and stockinfo_result.endswith('.json'):
    with open(stockinfo_result, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = stockinfo_result

# Create dictionary mapping symbol to company name
symbol_to_company = {}
for item in stockinfo_data:
    symbol = item['Symbol']
    desc = item['Company Description']
    
    # Extract company name by splitting at common descriptors
    name = desc
    for separator in [' specializes', ' is a', ' operates', ' provides', ' focuses', ' offers', ' is dedicated', ' is focused', ' is', ',']:
        if separator in desc:
            name = desc.split(separator)[0]
            break
    
    # Clean up
    name = name.strip()
    if len(name) > 80:
        name = name[:80] + '...'
    
    symbol_to_company[symbol] = name

# Get sample result for testing
sample_dict = {k: symbol_to_company[k] for k in list(symbol_to_company.keys())[:5]}

print("__RESULT__:")
print(json.dumps({"sample": sample_dict, "total": len(symbol_to_company)}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:4': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:12': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}], 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.execute_python:14': {'symbol_mapping': {'AGMH': 'AGM Group Holdings Inc.', 'ALACU': 'Alberton Acquisition Corporation', 'AMHC': 'Amplitude Healthcare Acquisition Corporation', 'ANDA': 'Andina Acquisition Corp. III', 'APEX': 'Apex Global Brands Inc.', 'BCLI': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine', 'BHAT': 'Blue Hat Interactive Entertainment Technology', 'BIOC': 'Biocept', 'BKYI': 'BIO-key International', 'BLFS': 'BioLife Solutions', 'BOSC': 'B.O.S. Better Online Solutions', 'BOTJ': 'Bank of the James Financial Group', 'BWEN': 'Broadwind Energy', 'CBAT': 'CBAK Energy Technology', 'CCCL': 'China Ceramics Co.', 'CDMOP': 'Avid Bioservices', 'CEMI': 'Chembio Diagnostics', 'CFBK': 'Central Federal Corporation', 'CFFA': 'CF Finance Acquisition Corp.', 'CLRB': 'Cellectar Biosciences', 'CORV': 'Correvio Pharma Corp.', 'CPAAU': 'Conyers Park II Acquisition Corp.', 'CPAH': 'CounterPath Corporation', 'CUBA': 'The Herzfeld Caribbean Basin Fund', 'CVV': 'CVD Equipment Corporation', 'DZSI': 'DASAN Zhone Solutions', 'ELSE': 'Electro-Sensors', 'EXPC': 'Experience Investment Corp.', 'EYEG': 'Eyegate Pharmaceuticals', 'FAMI': 'Farmmi', 'FNCB': 'FNCB Bancorp Inc.', 'FSBW': 'FS Bancorp', 'FTFT': 'Future FinTech Group Inc.', 'GDYN': 'Grid Dynamics Holdings', 'GLG': 'TD Holdings', 'GRNVU': 'GreenVision Acquisition Corp', 'GTEC': 'Greenland Technologies Holding Corporation', 'HCCOU': 'Healthcare Merger Corp.', 'HNNA': 'Hennessy Advisors', 'HQI': 'HireQuest', 'HRTX': 'Heron Therapeutics', 'IDEX': 'Ideanomics', 'IGIC': 'International General Insurance Holdings Ltd.', 'IOTS': 'Adesto Technologies Corporation', 'ISNS': 'Image Sensing Systems', 'ITI': 'Iteris', 'LACQ': 'Leisure Acquisition Corp.', 'MBCN': 'Middlefield Banc Corp.', 'MBNKP': 'Medallion Bank offers specialized financial services', 'MCEP': 'Mid-Con Energy Partners', 'MLND': 'Millendo Therapeutics', 'MMAC': 'MMA Capital Holdings', 'MNCLU': 'Monocle Acquisition Corporation', 'MNPR': 'Monopar Therapeutics Inc. is dedicated to developing innovative treatments for life-threatening diseases', 'NVEE': 'NV5 Global', 'NXTD': 'NXT-ID Inc.', 'OPOF': 'Old Point Financial Corporation', 'OPTT': 'Ocean Power Technologies', 'ORGO': 'Organogenesis Holdings Inc.', 'ORSNU': 'Orisun Acquisition Corp.', 'OTEL': 'Otelco Inc.', 'PBFS': 'Pioneer Bancorp', 'PBTS': 'Powerbridge Technologies Co.', 'PCSB': 'PCSB Financial Corporation', 'PECK': 'The Peck Company Holdings', 'PEIX': 'Pacific Ethanol', 'PFIE': 'Profire Energy', 'PLIN': 'China Xiangtai Food Co.', 'POPE': 'Pope Resources - Limited Partnership is dedicated to managing timberland and real estate', 'QRHC': 'Quest Resource Holding Corporation', 'SES': 'Synthesis Energy Systems', 'SHSP': 'SharpSpring', 'SNSS': 'Sunesis Pharmaceuticals', 'SSNT': 'SilverSun Technologies', 'STKS': 'The ONE Group Hospitality', 'TGLS': 'Tecnoglass Inc.', 'TMSR': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials', 'VERB': 'Verb Technology Company', 'VMD': 'Viemed Healthcare', 'VRRM': 'Verra Mobility Corporation', 'VTIQW': 'VectoIQ Acquisition Corp.', 'VVPR': 'VivoPower International PLC', 'WHLM': 'Wilhelmina International', 'WHLR': 'Wheeler Real Estate Investment Trust', 'XBIOW': 'Xenetic Biosciences', 'XPEL': 'XPEL'}, 'count': 86}}

exec(code, env_args)
