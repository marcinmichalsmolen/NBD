printjson(db.people.find({ $where: function () { return this.birth_date > "2000-01-01T00:00:00Z" } }, { "first_name": 1, "last_name": 1, "location": { "city": 1 } }).toArray())
