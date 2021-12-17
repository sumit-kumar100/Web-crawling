from requests import Session
import json
import time
import pandas as pd

s = Session()

# Request Headers
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
s.headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
s.headers['accept-encoding'] = 'gzip, deflate, br'
s.headers['accept-language'] = 'en-US,en;q=0.9'
s.headers['cache-control'] = 'max-age=0'
s.headers['dnt'] = '1'
# Note :- Need to changed as per requirement.
s.headers['cookie'] = 'ASP.NET_SessionId=fyfqosninlvou3xl4d53udka; __RequestVerificationToken_L2hvbWU1=z8UAX5ZSyIYpICImRvdFxati4lICwYb1ASRWmCh1xJfkPlyaFVSVQwBcPEgmSExCTwSdxpJEGEEmdB4cYOZUykLKLDA1; __zlcmid=14ak6aNqko5mmmm; __RequestVerificationToken_L2hvc3BpdGFscw2=OMcgUJ0kXaNKWgnzquGdxyTocDVNfcECKYflYo3eTzrts5SptVhGb0IEiibp9RUIfCaElL2Hf3DjmySfS9IEc96KCYc1; .AspNet.ApplicationCookie=Pkuffiab8RDqQVEKEf0xVbPOzwaH4ueQxTDMNHAvE9KQuG5qxkLInfgb04zGtE2ii0gexOaznbEM8gwSSPDAW6bd_zP1kNYSAa4NYr3m2k9A4goaKKpyHYi6nYtfTDrDCv33g6q_03NmmmQGa0NDaRWwp2oWnxXJM6nPSKdiV9uU-i64UxxV0O2L_1FAd7nvoGhuO8Goq6iRiJMIjDZKSWjcinL4N_L58yxkak9sG4cY96hkYODph8fRq1kLSzFeEAi30UCgc5qX9H6XA_WGDdIj2hvcmW-Mpth5-Q0UosuhFxp7KNUQIvfvctkvVVqjQbWGrTdT4ZypAaBsV0RtHLzai6IFeKVLDJbZ5rf9UkLP8FyoRzPKXMPHBj50y-QqVCC70yuFsHVoUaaEkaLJT6imVW0oBScIMxQQSAXjebnIZB-QBOl3UIf2sZ91x4cfdNu0bsSw8WWYzOJGNApPk2eUyYQbI0AFTU5Rr_95key2fqPruRuFlKvPs9eiJosTPk930bpRJq32HtJ-vFq9GL9c50R47vC8KCfHjgpq2z-yfy2JwcXIEzKGdcDOTxmT1i6tBloQo8qQq4P2FBK1O0aAekpMXWm-lkylgtx39AK908SIHKpDkPjP9lFc7fAWN3lBW0CwPVKBHSHLLjXUxECB3WN8vSbXv_y5oEEo3nR_kadNfkejVT0M16RwX7Z4780lmfdJozUYnae3236_zg3jsxPUCXb5ERd5FElKjVfKczY_Wh8dHXHS6JyJsCkOGNT18QQBFUbMPZW7B0hLicDt_DDI4OXXq2sGhbNFm_hR9kYq7LTZNypG850SKvo1GQQbk1OXPW8xYQdQT4q31yahVfZ1CT7dTddhM6eCis5B6F4ussllGobRbu31bchdSCA5B37rc8PAWVJ4_zJ2d9QRu9ZtOojS1fI-VPlL30aL3S49WWno78w0jumHolKGSHzKQXEV4x6QB2ch2aF0MgWMFrb2RsYs2_HLnDWeChUVg0zp2yC3AqIMyutyRtAb25wEzfAHX8zuysyFboKOzBqZui2jI8ZOYRmoLIwT6MttisLBHkc1iQLwMQujVyqC7l3TlO0M_sYIflkmQBJVqtnaBI-NTFukbR_nKUoIaeOgXFxy5SR7ZouSlJz6MrRQGFrtDLLTBvmeMZ8NfPX9YzliRiE4fBp_rRHwKk8gR4H9J69N9se5UV-KV52_IKyDDvqC8gTZosam1VFqxlIp0EELd1G1uz4CcMO9PVbyM2YgPNqLLIvmFgabJ9II0IXw_kSAz6G5c_vbcEdqqySP8kkenshcFro2NwU8BCx-WwXhTa0DE0kfPeE3qi-0rTsPfI_YNi2SLfR6cLrohyFgkupC6zRHjsGsdr3-r84tmtWpAFmPgoHm4KvIFSLsLgSjw4Do4AddjgFG_eAdC6mK2JlU0HcYZrgkAq7UZHm4fkO_Gqxicc3-5Zun4MBsvMUH32OKrO86KC_t7xuQTyaPBmJnAh0Eow8vZNhVaQ6yEa39biwhTpms_SzBF4Qk56GdTjsdMaFLgiUW4B9M-IgPtuGBR-GG4IotZdStkLBAl2UPipQ1x1i-oDeTmqFPJvTYpF489hgqpU7zU8ogzVwdlat3Q1DcQVxCw6QhkJwRkPh1HJjYTtkV26O01pgRKZfjYX4LWUrXTnL79R_Afjrk6FIwhW4YiQQncJbU7kbFl1RiUgLA0T9B7XZEZsIL0lhctMVAxJYRsMJ4ERZcbU_SZt14TWRS1wOo7Fu2E_YqtrfHT7MC-3tQEyQ0-C9zP_-yYid7wwOn6ya0CtdISe9rRaRQYlY6m3Qy0opTufwS6-iarRL77gaezx1sBy20Dn__xQ_O9VDfkosyru0_pJnUZpMULF9nvKXbIGd4b2blG0taA06A8n3JMpRgDFAIoVnUzdIWgXESHyLCZ8Rer0NXW9b7Iu4eJqdKuK_K57Gb2DkR6uMLjMLxfcaExDh0rUmd1WYe6ekHfDFxfe4PmLmPDr0fqFI1dWN0tAhtio0WqgzoO3-CwDJFL9p_ZcX1hrHFqFhMyWlv4MpLe-3W_ifgh739BslyIMSeldxJuj-NKq-MKf_hHh8lsqLSpiw2RPoCl8d-tvp5ojZnq7bRhtu_SA27Wc5o0iF6nReTi3Qg1lckhQJC6WUUrvZ1pNPuGMLVdp5YNL9HYwDcHGcSi199u0o1EL86fAN9XZRrXn66jsa_XwQ93igWz07---h448hI7LW-sNorSd9A4ndewRlkKXvABYf8lBCVgUH6Ce9gaXJHQ2ZOLBH375R9aGO33pA6Xjeq-CXCXOYGms20G0IJ5JKpQ7WVh9l-A1O4qoki7YeOZ-feRtimLa9DLMgQkJWYPdhVsTe500Ut7UsfdeN_ni933ZanB2_KW1Xw81iKesbZ9Iv08C_BRSoTJzsBHflyDT2Te-YdMTvhriPbRDFJyZSzTzJSo_3iyaf5C670amH7c2ulxjTLVGuxzFw1Z7RktBlnSuAAeg8rfDFpi65kgJgUjFhvxOYamArF9hoZAYrSkDxWHxdPFp0juhtl5De0-zdV2dniuWz1urUfBGPf9dV5z1NRDon6uFNf9qGIyvusjEB5kmSxwOdSEska-TnyKow6BVQdJryJbzeiOcjIPk1bWYBPSAUP2RdBjNFtJGsNwK4Up9oF3Q7_JRiZC1bH8C3Y-PpZpXwd6sedo88W_OXmkeoNxI-obqzfNtx4SsUTYmuMvX0JF5G3wpo1vHJdV4Q6YyC9BuLAt4hrDhZ7_T5lQ_KzfPv9yZDVRywCNeeS6nXDplqoK5GAtrih4_JerJ17t832GKclGJSui2oL0k9zyD1dQnf1Nnl-9b-eUebuqRO-vLIcB5_F_WZsVJaAokGekn9KGP7DODGVSSl-xiV3WznhtmnSXmUj_qxiINrD93j7V9pW-Dk5mMRysUTFictGzezgBR0qyYKZulZ-XL3YXrvHrCiaZ1bPAROKG2GAIn8yO6vHcGzwjc1hhTNbLxNV22i94PtV0nVbSxcDLZKNcpU9kGFoSTDsL7KoOT1SI7Px6FkgTQFFybjs08xQyvgsqxQwvvUA_WE7ohFLxmq_7fn824QKcpPDslN6mqDo6GIEzR3FUeb3R9MLmuSwXk2TMsz1kIIOp1aJ4OR7SiP0c9IE33mLOgCXUlL8CDAoxC7n2DcWvouQ7ZnryE_h_mKQEC4S2KOtqBqHApogPx_6FuwhsuOsJmih8xcBzve97l4pQhdfs2p262GrvaV7ZGHmPKfWlyXBc_Tll5m_J9dGWvPUMwGzDO4Y7A7l7QQX_7cBNxaFlHoW7v7DCYbHisuuA7uX7vmi-CKilHBRXvz3SahkcgjmbUF4-0SGQWxXHDik9xdQfRvdpm7fo3IKsMaeIyJYP9Yc6pxNUq27dXPkANY; site24x7rumID=8231115718039878.1639000583204.1639000583204'

# List of Year for Data
years = ['2021','2020','2019','2018','2017','2016','2015','2014','2013','2012']

for year in years:
    # Page Number
    page = 1
    # Data Information
    DRG_CODE = list()
    DRG_DESCRIPTION = list()
    CHARGES_MEDICARE = list()
    COST_PER_DISCHARGE = list()
    CMI_ADJUSTED_COST_PER_DISCHARGE = list()
    CMI_WAGE_ADJUSTED_COST_PER_DISCHARGE = list()
    CLAIMS_MEDICARE = list()

    while True:
        r = s.get(f'https://www.defhc.com/hospitals/api/export/json/SE9TUElUQUwuRmFjaWxpdHlQcm9maWxlc19DbGFpbXNBbmFseXRpY3NfSW5zdGl0dXRpb24%3d?hospital_id=4712&sort=CHARGES_MEDICARE&sortdir=DESC&pagesize=25&claim_type_id=1&code_view_id=1&payer_id=1&textSearch=&page={page}&CLAIM_YEAR={year}&_select=RFJH%2CRFJHfEdlbmVyYWx8fHx8RFJH%2CRFJHX0RFU0NSSVBUSU9OfEdlbmVyYWx8fHx8RFJHX0RFU0NSSVBUSU9O%2CQ0hBUkdFU19NRURJQ0FSRXxDdXJyZW5jeXwkIywjIzA7KCQjLCMjMCl8fHxDSEFSR0VTX01FRElDQVJF%2CQ09TVF9QRVJfRElTQ0hBUkdFfEN1cnJlbmN5fCQjLCMjMDsoJCMsIyMwKXx8fENPU1RfUEVSX0RJU0NIQVJHRQ%3D%3D%2CQ01JX0FESlVTVEVEX0NPU1RfUEVSX0RJU0NIQVJHRXxDdXJyZW5jeXwkIywjIzA7KCQjLCMjMCl8fHxDTUlfQURKVVNURURfQ09TVF9QRVJfRElTQ0hBUkdF%2CQ01JX1dBR0VfQURKVVNURURfQ09TVF9QRVJfRElTQ0hBUkdFfEN1cnJlbmN5fCQjLCMjMDsoJCMsIyMwKXx8fENNSV9XQUdFX0FESlVTVEVEX0NPU1RfUEVSX0RJU0NIQVJHRQ%3D%3D%2CQ0xBSU1TX01FRElDQVJFfE51bWVyaWN8IywjIzA7KCMsIyMwKXx8fENMQUlNU19NRURJQ0FSRQ%3D%3D')
        tree = json.loads(r.content)
        print(tree)
        if len(tree.get('records')) != 0:
            for data in tree.get('records'):
                DRG_CODE.append(data['DRG'])
                DRG_DESCRIPTION.append(data['DRG_DESCRIPTION'])
                CHARGES_MEDICARE.append(data['CHARGES_MEDICARE'])
                COST_PER_DISCHARGE.append(data['COST_PER_DISCHARGE'])
                CMI_ADJUSTED_COST_PER_DISCHARGE.append(data['CMI_ADJUSTED_COST_PER_DISCHARGE'])
                CMI_WAGE_ADJUSTED_COST_PER_DISCHARGE.append(data['CMI_WAGE_ADJUSTED_COST_PER_DISCHARGE'])
                CLAIMS_MEDICARE.append(data['CLAIMS_MEDICARE'])
        else:
            break
        # Waitin For Next Request
        time.sleep(5)
        # Increment Statement
        page += 1

    # dataframe
    df = pd.DataFrame(
        {
            'DRG_CODE': DRG_CODE,
            'DRG_DESCRIPTION': DRG_DESCRIPTION,
            'CHARGES_MEDICARE':CHARGES_MEDICARE,
            'COST_PER_DISCHARGE':COST_PER_DISCHARGE,
            'CMI_ADJUSTED_COST_PER_DISCHARGE':CMI_ADJUSTED_COST_PER_DISCHARGE,
            'CMI_WAGE_ADJUSTED_COST_PER_DISCHARGE':CMI_WAGE_ADJUSTED_COST_PER_DISCHARGE,
            'CLAIMS_MEDICARE':CLAIMS_MEDICARE
        }
    )
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(f'Year_{year}.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

