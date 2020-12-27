from filter_for_app import visa_filter

returned_country = 'Afghanistan'
returned_visa_type = 'A2'
returned_month = 'march'
returned_year = '2017'

result = visa_filter( returned_country, returned_year, returned_month, returned_visa_type)
print (result)