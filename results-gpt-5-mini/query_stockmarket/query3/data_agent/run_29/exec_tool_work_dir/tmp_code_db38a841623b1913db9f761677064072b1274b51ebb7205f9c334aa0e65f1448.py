code = """import math
import json
# Load the query results
stock_info = var_call_Ao75WkiFuh7nXwEZyOasgK8c
avg_vars = [
    var_call_Kpo4GfGtdyHvexRG4jtVVQiD,
    var_call_QGBFAg3dgfUi5zDzqNlKQHDg,
    var_call_Pi9NKObNuqPJCbrKZgmVuMTQ,
    var_call_bGX4lXKCujNrYXjPEftslGXi,
    var_call_wmmh082yto2iu5W5vfPfz914,
    var_call_LwevdqiefanlouFfdz385cmr,
    var_call_6VqIa4DgaMDCk4GbaGINH5V8,
    var_call_lklJU9Cnw8vv9ivPCdlG9Q0H,
    var_call_51NOxMlVe9m5fL0yhR6pxKse,
    var_call_qRZlYyT7DkkPILXtt67rtLpY,
    var_call_ibKkMz2NWbNnAvHkmb86g6mA,
    var_call_CX7wtQYZejKIYw7ESkwVju0d,
    var_call_6GuakQgnbmGnsVBP2R1bjFOO,
    var_call_201DFQjL6j571MZXFSIyinhG,
    var_call_7nt6l4t8UZ6c140gRigZZ18l,
    var_call_qqV9nrLc6OdgyK3v9nViZB0a,
    var_call_pYgJrqQ2xiF2SeWY61NKQE7l,
    var_call_bG2zblpBv1p6CmW98e5otEnt,
    var_call_2eh5zIXJIzkbKosKoWkDdlGc,
    var_call_j7DobXLOVF1d0OrWJAsqf985,
    var_call_jd9jnc2vZrHhzZZkB9ba78SG,
    var_call_GVGFUNMciP4qzFAkC0ZpKJhx,
    var_call_wV2aREcVdJzYk0GQG3P9eSPI,
    var_call_EhRvkXiLWm0pyQg55eJVacJb,
]
# Extract avg volumes as floats (or None)
avg_list = []
for item in avg_vars:
    # each is a list with one dict {'avg_volume': '...'}
    if not item or not isinstance(item, list) or len(item) == 0:
        avg_list.append(None)
        continue
    val = item[0].get('avg_volume')
    try:
        f = float(val)
        if math.isnan(f):
            avg_list.append(None)
        else:
            avg_list.append(f)
    except Exception:
        avg_list.append(None)

# Combine with stock_info entries
results = []
for i, info in enumerate(stock_info):
    symbol = info.get('Symbol')
    company = info.get('Company Description')
    avg = avg_list[i] if i < len(avg_list) else None
    if avg is not None:
        results.append({
            'Symbol': symbol,
            'Company Description': company,
            'avg_volume_2008': avg
        })

# Print result as JSON string per required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_Ao75WkiFuh7nXwEZyOasgK8c': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G', 'ETF': 'N'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q', 'ETF': 'N'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G', 'ETF': 'N'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q', 'ETF': 'N'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G', 'ETF': 'N'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S', 'ETF': 'N'}], 'var_call_Kpo4GfGtdyHvexRG4jtVVQiD': [{'avg_volume': 'nan'}], 'var_call_QGBFAg3dgfUi5zDzqNlKQHDg': [{'avg_volume': 'nan'}], 'var_call_Pi9NKObNuqPJCbrKZgmVuMTQ': [{'avg_volume': '23781.422924901184'}], 'var_call_bGX4lXKCujNrYXjPEftslGXi': [{'avg_volume': 'nan'}], 'var_call_wmmh082yto2iu5W5vfPfz914': [{'avg_volume': '10988.142292490118'}], 'var_call_LwevdqiefanlouFfdz385cmr': [{'avg_volume': '86223.32015810277'}], 'var_call_6VqIa4DgaMDCk4GbaGINH5V8': [{'avg_volume': '4366.798418972332'}], 'var_call_lklJU9Cnw8vv9ivPCdlG9Q0H': [{'avg_volume': '145247.8260869565'}], 'var_call_51NOxMlVe9m5fL0yhR6pxKse': [{'avg_volume': '375.49407114624506'}], 'var_call_qRZlYyT7DkkPILXtt67rtLpY': [{'avg_volume': '15578.656126482214'}], 'var_call_ibKkMz2NWbNnAvHkmb86g6mA': [{'avg_volume': 'nan'}], 'var_call_CX7wtQYZejKIYw7ESkwVju0d': [{'avg_volume': '9.845238095238095'}], 'var_call_6GuakQgnbmGnsVBP2R1bjFOO': [{'avg_volume': '254397.62845849802'}], 'var_call_201DFQjL6j571MZXFSIyinhG': [{'avg_volume': '10.276679841897232'}], 'var_call_7nt6l4t8UZ6c140gRigZZ18l': [{'avg_volume': 'nan'}], 'var_call_qqV9nrLc6OdgyK3v9nViZB0a': [{'avg_volume': 'nan'}], 'var_call_pYgJrqQ2xiF2SeWY61NKQE7l': [{'avg_volume': '254.1501976284585'}], 'var_call_bG2zblpBv1p6CmW98e5otEnt': [{'avg_volume': '10706.719367588932'}], 'var_call_2eh5zIXJIzkbKosKoWkDdlGc': [{'avg_volume': 'nan'}], 'var_call_j7DobXLOVF1d0OrWJAsqf985': [{'avg_volume': '2390.513833992095'}], 'var_call_jd9jnc2vZrHhzZZkB9ba78SG': [{'avg_volume': '781.8181818181819'}], 'var_call_GVGFUNMciP4qzFAkC0ZpKJhx': [{'avg_volume': 'nan'}], 'var_call_wV2aREcVdJzYk0GQG3P9eSPI': [{'avg_volume': '36836.36363636364'}], 'var_call_EhRvkXiLWm0pyQg55eJVacJb': [{'avg_volume': 'nan'}]}

exec(code, env_args)
