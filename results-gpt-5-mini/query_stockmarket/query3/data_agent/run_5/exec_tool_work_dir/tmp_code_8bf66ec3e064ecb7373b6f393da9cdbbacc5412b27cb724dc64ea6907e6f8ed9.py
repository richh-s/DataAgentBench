code = """import json
# Collect results from the query_db calls stored in various keys
keys = [
    'var_call_t3hiN0qYt1nQN0inx8jgt5h6',
    'var_call_snu2KKYaIlt5D3ysoZ8Sk2pc',
    'var_call_ed0Dp0lWi48fHwCdVmYpKoD5',
    'var_call_prPQfufURun0u5PsAAz6bwf1',
    'var_call_toDxUEHHkEjqwNzePd51AfrG',
    'var_call_9W7jKznym42jtr8Kp7QheZkJ',
    'var_call_k0K8MGOW8fDLVDa0woB4hV2G',
    'var_call_gNLBfBNR4xFgXUxjIzpk36Kw',
    'var_call_1vwzL03gRAfUK1tiCQe2Fvet',
    'var_call_Ul9WkuQqWHQq08Lcgux3qgrq',
    'var_call_NcDYyYrHRiDv8wyuJyENcYKY',
    'var_call_7H3PuM0PiW33O91oqPiEDFSw',
    'var_call_CYWNkqbCed93SwpbREGpwIDh',
    'var_call_Jfw2NtqcFaY1gwlqSM8mqqYJ',
    'var_call_tyzGEgXZfxiHAlm0RoaL2UJ1',
    'var_call_YPKtUN4IGhWsgOhNfAOxd63n',
    'var_call_c8hd1SKiBU0r7QWfxLbSypD3',
    'var_call_A11IPoJBpYyep7IMc0NDHIZk',
    'var_call_8GSBS3y9ndlbBDGr6XGQPcEx',
    'var_call_mCXCal8wK21gxlvfjreZP9lb',
    'var_call_GczdC9DpEDoBHrTtyMRJybA8',
    'var_call_ib8WpUWY0xmnbcZCVnKejK5e',
    'var_call_j998mu6nz5iv6HvLLEddh0v7',
    'var_call_52kHfk6cPBzSmKaUau1qpK1B',
    'var_call_u1zk6C8y7Fez2H0o1DlPt3Qp'
]
results = []
for k in keys:
    recs = globals()[k]
    if isinstance(recs, list) and len(recs)>0:
        r = recs[0]
        sym = r.get('Symbol')
        avg = r.get('avg_vol')
        # convert 'nan' strings to None
        if isinstance(avg, str) and avg.lower()=='nan':
            avg_val = None
        else:
            try:
                avg_val = float(avg)
            except:
                avg_val = None
        if avg_val is not None:
            results.append({'Symbol': sym, 'avg_daily_volume_2008': avg_val})
# Now join with company names from stockinfo
stockinfo = var_call_01WPpnQCJQRpmjfuQ2XpdU75
info_map = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}
final = []
for r in results:
    sym = r['Symbol']
    name = info_map.get(sym)
    final.append({'Symbol': sym, 'Company Description': name, 'avg_daily_volume_2008': r['avg_daily_volume_2008']})
print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_01WPpnQCJQRpmjfuQ2XpdU75': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_2U9XGVwUGGRlbXq53eI9I3fs': 'file_storage/call_2U9XGVwUGGRlbXq53eI9I3fs.json', 'var_call_i018RNo4fGXe5IB2lqs1Lhrh': {'count_stockinfo': 25, 'count_intersect': 25}, 'var_call_cJDkpVOSeNvMMx9nA47cDhYq': {'intersect_symbols': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW']}, 'var_call_t3hiN0qYt1nQN0inx8jgt5h6': [{'Symbol': 'AGMH', 'avg_vol': 'nan'}], 'var_call_snu2KKYaIlt5D3ysoZ8Sk2pc': [{'Symbol': 'AMTX', 'avg_vol': 'nan'}], 'var_call_ed0Dp0lWi48fHwCdVmYpKoD5': [{'Symbol': 'APEX', 'avg_vol': '23781.422924901184'}], 'var_call_prPQfufURun0u5PsAAz6bwf1': [{'Symbol': 'BIOC', 'avg_vol': 'nan'}], 'var_call_toDxUEHHkEjqwNzePd51AfrG': [{'Symbol': 'BKYI', 'avg_vol': '10988.142292490118'}], 'var_call_9W7jKznym42jtr8Kp7QheZkJ': [{'Symbol': 'CBAT', 'avg_vol': '86223.32015810277'}], 'var_call_k0K8MGOW8fDLVDa0woB4hV2G': [{'Symbol': 'CCCL', 'avg_vol': '4366.798418972332'}], 'var_call_gNLBfBNR4xFgXUxjIzpk36Kw': [{'Symbol': 'CORV', 'avg_vol': '145247.8260869565'}], 'var_call_1vwzL03gRAfUK1tiCQe2Fvet': [{'Symbol': 'CPAH', 'avg_vol': '375.49407114624506'}], 'var_call_Ul9WkuQqWHQq08Lcgux3qgrq': [{'Symbol': 'DZSI', 'avg_vol': '15578.656126482214'}], 'var_call_NcDYyYrHRiDv8wyuJyENcYKY': [{'Symbol': 'FAMI', 'avg_vol': 'nan'}], 'var_call_7H3PuM0PiW33O91oqPiEDFSw': [{'Symbol': 'FTFT', 'avg_vol': '9.845238095238095'}], 'var_call_CYWNkqbCed93SwpbREGpwIDh': [{'Symbol': 'FTR', 'avg_vol': '254397.62845849802'}], 'var_call_Jfw2NtqcFaY1gwlqSM8mqqYJ': [{'Symbol': 'IDEX', 'avg_vol': '10.276679841897232'}], 'var_call_tyzGEgXZfxiHAlm0RoaL2UJ1': [{'Symbol': 'ISDS', 'avg_vol': 'nan'}], 'var_call_YPKtUN4IGhWsgOhNfAOxd63n': [{'Symbol': 'MCEP', 'avg_vol': 'nan'}], 'var_call_c8hd1SKiBU0r7QWfxLbSypD3': [{'Symbol': 'NXTD', 'avg_vol': 'nan'}], 'var_call_A11IPoJBpYyep7IMc0NDHIZk': [{'Symbol': 'OPTT', 'avg_vol': '254.1501976284585'}], 'var_call_8GSBS3y9ndlbBDGr6XGQPcEx': [{'Symbol': 'PEIX', 'avg_vol': '10706.719367588932'}], 'var_call_mCXCal8wK21gxlvfjreZP9lb': [{'Symbol': 'RBZ', 'avg_vol': 'nan'}], 'var_call_GczdC9DpEDoBHrTtyMRJybA8': [{'Symbol': 'SES', 'avg_vol': '2390.513833992095'}], 'var_call_ib8WpUWY0xmnbcZCVnKejK5e': [{'Symbol': 'SNSS', 'avg_vol': '781.8181818181819'}], 'var_call_j998mu6nz5iv6HvLLEddh0v7': [{'Symbol': 'SPI', 'avg_vol': 'nan'}], 'var_call_52kHfk6cPBzSmKaUau1qpK1B': [{'Symbol': 'SYPR', 'avg_vol': '36836.36363636364'}], 'var_call_u1zk6C8y7Fez2H0o1DlPt3Qp': [{'Symbol': 'VTIQW', 'avg_vol': 'nan'}]}

exec(code, env_args)
