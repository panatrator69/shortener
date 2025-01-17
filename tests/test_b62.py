"""Unit tests for the base62 encoding module."""

import pytest

from shortener import b62


@pytest.mark.parametrize(
    "integer,string",
    [
        (0, "0"),
        (1, "1"),
        (5, "5"),
        (10, "a"),
        (61, "Z"),
        (62, "10"),
        (63, "11"),
        (654321, "2Kdz"),
        # When all bits are flipped
        (62**1, str(10**1)),
        (62**12, str(10**12)),
        (62**24, str(10**24)),
    ],
)
def test_encode_and_decode_match(integer, string) -> None:
    encoded_integer = b62.encode(integer)
    assert encoded_integer == string

    decoded_string = b62.decode(encoded_integer)
    assert decoded_string == integer
