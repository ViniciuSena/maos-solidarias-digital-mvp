def ja_recebeu_no_mes(meses_das_entregas, mes_referencia):
    """Retorna True se a família já recebeu uma cesta no mês (formato AAAA-MM)."""
    return mes_referencia in meses_das_entregas
