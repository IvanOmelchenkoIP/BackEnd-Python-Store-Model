from backend import app

@app.route("/newuser", methods = ["POST"])
def create_user():
    pass

@app.route("/newcategory", methods = ["POST"])
def create_category():
    pass

@app.route("/newrecord", methods = ["POST"])
def create_record():
    pass

@app.route("/categories")
def get_categories():
    pass

@app.route("/userrecords")
def get_records_by_user():
    pass

@app.route("/categoryrecords")
def get_records_by_category():
    pass