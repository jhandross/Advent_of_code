DIGITS = "=-012"
SNAFU_BASE = len(DIGITS)
ZERO_OFFSET = DIGITS.index("0")


def parse_snafu(snafu: str) -> int:
    num = 0
    for digit in snafu:
            num *= SNAFU_BASE
            num += DIGITS.index(digit) - ZERO_OFFSET
    return num


def to_snafu(num: int) -> str:
    snafu = ""
    while num:
        shifted_index = (num + ZERO_OFFSET) % SNAFU_BASE
        snafu += DIGITS[shifted_index]
        if shifted_index < ZERO_OFFSET:
            num += SNAFU_BASE
        num //= SNAFU_BASE
    return snafu[::-1]


input = open("25.txt").read().splitlines()
print(to_snafu(sum(parse_snafu(snafu) for snafu in input)))