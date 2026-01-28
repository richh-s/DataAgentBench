code = """import json
stockinfo = var_call_mXtAnJzxUN4TeGoIE46vXazQ
var_keys = [
    'var_call_s1VdU8uxmXpGqDFEKF7EHh1m',
    'var_call_TzVs5PTYH2em01ymEK9YO0Nj',
    'var_call_IrLOa8TnXos4e3EAl6d4VCAT',
    'var_call_o9wIdQNWZO1mbcGhL7Fa84HZ',
    'var_call_PQvR4ruqYeihGEjpxhCBggZy',
    'var_call_8a1Tly3p3EhkeSqP4ci3byya',
    'var_call_dYkAdy6u9e4UBuzBX7aBguvO',
    'var_call_Eijvz7gIpKzQqeqI4sHcV0oy',
    'var_call_9OvKAwreFzXZSZ4N5Y3PVd9l',
    'var_call_OOduSY20e6her0KEVx33fa9B',
    'var_call_lpnx6t9DKah5jQHjqgoVJkYi',
    'var_call_6qDZ3ZX2EJePmd5Q1htBmEz8',
    'var_call_f07ctMB7cuILzZx9kqHM0KVv',
    'var_call_A5TwAJ9iO383XXSF7nwkNetr',
    'var_call_SbnnoD7bDhuaTXunlYOdOqoF',
    'var_call_aghwpNXefJmFDCG9Mp5y4OBT',
    'var_call_CGSMq4TCXkt9OcdAeJgADYYh',
    'var_call_BlroBiBHIFM3k6JI2Ztl3G4d',
    'var_call_j6Q1O9asuluNE977yaoXNhkf',
    'var_call_bFTOx5n782ghBLyzsbmSnmYd',
    'var_call_2OCxrrnSXFYGJk6ccMYCggaF',
    'var_call_yFAh4QklLAoJi2ggAY5y7Fht',
    'var_call_uZ5eC8D20BrWp8Xayfzl5t0k',
    'var_call_QX7yfW6KlM7EEoUS1DHTymHI',
    'var_call_nIvTkgAnRr1l2xAMtqY6VELQ'
]
results = []
for i, entry in enumerate(stockinfo):
    sym = entry.get('Symbol')
    comp = entry.get('Company Description')
    key = var_keys[i]
    query_res = globals().get(key)
    if not query_res or len(query_res)==0:
        continue
    r0 = query_res[0]
    avg = r0.get('avg_volume')
    cnt = r0.get('cnt')
    if avg is None or cnt is None:
        continue
    if avg == 'nan' or cnt == '0':
        continue
    try:
        avgf = float(avg)
    except:
        continue
    results.append({'Company Description': comp, 'Symbol': sym, 'avg_volume_2008': avgf})
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_mXtAnJzxUN4TeGoIE46vXazQ': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D'}], 'var_call_s1VdU8uxmXpGqDFEKF7EHh1m': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_TzVs5PTYH2em01ymEK9YO0Nj': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_IrLOa8TnXos4e3EAl6d4VCAT': [{'avg_volume': '23781.422924901184', 'cnt': '253'}], 'var_call_o9wIdQNWZO1mbcGhL7Fa84HZ': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_PQvR4ruqYeihGEjpxhCBggZy': [{'avg_volume': '10988.142292490118', 'cnt': '253'}], 'var_call_8a1Tly3p3EhkeSqP4ci3byya': [{'avg_volume': '86223.32015810277', 'cnt': '253'}], 'var_call_dYkAdy6u9e4UBuzBX7aBguvO': [{'avg_volume': '4366.798418972332', 'cnt': '253'}], 'var_call_Eijvz7gIpKzQqeqI4sHcV0oy': [{'avg_volume': '145247.8260869565', 'cnt': '253'}], 'var_call_9OvKAwreFzXZSZ4N5Y3PVd9l': [{'avg_volume': '375.49407114624506', 'cnt': '253'}], 'var_call_OOduSY20e6her0KEVx33fa9B': [{'avg_volume': '15578.656126482214', 'cnt': '253'}], 'var_call_lpnx6t9DKah5jQHjqgoVJkYi': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_6qDZ3ZX2EJePmd5Q1htBmEz8': [{'avg_volume': '9.845238095238095', 'cnt': '168'}], 'var_call_f07ctMB7cuILzZx9kqHM0KVv': [{'avg_volume': '254397.62845849802', 'cnt': '253'}], 'var_call_A5TwAJ9iO383XXSF7nwkNetr': [{'avg_volume': '10.276679841897232', 'cnt': '253'}], 'var_call_SbnnoD7bDhuaTXunlYOdOqoF': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_aghwpNXefJmFDCG9Mp5y4OBT': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_CGSMq4TCXkt9OcdAeJgADYYh': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_BlroBiBHIFM3k6JI2Ztl3G4d': [{'avg_volume': '254.1501976284585', 'cnt': '253'}], 'var_call_j6Q1O9asuluNE977yaoXNhkf': [{'avg_volume': '10706.719367588932', 'cnt': '253'}], 'var_call_bFTOx5n782ghBLyzsbmSnmYd': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_2OCxrrnSXFYGJk6ccMYCggaF': [{'avg_volume': '2390.513833992095', 'cnt': '253'}], 'var_call_yFAh4QklLAoJi2ggAY5y7Fht': [{'avg_volume': '781.8181818181819', 'cnt': '253'}], 'var_call_uZ5eC8D20BrWp8Xayfzl5t0k': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_QX7yfW6KlM7EEoUS1DHTymHI': [{'avg_volume': '36836.36363636364', 'cnt': '253'}], 'var_call_nIvTkgAnRr1l2xAMtqY6VELQ': [{'avg_volume': 'nan', 'cnt': '0'}]}

exec(code, env_args)
