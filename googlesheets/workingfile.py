import gspread

gc=gspread.service_account(filename='code.json')
sh=gc.open('scrapetosheet').sheet1

sh.append_row(["first","second","third"])