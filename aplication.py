from flask import Flask

app = Flask("Aplicatia Mea")

@app.route("/")
def index():
    return "<h1>Salut</h1>"

@app.route("/contact")
def contact():
    with open("contact.html") as f:
        return f.read()

visit = 0
@app.route("/counter")
def count_visit():
    global visit
    visit +=1 
    return f"am fost vizitate de {visit} ori"

@app.route("/salut/<nume>")
def salut(nume):
    return f"Salut {nume}"

sales_counter ={
    "google": 0,
    "facebook": 0
}
@app.route("/<channel>")
def lead(channel):
    global sales_counter
    try:
        sales_counter[channel] += 1
    except KeyError:
        sales_counter[channel] = 1
    return sales_counter

    # if channel == "google":
    #     sales_counter["google"] += 1
    #     return sales_counter
    # elif channel == "facebook":
    #     sales_counter["facebook"] += 1
    #     return sales_counter
    # else:
    #     sales_counter.append(channel)
    #     return sales_counter

if __name__ == "__main__":
    app.run()