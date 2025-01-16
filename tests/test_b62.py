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
        (654321, "2Kdz"),
    ],
)
def test_encode_and_decode_match(integer, string) -> None:
    encoded_integer = b62.encode(integer)
    assert encoded_integer == string

    decoded_string = b62.decode(encoded_integer)
    assert decoded_string == integer
