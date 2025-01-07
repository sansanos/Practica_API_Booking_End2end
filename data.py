auth_body = {
    "username" : "admin",
    "password" : "password123"
}

create_body = {
    "firstname" : "San",
    "lastname" : "San",
    "totalprice" : 200,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "NoBreakfast"
}

put_body = {
    "firstname" : "Santi",
    "lastname" : "Sanchez",
    "totalprice" : 250,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

