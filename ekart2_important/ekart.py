import json
from requests import Session
s = Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
null = None
true = True
data = {"pidLidMap":{"SNDFBM2PHUAMSNYJ":"LSTSNDFBM2PHUAMSNYJMMVZDA"},"pincode":"","snippetContext":{"facetMap":{},"layout":"grid","query":null,"queryType":null,"storePath":"osp/iko/9d5","viewType":"QUICK_VIEW"},"showSuperTitle":true}
# data = {
#     "pidLipMap":{
#         'SNDFQ39HFVKEVSMX':"LSTSNDFQ39HFVKEVSMXV8FMB0",
#     }
#     'pincode':'""',
#     'snippetContext':{
#         'showSuperTitle':'true',
#         'facetMap': '{}',
#         'query':'null',
#         'queryType':'null',
#         'layout':'grid',
#         'storePath':"osp/iko/9d5",
#         'viewType':"QUICK_VIEW"
#     }
# }

s.headers['Accept'] = '*/*'
s.headers['Accept-Encoding'] = 'gzip, deflate, br'
s.headers['Accept-language'] = 'en-US,en;q=0.5'
s.headers['Connection'] = 'keep-alive'
s.headers['Content-Length'] = '226'
s.headers['Content-Type'] = 'application/json'
s.headers['Cookie'] = 'T=TI160293880018000344207488901380401087114754949152383421901410494468; SN=VIE9B9F5AA3CA04ABCBAE5384914C0512D.TOK364F13C6AF9A4CB3A276352F8053E8F8.1612337126.LO; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18661%7CMCMID%7C24269649499681467392753798523122392141%7CMCAAMLH-1612663146%7C12%7CMCAAMB-1612893254%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1612295654s%7CNONE%7CMCAID%7CNONE; S=d1t10P04/cGZKPz8/e3I/Pz8/Pz5r4dyK3U0bTBTTGHrC+RKKR/wfRnPxlgk+na1Us6sresZmKbmJP5XrAlTSk9PUDQ==; s_cc=true; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; s_sq=%5B%5BB%5D%5D; gpv_pn=Store%20%3AFootwear%7CWomen%27s%20Footwear%7CFlats; gpv_pn_t=Store%20Browse'
s.headers['Host'] = '2.rome.api.flipkart.com'
s.headers['Origin'] = 'https://www.flipkart.com'
s.headers['Referer'] = 'https://www.flipkart.com/womens-footwear/flats/pr?sid=osp%2Ciko%2C9d5&otracker=nmenu_sub_Women_0_Flats&page=1'
s.headers['X-User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0 FKUA/website/42/website/Desktop'

r = s.post('https://2.rome.api.flipkart.com/api/4/product/swatch',data=json.dumps(data))
# json
tree = json.loads(r.content)
print(tree)

























