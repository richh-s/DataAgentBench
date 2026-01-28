code = """import json, math
# stock info
info = var_call_vMc2iXxRYlxwCrGmsWPRPJqG
# results for each symbol in the same order as info
results = [
    var_call_U5Mx4I2jSYDA26lnAylAUUfJ,
    var_call_mwohzLfgNOi352GYudYHSbN5,
    var_call_GzY60VlyDHMVif1dxEC45a5E,
    var_call_Wz3ih9fZV1XuGTrTb0VZVuO7,
    var_call_VnwVeJcGmopTPkAFrvImMpc4,
    var_call_4CQnNLMgBaaKvDAJlMd85oop,
    var_call_CXeUmm1GzBs55HkMO7evAtW7,
    var_call_Rtin8wLTPnFOYwFRsdFD6xXm,
    var_call_4aYDYm9tuUz8OcB1aO7vbM7c,
    var_call_qNpBtewJruguDIM4Hhi3Li2C,
    var_call_0t33RhQEw5imZrYCujYPwgPc,
    var_call_2mafqQh64nAhk5bZMeg0h9MR,
    var_call_vd3xl7BumdhqDbYfEoYH2qyy,
    var_call_Bda5aVECYQ912zW4Llj3txbq,
    var_call_0SD4LHdmvQUec0iTXuEZBtu7,
    var_call_3SiYtW5GcjEK5ik5V0Ad1XOU,
    var_call_bPL0jk16cZSK1HwDFl2kqafd,
    var_call_gD5rYLrk78zUsTVOhRl2nMRb,
    var_call_YfIf7p8hwE4nNL4NBDgy3OOD,
    var_call_krK1LcaIo7Zx4iaWXi9xZW8C,
    var_call_ZwHcHe4BQsjpMGYK1W0JRjaw,
    var_call_BIWAOXKLMdfk4AanLf8PkYzf,
    var_call_uVi3zTMdlwMCJsCrg8vZ6iuj,
    var_call_ze0dlPPYUhPNhVRNHSHJLPYa,
    var_call_UaD2cvqDyX3llfcapJDIDFOo,
]

output = []
for i, rec in enumerate(info):
    symbol = rec.get('symbol')
    company = rec.get('company')
    res_list = results[i]
    # each res_list is expected to be a list with one dict
    if not res_list:
        continue
    res = res_list[0]
    avg_raw = res.get('avg_volume')
    cnt_raw = res.get('cnt')
    # parse cnt
    try:
        cnt = int(cnt_raw)
    except Exception:
        try:
            cnt = int(float(cnt_raw))
        except Exception:
            cnt = 0
    # parse avg
    avg = None
    try:
        avg = float(avg_raw)
        if math.isnan(avg):
            avg = None
    except Exception:
        avg = None
    if cnt > 0 and avg is not None:
        output.append({
            'symbol': symbol,
            'company': company,
            'avg_daily_volume_2008': avg
        })

result_str = json.dumps(output)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_vMc2iXxRYlxwCrGmsWPRPJqG': [{'symbol': 'AGMH', 'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'fin_status': 'D'}, {'symbol': 'AMTX', 'company': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'fin_status': 'D'}, {'symbol': 'APEX', 'company': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'fin_status': 'D'}, {'symbol': 'BIOC', 'company': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'fin_status': 'D'}, {'symbol': 'BKYI', 'company': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'fin_status': 'D'}, {'symbol': 'CBAT', 'company': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'fin_status': 'D'}, {'symbol': 'CCCL', 'company': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'fin_status': 'D'}, {'symbol': 'CORV', 'company': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'fin_status': 'D'}, {'symbol': 'CPAH', 'company': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'fin_status': 'D'}, {'symbol': 'DZSI', 'company': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'fin_status': 'D'}, {'symbol': 'FAMI', 'company': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'fin_status': 'D'}, {'symbol': 'FTFT', 'company': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'fin_status': 'D'}, {'symbol': 'FTR', 'company': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'fin_status': 'D'}, {'symbol': 'IDEX', 'company': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'fin_status': 'D'}, {'symbol': 'ISDS', 'company': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'fin_status': 'D'}, {'symbol': 'MCEP', 'company': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'fin_status': 'D'}, {'symbol': 'NXTD', 'company': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'fin_status': 'D'}, {'symbol': 'OPTT', 'company': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'fin_status': 'D'}, {'symbol': 'PEIX', 'company': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'fin_status': 'D'}, {'symbol': 'RBZ', 'company': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'fin_status': 'D'}, {'symbol': 'SES', 'company': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'fin_status': 'H'}, {'symbol': 'SNSS', 'company': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'fin_status': 'D'}, {'symbol': 'SPI', 'company': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'fin_status': 'D'}, {'symbol': 'SYPR', 'company': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'fin_status': 'D'}, {'symbol': 'VTIQW', 'company': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'fin_status': 'D'}], 'var_call_U5Mx4I2jSYDA26lnAylAUUfJ': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_mwohzLfgNOi352GYudYHSbN5': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_GzY60VlyDHMVif1dxEC45a5E': [{'avg_volume': '23781.422924901184', 'cnt': '253'}], 'var_call_Wz3ih9fZV1XuGTrTb0VZVuO7': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_VnwVeJcGmopTPkAFrvImMpc4': [{'avg_volume': '10988.142292490118', 'cnt': '253'}], 'var_call_4CQnNLMgBaaKvDAJlMd85oop': [{'avg_volume': '86223.32015810277', 'cnt': '253'}], 'var_call_CXeUmm1GzBs55HkMO7evAtW7': [{'avg_volume': '4366.798418972332', 'cnt': '253'}], 'var_call_Rtin8wLTPnFOYwFRsdFD6xXm': [{'avg_volume': '145247.8260869565', 'cnt': '253'}], 'var_call_4aYDYm9tuUz8OcB1aO7vbM7c': [{'avg_volume': '375.49407114624506', 'cnt': '253'}], 'var_call_qNpBtewJruguDIM4Hhi3Li2C': [{'avg_volume': '15578.656126482214', 'cnt': '253'}], 'var_call_0t33RhQEw5imZrYCujYPwgPc': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_2mafqQh64nAhk5bZMeg0h9MR': [{'avg_volume': '9.845238095238095', 'cnt': '168'}], 'var_call_vd3xl7BumdhqDbYfEoYH2qyy': [{'avg_volume': '254397.62845849802', 'cnt': '253'}], 'var_call_Bda5aVECYQ912zW4Llj3txbq': [{'avg_volume': '10.276679841897232', 'cnt': '253'}], 'var_call_0SD4LHdmvQUec0iTXuEZBtu7': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_3SiYtW5GcjEK5ik5V0Ad1XOU': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_bPL0jk16cZSK1HwDFl2kqafd': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_gD5rYLrk78zUsTVOhRl2nMRb': [{'avg_volume': '254.1501976284585', 'cnt': '253'}], 'var_call_YfIf7p8hwE4nNL4NBDgy3OOD': [{'avg_volume': '10706.719367588932', 'cnt': '253'}], 'var_call_krK1LcaIo7Zx4iaWXi9xZW8C': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_ZwHcHe4BQsjpMGYK1W0JRjaw': [{'avg_volume': '2390.513833992095', 'cnt': '253'}], 'var_call_BIWAOXKLMdfk4AanLf8PkYzf': [{'avg_volume': '781.8181818181819', 'cnt': '253'}], 'var_call_uVi3zTMdlwMCJsCrg8vZ6iuj': [{'avg_volume': 'nan', 'cnt': '0'}], 'var_call_ze0dlPPYUhPNhVRNHSHJLPYa': [{'avg_volume': '36836.36363636364', 'cnt': '253'}], 'var_call_UaD2cvqDyX3llfcapJDIDFOo': [{'avg_volume': 'nan', 'cnt': '0'}]}

exec(code, env_args)
