def pdf_downloader(url, folder_location, download_list):
    """Download pdfs from the target url,
    Note: This function is customized for NI VISA monthly stats webpage"""
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

        # Only download the file(from source) if it is in the download_list
        if filename.split('\\')[-1][0:-4] in download_list:
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(url, link['href'])).content)

            print(f'{filename} is downloaded...')

    print("All files downloaded")
    return

# ================================================================== #
