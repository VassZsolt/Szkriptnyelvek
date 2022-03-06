from Ekezetek_eltavolitasa import text_change


def test_text_change():
    assert text_change("zászló") == "zaszlo"
    assert text_change("Ádám") == "Adam"
    assert text_change("Alma") == "Alma"
    assert text_change("Érem") == "Erem"
    assert text_change("Öszvér") == "Oszver"
    assert text_change("Útonálló") == "Utonallo"
    assert text_change("Üveg") == "Uveg"
    assert text_change("űr") == "ur"
