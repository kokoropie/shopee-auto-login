import requests
from requests.structures import CaseInsensitiveDict

url = "https://shopee.vn/mkt/coins/api/v2/checkin_new"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["accept-encoding"] = "gzip, deflate, br"
headers["accept-language"] = "vi,en-US;q=0.9,en;q=0.8"
headers["content-length"] = "2"
headers["Content-Type"] = "application/json"
headers["cookie"] = 'SPC_PC_HYBRID_ID=9; REC_T_ID=3188c1db-db29-11eb-90a2-9440c93c99f8; _gcl_au=1.1.308989899.1625225557; _med=cpc; csrftoken=7CTDVoY9Tuqwha60pwJI7OXrJAtbex3K; SPC_F=s0zIITyyfzoP4j34gY0nu4aainIJu4xV; _hjid=a46c4aa4-fad7-4d4e-b4e9-53ebe1f430ec; G_ENABLED_IDPS=google; SPC_CLIENTID=czB6SUlUeXlmem9Qzlkfzzjsqkovrdpk; SPC_SSN=o; SPC_WSS=o; SPC_SI=mall.5RKavNASdkcnW8xorHZK6tnDKyxviWxs; _gid=GA1.2.1023429269.1626090128; SPC_U=223155327; SPC_EC=tImpb++wgfaq89F8KrBZ3hOIF7FiB+jpXy3Ig/H5xxPNYPHmeomgIAUQTMEwM10OSxcCpzoFEIBXvflKKrKxXuywaG50lSCjteGPhhmzh5RZaP0nt7Hwj3uqAx1TrvPwopubuAOVVeDHqZEqvNkPbedInwrLBl2Qv82MLJFgrUc=; SPC_IA=1; _gcl_aw=GCL.1626090282.Cj0KCQjw0K-HBhDDARIsAFJ6UGgMbw4AYhaT_KkMMWJL0Our3MF5tGeVITATKHonFnzrbwCRHS3rBZUaArLVEALw_wcB; _gac_UA-61914164-6=1.1626090332.Cj0KCQjw0K-HBhDDARIsAFJ6UGgMbw4AYhaT_KkMMWJL0Our3MF5tGeVITATKHonFnzrbwCRHS3rBZUaArLVEALw_wcB; SPC_R_T_ID="Z+UHfFWt7y3/elpwZ52KFc+GNdTAL2hg25/LaurFx2deRfd+9Kgy/ITUuf6kQSK1ABgEAkznr70ax8LTCO5YEwqD2BPGhqEfw1BOTrP/1IU="; SPC_T_IV="/C2jw8lwG/3YYNsWEGggIA=="; SPC_R_T_IV="/C2jw8lwG/3YYNsWEGggIA=="; SPC_T_ID="Z+UHfFWt7y3/elpwZ52KFc+GNdTAL2hg25/LaurFx2deRfd+9Kgy/ITUuf6kQSK1ABgEAkznr70ax8LTCO5YEwqD2BPGhqEfw1BOTrP/1IU="; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.272215217.1625225561; cto_bundle=xnGVD19ZUzhOZzh4d0plRE5NQ1lib1plWVllRThWTTNUa3JyclRLZkl4R2szbWFaSFFmWmxYRW9TejNFWUt6Rk9HSm51NWtwYXBOU1ZDdlRkMTZSeGptSmgxMmtneTdRQmpLbVVMaElmN3VOYmt5bTlRb2Vud0N3RlNHenRHd3dJUzE2WVV2SFNLNDJZM3dQdTlpTzg2TTlqcGclM0QlM0Q; _dc_gtm_UA-61914164-6=1; _ga_M32T05RVZT=GS1.1.1626145583.7.1.1626145707.31'
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"
headers["x-api-source"] = "pc"
headers["x-csrftoken"] = "7CTDVoY9Tuqwha60pwJI7OXrJAtbex3K"
headers["x-requested-with"] = "XMLHttpRequest"
headers["x-shopee-language"] = "vi"

data = "{}"


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

