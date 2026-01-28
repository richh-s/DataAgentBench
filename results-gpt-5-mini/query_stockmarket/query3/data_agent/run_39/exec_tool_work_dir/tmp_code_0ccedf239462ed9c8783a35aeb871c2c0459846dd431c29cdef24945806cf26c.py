code = """import json
import math
# stockinfo records
stockinfo = var_call_OrLY2JHc1WMEKrOTOEAZEHUK
# Map symbol to company description
comp_map = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}
# Mapping of symbol to the corresponding avg_volume result variable
mapping = [
    ('AGMH', var_call_zv4nySDbqUpMnmo4BSZsEmHl),
    ('AMTX', var_call_a2VrXbAX33S3Dxi92kMAA85h),
    ('APEX', var_call_ScAUDSFi8a7LdgGXNcz6uwKc),
    ('BIOC', var_call_kTRh2aA9K9qVn4lqPuHblM9r),
    ('BKYI', var_call_pva0laJF6faVW1dw4PSd8heA),
    ('CBAT', var_call_TJl7xXR8wklpgoSSVeTztVJz),
    ('CCCL', var_call_FlYIhi8HbHVfdDmHDtZgpEtP),
    ('CORV', var_call_9jyJEgH4Xk47J3qTZYu18xej),
    ('CPAH', var_call_duMvgfLFr5Uborw7GMjL68XD),
    ('DZSI', var_call_GXPH8VgP2qMAnk3Z1XjwYW7t),
    ('FAMI', var_call_ghJraV5Lf0rm8PTgROiKKYQP),
    ('FTFT', var_call_JY0FK7bMGhaCEUrdlMNVT480),
    ('FTR', var_call_WYnRuxWQLhI3eYOmt4l6W5pw),
    ('IDEX', var_call_bf5kZPGb83qYlwrYYY9oywvM),
    ('ISDS', var_call_IB1vfJEkB84mTWEe72HsMeqM),
    ('MCEP', var_call_JAo2FJZqgo39dij9w4hQAouX),
    ('NXTD', var_call_Qq3zL0tcRJYEzafvBbPICBxP),
    ('OPTT', var_call_SwFcUNyWu05tivHdLOXcKQmP),
    ('PEIX', var_call_EHQezlEoRndlcQhm3wgns1sh),
    ('RBZ', var_call_CXEaZVbzT4qQY9BF7PpbOwXo),
    ('SES', var_call_WSqps2mhVt68gQaSRKAGOg13),
    ('SNSS', var_call_YBblpSeb0ZrgrFuqT5IRx59H),
    ('SPI', var_call_BMt0KsAkLs1pTt9FntsaaS3z),
    ('SYPR', var_call_awGvMdIXMuMOJvsMDMRJVnKb),
    ('VTIQW', var_call_IhLxbEu3bewbGLvNVB1zd1A6)
]

results = []
for sym, var in mapping:
    try:
        rec = var[0]
        raw = rec.get('avg_volume')
        # convert to float if possible
        val = float(raw)
        if math.isnan(val):
            continue
        # include only if company is in comp_map
        comp = comp_map.get(sym, '')
        results.append({'Symbol': sym, 'Company Description': comp, 'avg_volume': val})
    except Exception:
        continue

# Sort results by Symbol for consistent ordering
results = sorted(results, key=lambda x: x['Symbol'])
output = json.dumps(results)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_OrLY2JHc1WMEKrOTOEAZEHUK': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Market Category': 'S', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Market Category': 'S', 'Financial Status': 'D'}], 'var_call_zv4nySDbqUpMnmo4BSZsEmHl': [{'avg_volume': 'nan'}], 'var_call_a2VrXbAX33S3Dxi92kMAA85h': [{'avg_volume': 'nan'}], 'var_call_ScAUDSFi8a7LdgGXNcz6uwKc': [{'avg_volume': '23781.422924901184'}], 'var_call_kTRh2aA9K9qVn4lqPuHblM9r': [{'avg_volume': 'nan'}], 'var_call_pva0laJF6faVW1dw4PSd8heA': [{'avg_volume': '10988.142292490118'}], 'var_call_TJl7xXR8wklpgoSSVeTztVJz': [{'avg_volume': '86223.32015810277'}], 'var_call_FlYIhi8HbHVfdDmHDtZgpEtP': [{'avg_volume': '4366.798418972332'}], 'var_call_9jyJEgH4Xk47J3qTZYu18xej': [{'avg_volume': '145247.8260869565'}], 'var_call_duMvgfLFr5Uborw7GMjL68XD': [{'avg_volume': '375.49407114624506'}], 'var_call_GXPH8VgP2qMAnk3Z1XjwYW7t': [{'avg_volume': '15578.656126482214'}], 'var_call_ghJraV5Lf0rm8PTgROiKKYQP': [{'avg_volume': 'nan'}], 'var_call_JY0FK7bMGhaCEUrdlMNVT480': [{'avg_volume': '9.845238095238095'}], 'var_call_WYnRuxWQLhI3eYOmt4l6W5pw': [{'avg_volume': '254397.62845849802'}], 'var_call_bf5kZPGb83qYlwrYYY9oywvM': [{'avg_volume': '10.276679841897232'}], 'var_call_IB1vfJEkB84mTWEe72HsMeqM': [{'avg_volume': 'nan'}], 'var_call_JAo2FJZqgo39dij9w4hQAouX': [{'avg_volume': 'nan'}], 'var_call_Qq3zL0tcRJYEzafvBbPICBxP': [{'avg_volume': 'nan'}], 'var_call_SwFcUNyWu05tivHdLOXcKQmP': [{'avg_volume': '254.1501976284585'}], 'var_call_EHQezlEoRndlcQhm3wgns1sh': [{'avg_volume': '10706.719367588932'}], 'var_call_CXEaZVbzT4qQY9BF7PpbOwXo': [{'avg_volume': 'nan'}], 'var_call_WSqps2mhVt68gQaSRKAGOg13': [{'avg_volume': '2390.513833992095'}], 'var_call_YBblpSeb0ZrgrFuqT5IRx59H': [{'avg_volume': '781.8181818181819'}], 'var_call_BMt0KsAkLs1pTt9FntsaaS3z': [{'avg_volume': 'nan'}], 'var_call_awGvMdIXMuMOJvsMDMRJVnKb': [{'avg_volume': '36836.36363636364'}], 'var_call_IhLxbEu3bewbGLvNVB1zd1A6': [{'avg_volume': 'nan'}]}

exec(code, env_args)
