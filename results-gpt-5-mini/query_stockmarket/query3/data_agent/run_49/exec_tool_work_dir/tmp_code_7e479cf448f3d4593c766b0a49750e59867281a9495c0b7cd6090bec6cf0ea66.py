code = """import json
# stock info list
stock_list = var_call_o9cRPF7w4hVulj0nIv51KSRD
# mapping symbols to company description
symbol_to_company = {item['symbol']: item['company'] for item in stock_list}

symbols = ["AGMH","AMTX","APEX","BIOC","BKYI","CBAT","CCCL","CORV","CPAH","DZSI","FAMI","FTFT","FTR","IDEX","ISDS","MCEP","NXTD","OPTT","PEIX","RBZ","SNSS","SPI","SYPR","VTIQW"]
var_keys = [
    'var_call_9YSne2hEeuoIKt0Cv6uDWVpr',
    'var_call_5BqLSDMzS3aoDtK1hSj4EYEQ',
    'var_call_DK3B6LAT7RVSxn9pggrUvNNp',
    'var_call_FtAT8E5nXC1qVj7pYNLeI1lF',
    'var_call_lVmpVao6vTIMTW2lDYBo4X2C',
    'var_call_tEhHd7lXci4iwoa86J0O8mxH',
    'var_call_zXaFQdtnC41nAea4grdCrsb5',
    'var_call_pxYTm1Lhc8vefPQgKoLXAhXk',
    'var_call_NHWfd6nBb4sH9YHBytPnRuAk',
    'var_call_H6FH29myVkz6FYGa3ybpYmXv',
    'var_call_bPHjL4AiBSXIAVIc0bByARwr',
    'var_call_dMErLwsf85h1Uv9rYqrrqTL2',
    'var_call_UDF37IlM1Y3z31QTSSqeXLSJ',
    'var_call_7r2dVf4z5kS3flkfpPZhtxhj',
    'var_call_EJX5vVJ9309tN56uHvGw38hM',
    'var_call_B28oFRGHnlo8NMlkthPb2W81',
    'var_call_uJ3uNs659JSX5qYWOi0BxUl2',
    'var_call_bkf8dj41WF7R1a6iIJtsntzm',
    'var_call_LSoZas7sbRz26O6pxb6SuKL2',
    'var_call_nKndNEnzCFc79J0NLWsMq05m',
    'var_call_OWRNgVm8MZMXyjXswz5G5v7P',
    'var_call_5EKrwzuDxQox7pQVZKBOxA3L',
    'var_call_btq18yBAmpfPfqCltpadXVxG',
    'var_call_MByfVqqr61ID0YjEvocjvDHP'
]

results = []
for sym, key in zip(symbols, var_keys):
    recs = globals().get(key)
    if not recs:
        continue
    rec = recs[0]
    try:
        cnt = int(rec.get('cnt'))
    except:
        try:
            cnt = int(float(rec.get('cnt')))
        except:
            cnt = 0
    avg_raw = rec.get('avg_vol')
    try:
        avg = float(avg_raw)
    except:
        avg = None
    if cnt > 0 and avg is not None and not (avg != avg):  # not NaN
        company = symbol_to_company.get(sym, None)
        results.append({
            'symbol': sym,
            'company': company,
            'avg_daily_volume_2008': avg
        })

output = json.dumps(results)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_o9cRPF7w4hVulj0nIv51KSRD': [{'symbol': 'AGMH', 'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'AMTX', 'company': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'fin_status': 'D', 'market_cat': 'G'}, {'symbol': 'APEX', 'company': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'BIOC', 'company': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'BKYI', 'company': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'CBAT', 'company': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'CCCL', 'company': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'CORV', 'company': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'CPAH', 'company': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'DZSI', 'company': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'FAMI', 'company': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'FTFT', 'company': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'FTR', 'company': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'fin_status': 'D', 'market_cat': 'Q'}, {'symbol': 'IDEX', 'company': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'ISDS', 'company': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'fin_status': 'D', 'market_cat': 'G'}, {'symbol': 'MCEP', 'company': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'NXTD', 'company': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'OPTT', 'company': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'PEIX', 'company': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'RBZ', 'company': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'fin_status': 'D', 'market_cat': 'G'}, {'symbol': 'SNSS', 'company': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'fin_status': 'D', 'market_cat': 'S'}, {'symbol': 'SPI', 'company': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'fin_status': 'D', 'market_cat': 'Q'}, {'symbol': 'SYPR', 'company': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'fin_status': 'D', 'market_cat': 'G'}, {'symbol': 'VTIQW', 'company': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'fin_status': 'D', 'market_cat': 'S'}], 'var_call_9YSne2hEeuoIKt0Cv6uDWVpr': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_5BqLSDMzS3aoDtK1hSj4EYEQ': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_DK3B6LAT7RVSxn9pggrUvNNp': [{'cnt': '253', 'avg_vol': '23781.422924901184'}], 'var_call_FtAT8E5nXC1qVj7pYNLeI1lF': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_lVmpVao6vTIMTW2lDYBo4X2C': [{'cnt': '253', 'avg_vol': '10988.142292490118'}], 'var_call_tEhHd7lXci4iwoa86J0O8mxH': [{'cnt': '253', 'avg_vol': '86223.32015810277'}], 'var_call_zXaFQdtnC41nAea4grdCrsb5': [{'cnt': '253', 'avg_vol': '4366.798418972332'}], 'var_call_pxYTm1Lhc8vefPQgKoLXAhXk': [{'cnt': '253', 'avg_vol': '145247.8260869565'}], 'var_call_NHWfd6nBb4sH9YHBytPnRuAk': [{'cnt': '253', 'avg_vol': '375.49407114624506'}], 'var_call_H6FH29myVkz6FYGa3ybpYmXv': [{'cnt': '253', 'avg_vol': '15578.656126482214'}], 'var_call_bPHjL4AiBSXIAVIc0bByARwr': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_dMErLwsf85h1Uv9rYqrrqTL2': [{'cnt': '168', 'avg_vol': '9.845238095238095'}], 'var_call_UDF37IlM1Y3z31QTSSqeXLSJ': [{'cnt': '253', 'avg_vol': '254397.62845849802'}], 'var_call_7r2dVf4z5kS3flkfpPZhtxhj': [{'cnt': '253', 'avg_vol': '10.276679841897232'}], 'var_call_EJX5vVJ9309tN56uHvGw38hM': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_B28oFRGHnlo8NMlkthPb2W81': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_uJ3uNs659JSX5qYWOi0BxUl2': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_bkf8dj41WF7R1a6iIJtsntzm': [{'cnt': '253', 'avg_vol': '254.1501976284585'}], 'var_call_LSoZas7sbRz26O6pxb6SuKL2': [{'cnt': '253', 'avg_vol': '10706.719367588932'}], 'var_call_nKndNEnzCFc79J0NLWsMq05m': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_OWRNgVm8MZMXyjXswz5G5v7P': [{'cnt': '253', 'avg_vol': '781.8181818181819'}], 'var_call_5EKrwzuDxQox7pQVZKBOxA3L': [{'cnt': '0', 'avg_vol': 'nan'}], 'var_call_btq18yBAmpfPfqCltpadXVxG': [{'cnt': '253', 'avg_vol': '36836.36363636364'}], 'var_call_MByfVqqr61ID0YjEvocjvDHP': [{'cnt': '0', 'avg_vol': 'nan'}]}

exec(code, env_args)
