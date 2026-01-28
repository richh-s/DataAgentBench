code = """import json
import math
# stockinfo records
stockinfo = var_call_5XwzGnGK6QE3MaI6rkscTkMK
# mapping from symbol to the avg query result variable names
mapping = {
"AGMH": var_call_YpiFGRoKypG0ntUEaAgTENkw,
"AMTX": var_call_e7EBjG3T83fpisFDioVQvQ89,
"APEX": var_call_K3pxLCXOg6uA2MX9Wvdx5wl0,
"BIOC": var_call_SSgZjQIY3gELSNMHolDScsmR,
"BKYI": var_call_6MPVKjtcyURapACqxOKay15N,
"CBAT": var_call_XknreEDCypjaSlznCBSk5Bwc,
"CCCL": var_call_GTW4K49QnXqi5kJ3DrYqfvzd,
"CORV": var_call_iUl5c7bq6edJ6IDDzPHzBAAO,
"CPAH": var_call_chyXIkqNT69ViSdUiF4Ra0Wg,
"DZSI": var_call_wTsGo1aw33og5cTf08P4S6Ax,
"FAMI": var_call_Oj19tTB6UJrLWETOHn7B6nOK,
"FTFT": var_call_c2DT6VnWfxiZz8sFivJeV6Z5,
"FTR": var_call_McB4C9umfIT6KN6VVbFAGuSH,
"IDEX": var_call_knxFBaIDIbSLgGQGVfMeIK8X,
"ISDS": var_call_lUSfxcT8jDCqGVgjweiIC6Ck,
"MCEP": var_call_ZuCerCj7CstYjRyrolwuBKRW,
"NXTD": var_call_gLZIMbgnEJGIY0Z7VkCtDqKQ,
"OPTT": var_call_O5ToLlg8jgfrybvUGMhQKqqD,
"PEIX": var_call_6gGofXj2szi8NiMOTALITjBR,
"RBZ": var_call_rChcLsXhuS0YyF1muGAcX1nW,
"SES": var_call_g4UDKMotsAk3dVPRI0KcnFbG,
"SNSS": var_call_kMzs3WZbdLh8Q8ocmvny6dre,
"SPI": var_call_K8lCHnFHlAJGX5bQBHWudT8T,
"SYPR": var_call_JRA19IjqgzbVn93C0FNzPgV8,
"VTIQW": var_call_WXGBl9EUJItWc3Ix5pS9WdZ1
}

results = []
# Build symbol -> company description
sym_to_name = {rec['Symbol']: rec.get('Company Description') for rec in stockinfo}

for sym, rec_list in mapping.items():
    # rec_list is a list like [{"avg_vol": "...", "cnt": "..."}]
    if not rec_list or len(rec_list) == 0:
        continue
    rec = rec_list[0]
    cnt = rec.get('cnt')
    avg = rec.get('avg_vol')
    # convert cnt to int if possible
    try:
        cnt_val = int(cnt)
    except Exception:
        try:
            cnt_val = int(float(cnt))
        except Exception:
            cnt_val = 0
    # Only include if there is trading volume (cnt > 0) and avg is not nan
    include = cnt_val > 0
    avg_val = None
    if avg is None:
        include = False
    else:
        try:
            avg_val = float(avg)
            if math.isnan(avg_val):
                include = False
        except Exception:
            include = False
    if include:
        results.append({
            "Symbol": sym,
            "Company Description": sym_to_name.get(sym),
            "Average Daily Volume 2008": avg_val
        })

# Sort results by Symbol for consistent ordering
results = sorted(results, key=lambda x: x['Symbol'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_5XwzGnGK6QE3MaI6rkscTkMK': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_aaUa7O2dUhAxmJGIJijhllyH': 'file_storage/call_aaUa7O2dUhAxmJGIJijhllyH.json', 'var_call_YpiFGRoKypG0ntUEaAgTENkw': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_e7EBjG3T83fpisFDioVQvQ89': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_K3pxLCXOg6uA2MX9Wvdx5wl0': [{'avg_vol': '23781.422924901184', 'cnt': '253'}], 'var_call_SSgZjQIY3gELSNMHolDScsmR': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_6MPVKjtcyURapACqxOKay15N': [{'avg_vol': '10988.142292490118', 'cnt': '253'}], 'var_call_XknreEDCypjaSlznCBSk5Bwc': [{'avg_vol': '86223.32015810277', 'cnt': '253'}], 'var_call_GTW4K49QnXqi5kJ3DrYqfvzd': [{'avg_vol': '4366.798418972332', 'cnt': '253'}], 'var_call_iUl5c7bq6edJ6IDDzPHzBAAO': [{'avg_vol': '145247.8260869565', 'cnt': '253'}], 'var_call_chyXIkqNT69ViSdUiF4Ra0Wg': [{'avg_vol': '375.49407114624506', 'cnt': '253'}], 'var_call_wTsGo1aw33og5cTf08P4S6Ax': [{'avg_vol': '15578.656126482214', 'cnt': '253'}], 'var_call_Oj19tTB6UJrLWETOHn7B6nOK': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_c2DT6VnWfxiZz8sFivJeV6Z5': [{'avg_vol': '9.845238095238095', 'cnt': '168'}], 'var_call_McB4C9umfIT6KN6VVbFAGuSH': [{'avg_vol': '254397.62845849802', 'cnt': '253'}], 'var_call_knxFBaIDIbSLgGQGVfMeIK8X': [{'avg_vol': '10.276679841897232', 'cnt': '253'}], 'var_call_lUSfxcT8jDCqGVgjweiIC6Ck': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_ZuCerCj7CstYjRyrolwuBKRW': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_gLZIMbgnEJGIY0Z7VkCtDqKQ': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_O5ToLlg8jgfrybvUGMhQKqqD': [{'avg_vol': '254.1501976284585', 'cnt': '253'}], 'var_call_6gGofXj2szi8NiMOTALITjBR': [{'avg_vol': '10706.719367588932', 'cnt': '253'}], 'var_call_rChcLsXhuS0YyF1muGAcX1nW': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_g4UDKMotsAk3dVPRI0KcnFbG': [{'avg_vol': '2390.513833992095', 'cnt': '253'}], 'var_call_kMzs3WZbdLh8Q8ocmvny6dre': [{'avg_vol': '781.8181818181819', 'cnt': '253'}], 'var_call_K8lCHnFHlAJGX5bQBHWudT8T': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_JRA19IjqgzbVn93C0FNzPgV8': [{'avg_vol': '36836.36363636364', 'cnt': '253'}], 'var_call_WXGBl9EUJItWc3Ix5pS9WdZ1': [{'avg_vol': 'nan', 'cnt': '0'}]}

exec(code, env_args)
