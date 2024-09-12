import os

def formatParagraphs():
    print("Cleaning up paragraphs....")
    
    # Read the text file
    print(f"Reading input file...")

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    lines = [line.replace('\n', ' ') for line in lines]
    lines = [line.replace('(Risas)', '\n\n') for line in lines]

    # Write modified lines to a text file
    with open('formatted_paragraphs.txt', 'w') as file:
        file.writelines(lines)
    
    print("Output text file created")
    print("Done.")


if __name__ == "__main__":
    formatParagraphs()