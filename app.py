from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    # importing lists of options for dropdown(select) elements of the form
    from lists_for_app import lists
    countries, years, months, visa_types = lists()

    if request.method == 'POST':
        # Get input from user
        returned_country = request.form['country']
        returned_year = request.form['year']
        returned_month = request.form['month']
        returned_visa_type = request.form['visa_type']

        from filter_for_app import visa_filter
        try:
            result = visa_filter(returned_country, returned_year, returned_month, returned_visa_type)
        except:
            result = 0

        try:
            return render_template('index.html',
                                   returned_country=returned_country,
                                   returned_year=returned_year,
                                   returned_month=returned_month,
                                   returned_visa_type=returned_visa_type,
                                   countries=countries,
                                   years=years,
                                   months=months,
                                   visa_types=visa_types,
                                   result=result)
        except:
            redirect('/')
    else:  # this is for request.method = 'GET' i.e. ~ loading the homepage for the first time
        return render_template('index.html',
                               countries=countries,
                               months=months,
                               years=years,
                               visa_types=visa_types)


if __name__ == "__main__":
    app.run(debug=True)
