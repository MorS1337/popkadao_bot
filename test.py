import requests

url = "https://m.tb.cn/h.51ZaAqw?tk=ziyjdFGDEEt"

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "cna=YwRPHcDR2XICAbDVsZ2Qx2wW; xlly_s=1; _m_h5_tk=6c09fabf194e3efc2de59035abfe64a1_1690842811693; _m_h5_tk_enc=2502c2cbd99aef0319e615e67c6d9687; isg=BMLCuxuEElW-aA4JKikFKrfZE8gkk8at8-Kj-wzb6zXgX2LZ9CKwvHKZD0MjDz5F",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)
print(req.text)