import pandas as pd
from openpyxl import load_workbook

# Read the text file
print(f"Reading input file ")

with open('input.txt', 'r') as file:
    lines = file.readlines()

## Remove the word "type", punctuation and extra spacing from each line
lines = [line.replace(' type ', '').replace(' type', '').replace(':', ' ').replace('  ', ' ').replace('  ', ' ').strip() for line in lines]


# Write modified lines to a text file
with open('output.txt', 'w') as file:
    file.writelines(lines)

print(f"Output text file created")

# Create a DataFrame with the lines
df = pd.DataFrame({'Items': lines})

# Write DataFrame to an Excel file
df.to_excel('output.xlsx', index=False, header=False)

print(f"Output Excel file created")