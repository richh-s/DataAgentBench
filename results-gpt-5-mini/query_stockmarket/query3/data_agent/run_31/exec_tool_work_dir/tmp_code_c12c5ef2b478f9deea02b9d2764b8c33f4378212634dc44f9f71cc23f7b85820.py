code = """import json
import math
# stockinfo results
stock_info = var_call_EDX1M1PKrq9Dd5V756dSGtxm
# avg volume query results in the same order as stock_info symbols
avg_vars = [
    var_call_sfo2GrLUrpBl0FbC76XSbcdE,
    var_call_CGpGHECSEb2gEIe1NaPnXWkD,
    var_call_eP0ULKKFJlD06bbOOlnucTq0,
    var_call_3pcpL1oGZU4UqAuS2ih7cSA2,
    var_call_6hrjcL5acPQqOxLA7x9NTXzs,
    var_call_lPpLib48vTYhmcQMPUlTHXpv,
    var_call_bPNLQYLUdHcRFgQoN38wZYdJ,
    var_call_8d1sA3uU01BrWDLp3UbX7zAf,
    var_call_efil4ASF8zSvBWma5w4E8Xqj,
    var_call_flJLiq3rXfedPobrLj7LP8Sh,
    var_call_QBzEC6scKvKClMsFzJhPIaVJ,
    var_call_ftI6vYxZ7j9lKprZazQwby71,
    var_call_hgvhPDQGfanf7NxieRrrYyhx,
    var_call_pP06SC7NHyIgaoygTG5XvHBA,
    var_call_TQoK3s3kPt1TVIqZjqEtm7sC,
    var_call_PBBXq3lTo3SWGIyuuuEVsF8c,
    var_call_UoLvGgXv5Y8orabRwRcfEIKU,
    var_call_X3e51guQG0ACGv7Ni6RdhUuV,
    var_call_HH3FydqBJ98MFIpILunobVYY,
    var_call_oMU7hu9HN5rwnPhC4wYpHuRv,
    var_call_SLN96OL0deitetIrQltbBBCX,
    var_call_mp9mlBSKXpaMYCnecsrj1lv2,
    var_call_tf6qWi5evd5gIxS8zpiay86s,
    var_call_pQCbBFvbV1RX1gk2VRlkxrsU,
    var_call_iUfo4iUX4blzLRhVVxIamlHS,
]

results = []
for i, info in enumerate(stock_info):
    symbol = info.get('Symbol')
    company = info.get('Company Description')
    # each avg_vars entry is a list with one dict like {'avg_volume': '...'}
    avg_entry = avg_vars[i][0] if avg_vars[i] and len(avg_vars[i])>0 else None
    avg_raw = avg_entry.get('avg_volume') if avg_entry else None
    try:
        avg_val = float(avg_raw)
    except Exception:
        avg_val = float('nan')
    if not math.isnan(avg_val):
        results.append({'Company Name': company, 'Symbol': symbol, 'AvgDailyVolume2008': avg_val})

# produce JSON string
output = json.dumps(results)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_EDX1M1PKrq9Dd5V756dSGtxm': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_sfo2GrLUrpBl0FbC76XSbcdE': [{'avg_volume': 'nan'}], 'var_call_CGpGHECSEb2gEIe1NaPnXWkD': [{'avg_volume': 'nan'}], 'var_call_eP0ULKKFJlD06bbOOlnucTq0': [{'avg_volume': '23781.422924901184'}], 'var_call_3pcpL1oGZU4UqAuS2ih7cSA2': [{'avg_volume': 'nan'}], 'var_call_6hrjcL5acPQqOxLA7x9NTXzs': [{'avg_volume': '10988.142292490118'}], 'var_call_lPpLib48vTYhmcQMPUlTHXpv': [{'avg_volume': '86223.32015810277'}], 'var_call_bPNLQYLUdHcRFgQoN38wZYdJ': [{'avg_volume': '4366.798418972332'}], 'var_call_8d1sA3uU01BrWDLp3UbX7zAf': [{'avg_volume': '145247.8260869565'}], 'var_call_efil4ASF8zSvBWma5w4E8Xqj': [{'avg_volume': '375.49407114624506'}], 'var_call_flJLiq3rXfedPobrLj7LP8Sh': [{'avg_volume': '15578.656126482214'}], 'var_call_QBzEC6scKvKClMsFzJhPIaVJ': [{'avg_volume': 'nan'}], 'var_call_ftI6vYxZ7j9lKprZazQwby71': [{'avg_volume': '9.845238095238095'}], 'var_call_hgvhPDQGfanf7NxieRrrYyhx': [{'avg_volume': '254397.62845849802'}], 'var_call_pP06SC7NHyIgaoygTG5XvHBA': [{'avg_volume': '10.276679841897232'}], 'var_call_TQoK3s3kPt1TVIqZjqEtm7sC': [{'avg_volume': 'nan'}], 'var_call_PBBXq3lTo3SWGIyuuuEVsF8c': [{'avg_volume': 'nan'}], 'var_call_UoLvGgXv5Y8orabRwRcfEIKU': [{'avg_volume': 'nan'}], 'var_call_X3e51guQG0ACGv7Ni6RdhUuV': [{'avg_volume': '254.1501976284585'}], 'var_call_HH3FydqBJ98MFIpILunobVYY': [{'avg_volume': '10706.719367588932'}], 'var_call_oMU7hu9HN5rwnPhC4wYpHuRv': [{'avg_volume': 'nan'}], 'var_call_SLN96OL0deitetIrQltbBBCX': [{'avg_volume': '2390.513833992095'}], 'var_call_mp9mlBSKXpaMYCnecsrj1lv2': [{'avg_volume': '781.8181818181819'}], 'var_call_tf6qWi5evd5gIxS8zpiay86s': [{'avg_volume': 'nan'}], 'var_call_pQCbBFvbV1RX1gk2VRlkxrsU': [{'avg_volume': '36836.36363636364'}], 'var_call_iUfo4iUX4blzLRhVVxIamlHS': [{'avg_volume': 'nan'}]}

exec(code, env_args)
