from utils.eth import dec_to_hex, hex_to_dec, hex_to_dec_string


def test_hex_converting():
    original_number = 1999

    hex_number = dec_to_hex(original_number)
    dec_number = hex_to_dec(hex_number)

    assert original_number == dec_number


def test_hex_string():
    original_number = 1999

    hex_number = dec_to_hex(original_number)
    dec_number_in_string = hex_to_dec_string(hex_number)

    assert str(original_number) == dec_number_in_string
