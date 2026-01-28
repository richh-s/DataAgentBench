code = """import json
# load stockinfo records
stockinfo = var_call_yA9AGDnW3RqoWSIU9WoyuYyZ
# mapping symbol to the corresponding avg result variable
avg_map = {
    'AGMH': var_call_tBNvdcD7KpBX7203UzgfMi3E,
    'AMTX': var_call_WA4vdhUb1idnjGhhpwbiCyzS,
    'APEX': var_call_d4mQEG3tCAdr9r3ZHrujYSim,
    'BIOC': var_call_0bTc7uiSeAag0TadnJciOELO,
    'BKYI': var_call_FTsg7PsLSYcRWL8etNIzhgWd,
    'CBAT': var_call_Rmvz81FkteyNZyKop69TcDh2,
    'CCCL': var_call_q1EwsUSLPhhERyuadjkK0tJt,
    'CORV': var_call_HlyC7cZTyFvwEgDyB31hMZN8,
    'CPAH': var_call_7Xpf8vwyJH7nLfSTcycq0Hbt,
    'DZSI': var_call_wZAh7qy75u8MHQwDH9kL60LL,
    'FAMI': var_call_5XMGmj64SSsmbrFHL9NvEQDv,
    'FTFT': var_call_gB4mkGcZdgAWlFGwdJ3eKj1H,
    'FTR': var_call_LBarPsfZOKSiXaiKD1qbjKdj,
    'IDEX': var_call_h0iov3qIdH9y4htnhiC4JOUI,
    'ISDS': var_call_57AM5KjP9wI9hfOI49qUw5Ma,
    'MCEP': var_call_4cqTvq1vrLfyLZ5jt9F0bOBS,
    'NXTD': var_call_ECakwrox7uzzPzjj4d9ulApy,
    'OPTT': var_call_SR6Qf5ZycrmwlqavRSQnJNcn,
    'PEIX': var_call_qeRXhBhgyKn4OPjBriVgqrgb,
    'RBZ': var_call_3Ux60Wq1ONbbzmMNVh1RTPkq,
    'SES': var_call_BeI1L4vSj1EtuHMf1XJeRuWE,
    'SNSS': var_call_CjMTYLi3YnvjxXedWImItRaR,
    'SPI': var_call_TcjU8UFV40mEqhigJOYKFh3N,
    'SYPR': var_call_xNyKuAiwBRsEGwiQvLbJJJ6v,
    'VTIQW': var_call_cVq8PahVSNhwDW7oI98cvdW5,
}
# build symbol -> company description from stockinfo
sym_to_desc = {r['Symbol']: r.get('Company Description') for r in stockinfo}
results = []
for sym, rec in avg_map.items():
    # each rec is a list like [{"avg_vol": "nan"}] or numeric string
    if not isinstance(rec, list) or len(rec) == 0:
        continue
    val = rec[0].get('avg_vol')
    # filter out NaN or None
    try:
        if val is None:
            continue
        # val may be a string 'nan' or numeric string
        f = float(val)
        if f != f:  # NaN check
            continue
    except Exception:
        continue
    desc = sym_to_desc.get(sym)
    results.append({'Symbol': sym, 'Company Description': desc, 'avg_vol_2008': f})
# sort results by Symbol
results = sorted(results, key=lambda x: x['Symbol'])
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_yA9AGDnW3RqoWSIU9WoyuYyZ': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Market Category': 'S', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Market Category': 'S', 'Financial Status': 'D'}], 'var_call_tBNvdcD7KpBX7203UzgfMi3E': [{'avg_vol': 'nan'}], 'var_call_WA4vdhUb1idnjGhhpwbiCyzS': [{'avg_vol': 'nan'}], 'var_call_d4mQEG3tCAdr9r3ZHrujYSim': [{'avg_vol': '23781.422924901184'}], 'var_call_0bTc7uiSeAag0TadnJciOELO': [{'avg_vol': 'nan'}], 'var_call_FTsg7PsLSYcRWL8etNIzhgWd': [{'avg_vol': '10988.142292490118'}], 'var_call_Rmvz81FkteyNZyKop69TcDh2': [{'avg_vol': '86223.32015810277'}], 'var_call_q1EwsUSLPhhERyuadjkK0tJt': [{'avg_vol': '4366.798418972332'}], 'var_call_HlyC7cZTyFvwEgDyB31hMZN8': [{'avg_vol': '145247.8260869565'}], 'var_call_7Xpf8vwyJH7nLfSTcycq0Hbt': [{'avg_vol': '375.49407114624506'}], 'var_call_wZAh7qy75u8MHQwDH9kL60LL': [{'avg_vol': '15578.656126482214'}], 'var_call_5XMGmj64SSsmbrFHL9NvEQDv': [{'avg_vol': 'nan'}], 'var_call_gB4mkGcZdgAWlFGwdJ3eKj1H': [{'avg_vol': '9.845238095238095'}], 'var_call_LBarPsfZOKSiXaiKD1qbjKdj': [{'avg_vol': '254397.62845849802'}], 'var_call_h0iov3qIdH9y4htnhiC4JOUI': [{'avg_vol': '10.276679841897232'}], 'var_call_57AM5KjP9wI9hfOI49qUw5Ma': [{'avg_vol': 'nan'}], 'var_call_4cqTvq1vrLfyLZ5jt9F0bOBS': [{'avg_vol': 'nan'}], 'var_call_ECakwrox7uzzPzjj4d9ulApy': [{'avg_vol': 'nan'}], 'var_call_SR6Qf5ZycrmwlqavRSQnJNcn': [{'avg_vol': '254.1501976284585'}], 'var_call_qeRXhBhgyKn4OPjBriVgqrgb': [{'avg_vol': '10706.719367588932'}], 'var_call_3Ux60Wq1ONbbzmMNVh1RTPkq': [{'avg_vol': 'nan'}], 'var_call_BeI1L4vSj1EtuHMf1XJeRuWE': [{'avg_vol': '2390.513833992095'}], 'var_call_CjMTYLi3YnvjxXedWImItRaR': [{'avg_vol': '781.8181818181819'}], 'var_call_TcjU8UFV40mEqhigJOYKFh3N': [{'avg_vol': 'nan'}], 'var_call_xNyKuAiwBRsEGwiQvLbJJJ6v': [{'avg_vol': '36836.36363636364'}], 'var_call_cVq8PahVSNhwDW7oI98cvdW5': [{'avg_vol': 'nan'}]}

exec(code, env_args)
