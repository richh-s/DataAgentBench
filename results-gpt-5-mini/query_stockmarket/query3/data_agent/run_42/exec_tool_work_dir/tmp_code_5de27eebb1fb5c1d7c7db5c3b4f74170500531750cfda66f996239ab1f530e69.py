code = """import json
# load stockinfo results
stockinfo = var_call_KjMggfqrWUmE6HYP3clfSZJq
# mapping symbol to company description
symbol_to_company = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}
# mapping of symbols to their query result variables
symbol_vars = {
    'AGMH': var_call_fZWpCxQguTWwwP1jB4zvynME,
    'AMTX': var_call_0A3GvYRpu71pcu7EP6iL0jND,
    'APEX': var_call_qyMoi3aKA1wEveYRS9fhxcVH,
    'BIOC': var_call_DDuH9fSZdSEf65QscOUcol2K,
    'BKYI': var_call_hiuKURnIMs8UHLy6MrxJaEln,
    'CBAT': var_call_yYjGSVWnfJ5asE8zv47ZZ4p7,
    'CCCL': var_call_TR0JsFnJJQnjjtviB2Yc7AZA,
    'CORV': var_call_LRii1baBXI4cpqxibfPNcEyR,
    'CPAH': var_call_vaFIAfnd2iS5WMv8Em0bIHpW,
    'DZSI': var_call_2mjYaECCdVmGUDq9YdDLZoKr,
    'FAMI': var_call_tfkRncR62LyGQZL7aGhwAYKH,
    'FTFT': var_call_mWVH5GAgFb6nqd4faIWV3OM4,
    'FTR': var_call_tMkGn4pB6l0ZnTzADAElRSRx,
    'IDEX': var_call_ORjY9HoJoPBGQjLmdauH8fBv,
    'ISDS': var_call_F1PvquOI7jlbbpbiaMTawrmS,
    'MCEP': var_call_BrsqlbeQEHxmOthTzwyi8fEV,
    'NXTD': var_call_wIVQAN3a3c0ymTV7IkcbZh6L,
    'OPTT': var_call_8dgOdso56Q2R8gzZzxHjDErZ,
    'PEIX': var_call_e0fMYrIM1kAAiR3pd7HLpiSQ,
    'RBZ': var_call_gaGOW6ajrehzPa4VFZZLqCyM,
    'SES': var_call_Hbu54zuhQDpWyiVrZbsbjqvI,
    'SNSS': var_call_Bl5QyKC07YdwwEaQ4qDgH3QJ,
    'SPI': var_call_rc1od4Ju71IewXQoXZvvao0a,
    'SYPR': var_call_u4Je9X9UD5gatDIdmyVM3RxE,
    'VTIQW': var_call_OKei5BtVvShlEZqdLQcDfywH
}

results = []
for symbol, var in symbol_vars.items():
    # each var is a list with one dict {'avg_volume': '...'}
    try:
        avg_str = var[0].get('avg_volume')
    except Exception:
        continue
    if avg_str is None:
        continue
    # some results use string "nan"
    if isinstance(avg_str, str) and avg_str.lower() == 'nan':
        continue
    # convert to float
    try:
        avg_val = float(avg_str)
    except Exception:
        continue
    # only include if there was trading volume (avg > 0)
    if avg_val <= 0:
        continue
    company = symbol_to_company.get(symbol, None)
    results.append({'Symbol': symbol, 'Company Description': company, 'avg_daily_volume_2008': avg_val})

# sort results by Symbol for deterministic output
results = sorted(results, key=lambda x: x['Symbol'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_KjMggfqrWUmE6HYP3clfSZJq': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_QVj4xBgEZPHdAjwnMvcLqLOx': 'file_storage/call_QVj4xBgEZPHdAjwnMvcLqLOx.json', 'var_call_fZWpCxQguTWwwP1jB4zvynME': [{'avg_volume': 'nan'}], 'var_call_0A3GvYRpu71pcu7EP6iL0jND': [{'avg_volume': 'nan'}], 'var_call_qyMoi3aKA1wEveYRS9fhxcVH': [{'avg_volume': '23781.422924901184'}], 'var_call_DDuH9fSZdSEf65QscOUcol2K': [{'avg_volume': 'nan'}], 'var_call_hiuKURnIMs8UHLy6MrxJaEln': [{'avg_volume': '10988.142292490118'}], 'var_call_yYjGSVWnfJ5asE8zv47ZZ4p7': [{'avg_volume': '86223.32015810277'}], 'var_call_TR0JsFnJJQnjjtviB2Yc7AZA': [{'avg_volume': '4366.798418972332'}], 'var_call_LRii1baBXI4cpqxibfPNcEyR': [{'avg_volume': '145247.8260869565'}], 'var_call_vaFIAfnd2iS5WMv8Em0bIHpW': [{'avg_volume': '375.49407114624506'}], 'var_call_2mjYaECCdVmGUDq9YdDLZoKr': [{'avg_volume': '15578.656126482214'}], 'var_call_tfkRncR62LyGQZL7aGhwAYKH': [{'avg_volume': 'nan'}], 'var_call_mWVH5GAgFb6nqd4faIWV3OM4': [{'avg_volume': '9.845238095238095'}], 'var_call_tMkGn4pB6l0ZnTzADAElRSRx': [{'avg_volume': '254397.62845849802'}], 'var_call_ORjY9HoJoPBGQjLmdauH8fBv': [{'avg_volume': '10.276679841897232'}], 'var_call_F1PvquOI7jlbbpbiaMTawrmS': [{'avg_volume': 'nan'}], 'var_call_BrsqlbeQEHxmOthTzwyi8fEV': [{'avg_volume': 'nan'}], 'var_call_wIVQAN3a3c0ymTV7IkcbZh6L': [{'avg_volume': 'nan'}], 'var_call_8dgOdso56Q2R8gzZzxHjDErZ': [{'avg_volume': '254.1501976284585'}], 'var_call_e0fMYrIM1kAAiR3pd7HLpiSQ': [{'avg_volume': '10706.719367588932'}], 'var_call_gaGOW6ajrehzPa4VFZZLqCyM': [{'avg_volume': 'nan'}], 'var_call_Hbu54zuhQDpWyiVrZbsbjqvI': [{'avg_volume': '2390.513833992095'}], 'var_call_Bl5QyKC07YdwwEaQ4qDgH3QJ': [{'avg_volume': '781.8181818181819'}], 'var_call_rc1od4Ju71IewXQoXZvvao0a': [{'avg_volume': 'nan'}], 'var_call_u4Je9X9UD5gatDIdmyVM3RxE': [{'avg_volume': '36836.36363636364'}], 'var_call_OKei5BtVvShlEZqdLQcDfywH': [{'avg_volume': 'nan'}]}

exec(code, env_args)
