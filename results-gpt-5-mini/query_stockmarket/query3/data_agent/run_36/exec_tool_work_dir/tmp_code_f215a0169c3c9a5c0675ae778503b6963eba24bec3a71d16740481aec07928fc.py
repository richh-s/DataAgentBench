code = """import json
# load stockinfo query result
stockinfo = var_call_C9CUIdq6GjQ9Oj7phVSJjUVp
# load trade avg results in the same order as stockinfo entries
results = [var_call_ePFjCON7G4Zu5GvGvi9lkHXG,
           var_call_a26ZiR8fVj4LezMKUiuc5YM8,
           var_call_dt1yM34dqY1ydjQFZYExap5Z,
           var_call_FgrfeALUhNqCZB6rumXS4zkC,
           var_call_ndoEQg27hK1hUZFpqF6O5kMD,
           var_call_DdmZQn0JhtMJhug763DoD1JQ,
           var_call_kcyriKujU1l7zjiXrU6mSbA2,
           var_call_RWHWBmpVsD8zzWfMG4JcRoro,
           var_call_o4QdZGTba334HQYFWV5excUd,
           var_call_9tbsyI4VY71MICpEX2pwRkqA,
           var_call_NPKXRYMVGVEvblqigyoGTk4v,
           var_call_AK2FJioz9aozdOHkXI2esx6X,
           var_call_4oBeXh1zuV7v70hVPA5tXWc1,
           var_call_VyfO1VG9007zf0x6GjeSXBlI,
           var_call_Ju53TX43vS8uLznXlGYPpglN,
           var_call_xze2epxfLbfqmfsWG2t3vPGX,
           var_call_qBjG5efFwrTePNa6WqUUtnzf,
           var_call_eA5Qe5xEMsUggLpw8hWRezYJ,
           var_call_LgNEsnhVwt48ViaHsCXCw8Y6,
           var_call_zteoF7lKw3HTHanzRQnTmREP,
           var_call_mJsG2AseKdFIKt6V3MsJLovJ,
           var_call_m8ghwwBcShjrSitSFVJCkVS0,
           var_call_qcoxu8444LfzwHLWK22QVPWx,
           var_call_gmyQs1SKSKy4LxoFdM9Dq2o4,
           var_call_Vuu1op8uDlhCCr3amTYB2g2R]

output = []
for si, res in zip(stockinfo, results):
    sym = si.get('Symbol')
    name = si.get('Company Description')
    # res is a list with one dict
    r = res[0]
    avg = r.get('avg_vol')
    cnt = r.get('cnt')
    # Exclude if count is '0' or avg is 'nan'
    try:
        has_data = int(cnt) > 0
    except Exception:
        has_data = False
    if not has_data:
        continue
    try:
        avg_f = float(avg)
        if avg_f != avg_f:  # check nan
            continue
    except Exception:
        continue
    output.append({
        'Symbol': sym,
        'Company Description': name,
        'Average Daily Volume 2008': avg_f
    })

# produce JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_C9CUIdq6GjQ9Oj7phVSJjUVp': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Market Category': 'S', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Market Category': 'S', 'Financial Status': 'D'}], 'var_call_OBxWB21n8XWssVlxplx9pr4S': 'file_storage/call_OBxWB21n8XWssVlxplx9pr4S.json', 'var_call_ePFjCON7G4Zu5GvGvi9lkHXG': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_a26ZiR8fVj4LezMKUiuc5YM8': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_dt1yM34dqY1ydjQFZYExap5Z': [{'avg_vol': '23781.422924901184', 'cnt': '253'}], 'var_call_FgrfeALUhNqCZB6rumXS4zkC': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_ndoEQg27hK1hUZFpqF6O5kMD': [{'avg_vol': '10988.142292490118', 'cnt': '253'}], 'var_call_DdmZQn0JhtMJhug763DoD1JQ': [{'avg_vol': '86223.32015810277', 'cnt': '253'}], 'var_call_kcyriKujU1l7zjiXrU6mSbA2': [{'avg_vol': '4366.798418972332', 'cnt': '253'}], 'var_call_RWHWBmpVsD8zzWfMG4JcRoro': [{'avg_vol': '145247.8260869565', 'cnt': '253'}], 'var_call_o4QdZGTba334HQYFWV5excUd': [{'avg_vol': '375.49407114624506', 'cnt': '253'}], 'var_call_9tbsyI4VY71MICpEX2pwRkqA': [{'avg_vol': '15578.656126482214', 'cnt': '253'}], 'var_call_NPKXRYMVGVEvblqigyoGTk4v': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_AK2FJioz9aozdOHkXI2esx6X': [{'avg_vol': '9.845238095238095', 'cnt': '168'}], 'var_call_4oBeXh1zuV7v70hVPA5tXWc1': [{'avg_vol': '254397.62845849802', 'cnt': '253'}], 'var_call_VyfO1VG9007zf0x6GjeSXBlI': [{'avg_vol': '10.276679841897232', 'cnt': '253'}], 'var_call_Ju53TX43vS8uLznXlGYPpglN': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_xze2epxfLbfqmfsWG2t3vPGX': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_qBjG5efFwrTePNa6WqUUtnzf': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_eA5Qe5xEMsUggLpw8hWRezYJ': [{'avg_vol': '254.1501976284585', 'cnt': '253'}], 'var_call_LgNEsnhVwt48ViaHsCXCw8Y6': [{'avg_vol': '10706.719367588932', 'cnt': '253'}], 'var_call_zteoF7lKw3HTHanzRQnTmREP': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_mJsG2AseKdFIKt6V3MsJLovJ': [{'avg_vol': '2390.513833992095', 'cnt': '253'}], 'var_call_m8ghwwBcShjrSitSFVJCkVS0': [{'avg_vol': '781.8181818181819', 'cnt': '253'}], 'var_call_qcoxu8444LfzwHLWK22QVPWx': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_gmyQs1SKSKy4LxoFdM9Dq2o4': [{'avg_vol': '36836.36363636364', 'cnt': '253'}], 'var_call_Vuu1op8uDlhCCr3amTYB2g2R': [{'avg_vol': 'nan', 'cnt': '0'}]}

exec(code, env_args)
