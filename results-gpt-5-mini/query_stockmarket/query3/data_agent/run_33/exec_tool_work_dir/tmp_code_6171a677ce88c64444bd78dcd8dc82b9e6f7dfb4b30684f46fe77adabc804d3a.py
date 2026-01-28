code = """import json
# Load company metadata
companies = var_call_GPyo0kiBervuwbIw399oJGwf
# Keys for the corresponding trade queries in the same order as companies filtered earlier
trade_keys = [
    'var_call_zEEz1g6d5cRDRseof70JuqKN',
    'var_call_OAhIsRi25hczTAKJRDEPZyeq',
    'var_call_BOFzNZ1epE9U9KjK7GXowdKw',
    'var_call_JrJ6mIPCfOooq1h3Uih4tPb6',
    'var_call_Yqu615br69e3RnZSoNwMuyMw',
    'var_call_ecPczrw4EIhGTg3kvZW8vVBM',
    'var_call_PEwQj7KRR8Fga9NJFBKAxPob',
    'var_call_eTQO6VavpmtZxhldEUlqQaxA',
    'var_call_ErXLOrj17kq26PV5jHEqYl73',
    'var_call_Lj3eJTnJ0rYMiBqtvS2T1dLH',
    'var_call_vtJrxnOFYZ2k2Gfbk8XsXh4q',
    'var_call_nmbvtak749WalfYnzS4LDUal',
    'var_call_k9gKl8QWqTpjv9QPnzZTVgPN',
    'var_call_Ejhv6eRBsK3vwIZPZdX5eubi',
    'var_call_zB2JqlXehxlnJLhAwcHS1svF',
    'var_call_aDYbDyISOD5j7U4xxl46ZyJi',
    'var_call_UYyI2XyIiCNWKWQ340exZBMn',
    'var_call_HosyS3nk8clJWK6QFDaVnuGR',
    'var_call_zkDkqcrGVkC51uhA3uR75gCM',
    'var_call_165g3JWmrFULaUeL21e7Gv0H',
    'var_call_pIJXpIvxsADx3BGOooo0Iovk',
    'var_call_0CAun2lCOgJVreksQCRNvcfp',
    'var_call_LHpqtcrkGkxso3U0GP2n5JeV',
    'var_call_bSs3QnWnxo5dAnXd7D2tKHq7',
    'var_call_jbyJiOOtpE80xP4X6u0nZg5i'
]

results = []
# Iterate through companies and corresponding trade query results
for comp, key in zip(companies, trade_keys):
    sym = comp.get('Symbol')
    desc = comp.get('Company Description')
    # get trade result variable by name
    trade_res = globals().get(key)
    if not trade_res:
        continue
    # trade_res is a list with one dict
    rec = trade_res[0]
    avg_vol = rec.get('avg_vol')
    cnt = rec.get('cnt')
    # convert cnt to int if possible
    try:
        cnt_i = int(cnt)
    except Exception:
        cnt_i = 0
    # consider having trading volume in 2008 if cnt_i > 0 and avg_vol is not nan
    if cnt_i > 0 and avg_vol not in (None, 'nan'):
        try:
            avg_f = float(avg_vol)
        except Exception:
            continue
        results.append({
            'Symbol': sym,
            'Company Description': desc,
            'Average Daily Volume 2008': avg_f
        })

# Print result as JSON-serializable string
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_GPyo0kiBervuwbIw399oJGwf': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_zEEz1g6d5cRDRseof70JuqKN': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_OAhIsRi25hczTAKJRDEPZyeq': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_BOFzNZ1epE9U9KjK7GXowdKw': [{'avg_vol': '23781.422924901184', 'cnt': '253'}], 'var_call_JrJ6mIPCfOooq1h3Uih4tPb6': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_Yqu615br69e3RnZSoNwMuyMw': [{'avg_vol': '10988.142292490118', 'cnt': '253'}], 'var_call_ecPczrw4EIhGTg3kvZW8vVBM': [{'avg_vol': '86223.32015810277', 'cnt': '253'}], 'var_call_PEwQj7KRR8Fga9NJFBKAxPob': [{'avg_vol': '4366.798418972332', 'cnt': '253'}], 'var_call_eTQO6VavpmtZxhldEUlqQaxA': [{'avg_vol': '145247.8260869565', 'cnt': '253'}], 'var_call_ErXLOrj17kq26PV5jHEqYl73': [{'avg_vol': '375.49407114624506', 'cnt': '253'}], 'var_call_Lj3eJTnJ0rYMiBqtvS2T1dLH': [{'avg_vol': '15578.656126482214', 'cnt': '253'}], 'var_call_vtJrxnOFYZ2k2Gfbk8XsXh4q': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_nmbvtak749WalfYnzS4LDUal': [{'avg_vol': '9.845238095238095', 'cnt': '168'}], 'var_call_k9gKl8QWqTpjv9QPnzZTVgPN': [{'avg_vol': '254397.62845849802', 'cnt': '253'}], 'var_call_Ejhv6eRBsK3vwIZPZdX5eubi': [{'avg_vol': '10.276679841897232', 'cnt': '253'}], 'var_call_zB2JqlXehxlnJLhAwcHS1svF': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_aDYbDyISOD5j7U4xxl46ZyJi': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_UYyI2XyIiCNWKWQ340exZBMn': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_HosyS3nk8clJWK6QFDaVnuGR': [{'avg_vol': '254.1501976284585', 'cnt': '253'}], 'var_call_zkDkqcrGVkC51uhA3uR75gCM': [{'avg_vol': '10706.719367588932', 'cnt': '253'}], 'var_call_165g3JWmrFULaUeL21e7Gv0H': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_pIJXpIvxsADx3BGOooo0Iovk': [{'avg_vol': '2390.513833992095', 'cnt': '253'}], 'var_call_0CAun2lCOgJVreksQCRNvcfp': [{'avg_vol': '781.8181818181819', 'cnt': '253'}], 'var_call_LHpqtcrkGkxso3U0GP2n5JeV': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_bSs3QnWnxo5dAnXd7D2tKHq7': [{'avg_vol': '36836.36363636364', 'cnt': '253'}], 'var_call_jbyJiOOtpE80xP4X6u0nZg5i': [{'avg_vol': 'nan', 'cnt': '0'}]}

exec(code, env_args)
