printjson(db.people.insertOne({
    "sex" : "Male",
    "first_name" : "Marcin",
    "last_name" : "Smolen",
    "job" : "Specialist in Analyses and Strategy Department",
    "email" : "marcin@xware.pl",
    "location" : {
            "city" : "Warsaw",
            "address" : {
                    "streetname" : "Sieciechowska",
                    "streetnumber" : "1"
            }
    },
    "description" : "Debian Linux",
    "height" : "184",
    "weight" : "100",
    "birth_date" : "1979-12-15T18:10:03Z",
    "nationality" : "Polish",
    "credit" : [
            {
                    "type" : "mastercard",
                    "number" : "452828939100098699",
                    "currency" : "PLN",
                    "balance" : "20000.00"
            }
    ]
}))