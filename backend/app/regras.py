import re

PADRAO_MES = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")


def mes_valido(mes):
    """Retorna True se o texto estiver no formato AAAA-MM."""
    return bool(PADRAO_MES.match(mes))


def ja_recebeu_no_mes(meses_das_entregas, mes_referencia):
    """Retorna True se a família já recebeu uma cesta no mês (formato AAAA-MM)."""
    if not mes_valido(mes_referencia):
        raise ValueError("mes_referencia deve estar no formato AAAA-MM")
    return mes_referencia in meses_das_entregas
