# Report-Generator

An automator app for converting pdf to image, scraping some values from them and write to excel files.
The flow of this app is:
1. The raw data on pdf files (as default generated from network monitoring app).
2. A template of excel that to be filled in automatically.
3. From the raw data (1) the table section is scrapped for each ID. This process is converting the pdf page into image then cropped on the specific area (the table that we want to scrap).
4. After the image of table is crated, by using OCR by pytesseract, some data value are generated.
5. The data will be transfered into the template of excel (2) including the cropped image from pdf (3) in the specified cells and row.
6.
