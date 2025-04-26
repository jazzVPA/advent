SNAFU_to_dec = {'2': 2, '1': 1, '0': 0, '-': -1, '=':-2}
dec_to_SNAFU = {i: j for j, i in SNAFU_to_dec.items()}

def convert_dec_to_SANFU(number: int) -> str:
    if number == 0:
        return '0'

    SNAFU = []
    while number != 0:
        number, remainder = divmod(number + 2 , 5)
        SNAFU.append(dec_to_SNAFU[remainder - 2])
    return ''.join(reversed(SNAFU))
