code = """import json
stock = var_call_HUQRlZnrgA1GNQHlyxvBDQEo
trade_vars = [
    var_call_f83UQgXsrv0rYld85IlCa8wt,
    var_call_iTLCUxtU8TzzYJ9SrLomXPbz,
    var_call_E1TyCFNR4TM4aVsexHQIflcI,
    var_call_BnMRrX04lvUIftBefcv4pPYp,
    var_call_r1Oe8Zrkg7YJqy0cOrm9QArv,
    var_call_sgxCmHq0q8LxumP38D5LSPWG,
    var_call_uxFCMMesrseV53MMv1DR8TSA,
    var_call_wtGE5tSzYQFtUcsabyF07T8K,
    var_call_k7NwavZIuFLVyssiUn8uAgmt,
    var_call_vtB5eJsh1cKKYS8RkNG24L1o,
    var_call_nijzyFNGE1ivMVVHLSqyz33G,
    var_call_IjvU9YWJ7iL6lDrHdNeMKEwb,
    var_call_Hf5g4su6DdHyn8JbYo1PzJNh,
    var_call_BFg5ja1mu1HcKl2oFHMotXwx,
    var_call_NGcMhzdYUrLvpCF6IfycSetJ,
    var_call_IGQmFJ4pySkUrgnehtTf9uIu,
    var_call_tCfHsz4VyBoxjlv0KXdGqlLl,
    var_call_R3EcjsArZsavgN1HqKVCR4b5,
    var_call_wXXOWIKDSs8xtoNs5h2Y903n,
    var_call_cd916UpLj7E9ipiPh72DLGAM,
    var_call_KMiSLXMDRob7InIXJ8SbjapR,
    var_call_ut8tJKFc5iB8NquAz2WREPdr,
    var_call_olqZgEMV7YLBa5nzXJ7kuoVF,
    var_call_I67fGJ5EnlmzIAiAyPcPIQjC,
    var_call_nmRkiYiA28KrUCYo5lALdhbf
]

out = []
for i, s in enumerate(stock):
    if i >= len(trade_vars):
        break
    tv = trade_vars[i]
    if not tv:
        continue
    rec = tv[0]
    avg = rec.get('avg_vol')
    cnt = rec.get('cnt')
    try:
        cnt_i = int(cnt)
    except Exception:
        cnt_i = 0
    if cnt_i == 0:
        continue
    if isinstance(avg, str) and avg.lower() == 'nan':
        continue
    try:
        avg_f = float(avg)
    except Exception:
        continue
    out.append({
        'Symbol': s.get('Symbol'),
        'Company Description': s.get('Company Description'),
        'avg_daily_volume_2008': avg_f
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_HUQRlZnrgA1GNQHlyxvBDQEo': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_cUBGWE0YL2juqSiB97nrtrXm': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_f83UQgXsrv0rYld85IlCa8wt': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_iTLCUxtU8TzzYJ9SrLomXPbz': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_E1TyCFNR4TM4aVsexHQIflcI': [{'avg_vol': '23781.422924901184', 'cnt': '253'}], 'var_call_BnMRrX04lvUIftBefcv4pPYp': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_r1Oe8Zrkg7YJqy0cOrm9QArv': [{'avg_vol': '10988.142292490118', 'cnt': '253'}], 'var_call_sgxCmHq0q8LxumP38D5LSPWG': [{'avg_vol': '86223.32015810277', 'cnt': '253'}], 'var_call_uxFCMMesrseV53MMv1DR8TSA': [{'avg_vol': '4366.798418972332', 'cnt': '253'}], 'var_call_wtGE5tSzYQFtUcsabyF07T8K': [{'avg_vol': '145247.8260869565', 'cnt': '253'}], 'var_call_k7NwavZIuFLVyssiUn8uAgmt': [{'avg_vol': '375.49407114624506', 'cnt': '253'}], 'var_call_vtB5eJsh1cKKYS8RkNG24L1o': [{'avg_vol': '15578.656126482214', 'cnt': '253'}], 'var_call_nijzyFNGE1ivMVVHLSqyz33G': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_IjvU9YWJ7iL6lDrHdNeMKEwb': [{'avg_vol': '9.845238095238095', 'cnt': '168'}], 'var_call_Hf5g4su6DdHyn8JbYo1PzJNh': [{'avg_vol': '254397.62845849802', 'cnt': '253'}], 'var_call_BFg5ja1mu1HcKl2oFHMotXwx': [{'avg_vol': '10.276679841897232', 'cnt': '253'}], 'var_call_NGcMhzdYUrLvpCF6IfycSetJ': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_IGQmFJ4pySkUrgnehtTf9uIu': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_tCfHsz4VyBoxjlv0KXdGqlLl': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_R3EcjsArZsavgN1HqKVCR4b5': [{'avg_vol': '254.1501976284585', 'cnt': '253'}], 'var_call_wXXOWIKDSs8xtoNs5h2Y903n': [{'avg_vol': '10706.719367588932', 'cnt': '253'}], 'var_call_cd916UpLj7E9ipiPh72DLGAM': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_KMiSLXMDRob7InIXJ8SbjapR': [{'avg_vol': '2390.513833992095', 'cnt': '253'}], 'var_call_ut8tJKFc5iB8NquAz2WREPdr': [{'avg_vol': '781.8181818181819', 'cnt': '253'}], 'var_call_olqZgEMV7YLBa5nzXJ7kuoVF': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_I67fGJ5EnlmzIAiAyPcPIQjC': [{'avg_vol': '36836.36363636364', 'cnt': '253'}], 'var_call_nmRkiYiA28KrUCYo5lALdhbf': [{'avg_vol': 'nan', 'cnt': '0'}]}

exec(code, env_args)
