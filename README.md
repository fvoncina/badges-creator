# Requirements
Python 3

- Install segno  
`python -m pip install segno`

- Install pdfkit  
`python -m pip install pdfkit`  

- Install wkhtmltopdf  

  - Windows:  
  Download from: http://wkhtmltopdf.org/downloads.html
  - Linux:  
  `sudo apt-get install wkhtmltopdf`
  - Mac:  
  `brew install wkhtmltopdf`  


# CSV File

The csv file need to be at `./data.csv`, same folder as the .py file.  

Should have this structure:  
- First row contains column names
- 1 Column the Manager Code
- 2 Column the First Name
- 3 Column the Last Name
- 4 Column the Link

See `data.csv` for reference  

# Template  

The template file should be at `./template/template.html`. 
The images should be embedded as base64.  

# Output  
The program will create an `output` folder.  
Within the `output` folder the program will create a folder for each manager, inside the manager folder the pdfs will be written.  

# Usage  
`python main.py`





