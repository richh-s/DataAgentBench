code = """import json

# Load symbols
path = locals()['var_function-call-18110408372543862567']
with open(path, 'r') as f:
    symbols = json.load(f)

state = {"index": 0, "found_symbols": []}
batch = symbols[0:150]
state['index'] = 150

parts = []
for s in batch:
    # Construct query with concatenation to avoid f-string issues
    # SELECT 'SYM' s, MAX("Adj Close") m FROM "SYM" WHERE "Date" BETWEEN '2015-01-01' AND '2015-12-31'
    q = "SELECT '" + s + "' s, MAX(\"Adj Close\") m FROM \"" + s + "\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'"
    parts.append(q)

full_query = "SELECT s, m FROM (" + " UNION ALL ".join(parts) + ") WHERE m > 200"

with open('state.json', 'w') as f:
    json.dump(state, f)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-5893355739321017328': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-7854825807515924036': 'file_storage/function-call-7854825807515924036.json', 'var_function-call-78437376934120291': 'file_storage/function-call-78437376934120291.json', 'var_function-call-18110408372543862567': 'file_storage/function-call-18110408372543862567.json', 'var_function-call-5586898870354241742': 1435, 'var_function-call-14458840651299677807': [{'Date': '2018-08-15'}], 'var_function-call-14462412836344497414': ['RYE', 'RYF', 'RYH', 'RYJ', 'RYT', 'RYU', 'RYZZ', 'RZG', 'RZV', 'SAA', 'SBB', 'SBIO', 'SBM', 'SCAP', 'SCC', 'SCHA', 'SCHB', 'SCHC', 'SCHD', 'SCHE', 'SCHF', 'SCHG', 'SCHH', 'SCHI', 'SCHJ', 'SCHK', 'SCHM', 'SCHO', 'SCHP', 'SCHQ', 'SCHR', 'SCHV', 'SCHX', 'SCHZ', 'SCID', 'SCIF', 'SCIJ', 'SCIU', 'SCIX', 'SCJ', 'SCO', 'SDAG', 'SDCI', 'SDD', 'SDEM', 'SDGA', 'SDIV', 'SDOG', 'SDOW', 'SDP', 'SDS', 'SDY', 'SEF', 'SEIX', 'SFY', 'SFYF', 'SFYX', 'SGDJ', 'SGDM', 'SGOL', 'SH', 'SHE', 'SHM', 'SHYG', 'SHYL', 'SIJ', 'SIL', 'SILJ', 'SIMS', 'SIVR', 'SIZE', 'SJB', 'SJNK', 'SKF', 'SLV', 'SLX', 'SLY', 'SLYG', 'SLYV', 'SMDD', 'SMDY', 'SMEZ', 'SMLF', 'SMLL', 'SMLV', 'SMMU', 'SMN', 'SMOG', 'SNPE', 'SOIL', 'SOXL', 'SOXS', 'SOYB', 'SPAB', 'SPBO', 'SPDN', 'SPDV', 'SPDW', 'SPEM', 'SPEU', 'SPFF', 'SPGM', 'SPGP', 'SPHB', 'SPHD', 'SPHQ', 'SPHY', 'SPIB', 'SPIP', 'SPLB', 'SPLG', 'SPLV', 'SPMB', 'SPMD', 'SPMO', 'SPPP', 'SPSB', 'SPSK', 'SPSM', 'SPTI', 'SPTL', 'SPTM', 'SPTS', 'SPUS', 'SPUU', 'SPVM', 'SPVU', 'SPXB', 'SPXE', 'SPXL', 'SPXN', 'SPXS', 'SPXT', 'SPXU', 'SPXV', 'SPY', 'SPYB', 'SPYD', 'SPYG', 'SPYV', 'SPYX', 'SRLN', 'SRS', 'SRTY', 'SRVR', 'SSG', 'SSO', 'SSPY', 'SSUS', 'STIP', 'STPZ', 'SUB', 'SUSA', 'SVXY', 'SWAN', 'SYE', 'SYG', 'SYV', 'SZK', 'SZNE', 'TAGS', 'TAN', 'TAWK', 'TAXF', 'TBF', 'TBND', 'TBT', 'TBX', 'TDTF', 'TDTT', 'TECB', 'TECL', 'TECS', 'TERM', 'TFI', 'TFLO', 'THCX', 'THD', 'TIP', 'TIPX', 'TIPZ', 'TLDH', 'TLEH', 'TLH', 'TLTD', 'TLTE', 'TMF', 'TMV', 'TNA', 'TOK', 'TOLZ', 'TOTL', 'TPHD', 'TPIF', 'TPLC', 'TPOR', 'TPSC', 'TPYP', 'TRND', 'TTT', 'TWM', 'TYBS', 'TYD', 'TYO', 'TZA', 'UBOT', 'UBR', 'UBT', 'UCC', 'UCO', 'UCON', 'UDN', 'UDOW', 'UEVM', 'UGA', 'UGE', 'UGL', 'UITB', 'UIVM', 'UJB', 'ULBR', 'ULE', 'ULST', 'ULTR', 'ULVM', 'UMDD', 'UNG', 'UNL', 'UPRO', 'UPV', 'UPW', 'URA', 'URE', 'URNM', 'URTH', 'URTY', 'USAI', 'USCI', 'USD', 'USDU', 'USDY', 'USFR', 'USHG', 'USI', 'USL', 'USO', 'USRT', 'USSG', 'UST', 'USTB', 'USVM', 'UTES', 'UTRN', 'UTSL', 'UUP', 'UVXY', 'UWM', 'UWT', 'UXI', 'UYG', 'UYM', 'VALQ', 'VALT', 'VAW', 'VB', 'VBK', 'VBND', 'VBR', 'VCR', 'VDC', 'VDE', 'VEA', 'VEGA', 'VEGI', 'VEGN', 'VEU', 'VFH', 'VGFO', 'VGK', 'VGT', 'VHT', 'VIDI', 'VIG', 'VIOG', 'VIOO', 'VIOV', 'VIS', 'VIXM', 'VIXY', 'VLU', 'VNLA', 'VNQ', 'VO', 'VOE', 'VOO', 'VOOG', 'VOOV', 'VOT', 'VOX', 'VPC', 'VPL', 'VPU', 'VRAI', 'VRP', 'VSL', 'VSS', 'VT', 'VTEB', 'VTI', 'VTV', 'VUG', 'VUSE', 'VV', 'VWO', 'VXF', 'VYM', 'WANT', 'WBIE', 'WBIF', 'WBIG', 'WBII', 'WBIL', 'WBIN', 'WBIT', 'WBIY', 'WCHN', 'WDIV', 'WEAT', 'WEBL', 'WEBS', 'WIP', 'WIZ', 'WOMN', 'WPS', 'WTMF', 'WWJD', 'XAR', 'XBI', 'XBUY', 'XCEM', 'XCOM', 'XDIV', 'XES', 'XHB', 'XHE', 'XHS', 'XITK', 'XLB', 'XLC', 'XLE', 'XLF', 'XLG', 'XLI', 'XLK', 'XLP', 'XLRE', 'XLSR', 'XLU', 'XLV', 'XLY', 'XME', 'XMHQ', 'XMLV', 'XMMO', 'XMVM', 'XNTK', 'XOP', 'XOUT', 'XPH', 'XPP', 'XRLV', 'XRT', 'XSD', 'XSLV', 'XSMO', 'XSOE', 'XSVM', 'XSW', 'XTH', 'XTL', 'XTN', 'XWEB', 'YANG', 'YCL', 'YCOM', 'YCS', 'YINN', 'YLD', 'YOLO', 'YXI', 'YYY', 'ZCAN', 'ZDEU', 'ZGBR', 'ZHOK', 'ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}

exec(code, env_args)
