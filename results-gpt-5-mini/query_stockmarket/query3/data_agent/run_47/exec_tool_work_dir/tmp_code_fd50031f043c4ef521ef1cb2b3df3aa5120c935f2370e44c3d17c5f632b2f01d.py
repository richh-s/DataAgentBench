code = """import json, math
# data from stockinfo query
info = var_call_ERlMMgBcGlcAYVaj1wdZiJj5
# mapping of symbols to the corresponding avg-volume query result variable names (in same order as the parallel queries)
var_names = [
    'var_call_WekFypB3UmGHXdERh5zDaD0J',
    'var_call_ZiA9TdYdaSMVnStpke0rQmRe',
    'var_call_711v72tNobBMFbeHpcxErkFa',
    'var_call_PgJlaL65T1cGyokeXh4upzuL',
    'var_call_Vrxu0Xpc0eTaXDe0BkDIk0DK',
    'var_call_ZBHUDSuVKjxxbVZE0Qh9yieN',
    'var_call_bjCgGfHZG9yciTJEfAwGJ9cO',
    'var_call_eW1rJ1NJJe6QOBAyO4exvtWR',
    'var_call_GDArXcxREKYAApeS0CIdnOxj',
    'var_call_qiVk1YqRvlT2JV7prNRoz5aF',
    'var_call_EKgrEklqCqspZaX9NCWCgDwK',
    'var_call_jRJgJBuCXSfGKwRbVDsXgBUS',
    'var_call_CzLVcLZGl4hSbmNDtuieVvW7',
    'var_call_GE4pBvLKik05uDHkINIxyDd2',
    'var_call_bq1izzNGZAkgJfpPme634vhS',
    'var_call_7Bc4uhEEcv5tMWScqnAaOtun',
    'var_call_LIW70inLv5JuoIdlCsZpjKh2',
    'var_call_ipFSbXI928M7KZD8KeiKMQBn',
    'var_call_I303T8rGSnoUL76wQzhRshWS',
    'var_call_c2f425NahMCAkznelnXGp42h',
    'var_call_NPZwYiXXnbg6zF3g6n1f2I84',
    'var_call_wcGuShVFnCx1a50LQfOhyJfw',
    'var_call_cG0YOhohF1C1iafUaw7Q7TOU',
    'var_call_HVa0O7vVnss20zqhCzO9pWUD',
    'var_call_HxjqQQDnINASuxIyTeUcMlMF'
]
results = []
for row, varname in zip(info, var_names):
    symbol = row.get('Symbol')
    desc = row.get('Company Description')
    # try to get the avg result variable
    avg_var = globals().get(varname)
    if not avg_var:
        continue
    # avg_var is expected to be a list with one dict
    rec = avg_var[0]
    avg_vol_raw = rec.get('avg_vol')
    cnt_raw = rec.get('cnt')
    try:
        cnt = int(cnt_raw)
    except Exception:
        try:
            cnt = int(float(cnt_raw))
        except Exception:
            cnt = 0
    # treat 'nan' (string) or actual NaN as missing
    avg_vol = None
    if isinstance(avg_vol_raw, str):
        if avg_vol_raw.lower() != 'nan':
            try:
                avg_vol = float(avg_vol_raw)
            except Exception:
                avg_vol = None
    elif isinstance(avg_vol_raw, (int, float)):
        if not (isinstance(avg_vol_raw, float) and math.isnan(avg_vol_raw)):
            avg_vol = float(avg_vol_raw)
    # include only if there was trading volume (cnt>0) and avg_vol is not None
    if cnt > 0 and avg_vol is not None:
        # extract company name as first sentence before a period, fallback to full description
        company_name = desc.split('.')[0].strip() if isinstance(desc, str) and '.' in desc else (desc if isinstance(desc, str) else None)
        results.append({'Symbol': symbol, 'CompanyName': company_name, 'AverageDailyVolume2008': avg_vol})
# produce JSON string
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ERlMMgBcGlcAYVaj1wdZiJj5': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q', 'Nasdaq Traded': 'Y'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}], 'var_call_WekFypB3UmGHXdERh5zDaD0J': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_ZiA9TdYdaSMVnStpke0rQmRe': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_711v72tNobBMFbeHpcxErkFa': [{'avg_vol': '23781.422924901184', 'cnt': '253'}], 'var_call_PgJlaL65T1cGyokeXh4upzuL': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_Vrxu0Xpc0eTaXDe0BkDIk0DK': [{'avg_vol': '10988.142292490118', 'cnt': '253'}], 'var_call_ZBHUDSuVKjxxbVZE0Qh9yieN': [{'avg_vol': '86223.32015810277', 'cnt': '253'}], 'var_call_bjCgGfHZG9yciTJEfAwGJ9cO': [{'avg_vol': '4366.798418972332', 'cnt': '253'}], 'var_call_eW1rJ1NJJe6QOBAyO4exvtWR': [{'avg_vol': '145247.8260869565', 'cnt': '253'}], 'var_call_GDArXcxREKYAApeS0CIdnOxj': [{'avg_vol': '375.49407114624506', 'cnt': '253'}], 'var_call_qiVk1YqRvlT2JV7prNRoz5aF': [{'avg_vol': '15578.656126482214', 'cnt': '253'}], 'var_call_EKgrEklqCqspZaX9NCWCgDwK': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_jRJgJBuCXSfGKwRbVDsXgBUS': [{'avg_vol': '9.845238095238095', 'cnt': '168'}], 'var_call_CzLVcLZGl4hSbmNDtuieVvW7': [{'avg_vol': '254397.62845849802', 'cnt': '253'}], 'var_call_GE4pBvLKik05uDHkINIxyDd2': [{'avg_vol': '10.276679841897232', 'cnt': '253'}], 'var_call_bq1izzNGZAkgJfpPme634vhS': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_7Bc4uhEEcv5tMWScqnAaOtun': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_LIW70inLv5JuoIdlCsZpjKh2': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_ipFSbXI928M7KZD8KeiKMQBn': [{'avg_vol': '254.1501976284585', 'cnt': '253'}], 'var_call_I303T8rGSnoUL76wQzhRshWS': [{'avg_vol': '10706.719367588932', 'cnt': '253'}], 'var_call_c2f425NahMCAkznelnXGp42h': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_NPZwYiXXnbg6zF3g6n1f2I84': [{'avg_vol': '2390.513833992095', 'cnt': '253'}], 'var_call_wcGuShVFnCx1a50LQfOhyJfw': [{'avg_vol': '781.8181818181819', 'cnt': '253'}], 'var_call_cG0YOhohF1C1iafUaw7Q7TOU': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_HVa0O7vVnss20zqhCzO9pWUD': [{'avg_vol': '36836.36363636364', 'cnt': '253'}], 'var_call_HxjqQQDnINASuxIyTeUcMlMF': [{'avg_vol': 'nan', 'cnt': '0'}]}

exec(code, env_args)
