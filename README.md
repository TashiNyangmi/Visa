https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics/nonimmigrant-visa-statistics/monthly-nonimmigrant-visa-issuances.html

Problem:
Let us start with the problem we are trying to solve here. 
The problem we are trying to solve here is related to the data on Visa issuance by the United States around the world. The data is made public by the U.S., but it is not exactly convenient to look it up and access it, and even for those who find it, it is not really easy to skim through the entire data to find information we’re looking for.
So,  the solution is to build a webapp that allows users to access this data in a drastically convenient manner. 
That is the primary goal.
How did I do this?
1.	Data Scraping and Cleaning
a.	pdf_downloader
i.	Used beautiful soup to download all desired PDFs 
(one for each month: by country and visa_type)
b.	pdf_to_csv
i.	used library:tabula to convert PDFs to CSVs
c.	csv_clean
i.	Cleaned CSV
d.	data_cleaning_exceptions
i.	For inconsistent ……
e.	master_df
i.	to merge all monthly data into a single master DataFrame
2.	Flask Webapp
a.	
3.	Deployed to Heroku

What is next?
1.	Frontend:
a.	Bootstrapping
b.	Basic Visualizations
i.	Trends
ii.	….
2.	Multi selection feature:
a.	Select range of dates and months[slicing]
b.	Implement pivot tables

Issues/ Questions:
1.	Initial Loading time [Link]
2.	Filtering method [Link]
a.	Using index or column
i.	If index: 
1.	both date and country [multi – index]
2.	date
3.	…other
3.	Store master_df as csv
4.	Deploy it using AWS? [Link]
a.	If yes?
i.	For experience
ii.	Better overall?
iii.	…other reason
b.	If no?
i.	Reason:
5.	Am I even paying attention to the right things?
a.	I know it’s not ML related. It does not even include any analytics.
b.	How useful it in terms of showcasing my skills? Initiative taking?
c.	

