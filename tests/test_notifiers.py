from panic_bracelet.notifiers import send_telegram

def test_send_telegram():
    status = send_telegram("Test message")
    assert status == 200
