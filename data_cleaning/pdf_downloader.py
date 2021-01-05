# Problems:
# In the target webpage, some files names have typos
# -- Hence, pdf for some years were not downloaded
# -- -- 1)October 2019
# -- -- -- filename is missing characters '-20%'
# -- -- -- '...202019%20NIV...' instead of '...202019%20-%20NIV...'
# ''' Downloaded and renamed manually '''

# -- -- 2)December 2017
# -- -- -- filename is missing the character 'a'
# -- -- --  'nationlity' instead of 'nationality'
# ''' Downloaded and renamed manually '''

# -- -- 3)September 2020
# -- -- -- filename is missing characters 'EMBER'
# -- -- -- 'SEPT...' instead of 'SEPTEMBER...'
# ''' Did something, can't remember'''

url = "https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics/nonimmigrant-visa-statistics/monthly-nonimmigrant-visa-issuances.html"

folder_location = r'C:\Users\Tashi Nyangmi\Desktop\visa\data_cleaning\pdf_raw'


def pdf_downloader(URL, location):
    import os
    import requests
    from urllib.parse import urljoin
    from bs4 import BeautifulSoup

    # If there is no such folder, the script will create one automatically
    if not os.path.exists(folder_location):
        print(f'{folder_location} not found')
        print('New folder created')
        os.mkdir(folder_location)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select("a[href$='%20-%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class.pdf']"):
        # Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location, link['href'].split('/')[-1])
        # shortening the filename by 'subtracting' the suffix
        suffix = '%20-%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class'
        filename = filename.replace(suffix, '')
        filename = filename.replace('%20', '_')  # replacing %20 with _ (e.g. april%202019 becomes april_2019)
        filename = filename.lower()

        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link['href'])).content)

        print(f'{filename} is downloaded...')
    print("All files downloaded")
    return


pdf_downloader(URL=url, location=folder_location)
