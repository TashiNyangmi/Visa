from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# from filter_for_app import visa_filter



app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    import pandas as pd
    master_df = pd.read_csv('data_cleaning/master_df.csv')
    countries = list(master_df['country'].unique())
    years = ['2017', '2018', '2019', '2020']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']
    visa_types = list(master_df['visa_type'].unique())

    # adding the option to view all to each filter category
    countries.insert(0, 'all')
    years.insert(0, 'all')
    months.insert(0, 'all')
    visa_types.insert(0, 'all')

    if request.method == 'POST':
        # Get input from user
        returned_country = request.form['country']
        returned_year = request.form['year']
        returned_month = request.form['month']
        returned_visa_type = request.form['visa_type']

        from filter_for_app import visa_filter
        result = visa_filter(returned_country, returned_year, returned_month, returned_visa_type)

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
