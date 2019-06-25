import pytest
from is_disposable_email import check

popular_domains = [
    'google@gmail.com',
    'outlook@outlook.com',
    'hotmail@hotmail.com',
    'mail@mail.com',
    'yahoo@yahoo.com',
    'gmx@gmx.com',
    'protonmail@protonmail.com',
    'aol@aol.com',
    'apple@icloud.com'
]


@pytest.mark.parametrize("domain", popular_domains)
def test_popular_domains(domain):
    assert not check(domain)


def test_getnada():
    assert check('getnada@getnada.com')
