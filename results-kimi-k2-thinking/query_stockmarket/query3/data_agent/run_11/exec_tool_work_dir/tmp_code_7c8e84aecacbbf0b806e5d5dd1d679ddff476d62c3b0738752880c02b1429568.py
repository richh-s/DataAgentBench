code = """import json

# Get stockinfo data
stockinfo_data = locals()['var_functions.query_db:0']

# Build a symbol to company info mapping
company_map = {}
for item in stockinfo_data:
    company_map[item['Symbol']] = {
        'company_name': item['Company Description'],
        'financial_status': item['Financial Status']
    }

# List of all query results (we need to collect them all)
# Let me gather all the query results systematically

# The pattern for query results:
# FTR: var_functions.query_db:22
# APEX: var_functions.query_db:30
# BKYI: var_functions.query_db:42
# CBAT: var_functions.query_db:44
# CCCL: var_functions.query_db:46
# CORV: var_functions.query_db:48
# CPAH: var_functions.query_db:50
# DZSI: var_functions.query_db:52
# IDEX: var_functions.query_db:56
# OPTT: var_functions.query_db:62
# FTFT: var_functions.query_db:68
# SNSS: var_functions.query_db:70

results = {}

# Process FTR
ftr_data = locals()['var_functions.query_db:22'][0]
results['FTR'] = {
    'avg_volume': float(ftr_data['avg_volume']) if ftr_data['avg_volume'] != 'nan' else None,
    'trading_days': int(ftr_data['trading_days'])
}

# Process APEX
apex_data = locals()['var_functions.query_db:30'][0]
results['APEX'] = {
    'avg_volume': float(apex_data['avg_volume']) if apex_data['avg_volume'] != 'nan' else None,
    'trading_days': int(apex_data['trading_days'])
}

# Process BKYI
bkyi_data = locals()['var_functions.query_db:42'][0]
results['BKYI'] = {
    'avg_volume': float(bkyi_data['avg_volume']) if bkyi_data['avg_volume'] != 'nan' else None,
    'trading_days': int(bkyi_data['trading_days'])
}

# Process CBAT
cbat_data = locals()['var_functions.query_db:44'][0]
results['CBAT'] = {
    'avg_volume': float(cbat_data['avg_volume']) if cbat_data['avg_volume'] != 'nan' else None,
    'trading_days': int(cbat_data['trading_days'])
}

# Process CCCL
cccl_data = locals()['var_functions.query_db:46'][0]
results['CCCL'] = {
    'avg_volume': float(cccl_data['avg_volume']) if cccl_data['avg_volume'] != 'nan' else None,
    'trading_days': int(cccl_data['trading_days'])
}

# Process CORV
corv_data = locals()['var_functions.query_db:48'][0]
results['CORV'] = {
    'avg_volume': float(corv_data['avg_volume']) if corv_data['avg_volume'] != 'nan' else None,
    'trading_days': int(corv_data['trading_days'])
}

# Process CPAH
cpah_data = locals()['var_functions.query_db:50'][0]
results['CPAH'] = {
    'avg_volume': float(cpah_data['avg_volume']) if cpah_data['avg_volume'] != 'nan' else None,
    'trading_days': int(cpah_data['trading_days'])
}

# Process DZSI
dzsi_data = locals()['var_functions.query_db:52'][0]
results['DZSI'] = {
    'avg_volume': float(dzsi_data['avg_volume']) if dzsi_data['avg_volume'] != 'nan' else None,
    'trading_days': int(dzsi_data['trading_days'])
}

# Process IDEX
idex_data = locals()['var_functions.query_db:56'][0]
results['IDEX'] = {
    'avg_volume': float(idex_data['avg_volume']) if idex_data['avg_volume'] != 'nan' else None,
    'trading_days': int(idex_data['trading_days'])
}

# Process OPTT
optt_data = locals()['var_functions.query_db:62'][0]
results['OPTT'] = {
    'avg_volume': float(optt_data['avg_volume']) if optt_data['avg_volume'] != 'nan' else None,
    'trading_days': int(optt_data['trading_days'])
}

# Process FTFT
ftft_data = locals()['var_functions.query_db:68'][0]
results['FTFT'] = {
    'avg_volume': float(ftft_data['avg_volume']) if ftft_data['avg_volume'] != 'nan' else None,
    'trading_days': int(ftft_data['trading_days'])
}

# Process SNSS
snss_data = locals()['var_functions.query_db:70'][0]
results['SNSS'] = {
    'avg_volume': float(snss_data['avg_volume']) if snss_data['avg_volume'] != 'nan' else None,
    'trading_days': int(snss_data['trading_days'])
}

# Now compile final results - only those with non-null avg_volume
final_results = []

for symbol, data in results.items():
    if data['avg_volume'] is not None and data['avg_volume'] > 0:
        final_results.append({
            'symbol': symbol,
            'company_name': company_map[symbol]['company_name'],
            'avg_volume_2008': round(data['avg_volume'], 2),
            'trading_days': data['trading_days']
        })

# Sort by avg_volume descending
final_results.sort(key=lambda x: x['avg_volume_2008'], reverse=True)

print('Final results count:', len(final_results))
print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Listing Exchange': 'Q', 'Market Category': 'S'}], 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'var_functions.execute_python:8': {'symbols': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'company_dict': {'AGMH': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'AMTX': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'APEX': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'BIOC': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'BKYI': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'CBAT': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'CCCL': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'CORV': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'CPAH': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'DZSI': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'FAMI': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'FTFT': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'FTR': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'IDEX': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'ISDS': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'MCEP': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'NXTD': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'OPTT': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'PEIX': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'RBZ': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'SES': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'SNSS': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'SPI': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'SYPR': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'VTIQW': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.'}}, 'var_functions.execute_python:10': {'AGMH': {'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'symbol': 'AGMH'}, 'AMTX': {'company_name': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'symbol': 'AMTX'}, 'APEX': {'company_name': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'symbol': 'APEX'}, 'BIOC': {'company_name': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'symbol': 'BIOC'}, 'BKYI': {'company_name': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'symbol': 'BKYI'}, 'CBAT': {'company_name': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'symbol': 'CBAT'}, 'CCCL': {'company_name': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'symbol': 'CCCL'}, 'CORV': {'company_name': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'symbol': 'CORV'}, 'CPAH': {'company_name': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'symbol': 'CPAH'}, 'DZSI': {'company_name': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'symbol': 'DZSI'}, 'FAMI': {'company_name': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'symbol': 'FAMI'}, 'FTFT': {'company_name': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'symbol': 'FTFT'}, 'FTR': {'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'symbol': 'FTR'}, 'IDEX': {'company_name': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'symbol': 'IDEX'}, 'ISDS': {'company_name': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'symbol': 'ISDS'}, 'MCEP': {'company_name': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'symbol': 'MCEP'}, 'NXTD': {'company_name': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'symbol': 'NXTD'}, 'OPTT': {'company_name': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'symbol': 'OPTT'}, 'PEIX': {'company_name': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'symbol': 'PEIX'}, 'RBZ': {'company_name': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'symbol': 'RBZ'}, 'SES': {'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'symbol': 'SES'}, 'SNSS': {'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'symbol': 'SNSS'}, 'SPI': {'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'symbol': 'SPI'}, 'SYPR': {'company_name': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'symbol': 'SYPR'}, 'VTIQW': {'company_name': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'symbol': 'VTIQW'}}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'Date': '2008-01-02', 'Volume': '168100.0'}, {'Date': '2008-01-03', 'Volume': '190200.0'}, {'Date': '2008-01-04', 'Volume': '201400.0'}, {'Date': '2008-01-07', 'Volume': '256300.0'}, {'Date': '2008-01-08', 'Volume': '406600.0'}], 'var_functions.query_db:16': [], 'var_functions.execute_python:18': {'tables_exist': [True, True, True, True, True]}, 'var_functions.query_db:20': [{'Date': '2008-01-02', 'Volume': '0'}, {'Date': '2008-01-03', 'Volume': '0'}, {'Date': '2008-01-04', 'Volume': '0'}, {'Date': '2008-01-07', 'Volume': '0'}, {'Date': '2008-01-08', 'Volume': '0'}], 'var_functions.query_db:22': [{'count': '253', 'avg_volume': '254397.62845849802'}], 'var_functions.execute_python:24': {'symbols': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'count': 25}, 'var_functions.execute_python:26': {'query_symbols': "'AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'", 'count': 25}, 'var_functions.query_db:30': [{'avg_volume': '23781.422924901184', 'trading_days': '253'}], 'var_functions.query_db:32': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.execute_python:33': {'count': 25, 'symbols': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW']}, 'var_functions.query_db:36': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.query_db:38': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.query_db:40': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.query_db:42': [{'avg_volume': '11209.677419354839', 'trading_days': '248'}], 'var_functions.query_db:44': [{'avg_volume': '86223.32015810277', 'trading_days': '253'}], 'var_functions.query_db:46': [{'avg_volume': '11159.59595959596', 'trading_days': '99'}], 'var_functions.query_db:48': [{'avg_volume': '145247.8260869565', 'trading_days': '253'}], 'var_functions.query_db:50': [{'avg_volume': '625.0', 'trading_days': '152'}], 'var_functions.query_db:52': [{'avg_volume': '15578.656126482214', 'trading_days': '253'}], 'var_functions.query_db:54': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.query_db:56': [{'avg_volume': '216.66666666666666', 'trading_days': '12'}], 'var_functions.query_db:58': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.query_db:60': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.query_db:62': [{'avg_volume': '299.06976744186045', 'trading_days': '215'}], 'var_functions.query_db:64': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.query_db:66': [{'avg_volume': 'nan', 'trading_days': '0'}], 'var_functions.query_db:68': [{'avg_volume': '66.16', 'trading_days': '25'}], 'var_functions.query_db:70': [{'avg_volume': '933.0188679245283', 'trading_days': '212'}]}

exec(code, env_args)
