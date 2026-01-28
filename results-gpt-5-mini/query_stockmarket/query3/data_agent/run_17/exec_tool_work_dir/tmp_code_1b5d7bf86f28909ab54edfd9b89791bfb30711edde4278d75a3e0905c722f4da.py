code = """import json
import math

stockinfo = var_call_7L4MB2O0hvibLbJwxkfTVLKx

avg_results_vars = [
    var_call_VFCJFIA0Vi3lb25Q5svWNiv2,
    var_call_zf5etAbAx9x61j8KCHFH6j5g,
    var_call_cLTCUlSzWEaLqmU9bJrV3vmD,
    var_call_YG3oAzna6KEIlpC4kDL5G4bx,
    var_call_XBWTfLS8EV6XcEW7AJ8moeIh,
    var_call_WaLtHaIb0q3SDCa15jb38pfE,
    var_call_V7fRuWxGKM9J6zO7zUCCwOzG,
    var_call_sWdoEVKFegoDcqolkOb4Welc,
    var_call_AiI72AVDqxzMCT0voDX9J1Gs,
    var_call_Nh4By1QbZsV8gdqMOHoriIXU,
    var_call_hOSoktiQLEzmqAZeypjUt8tb,
    var_call_emSKdpjm90P5Bd6DqyYNkffw,
    var_call_d2YeztirzhB0DwzRpXeEXeb1,
    var_call_ZqMUzTBgE6elMMqsSqllfS6b,
    var_call_ZHsNmVRxYOJ965DMKNeU668M,
    var_call_nAQuqDTrg0aykEwCYUozg4fg,
    var_call_RrdMgoNt1GKG4UqAiJ3VX7yi,
    var_call_YosVMQSEAKkIHg2ipFKTwflr,
    var_call_J0Pjn786WGM9pLzKAAkisxDh,
    var_call_cr7J4I23GY0h8zlWyM3edzkf,
    var_call_ixdbqBZikWg8Y1xIO9OFl7qW,
    var_call_TMqe1cVzZrJnf1o00qM97ypG,
    var_call_qHw3tH1dTuuExQuDh5pzY7Hb,
    var_call_Z1RxXZ827Qee7iudgUCqV3X5
]

results = []
for info, avg_var in zip(stockinfo, avg_results_vars):
    symbol = info.get('Symbol')
    comp_desc = info.get('Company Description')
    # avg_var is a list like [{"avg_vol": "..."}]
    if not avg_var or not isinstance(avg_var, list):
        continue
    val = avg_var[0].get('avg_vol')
    try:
        avg = float(val)
    except Exception:
        continue
    if math.isnan(avg):
        continue
    results.append({
        'Symbol': symbol,
        'Company Description': comp_desc,
        'Average Daily Volume 2008': avg
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_7L4MB2O0hvibLbJwxkfTVLKx': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_VFCJFIA0Vi3lb25Q5svWNiv2': [{'avg_vol': 'nan'}], 'var_call_zf5etAbAx9x61j8KCHFH6j5g': [{'avg_vol': 'nan'}], 'var_call_cLTCUlSzWEaLqmU9bJrV3vmD': [{'avg_vol': '23781.422924901184'}], 'var_call_YG3oAzna6KEIlpC4kDL5G4bx': [{'avg_vol': 'nan'}], 'var_call_XBWTfLS8EV6XcEW7AJ8moeIh': [{'avg_vol': '10988.142292490118'}], 'var_call_WaLtHaIb0q3SDCa15jb38pfE': [{'avg_vol': '86223.32015810277'}], 'var_call_V7fRuWxGKM9J6zO7zUCCwOzG': [{'avg_vol': '4366.798418972332'}], 'var_call_sWdoEVKFegoDcqolkOb4Welc': [{'avg_vol': '145247.8260869565'}], 'var_call_AiI72AVDqxzMCT0voDX9J1Gs': [{'avg_vol': '375.49407114624506'}], 'var_call_Nh4By1QbZsV8gdqMOHoriIXU': [{'avg_vol': '15578.656126482214'}], 'var_call_hOSoktiQLEzmqAZeypjUt8tb': [{'avg_vol': 'nan'}], 'var_call_emSKdpjm90P5Bd6DqyYNkffw': [{'avg_vol': '9.845238095238095'}], 'var_call_d2YeztirzhB0DwzRpXeEXeb1': [{'avg_vol': '254397.62845849802'}], 'var_call_ZqMUzTBgE6elMMqsSqllfS6b': [{'avg_vol': '10.276679841897232'}], 'var_call_ZHsNmVRxYOJ965DMKNeU668M': [{'avg_vol': 'nan'}], 'var_call_nAQuqDTrg0aykEwCYUozg4fg': [{'avg_vol': 'nan'}], 'var_call_RrdMgoNt1GKG4UqAiJ3VX7yi': [{'avg_vol': 'nan'}], 'var_call_YosVMQSEAKkIHg2ipFKTwflr': [{'avg_vol': '254.1501976284585'}], 'var_call_J0Pjn786WGM9pLzKAAkisxDh': [{'avg_vol': '10706.719367588932'}], 'var_call_cr7J4I23GY0h8zlWyM3edzkf': [{'avg_vol': 'nan'}], 'var_call_ixdbqBZikWg8Y1xIO9OFl7qW': [{'avg_vol': '781.8181818181819'}], 'var_call_TMqe1cVzZrJnf1o00qM97ypG': [{'avg_vol': 'nan'}], 'var_call_qHw3tH1dTuuExQuDh5pzY7Hb': [{'avg_vol': '36836.36363636364'}], 'var_call_Z1RxXZ827Qee7iudgUCqV3X5': [{'avg_vol': 'nan'}]}

exec(code, env_args)
