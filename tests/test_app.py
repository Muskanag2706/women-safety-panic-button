from panic_bracelet.app import load_contacts

def test_load_contacts():
    contacts = load_contacts()
    assert isinstance(contacts, list)
    assert "name" in contacts[0]
    assert "phone" in contacts[0]
