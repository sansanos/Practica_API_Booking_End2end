import request

def possitive_assert(response):
    code = response.status_code
    assert code == 200

def test_booking_id():
    response = request.get_booking_ids()
    possitive_assert(response)

def test_booking():
    response = request.get_booking()
    possitive_assert(response)

def test_create_booking():
    response = request.post_create_booking()
    possitive_assert(response)

