code = """import json, math
stockinfo = var_call_Ul4Wv1xvkquy3S5LwNbgtu6Z
# avg results from individual queries
avg_map = {
    'AGMH': var_call_sJCtdl1rjddS72TBT3fy1S2c,
    'AMTX': var_call_Vg7eZbvVvkaxs2LmzNowHMRE,
    'APEX': var_call_CSoqJJi5Q202IFONqr0tZefe,
    'BIOC': var_call_zHIGFxt7B4zk74b2m8dF8FNH,
    'BKYI': var_call_TA9nc3gAYLA6Jq1Apz1uU8ja,
    'CBAT': var_call_47zmR5GWeJyQmyDvlsb0lsri,
    'CCCL': var_call_ckotO8pJjSTlxusNgcKSykQw,
    'CORV': var_call_QrnIu2BFB6QNpOoFZZds05wa,
    'CPAH': var_call_uRdZ0Z6tVQ4JS7eCD1roWNKr,
    'DZSI': var_call_tKgyi6JWUT12vTukpO48LUiG,
    'FAMI': var_call_3qfIeF7k524viwrx5Ti4gFqh,
    'FTFT': var_call_s2VcDEF9AfblFxAMUInqI4pb,
    'FTR': var_call_3WbmgcmWlt2GL2S1BfeutqMu,
    'IDEX': var_call_u4oxPvzHjxzWC31MwMulDqwt,
    'ISDS': var_call_je4stQ4yd7YjhkzZC90Z15MU,
    'MCEP': var_call_tklaN1GTebSWidtV9fqAYFLs,
    'NXTD': var_call_uInNYuVmXv0PExknDyPWVguB,
    'OPTT': var_call_StENkfpHqxfOOplGxHU59Usm,
    'PEIX': var_call_QHwhFuP5sokEt4SjYZA7dwsi,
    'RBZ': var_call_8QevwcAbN40e7MY5wTboKqU1,
    'SNSS': var_call_CUBKO5lVcyknIwQxbnDrJuM3,
    'SPI': var_call_9crWhi5WvhI99uwqMtxl4vjk,
    'SYPR': var_call_3xUWPVKMR9ktng3Lu2dh4cdm,
    'VTIQW': var_call_knf5L7B6Xf8XhzObJDKfPhvD
}

# helper to parse avg
def parse_avg(rec_list):
    try:
        v = rec_list[0].get('avg_vol')
    except Exception:
        return None
    if v is None:
        return None
    # sometimes returned as string 'nan'
    try:
        fv = float(v)
        if math.isnan(fv):
            return None
        return fv
    except Exception:
        return None

results = []
for rec in stockinfo:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    if sym in avg_map:
        avg = parse_avg(avg_map[sym])
        if avg is not None:
            results.append({'Symbol': sym, 'Company Description': desc, 'avg_volume_2008': avg})

# sort results by Symbol for consistent order
results = sorted(results, key=lambda x: x['Symbol'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_Ul4Wv1xvkquy3S5LwNbgtu6Z': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_sJCtdl1rjddS72TBT3fy1S2c': [{'avg_vol': 'nan'}], 'var_call_Vg7eZbvVvkaxs2LmzNowHMRE': [{'avg_vol': 'nan'}], 'var_call_CSoqJJi5Q202IFONqr0tZefe': [{'avg_vol': '23781.422924901184'}], 'var_call_zHIGFxt7B4zk74b2m8dF8FNH': [{'avg_vol': 'nan'}], 'var_call_TA9nc3gAYLA6Jq1Apz1uU8ja': [{'avg_vol': '10988.142292490118'}], 'var_call_47zmR5GWeJyQmyDvlsb0lsri': [{'avg_vol': '86223.32015810277'}], 'var_call_ckotO8pJjSTlxusNgcKSykQw': [{'avg_vol': '4366.798418972332'}], 'var_call_QrnIu2BFB6QNpOoFZZds05wa': [{'avg_vol': '145247.8260869565'}], 'var_call_uRdZ0Z6tVQ4JS7eCD1roWNKr': [{'avg_vol': '375.49407114624506'}], 'var_call_tKgyi6JWUT12vTukpO48LUiG': [{'avg_vol': '15578.656126482214'}], 'var_call_3qfIeF7k524viwrx5Ti4gFqh': [{'avg_vol': 'nan'}], 'var_call_s2VcDEF9AfblFxAMUInqI4pb': [{'avg_vol': '9.845238095238095'}], 'var_call_3WbmgcmWlt2GL2S1BfeutqMu': [{'avg_vol': '254397.62845849802'}], 'var_call_u4oxPvzHjxzWC31MwMulDqwt': [{'avg_vol': '10.276679841897232'}], 'var_call_je4stQ4yd7YjhkzZC90Z15MU': [{'avg_vol': 'nan'}], 'var_call_tklaN1GTebSWidtV9fqAYFLs': [{'avg_vol': 'nan'}], 'var_call_uInNYuVmXv0PExknDyPWVguB': [{'avg_vol': 'nan'}], 'var_call_StENkfpHqxfOOplGxHU59Usm': [{'avg_vol': '254.1501976284585'}], 'var_call_QHwhFuP5sokEt4SjYZA7dwsi': [{'avg_vol': '10706.719367588932'}], 'var_call_8QevwcAbN40e7MY5wTboKqU1': [{'avg_vol': 'nan'}], 'var_call_CUBKO5lVcyknIwQxbnDrJuM3': [{'avg_vol': '781.8181818181819'}], 'var_call_9crWhi5WvhI99uwqMtxl4vjk': [{'avg_vol': 'nan'}], 'var_call_3xUWPVKMR9ktng3Lu2dh4cdm': [{'avg_vol': '36836.36363636364'}], 'var_call_knf5L7B6Xf8XhzObJDKfPhvD': [{'avg_vol': 'nan'}]}

exec(code, env_args)
