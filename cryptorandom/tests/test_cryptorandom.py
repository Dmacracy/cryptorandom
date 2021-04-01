"""Unit tests for cryptorandom PRNG"""

import numpy as np
from ..cryptorandom import SHA256, int_from_hash

def test_SHA256():
    """
    Test that SHA256 prng is instantiated correctly
    """
    r = SHA256(5)
    assert repr(r) == 'SHA256 PRNG. seed: 5 counter: 0 randbits_remaining: 0'
    assert str(r) == 'SHA256 PRNG. seed: 5 counter: 0 randbits_remaining: 0'

    assert r.getstate() == (5, 0, 0)
    r.next()
    assert r.getstate() == (5, 1, 0)
    r.jumpahead(5)
    assert r.getstate() == (5, 6, 0)
    r.seed(22)
    assert r.getstate() == (22, 0, 0)
    r.setstate(2345, 3)
    assert r.getstate() == (2345, 3, 0)
    r.randint(0, 100, 2)
    assert r.getstate() == (2345, 4, 242)