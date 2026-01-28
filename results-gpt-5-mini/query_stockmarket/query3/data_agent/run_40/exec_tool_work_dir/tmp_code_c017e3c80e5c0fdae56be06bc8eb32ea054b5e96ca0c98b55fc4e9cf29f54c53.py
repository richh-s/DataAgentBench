code = """import json, math
# load variables from storage
stockinfo = var_call_hUjlhrPyUQ5qQvjK3Et0mtTs
avg_vars = [var_call_PwT3PJVzHh2D2xRXhJUo5gWE, var_call_kzHXKsdFHQk5H4AbgqMhY3GR, var_call_GG2jFfL5Llhgnm0HIRG5PUFh, var_call_HpGovF9IPosQWccQn4yypcRd, var_call_nfL8BqN8qSWeL4IcrUEkDk6S, var_call_qyS0wMVV4s66pkNmbT869i9t, var_call_DlMe7fe0ivWCe22VjZMbdtDN, var_call_ScG0K0vH5udgE682WeUd9DVF, var_call_4wot8CNCY2itb0YYpFFDttyS, var_call_bpvVMS8LDtWMJFSf9IQex7Gc, var_call_JTsCAOaqd9LS3LhiOkkzWHaC, var_call_Ai6p6f3AOTOYcli0YH2hofGK, var_call_9ZaiKwUoN9ravI2kBBFY77Xy, var_call_b32CaNvbZFp2JSI2aOuLmfFG, var_call_XjwDQwUFshQ5mt6ZWcdBgpmD, var_call_nd9LAtzUwrRVaz9eAMiF7fMg, var_call_eE1ptooNgQMNzdl2epluJuWz, var_call_7Lciv1xHLaapNUvA663h81Lb, var_call_oQc5RrcHErKjor005cm6jqFg, var_call_CR9F1Kuhiy1oZxjZpSYzDsIS, var_call_NXx7uhCOxqfFXzWcRpSdNUTD, var_call_JbhoVusEMaft6Q6lrBrZvjv1, var_call_VXLaVvHufgv1OEpY7bJpDMIM, var_call_tTapMf2eCvfqv1CJNab3sik7, var_call_kOwHsLZsFhFP8pINdWNEW11t]

# helper to extract avg from each query result
def extract_avg(var):
    # var may be list or string
    if isinstance(var, str):
        try:
            parsed = json.loads(var)
        except Exception:
            return None
    else:
        parsed = var
    if not parsed or not isinstance(parsed, list):
        return None
    first = parsed[0]
    if not isinstance(first, dict) or 'avg_vol' not in first:
        return None
    val = first['avg_vol']
    if val is None:
        return None
    # sometimes value is string 'nan'
    if isinstance(val, str):
        if val.lower() == 'nan':
            return None
        try:
            f = float(val)
        except:
            return None
    else:
        try:
            f = float(val)
        except:
            return None
    if math.isnan(f):
        return None
    return f

results = []
# iterate through stockinfo entries and corresponding avg_vars
for i, si in enumerate(stockinfo):
    symbol = si.get('Symbol')
    company = si.get('Company Description')
    avg = extract_avg(avg_vars[i])
    if avg is not None:
        results.append({'Symbol': symbol, 'Company Description': company, 'AvgDailyVolume2008': avg})

# print JSON-serializable string as required
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_iaezj41wKfxSioHYf8OD0RHc': 'file_storage/call_iaezj41wKfxSioHYf8OD0RHc.json', 'var_call_hUjlhrPyUQ5qQvjK3Et0mtTs': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Market Category': 'S', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Market Category': 'S', 'Financial Status': 'D'}], 'var_call_PwT3PJVzHh2D2xRXhJUo5gWE': [{'avg_vol': 'nan'}], 'var_call_kzHXKsdFHQk5H4AbgqMhY3GR': [{'avg_vol': 'nan'}], 'var_call_GG2jFfL5Llhgnm0HIRG5PUFh': [{'avg_vol': '23781.422924901184'}], 'var_call_HpGovF9IPosQWccQn4yypcRd': [{'avg_vol': 'nan'}], 'var_call_nfL8BqN8qSWeL4IcrUEkDk6S': [{'avg_vol': '10988.142292490118'}], 'var_call_qyS0wMVV4s66pkNmbT869i9t': [{'avg_vol': '86223.32015810277'}], 'var_call_DlMe7fe0ivWCe22VjZMbdtDN': [{'avg_vol': '4366.798418972332'}], 'var_call_ScG0K0vH5udgE682WeUd9DVF': [{'avg_vol': '145247.8260869565'}], 'var_call_4wot8CNCY2itb0YYpFFDttyS': [{'avg_vol': '375.49407114624506'}], 'var_call_bpvVMS8LDtWMJFSf9IQex7Gc': [{'avg_vol': '15578.656126482214'}], 'var_call_JTsCAOaqd9LS3LhiOkkzWHaC': [{'avg_vol': 'nan'}], 'var_call_Ai6p6f3AOTOYcli0YH2hofGK': [{'avg_vol': '9.845238095238095'}], 'var_call_9ZaiKwUoN9ravI2kBBFY77Xy': [{'avg_vol': '254397.62845849802'}], 'var_call_b32CaNvbZFp2JSI2aOuLmfFG': [{'avg_vol': '10.276679841897232'}], 'var_call_XjwDQwUFshQ5mt6ZWcdBgpmD': [{'avg_vol': 'nan'}], 'var_call_nd9LAtzUwrRVaz9eAMiF7fMg': [{'avg_vol': 'nan'}], 'var_call_eE1ptooNgQMNzdl2epluJuWz': [{'avg_vol': 'nan'}], 'var_call_7Lciv1xHLaapNUvA663h81Lb': [{'avg_vol': '254.1501976284585'}], 'var_call_oQc5RrcHErKjor005cm6jqFg': [{'avg_vol': '10706.719367588932'}], 'var_call_CR9F1Kuhiy1oZxjZpSYzDsIS': [{'avg_vol': 'nan'}], 'var_call_NXx7uhCOxqfFXzWcRpSdNUTD': [{'avg_vol': '2390.513833992095'}], 'var_call_JbhoVusEMaft6Q6lrBrZvjv1': [{'avg_vol': '781.8181818181819'}], 'var_call_VXLaVvHufgv1OEpY7bJpDMIM': [{'avg_vol': 'nan'}], 'var_call_tTapMf2eCvfqv1CJNab3sik7': [{'avg_vol': '36836.36363636364'}], 'var_call_kOwHsLZsFhFP8pINdWNEW11t': [{'avg_vol': 'nan'}]}

exec(code, env_args)
