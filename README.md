# Report-Generator

An automator app for converting pdf to image, scraping some values from them and write to excel files.
This semi-automation application are including a program to:
1. Save attachment from outlook (the report is received on my outlook app). The whole process of this program is using pyautogui library. -- This can be achieved by running attachmentSaver.py
2. To check where is my pointer coordinate on my screen. -- This can be achieved by running checkPointer.py
3. Take a screenshot of any graph. At first, when we want to create a report we have to manually open the monitoring network server via web browser which only can be accessed through remote connection via AnyDesk/Team Viewer. Making this caputer of graph is automatically by screenshotGraphPRTG.py. (deprecated and replaced by the bot WhatsApp on my Selenium project).
4. Creating a ordered-list name files by using renaming.py. This works only on finder on MacOS.
5. The whole process of making this report is by using these program: '
  o) sbpdf2img.py --> is to convert the document file (pdf) to image file (png) and cropped only for the table section in a page.
  o) percentileFinder.py --> is to search the percentile value from the previous cropped image file.
  o) excelAuto.py --> is to fill the excel sheet (template report) which automatically insert images on each specified area and insert values on the specified fields.


The flow of this app is:
1. The raw data on pdf files (as default generated from network monitoring app).
2. A template of excel that to be filled in automatically.
3. From the raw data (1) the table section is scrapped for each ID. This process is converting the pdf page into image then cropped on the specific area (the table that we want to scrap).
4. After the image of table is crated, by using OCR by pytesseract, some data value are generated.
5. The data will be transfered into the template of excel (2) including the cropped image from pdf (3) in the specified cells and row.
