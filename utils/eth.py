def hex_to_dec(hex_input: str) -> int:
    return int(hex_input, 16)


def hex_to_dec_string(hex_input: str) -> str:
    converted_hex_to_int = hex_to_dec(hex_input)

    return str(converted_hex_to_int)


def dec_to_hex(dec_input: int) -> str:
    return hex(dec_input)
