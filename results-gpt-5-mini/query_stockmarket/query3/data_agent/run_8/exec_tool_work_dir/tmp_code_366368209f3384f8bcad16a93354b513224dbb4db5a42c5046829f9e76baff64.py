code = """import json
# Load stock info
info = var_call_Rq14Nwo0w7Pn5xVAdnnqYq06
# Map symbol to avg volume results from the parallel queries
avg_map = {
    'AGMH': var_call_vLvc405lJ1TPaDhmyoa82s9J[0]['avg_volume'],
    'AMTX': var_call_AHdOyLUGtwmaLwiKUH7WZ3ua[0]['avg_volume'],
    'APEX': var_call_IF34hetoy2kiJ1UEq9U6FjUp[0]['avg_volume'],
    'BIOC': var_call_sGHtwUrG7luXmHYteE1xMeWw[0]['avg_volume'],
    'BKYI': var_call_9EdOErjOT33dZZqSk5M1wR3i[0]['avg_volume'],
    'CBAT': var_call_waNkEBCHjRQ0KQ635aaVHYN4[0]['avg_volume'],
    'CCCL': var_call_abx1zaFE8NZ9Z87zqUVaOPGw[0]['avg_volume'],
    'CORV': var_call_qOO1oyXCgegQ8sXmopdnn2Y7[0]['avg_volume'],
    'CPAH': var_call_q4QwrY5NuG3PXlDDDZDia292[0]['avg_volume'],
    'DZSI': var_call_QnBzAsDBR43JTp85RXmi6X6U[0]['avg_volume'],
    'FAMI': var_call_GsyfKLDQ9jZ3wpWEvntcwyRY[0]['avg_volume'],
    'FTFT': var_call_NYhhpT4PbVVFr0nxjNg2Rclj[0]['avg_volume'],
    'FTR': var_call_4XTsAg5EhT8KAvIUChacsJyE[0]['avg_volume'],
    'IDEX': var_call_5amUz6ZYZ14hUGTPripM5vO6[0]['avg_volume'],
    'ISDS': var_call_HytUWgmm3htEe8Fd7zl6aYOJ[0]['avg_volume'],
    'MCEP': var_call_N8kAOiBMHXwg3RLPy9WLQ6UW[0]['avg_volume'],
    'NXTD': var_call_PFdOHWW6qV48hSfH362HIqUd[0]['avg_volume'],
    'OPTT': var_call_yOrLpUBAocWP9nBFYPlH1kqE[0]['avg_volume'],
    'PEIX': var_call_p130qU48CU6fG7wGsqZ67Y5A[0]['avg_volume'],
    'RBZ': var_call_AfeFcRwPoxw1YDpg1XzEdSSw[0]['avg_volume'],
    'SES': var_call_AHUslIsz9bo0LWYYiEAuWgyw[0]['avg_volume'],
    'SNSS': var_call_JKxVTI2iPXRiRDRb1YP7L7km[0]['avg_volume'],
    'SPI': var_call_DCBWPVvMJNCmfDKpAZchqlSb[0]['avg_volume'],
    'SYPR': var_call_lbfYjMOyAQSVc9k7nzJ6zkK6[0]['avg_volume'],
    'VTIQW': var_call_FRQXHFeOhz69AetxQ9xSeUCu[0]['avg_volume']
}

results = []
for row in info:
    sym = row['Symbol']
    comp = row.get('Company Description') or row.get('Company') or ''
    avg_raw = avg_map.get(sym)
    if avg_raw is None:
        continue
    # treat 'nan' (string) or null as missing
    try:
        avg_val = float(avg_raw)
    except Exception:
        continue
    if avg_val != avg_val:  # NaN check
        continue
    results.append({'Company Description': comp, 'Symbol': sym, 'avg_daily_volume_2008': avg_val})

# Build a plain-text answer listing each company and its avg volume
lines = []
for r in results:
    lines.append(f"{r['Company Description']} ({r['Symbol']}): {r['avg_daily_volume_2008']}")
final_text = "\n".join(lines)

print("__RESULT__:")
print(json.dumps(final_text))"""

env_args = {'var_call_Rq14Nwo0w7Pn5xVAdnnqYq06': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q', 'Nasdaq Traded': 'Y'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}], 'var_call_vLvc405lJ1TPaDhmyoa82s9J': [{'avg_volume': 'nan'}], 'var_call_AHdOyLUGtwmaLwiKUH7WZ3ua': [{'avg_volume': 'nan'}], 'var_call_IF34hetoy2kiJ1UEq9U6FjUp': [{'avg_volume': '23781.422924901184'}], 'var_call_sGHtwUrG7luXmHYteE1xMeWw': [{'avg_volume': 'nan'}], 'var_call_9EdOErjOT33dZZqSk5M1wR3i': [{'avg_volume': '10988.142292490118'}], 'var_call_waNkEBCHjRQ0KQ635aaVHYN4': [{'avg_volume': '86223.32015810277'}], 'var_call_abx1zaFE8NZ9Z87zqUVaOPGw': [{'avg_volume': '4366.798418972332'}], 'var_call_qOO1oyXCgegQ8sXmopdnn2Y7': [{'avg_volume': '145247.8260869565'}], 'var_call_q4QwrY5NuG3PXlDDDZDia292': [{'avg_volume': '375.49407114624506'}], 'var_call_QnBzAsDBR43JTp85RXmi6X6U': [{'avg_volume': '15578.656126482214'}], 'var_call_GsyfKLDQ9jZ3wpWEvntcwyRY': [{'avg_volume': 'nan'}], 'var_call_NYhhpT4PbVVFr0nxjNg2Rclj': [{'avg_volume': '9.845238095238095'}], 'var_call_4XTsAg5EhT8KAvIUChacsJyE': [{'avg_volume': '254397.62845849802'}], 'var_call_5amUz6ZYZ14hUGTPripM5vO6': [{'avg_volume': '10.276679841897232'}], 'var_call_HytUWgmm3htEe8Fd7zl6aYOJ': [{'avg_volume': 'nan'}], 'var_call_N8kAOiBMHXwg3RLPy9WLQ6UW': [{'avg_volume': 'nan'}], 'var_call_PFdOHWW6qV48hSfH362HIqUd': [{'avg_volume': 'nan'}], 'var_call_yOrLpUBAocWP9nBFYPlH1kqE': [{'avg_volume': '254.1501976284585'}], 'var_call_p130qU48CU6fG7wGsqZ67Y5A': [{'avg_volume': '10706.719367588932'}], 'var_call_AfeFcRwPoxw1YDpg1XzEdSSw': [{'avg_volume': 'nan'}], 'var_call_AHUslIsz9bo0LWYYiEAuWgyw': [{'avg_volume': '2390.513833992095'}], 'var_call_JKxVTI2iPXRiRDRb1YP7L7km': [{'avg_volume': '781.8181818181819'}], 'var_call_DCBWPVvMJNCmfDKpAZchqlSb': [{'avg_volume': 'nan'}], 'var_call_lbfYjMOyAQSVc9k7nzJ6zkK6': [{'avg_volume': '36836.36363636364'}], 'var_call_FRQXHFeOhz69AetxQ9xSeUCu': [{'avg_volume': 'nan'}]}

exec(code, env_args)
