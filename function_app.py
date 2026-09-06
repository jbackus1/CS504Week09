import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def calculate_age(year, month, day):
    today = datetime.date.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    return age

@app.route(route="http_trigger", methods=["GET", "POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    year = req.params.get("year")
    month = req.params.get("month")
    day = req.params.get("day")

    if not (year and month and day):
        try:
            body = req.get_json()
        except ValueError:
            body = {}
        year = year or body.get("year")
        month = month or body.get("month")
        day = day or body.get("day")

    if not (year and month and day):
        return func.HttpResponse(
            "Pass year, month, and day in the query string or JSON body.",
            status_code=400,
        )

    try:
        age = calculate_age(int(year), int(month), int(day))
    except ValueError:
        return func.HttpResponse("Invalid date.", status_code=400)

    return func.HttpResponse(
        json.dumps({"age": age, "message": f"Your age is: {age}"}),
        mimetype="application/json",
        status_code=200,
    )