code = """import json
companies = var_call_plPTIiU0RAOE5NSW4XsqDhWQ
# Results from trade queries in the same order as the companies list
results_vars = [
    var_call_L4p9X7n4NZsQUkfEwq8c7y5C,
    var_call_vHpkwEei1YDzfWTqoQ9eSVtX,
    var_call_U3OdCwIPu1ffq9Glp9DTfnrY,
    var_call_ZY2KLAKRoMJeJtnYYjwk3YLb,
    var_call_3ixtNviSV2LFWUCrb5IspCuX,
    var_call_Wnw5wJfyTy5wLWHvwPJ9BAGj,
    var_call_vdqDkukQ7XSvce6Rd2NgaUdl,
    var_call_u0XhtmyJUomRzV37BgfdqhLF,
    var_call_kJopInHbfbuYp7Vh3L16EdV1,
    var_call_hBXm4ZqjZPDFTXrEk4hi16G6,
    var_call_bu0JmmWxlXvNAbLje3TDpePm,
    var_call_l6KSYplEfW38j4vZRcLW6oC2,
    var_call_6QNSUsKAKb81MII6T88RxsVD,
    var_call_Xe96N1xzXkHYUmgsFfFUzcf1,
    var_call_okeAlrjlbyEurQlsvDAICEbg,
    var_call_CV7TMR6fftfl9GG5tzqFvjEU,
    var_call_MGnbwSN654JOaXRI1Cw9Wdhn,
    var_call_pBHO7B8aZqeTQVzLVVEzapWy,
    var_call_hW6eWuWO7X9zShfPHRKkdjBG,
    var_call_lcbJaaJQx20xivgCPNI53YrD,
    var_call_Sfq9vTSID5LU9mBrvi6X5kFn,
    var_call_nlTcX1Ix7GbqD0WdwIRNGIyu,
    var_call_oRtnMtBAdQGXidGFrx44aYYA,
    var_call_lQ4DghdH4qRgapGK0BOSrHRS,
    var_call_ve6PZPEgJ1bktPX93w8SVKVr
]
output = []
for comp, res in zip(companies, results_vars):
    sym = comp.get('Symbol')
    name = comp.get('Company Description')
    # res is expected to be a list with one dict
    if not isinstance(res, list) or len(res)==0:
        continue
    rec = res[0]
    avg = rec.get('avg_vol')
    cnt = rec.get('cnt')
    # convert cnt
    try:
        cnt_i = int(cnt)
    except Exception:
        try:
            cnt_i = int(float(cnt))
        except Exception:
            cnt_i = 0
    # determine avg numeric
    avg_num = None
    if avg is None:
        avg_num = None
    else:
        # avg may be string 'nan' or numeric string
        try:
            avg_f = float(avg)
            if not (avg_f != avg_f):  # check for nan
                avg_num = avg_f
        except Exception:
            avg_num = None
    if cnt_i>0 and avg_num is not None:
        output.append({"Symbol": sym, "Company Description": name, "AverageDailyVolume2008": avg_num})
# sort output by Symbol for consistency
output_sorted = sorted(output, key=lambda x: x['Symbol'])
print("__RESULT__:")
print(json.dumps(output_sorted))"""

env_args = {'var_call_plPTIiU0RAOE5NSW4XsqDhWQ': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q', 'Nasdaq Traded': 'Y'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}], 'var_call_L4p9X7n4NZsQUkfEwq8c7y5C': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_vHpkwEei1YDzfWTqoQ9eSVtX': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_U3OdCwIPu1ffq9Glp9DTfnrY': [{'avg_vol': '23781.422924901184', 'cnt': '253'}], 'var_call_ZY2KLAKRoMJeJtnYYjwk3YLb': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_3ixtNviSV2LFWUCrb5IspCuX': [{'avg_vol': '10988.142292490118', 'cnt': '253'}], 'var_call_Wnw5wJfyTy5wLWHvwPJ9BAGj': [{'avg_vol': '86223.32015810277', 'cnt': '253'}], 'var_call_vdqDkukQ7XSvce6Rd2NgaUdl': [{'avg_vol': '4366.798418972332', 'cnt': '253'}], 'var_call_u0XhtmyJUomRzV37BgfdqhLF': [{'avg_vol': '145247.8260869565', 'cnt': '253'}], 'var_call_kJopInHbfbuYp7Vh3L16EdV1': [{'avg_vol': '375.49407114624506', 'cnt': '253'}], 'var_call_hBXm4ZqjZPDFTXrEk4hi16G6': [{'avg_vol': '15578.656126482214', 'cnt': '253'}], 'var_call_bu0JmmWxlXvNAbLje3TDpePm': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_l6KSYplEfW38j4vZRcLW6oC2': [{'avg_vol': '9.845238095238095', 'cnt': '168'}], 'var_call_6QNSUsKAKb81MII6T88RxsVD': [{'avg_vol': '254397.62845849802', 'cnt': '253'}], 'var_call_Xe96N1xzXkHYUmgsFfFUzcf1': [{'avg_vol': '10.276679841897232', 'cnt': '253'}], 'var_call_okeAlrjlbyEurQlsvDAICEbg': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_CV7TMR6fftfl9GG5tzqFvjEU': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_MGnbwSN654JOaXRI1Cw9Wdhn': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_pBHO7B8aZqeTQVzLVVEzapWy': [{'avg_vol': '254.1501976284585', 'cnt': '253'}], 'var_call_hW6eWuWO7X9zShfPHRKkdjBG': [{'avg_vol': '10706.719367588932', 'cnt': '253'}], 'var_call_lcbJaaJQx20xivgCPNI53YrD': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_Sfq9vTSID5LU9mBrvi6X5kFn': [{'avg_vol': '2390.513833992095', 'cnt': '253'}], 'var_call_nlTcX1Ix7GbqD0WdwIRNGIyu': [{'avg_vol': '781.8181818181819', 'cnt': '253'}], 'var_call_oRtnMtBAdQGXidGFrx44aYYA': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_lQ4DghdH4qRgapGK0BOSrHRS': [{'avg_vol': '36836.36363636364', 'cnt': '253'}], 'var_call_ve6PZPEgJ1bktPX93w8SVKVr': [{'avg_vol': 'nan', 'cnt': '0'}]}

exec(code, env_args)
