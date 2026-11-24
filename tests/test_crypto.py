import pytest

from src.crypto import check_key


def test_missing_key_raises(monkeypatch):
    monkeypatch.delenv("DROP_KEY", raising=False)
    with pytest.raises(RuntimeError):
        check_key()
