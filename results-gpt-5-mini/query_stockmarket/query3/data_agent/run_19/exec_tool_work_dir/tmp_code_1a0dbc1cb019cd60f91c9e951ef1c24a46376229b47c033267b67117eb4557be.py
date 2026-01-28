code = """import json
# Use the results from previous calls available as variables
symbols = var_call_yNNm2rcHhbdyRBQDwr2sYyRM  # list of symbols

keys = [
    'var_call_m7fjufiyCFpUA3TphshzUNPP',
    'var_call_1BmDfo51AWZk8OQCxuH2oLPR',
    'var_call_BPHskCuLaDunF22QKvwgjnry',
    'var_call_WkIfAYeWXmnZtS7bh03Hx9mD',
    'var_call_9HDhIuFw3jt1FPhtBK7gY8ii',
    'var_call_oOx1MznZcmxsQ4e3w6Dcj8Fs',
    'var_call_0nZk3BaEQn7IKV0hrWXXb3p2',
    'var_call_848l0R5BLQ3l8DIdh5EDU8rd',
    'var_call_m8SINhdVpFRonBAx44IH6RHs',
    'var_call_D9rLh9YAgdQGxIM8c1QHyzlj',
    'var_call_YMaMptzx8nSSua2VLU457dtt',
    'var_call_GJyDUWYLlOt6tSlRPLaogEEf',
    'var_call_Yx16GOfkv2YnpmALG4hoT7PA',
    'var_call_uRQxaQv3tgNApT6mhDw8ze9f',
    'var_call_52nW7o9f2cR2Lz0Rx9rCe3Fv',
    'var_call_nIvWizKs7EkWwAyile7bbyox',
    'var_call_ohe9z5eJXKAdkCS7DVsyvKNF',
    'var_call_Afg9ktFyPh8U4BvR8jyZ8IhA',
    'var_call_r8ppUYnP72rbNi5bkqd0fGLp',
    'var_call_3vGq9kcaWWR6sVR7NJrlL3e3',
    'var_call_Vj2yUuLIn8OZ0oBYRgP3olAG',
    'var_call_2mDpEpfWk63p9khOaFOii6E8',
    'var_call_2Ghx8t8h8fhRIPDqki3kAGxg',
    'var_call_hbnUUne2Wy2wMTKP5FAWtwzF',
    'var_call_V9h7rEUQi3bjyuIR9sUxFrhr'
]

results = []
for sym, key in zip(symbols, keys):
    recs = globals().get(key)
    avg = None
    if recs and isinstance(recs, list) and len(recs) > 0:
        val = recs[0].get('avg_volume')
        if val is None:
            avg = None
        elif isinstance(val, str) and val.lower() == 'nan':
            avg = None
        else:
            try:
                avg = float(val)
            except:
                avg = None
    # Only include non-null averages
    if avg is not None:
        results.append({'Symbol': sym, 'avg_daily_volume_2008': avg})

# Map symbols to company descriptions from stockinfo query
symbol_to_name = {rec['Symbol']: rec['Company Description'] for rec in var_call_wZtFPvHQsDwLsEEF0IbiMek9}

final = []
for r in results:
    name = symbol_to_name.get(r['Symbol'], r['Symbol'])
    final.append({'Company Name': name, 'Average Daily Volume 2008': r['avg_daily_volume_2008']})

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_wZtFPvHQsDwLsEEF0IbiMek9': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Market Category': 'S', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Market Category': 'S', 'Financial Status': 'D'}], 'var_call_CG5nApAXIEzOgCwos238jmWY': 'file_storage/call_CG5nApAXIEzOgCwos238jmWY.json', 'var_call_yNNm2rcHhbdyRBQDwr2sYyRM': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'var_call_m7fjufiyCFpUA3TphshzUNPP': [{'avg_volume': 'nan'}], 'var_call_1BmDfo51AWZk8OQCxuH2oLPR': [{'avg_volume': 'nan'}], 'var_call_BPHskCuLaDunF22QKvwgjnry': [{'avg_volume': '23781.422924901184'}], 'var_call_WkIfAYeWXmnZtS7bh03Hx9mD': [{'avg_volume': 'nan'}], 'var_call_9HDhIuFw3jt1FPhtBK7gY8ii': [{'avg_volume': '10988.142292490118'}], 'var_call_oOx1MznZcmxsQ4e3w6Dcj8Fs': [{'avg_volume': '86223.32015810277'}], 'var_call_0nZk3BaEQn7IKV0hrWXXb3p2': [{'avg_volume': '4366.798418972332'}], 'var_call_848l0R5BLQ3l8DIdh5EDU8rd': [{'avg_volume': '145247.8260869565'}], 'var_call_m8SINhdVpFRonBAx44IH6RHs': [{'avg_volume': '375.49407114624506'}], 'var_call_D9rLh9YAgdQGxIM8c1QHyzlj': [{'avg_volume': '15578.656126482214'}], 'var_call_YMaMptzx8nSSua2VLU457dtt': [{'avg_volume': 'nan'}], 'var_call_GJyDUWYLlOt6tSlRPLaogEEf': [{'avg_volume': '9.845238095238095'}], 'var_call_Yx16GOfkv2YnpmALG4hoT7PA': [{'avg_volume': '254397.62845849802'}], 'var_call_uRQxaQv3tgNApT6mhDw8ze9f': [{'avg_volume': '10.276679841897232'}], 'var_call_52nW7o9f2cR2Lz0Rx9rCe3Fv': [{'avg_volume': 'nan'}], 'var_call_nIvWizKs7EkWwAyile7bbyox': [{'avg_volume': 'nan'}], 'var_call_ohe9z5eJXKAdkCS7DVsyvKNF': [{'avg_volume': 'nan'}], 'var_call_Afg9ktFyPh8U4BvR8jyZ8IhA': [{'avg_volume': '254.1501976284585'}], 'var_call_r8ppUYnP72rbNi5bkqd0fGLp': [{'avg_volume': '10706.719367588932'}], 'var_call_3vGq9kcaWWR6sVR7NJrlL3e3': [{'avg_volume': 'nan'}], 'var_call_Vj2yUuLIn8OZ0oBYRgP3olAG': [{'avg_volume': '2390.513833992095'}], 'var_call_2mDpEpfWk63p9khOaFOii6E8': [{'avg_volume': '781.8181818181819'}], 'var_call_2Ghx8t8h8fhRIPDqki3kAGxg': [{'avg_volume': 'nan'}], 'var_call_hbnUUne2Wy2wMTKP5FAWtwzF': [{'avg_volume': '36836.36363636364'}], 'var_call_V9h7rEUQi3bjyuIR9sUxFrhr': [{'avg_volume': 'nan'}]}

exec(code, env_args)
