def pdf_to_csv(input_file, output_file):
    """converts PDF to CSV (includes errors handling)"""
    import tabula
    try:
        tabula.convert_into(input_file, output_file, pages="all")
    except FileNotFoundError:
        print(f'{input_file} not found')
    return


# ----------------------------------------------------------------------------------


def pdf_to_json(input_file, output_file):
    import tabula
    import json
    tabula.convert_into(input_file, output_file, output_format="json", pages="all")

# stores all tables in the pdf in a list as DataFrames
# tables = tabula.read_pdf(input_file, pages="all", multiple_tables=True)

# ------------------------------------------------------------------------------------
# converts a PDF file directly into a CSV

# the first page in a PDF
# tabula.convert_into(file, "pdf/doubleeyes.csv")

# all the pages in a PDF
# output_file = "pdf_raw/OCTOBER%202020%20-%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class.csv"
# tabula.convert_into(input_file, output_file, pages="all")

# all the pages in all PDFs in a Directory
# tabula.convert_into_by_batch("/path/to/files", output_format = csv, pages = "all")

# ----------------------------------------------------------------------
# we can perform the same operation, except drop the files out to JSON instead, like below:
# tabula.convert_into_by_batch("/path/to/files", output_format = "json", pages = "all")
