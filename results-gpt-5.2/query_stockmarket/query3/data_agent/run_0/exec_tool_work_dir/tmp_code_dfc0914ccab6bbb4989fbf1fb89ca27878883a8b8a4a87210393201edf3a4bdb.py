code = """import json, pandas as pd
import duckdb

def load_list(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r') as f:
            return json.load(f)
    return maybe_path

stockinfo = pd.DataFrame(var_call_VeqcVlcXnG0mCkxw95T6Z5hd)
tables = set(load_list(var_call_Ye8ToM28XQiJYE153CrOGIlh))

symbols = [s for s in stockinfo['Symbol'].tolist() if s in tables]

con = duckdb.connect(database='stocktrade_database', read_only=True)
rows = []
for sym in symbols:
    q = f"""
    SELECT '{sym}' AS Symbol,
           AVG(CASE WHEN Volume IS NOT NULL THEN Volume END) AS avg_daily_volume_2008
    FROM "{sym}"
    WHERE Date >= '2008-01-01' AND Date <= '2008-12-31'
    """
    try:
        r = con.execute(q).fetchone()
        avgvol = r[1]
        if avgvol is not None:
            rows.append((sym, float(avgvol)))
    except Exception:
        continue

con.close()

avgdf = pd.DataFrame(rows, columns=['Symbol','avg_daily_volume_2008'])
res = stockinfo.merge(avgdf, on='Symbol', how='inner')
res = res[['company_name','Symbol','financial_status','avg_daily_volume_2008']].sort_values(['company_name','Symbol'])
res['avg_daily_volume_2008'] = res['avg_daily_volume_2008'].round(2)

answer_lines = []
for _, r in res.iterrows():
    answer_lines.append(f"{r['company_name']} ({r['Symbol']}) | Financial Status: {r['financial_status']} | Avg daily volume 2008: {r['avg_daily_volume_2008']}")

out = "\n".join(answer_lines) if answer_lines else "No matching companies found."

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VeqcVlcXnG0mCkxw95T6Z5hd': [{'Symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'AMTX', 'company_name': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'market_category': 'G', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'APEX', 'company_name': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'BIOC', 'company_name': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'BKYI', 'company_name': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'CBAT', 'company_name': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'CCCL', 'company_name': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'CORV', 'company_name': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'CPAH', 'company_name': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'DZSI', 'company_name': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'FAMI', 'company_name': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'FTFT', 'company_name': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'market_category': 'Q', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'IDEX', 'company_name': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'MCEP', 'company_name': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'NXTD', 'company_name': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'OPTT', 'company_name': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'PEIX', 'company_name': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'RBZ', 'company_name': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'market_category': 'G', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'SES', 'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'market_category': 'S', 'financial_status': 'H', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'SNSS', 'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'market_category': 'Q', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'SYPR', 'company_name': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'market_category': 'G', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'Symbol': 'VTIQW', 'company_name': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'market_category': 'S', 'financial_status': 'D', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}], 'var_call_Ye8ToM28XQiJYE153CrOGIlh': 'file_storage/call_Ye8ToM28XQiJYE153CrOGIlh.json'}

exec(code, env_args)
