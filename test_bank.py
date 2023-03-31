import bank

def main():
    test_bank()

def test_bank():
    assert bank.value('Hello') == '$0'
    assert bank.value('Hi') == '$20'
    assert bank.value('gamarjoba') == '$100'


if __name__ == "__main__":
    main()