code = """import json
# Access previous query results stored in variables
stock_rows = var_call_QmrDUEzhrtDzITkAID2zp9Hi

mapping = {
    'AGMH': var_call_gziO6nghWBUZBJVrSG1SXp3X,
    'AMTX': var_call_vgJ0GMKx7nao0g9sh9Ki6wK6,
    'APEX': var_call_1nvEVkOSHYwqEB5Dr98aS9b6,
    'BIOC': var_call_cJGKGacbOhXF3jYz2y5KouFS,
    'BKYI': var_call_xAoBBFxCAeJQr2cVDViGhEeR,
    'CBAT': var_call_OXCftMArkh6HuiJ2z6c0rRSe,
    'CCCL': var_call_7Zy7UmW91oALDX124HWdYCm0,
    'CORV': var_call_mufasm2bLDrqIBoka367Lfcf,
    'CPAH': var_call_YZd4WllEeWelH953MtnwFPEG,
    'DZSI': var_call_2CJ7cRfzHo64ZfsjqGqAs3I3,
    'FAMI': var_call_rX3OfLE6zNnPb8emYhT1EBPE,
    'FTFT': var_call_DBtj1aQ0x24AG1mrpIUahqfU,
    'FTR': var_call_NUMePm30mr68cVKmEpo34UYE,
    'IDEX': var_call_Jr4iZALZywpkcjusM3NLQ0ki,
    'ISDS': var_call_1jIhUQipMHdJMZvKBwj6EKmL,
    'MCEP': var_call_8vV7pRYAhwq0LcFVUA2JATd0,
    'NXTD': var_call_TghIgz4KOXwtiBcVjjYHaYn8,
    'OPTT': var_call_RFKZcAooAPlYsPKkcJLLLsG6,
    'PEIX': var_call_EXbEUJ5j7mOu36Y12L5LdHU5,
    'RBZ': var_call_i24uJKqrFksPfLi7w9vuNDQ1,
    'SNSS': var_call_SajOB10bWd9X2H1hPbPMZ0dS,
    'SPI': var_call_50Z2Kh6Icx6G7rmbDPkS2HR7,
    'SYPR': var_call_5fWNo8GFGDftcu7OPQzLd5Fo,
    'VTIQW': var_call_FCfBkkWpWvWpGgHRqGW4vb26,
}

results = []
for r in stock_rows:
    sym = r.get('Symbol')
    comp = r.get('Company Description')
    if sym in mapping:
        rec = mapping[sym]
        # rec is a list like [{'avg_vol': '...'}]
        if rec and isinstance(rec, list):
            val = rec[0].get('avg_vol')
            if val is None:
                continue
            sval = str(val)
            if sval.lower() == 'nan':
                continue
            try:
                f = float(val)
            except:
                continue
            results.append({'Symbol': sym, 'Company Description': comp, 'Average Daily Volume 2008': f})

# Sort results by company name
results_sorted = sorted(results, key=lambda x: x['Company Description'])

print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_QmrDUEzhrtDzITkAID2zp9Hi': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_gziO6nghWBUZBJVrSG1SXp3X': [{'avg_vol': 'nan'}], 'var_call_vgJ0GMKx7nao0g9sh9Ki6wK6': [{'avg_vol': 'nan'}], 'var_call_1nvEVkOSHYwqEB5Dr98aS9b6': [{'avg_vol': '23781.422924901184'}], 'var_call_cJGKGacbOhXF3jYz2y5KouFS': [{'avg_vol': 'nan'}], 'var_call_xAoBBFxCAeJQr2cVDViGhEeR': [{'avg_vol': '10988.142292490118'}], 'var_call_OXCftMArkh6HuiJ2z6c0rRSe': [{'avg_vol': '86223.32015810277'}], 'var_call_7Zy7UmW91oALDX124HWdYCm0': [{'avg_vol': '4366.798418972332'}], 'var_call_mufasm2bLDrqIBoka367Lfcf': [{'avg_vol': '145247.8260869565'}], 'var_call_YZd4WllEeWelH953MtnwFPEG': [{'avg_vol': '375.49407114624506'}], 'var_call_2CJ7cRfzHo64ZfsjqGqAs3I3': [{'avg_vol': '15578.656126482214'}], 'var_call_rX3OfLE6zNnPb8emYhT1EBPE': [{'avg_vol': 'nan'}], 'var_call_DBtj1aQ0x24AG1mrpIUahqfU': [{'avg_vol': '9.845238095238095'}], 'var_call_NUMePm30mr68cVKmEpo34UYE': [{'avg_vol': '254397.62845849802'}], 'var_call_Jr4iZALZywpkcjusM3NLQ0ki': [{'avg_vol': '10.276679841897232'}], 'var_call_1jIhUQipMHdJMZvKBwj6EKmL': [{'avg_vol': 'nan'}], 'var_call_8vV7pRYAhwq0LcFVUA2JATd0': [{'avg_vol': 'nan'}], 'var_call_TghIgz4KOXwtiBcVjjYHaYn8': [{'avg_vol': 'nan'}], 'var_call_RFKZcAooAPlYsPKkcJLLLsG6': [{'avg_vol': '254.1501976284585'}], 'var_call_EXbEUJ5j7mOu36Y12L5LdHU5': [{'avg_vol': '10706.719367588932'}], 'var_call_i24uJKqrFksPfLi7w9vuNDQ1': [{'avg_vol': 'nan'}], 'var_call_SajOB10bWd9X2H1hPbPMZ0dS': [{'avg_vol': '781.8181818181819'}], 'var_call_50Z2Kh6Icx6G7rmbDPkS2HR7': [{'avg_vol': 'nan'}], 'var_call_5fWNo8GFGDftcu7OPQzLd5Fo': [{'avg_vol': '36836.36363636364'}], 'var_call_FCfBkkWpWvWpGgHRqGW4vb26': [{'avg_vol': 'nan'}]}

exec(code, env_args)
