code = """import json
import math
# stockinfo results
stockinfo = var_call_dxsHuS2NZqbzhfy0ZHPrzbFH
# Mapping of symbol to company description
sym_to_name = {r['Symbol']: r['Company Description'] for r in stockinfo}
# Mapping of queried symbols to their corresponding result variable names
results_map = {
    'AGMH': var_call_5vWePkixlWBnsPYtauCPqgFc,
    'AMTX': var_call_THJQgZTqttIYSz6QzubamEsa,
    'APEX': var_call_MAbFPtKqNtRZUhdHHaaknxOr,
    'BIOC': var_call_E5Rj7UiRnLVciQiwjoQsWqmu,
    'BKYI': var_call_8FOOYKM7A2khVNdKbPZvPUqx,
    'CBAT': var_call_RcxJLfNpRNP84SBZDTgD9wLg,
    'CCCL': var_call_WTFRkkNbb8eu8cHwlrPTDNEK,
    'CORV': var_call_NLxTMoNNfejjEcT8oMIJVYby,
    'CPAH': var_call_AUvO4wbFBxHoka95LW87Lav7,
    'DZSI': var_call_Jy6eSGXXL8jxXKHlIIrqWaq9,
    'FAMI': var_call_qcMhSLbwLtpZS8F61zQtbFHW,
    'FTFT': var_call_YYE7MO87CvozJ44PfjPi63Pr,
    'FTR': var_call_6AAW7Yf9EregkMDp2IfYdptK,
    'IDEX': var_call_M4rg3br6ZEmPX8sPIEujn2JV,
    'ISDS': var_call_cf8JOOcIdwzFUg201nTVZTeh,
    'MCEP': var_call_MexpuAypGepViIPnFHpM4CyT,
    'NXTD': var_call_Z9HZkltJxMBBlZEN4RtKyDZw,
    'OPTT': var_call_pCIDW2NsQNyZrYsO5qWzcUbX,
    'PEIX': var_call_np7wuS1DhyLe8MRkpr2RnwMa,
    'RBZ': var_call_VseaIl4exTlQcl0jVePDFVq0,
    'SNSS': var_call_mHb0pPmVSBETRllEoS71hgqm,
    'SPI': var_call_qUSktrrkaNBi68Gkk0fYEmPR,
    'SYPR': var_call_M3WCxaHNLKiDBXQIBoBuSqN4,
    'VTIQW': var_call_nJOpN03yzQxntTLY7r89hivK
}

output = []
for sym, res in results_map.items():
    # Each res is a list with one dict
    if not isinstance(res, list) or len(res) == 0:
        continue
    entry = res[0]
    avg = entry.get('avg_vol')
    cnt = entry.get('count_vol')
    # treat strings
    try:
        cnt_val = int(cnt)
    except Exception:
        try:
            cnt_val = int(float(cnt))
        except Exception:
            cnt_val = 0
    # include only if there is trading volume (count>0) and avg not nan
    include = cnt_val > 0 and avg is not None and str(avg).lower() != 'nan'
    if include:
        try:
            avg_val = float(avg)
        except Exception:
            avg_val = None
        if avg_val is not None and not math.isnan(avg_val):
            name = sym_to_name.get(sym, sym)
            output.append({
                'Symbol': sym,
                'Company Description': name,
                'Average Daily Volume 2008': avg_val
            })

# Sort output by Symbol
output = sorted(output, key=lambda x: x['Symbol'])

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_dxsHuS2NZqbzhfy0ZHPrzbFH': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_6pk3Je4OUnSoUx2WxCuJFUQV': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_5vWePkixlWBnsPYtauCPqgFc': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_THJQgZTqttIYSz6QzubamEsa': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_MAbFPtKqNtRZUhdHHaaknxOr': [{'avg_vol': '23781.422924901184', 'count_vol': '253'}], 'var_call_E5Rj7UiRnLVciQiwjoQsWqmu': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_8FOOYKM7A2khVNdKbPZvPUqx': [{'avg_vol': '10988.142292490118', 'count_vol': '253'}], 'var_call_RcxJLfNpRNP84SBZDTgD9wLg': [{'avg_vol': '86223.32015810277', 'count_vol': '253'}], 'var_call_WTFRkkNbb8eu8cHwlrPTDNEK': [{'avg_vol': '4366.798418972332', 'count_vol': '253'}], 'var_call_NLxTMoNNfejjEcT8oMIJVYby': [{'avg_vol': '145247.8260869565', 'count_vol': '253'}], 'var_call_AUvO4wbFBxHoka95LW87Lav7': [{'avg_vol': '375.49407114624506', 'count_vol': '253'}], 'var_call_Jy6eSGXXL8jxXKHlIIrqWaq9': [{'avg_vol': '15578.656126482214', 'count_vol': '253'}], 'var_call_qcMhSLbwLtpZS8F61zQtbFHW': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_YYE7MO87CvozJ44PfjPi63Pr': [{'avg_vol': '9.845238095238095', 'count_vol': '168'}], 'var_call_6AAW7Yf9EregkMDp2IfYdptK': [{'avg_vol': '254397.62845849802', 'count_vol': '253'}], 'var_call_M4rg3br6ZEmPX8sPIEujn2JV': [{'avg_vol': '10.276679841897232', 'count_vol': '253'}], 'var_call_cf8JOOcIdwzFUg201nTVZTeh': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_MexpuAypGepViIPnFHpM4CyT': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_Z9HZkltJxMBBlZEN4RtKyDZw': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_pCIDW2NsQNyZrYsO5qWzcUbX': [{'avg_vol': '254.1501976284585', 'count_vol': '253'}], 'var_call_np7wuS1DhyLe8MRkpr2RnwMa': [{'avg_vol': '10706.719367588932', 'count_vol': '253'}], 'var_call_VseaIl4exTlQcl0jVePDFVq0': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_mHb0pPmVSBETRllEoS71hgqm': [{'avg_vol': '781.8181818181819', 'count_vol': '253'}], 'var_call_qUSktrrkaNBi68Gkk0fYEmPR': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_M3WCxaHNLKiDBXQIBoBuSqN4': [{'avg_vol': '36836.36363636364', 'count_vol': '253'}], 'var_call_nJOpN03yzQxntTLY7r89hivK': [{'avg_vol': 'nan', 'count_vol': '0'}]}

exec(code, env_args)
