import pytest

from app.regras import ja_recebeu_no_mes, mes_valido


def test_familia_que_ja_recebeu_no_mes():
    assert ja_recebeu_no_mes(["2026-10", "2026-11"], "2026-11") is True


def test_familia_que_nao_recebeu_no_mes():
    assert ja_recebeu_no_mes(["2026-10"], "2026-11") is False


def test_mes_valido_aceita_formato_correto():
    assert mes_valido("2026-11") is True
    assert mes_valido("2026-13") is False


def test_mes_invalido_gera_erro():
    with pytest.raises(ValueError):
        ja_recebeu_no_mes(["2026-10"], "11/2026")
