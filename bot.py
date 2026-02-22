import requests
import datetime
import os
import pandas as pd

# =========================
# CONFIGURAÇÕES
# =========================

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRBuYPsC6XDnfjGLkWF5saaL7wbEFTdRNamIT6vg3i13F3ngEfbP0JnuvHHefvpMMGuOm99yrpG69te/pub?output=csv"

# =========================
# EXECUÇÃO
# =========================

try:
    print("Baixando planilha...")
    df = pd.read_csv(URL)

    # Padronizar nomes das colunas
    df.columns = df.columns.str.strip().str.lower()

    print("Colunas encontradas:", df.columns.tolist())

    # Garantir que mes e dia sejam números inteiros
    df["mes"] = df["mes"].astype(float).astype(int)
    df["dia"] = df["dia"].astype(float).astype(int)

    from datetime import datetime
    from zoneinfo import ZoneInfo

    hoje = datetime.now(ZoneInfo("America/Sao_Paulo"))
    mes_atual = hoje.month
    dia_atual = hoje.day

    print("Hoje:", mes_atual, dia_atual)

    aniversariantes = df[
        (df["mes"] == mes_atual) &
        (df["dia"] == dia_atual)
    ]

    print("Aniversariantes encontrados:", len(aniversariantes))

    if not aniversariantes.empty:
        nomes = "\n".join(
            [f"• {nome}" for nome in aniversariantes["nome completo"]]
        )

        mensagem = f"""
🎉 Aniversariantes de Hoje 🎉

{nomes}

Que Deus abençoe grandemente esse novo ano! 🙏
"""

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        response = requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": mensagem
        })
        print("URL enviada:", f"https://api.telegram.org/bot{TOKEN}/sendMessage")
        print("Mensagem enviada:", response.status_code)

    else:
        print("Nenhum aniversariante hoje.")

except Exception as e:
    print("Erro na execução:", str(e))
