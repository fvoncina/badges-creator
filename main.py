import csv
import os
import segno
import pdfkit

#constants
__OUTPUT_FOLDER__ = "output"

def main():

    # create output folder
    if not os.path.exists(__OUTPUT_FOLDER__):
        os.makedirs(__OUTPUT_FOLDER__)


    print("Opening data.csv...")
    with (open("data.csv", mode='r', encoding='utf-8') as csv_file):
        csv_reader = csv.reader(csv_file)

        # assuming first row contains column names
        next(csv_reader)

        # load template html
        with open(os.path.join("template", "template.html"), 'r', encoding='utf-8') as html_file:
            html_contents = html_file.read()

        for row in csv_reader:
            manager = row[0]
            first_name = row[1]
            last_name = row[2]
            link = row[3]
            print("Processing {0} - {1} {2}".format(manager, first_name, last_name))
            manager_out_folder = os.path.join(__OUTPUT_FOLDER__, manager)
            out_file = os.path.join(manager_out_folder, "{0}-{1}.pdf".format(first_name, last_name))
            if not os.path.exists(manager_out_folder):
                os.makedirs(manager_out_folder)
            print("\tOut pdf: {0}".format(out_file))

            # create qr
            qr_code = segno.make(link)
            qr_svg = qr_code.svg_inline(scale=4)

            # replace on template
            html_row_content = html_contents.replace("[FIRST_NAME]", first_name).replace("[LAST_NAME]", last_name).replace("[QR]", qr_svg)

            # generate pdf
            pdfkit.from_string(html_row_content, out_file)


if __name__ == "__main__":
    main()