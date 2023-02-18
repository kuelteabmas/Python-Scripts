from docxtpl import DocxTemplate
from openpyxl import load_workbook

def iterating_column(path, sheet_name, col):
    # Import template document
    template = DocxTemplate('avery-template-1.docx')

    workbook = load_workbook(filename=path)
    if sheet_name not in workbook.sheetnames:
        print(f"'{sheet_name}' not found. Quitting.")
        return
        
    sheet = workbook[sheet_name]
    for cell in sheet[col]:

        # replace chars in fetched cell result
        cellData = cell.value

        s = str(cellData)
        s.translate({ord('\''):None})
        print(s)

        # Declare template variables
        context = {
            'name': s
        }

        # Copy data from variables to template variables
        template.render(context)

        # Write changes to new document
        fileName = "%s Type.docx"%(s)
        template.save(fileName)

if __name__ == "__main__":
    iterating_column("label-names.xlsx", sheet_name="Sheet1", col="A")
