code = """import json
# Load query results
info = var_call_d2z1VuOe4XqZQ9JzLP1P8074
# Corresponding volume query result variables in the same order as symbols in info
vol_keys = [
    var_call_HKZGUPb6FNxkpWKq3t2XKwhC,
    var_call_UtSOsPUNodY4w78nD64AJ8u7,
    var_call_EpAEtya5R6d6wbxchqhWwvKi,
    var_call_aOZbLEQZt6IfseiCUlTnyiny,
    var_call_WmnbZkfqnZGsGpvMAs4hwt9r,
    var_call_J9oRYdpQUavw2OCv6yJRKgP5,
    var_call_zsCJAFz7EzmujsOxQtlHlm6y,
    var_call_qoLT1xjnTbnPTOqWaTnXefyN,
    var_call_WYcN2HG7BfXheqe15NiWvgIl,
    var_call_yosgxF3mhOl3VLhM1DikHpQa,
    var_call_KRI3udrqX2rXDcvfUHWJGOmp,
    var_call_JCrKrl78stBlfbaNdn3oLP4s,
    var_call_3Wi4TrRie9YCTejgXq1GyQdt,
    var_call_UuMPctbao4X2FNbSR6cQqeSs,
    var_call_LfBG7YoRCpzTfXCEtQkly67p,
    var_call_gI676VeWVDrpAopTwsYus5BB,
    var_call_0ihYd7sCojcvgVdm0FeTUWIM,
    var_call_hETxNkIZNX4i5s4HdrTDhvXj,
    var_call_oBKxQQRIhfJUPnRTeJpaAtxU,
    var_call_CcQnVlo8ZyDLo4umAfX1DHj2,
    var_call_Z2stP4xiJTcOee45FQ9otqby,
    var_call_ginE9V0mwqe6q9sjL4rGLGn0,
    var_call_RWCFi3J8YwjE8kybXB5S19wT,
    var_call_TqbFzOqDt4Y88TdYmdjiHKgZ,
]

results = []
for idx, row in enumerate(info):
    symbol = row.get('Symbol')
    company_desc = row.get('Company Description')
    vol_entry = vol_keys[idx]
    # vol_entry may be a list-like or a JSON string
    if isinstance(vol_entry, str):
        try:
            vol_list = json.loads(vol_entry)
        except Exception:
            vol_list = None
    else:
        vol_list = vol_entry
    avg = None
    cnt = 0
    if isinstance(vol_list, list) and len(vol_list) > 0:
        ent = vol_list[0]
        raw_avg = ent.get('avg_volume') if isinstance(ent, dict) else None
        raw_cnt = ent.get('cnt') if isinstance(ent, dict) else None
        # convert cnt
        try:
            if raw_cnt is None:
                cnt = 0
            else:
                cnt = int(float(raw_cnt))
        except Exception:
            cnt = 0
        # convert avg
        try:
            if raw_avg is None:
                avg = None
            else:
                # handle strings like "nan"
                if isinstance(raw_avg, str) and raw_avg.lower() == 'nan':
                    avg = None
                else:
                    avg = float(raw_avg)
        except Exception:
            avg = None
    # include only if there was trading volume in 2008 and avg is not null
    if cnt > 0 and avg is not None:
        results.append({'Symbol': symbol, 'Company Description': company_desc, 'avg_volume_2008': avg})

# Output JSON string
out = json.dumps(results, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_d2z1VuOe4XqZQ9JzLP1P8074': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Market Category': 'G', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Market Category': 'Q', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Market Category': 'G', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Market Category': 'G', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Market Category': 'Q', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Market Category': 'G', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Market Category': 'S', 'Financial Status': 'D', 'Nasdaq Traded': 'Y'}], 'var_call_HKZGUPb6FNxkpWKq3t2XKwhC': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_UtSOsPUNodY4w78nD64AJ8u7': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_EpAEtya5R6d6wbxchqhWwvKi': [{'avg_volume': '23781.422924901184', 'cnt': '253'}], 'var_call_aOZbLEQZt6IfseiCUlTnyiny': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_WmnbZkfqnZGsGpvMAs4hwt9r': [{'avg_volume': '10988.142292490118', 'cnt': '253'}], 'var_call_J9oRYdpQUavw2OCv6yJRKgP5': [{'avg_volume': '86223.32015810277', 'cnt': '253'}], 'var_call_zsCJAFz7EzmujsOxQtlHlm6y': [{'avg_volume': '4366.798418972332', 'cnt': '253'}], 'var_call_qoLT1xjnTbnPTOqWaTnXefyN': [{'avg_volume': '145247.8260869565', 'cnt': '253'}], 'var_call_WYcN2HG7BfXheqe15NiWvgIl': [{'avg_volume': '375.49407114624506', 'cnt': '253'}], 'var_call_yosgxF3mhOl3VLhM1DikHpQa': [{'avg_volume': '15578.656126482214', 'cnt': '253'}], 'var_call_KRI3udrqX2rXDcvfUHWJGOmp': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_JCrKrl78stBlfbaNdn3oLP4s': [{'avg_volume': '9.845238095238095', 'cnt': '168'}], 'var_call_3Wi4TrRie9YCTejgXq1GyQdt': [{'avg_volume': '254397.62845849802', 'cnt': '253'}], 'var_call_UuMPctbao4X2FNbSR6cQqeSs': [{'avg_volume': '10.276679841897232', 'cnt': '253'}], 'var_call_LfBG7YoRCpzTfXCEtQkly67p': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_gI676VeWVDrpAopTwsYus5BB': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_0ihYd7sCojcvgVdm0FeTUWIM': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_hETxNkIZNX4i5s4HdrTDhvXj': [{'avg_volume': '254.1501976284585', 'cnt': '253'}], 'var_call_oBKxQQRIhfJUPnRTeJpaAtxU': [{'avg_volume': '10706.719367588932', 'cnt': '253'}], 'var_call_CcQnVlo8ZyDLo4umAfX1DHj2': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_Z2stP4xiJTcOee45FQ9otqby': [{'avg_volume': '781.8181818181819', 'cnt': '253'}], 'var_call_ginE9V0mwqe6q9sjL4rGLGn0': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_RWCFi3J8YwjE8kybXB5S19wT': [{'avg_volume': '36836.36363636364', 'cnt': '253'}], 'var_call_TqbFzOqDt4Y88TdYmdjiHKgZ': [{'avg_volume': 'nan', 'cnt': '0'}]}

exec(code, env_args)
