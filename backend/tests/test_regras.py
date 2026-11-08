from app.regras import ja_recebeu_no_mes


def test_familia_que_ja_recebeu_no_mes():
    assert ja_recebeu_no_mes(["2026-10", "2026-11"], "2026-11") is True


def test_familia_que_nao_recebeu_no_mes():
    assert ja_recebeu_no_mes(["2026-10"], "2026-11") is False
