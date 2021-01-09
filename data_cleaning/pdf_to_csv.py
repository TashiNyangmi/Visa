def pdf_to_csv(input_file, output_file):
    """converts PDF to CSV (includes errors handling)"""
    import tabula
    try:
        tabula.convert_into(input_file, output_file, pages="all")
    except FileNotFoundError:
        print(f'{input_file} not found')
    return


# ================================================================== #
pdf_to_csv("Nonimmigrant Visa Symbols.pdf", "nivisa_symbols.csv")
