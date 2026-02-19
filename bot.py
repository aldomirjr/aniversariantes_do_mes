import requests
import datetime
import os
import pandas as pd

TOKEN = os.getenv("8315623446:AAG7PqkDBZkM6FSqHbUxTtt0N-_MAbp1YSY")
CHAT_ID = os.getenv("https://t.me/+xwiYQWEP6hdiZDFh")

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRBuYPsC6XDnfjGLkWF5saaL7wbEFTdRNamIT6vg3i13F3ngEfbP0JnuvHHefvpMMGuOm99yrpG69te/pub?output=csv"

df = pd.read_csv(URL)

# Garantir que Mes e dia sejam número
df["Mes"] = df["Mes"].astype(int)
df["dia"] = df["dia"].astype(int)

hoje = datetime.datetime.now()
mes_atual = hoje.month
dia_atual = hoje.day

aniversariantes = df[
    (df["Mes"] == mes_atual) &
    (df["dia"] == dia_atual)
]

if not aniversariantes.empty:
    nomes = "\n".join(
        [f"• {nome}" for nome in aniversariantes["Nome completo"]]
    )

    mensagem = f"""
🎉 Aniversariantes de Hoje 🎉

{nomes}

Que Deus abençoe grandemente esse novo ano! 🙏
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensagem
    })
