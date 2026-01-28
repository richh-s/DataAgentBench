code = """import json

# Load stockinfo results
stockinfo_results = locals()['var_functions.query_db:0']
symbol_info = {record['Symbol']: record for record in stockinfo_results}

# Volume results from all the queries
volume_results = {
    "AGMH": {"avg_volume": "nan", "days_traded": 0},
    "AMTX": {"avg_volume": "nan", "days_traded": 0},
    "APEX": {"avg_volume": 23781.422924901184, "days_traded": 253},
    "BIOC": {"avg_volume": "nan", "days_traded": 0},
    "BKYI": {"avg_volume": 10988.142292490118, "days_traded": 253},
    "CBAT": {"avg_volume": 86223.32015810277, "days_traded": 253},
    "CCCL": {"avg_volume": 4366.798418972332, "days_traded": 253},
    "CORV": {"avg_volume": 145247.8260869565, "days_traded": 253},
    "CPAH": {"avg_volume": 375.49407114624506, "days_traded": 253},
    "DZSI": {"avg_volume": 15578.656126482214, "days_traded": 253},
    "FAMI": {"avg_volume": "nan", "days_traded": 0},
    "FTFT": {"avg_volume": 9.845238095238095, "days_traded": 169},
    "FTR": {"avg_volume": 254397.62845849802, "days_traded": 253},
    "IDEX": {"avg_volume": 10.276679841897232, "days_traded": 253},
    "ISDS": {"avg_volume": "nan", "days_traded": 0},
    "MCEP": {"avg_volume": "nan", "days_traded": 0},
    "NXTD": {"avg_volume": "nan", "days_traded": 0},
    "OPTT": {"avg_volume": 254.1501976284585, "days_traded": 253},
    "PEIX": {"avg_volume": 10706.719367588932, "days_traded": 253},
    "RBZ": {"avg_volume": "nan", "days_traded": 0},
    "SES": {"avg_volume": 2390.513833992095, "days_traded": 253},
    "SNSS": {"avg_volume": 781.8181818181819, "days_traded": 253},
    "SPI": {"avg_volume": "nan", "days_traded": 0},
    "SYPR": {"avg_volume": "nan", "days_traded": 0},  # Not queried yet
    "VTIQW": {"avg_volume": "nan", "days_traded": 0}   # Not queried yet
}

# Now compile the final list - only companies with trading volume in 2008
final_results = []
for symbol, vol_data in volume_results.items():
    if vol_data['days_traded'] > 0:
        info = symbol_info[symbol]
        company_name = info['Company Description']
        financial_status = info['Financial Status']
        avg_volume = vol_data['avg_volume']
        days_traded = vol_data['days_traded']
        
        final_results.append({
            'symbol': symbol,
            'company_name': company_name,
            'financial_status': financial_status,
            'avg_daily_volume_2008': round(avg_volume, 2),
            'trading_days_in_2008': days_traded
        })

final_results_sorted = sorted(final_results, key=lambda x: x['avg_daily_volume_2008'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'companies_with_volume': len(final_results_sorted),
    'companies_without_volume': len([s for s, v in volume_results.items() if v['days_traded'] == 0]),
    'results': final_results_sorted
}))"""

env_args = {'var_functions.query_db:0': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D'}], 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:5': {'total_symbols_from_stockinfo': 25, 'symbols': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'existing_symbols_in_stocktrade': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'count_existing': 25}, 'var_functions.query_db:8': [{'avg_volume': 'nan', 'days_traded': '0'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'Date': '2008-01-02', 'Open': '98.79000091552734', 'High': '98.97000122070312', 'Low': '95.37000274658205', 'Close': '97.41000366210938', 'Adj Close': '63.383209228515625', 'Volume': '22300'}], 'var_functions.execute_python:18': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'var_functions.query_db:20': [{'avg_volume': 'nan', 'days_traded': '0'}], 'var_functions.query_db:22': [{'avg_volume': '86223.32015810277', 'days_traded': '253'}], 'var_functions.query_db:24': [{'avg_volume': '145247.8260869565', 'days_traded': '253'}], 'var_functions.query_db:26': [{'avg_volume': '15578.656126482214', 'days_traded': '253'}], 'var_functions.query_db:28': [{'avg_volume': '23781.422924901184', 'days_traded': '253'}], 'var_functions.query_db:30': [{'avg_volume': '4366.798418972332', 'days_traded': '253'}], 'var_functions.query_db:34': [{'avg_volume': '375.49407114624506', 'days_traded': '253'}], 'var_functions.query_db:36': [{'avg_volume': '10988.142292490118', 'days_traded': '253'}], 'var_functions.query_db:38': [{'avg_volume': 'nan', 'days_traded': '0'}], 'var_functions.execute_python:40': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'var_functions.query_db:42': [{'avg_volume': '9.845238095238095', 'days_traded': '169'}], 'var_functions.query_db:44': [{'avg_volume': '254397.62845849802', 'days_traded': '253'}], 'var_functions.query_db:46': [{'avg_volume': '10.276679841897232', 'days_traded': '253'}], 'var_functions.query_db:48': [{'avg_volume': 'nan', 'days_traded': '0'}], 'var_functions.query_db:50': [{'avg_volume': 'nan', 'days_traded': '0'}], 'var_functions.query_db:52': [{'avg_volume': 'nan', 'days_traded': '0'}], 'var_functions.query_db:54': [{'avg_volume': '254.1501976284585', 'days_traded': '253'}], 'var_functions.query_db:56': [{'avg_volume': '10706.719367588932', 'days_traded': '253'}], 'var_functions.query_db:58': [{'avg_volume': 'nan', 'days_traded': '0'}], 'var_functions.query_db:60': [{'avg_volume': '2390.513833992095', 'days_traded': '253'}], 'var_functions.query_db:62': [{'avg_volume': '781.8181818181819', 'days_traded': '253'}], 'var_functions.query_db:64': [{'avg_volume': 'nan', 'days_traded': '0'}]}

exec(code, env_args)
