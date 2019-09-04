from django.shortcuts import render
import xlwt
# now-django-example/example_app/views.py
from datetime import datetime
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = '''
    <html>
        <body>
            <h1>Hello from Zeit Now!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

# def dlxl(request):
#     return HttpResponse('dlxl')




def dlxl(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    #decide file name
    response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

    #creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    #adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    #column header names, you can use your own headers here
    columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]

    #write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    #get your data, from database or from a text file...
#     data = get_data() #dummy method to fetch data.
    for my_row in [('a','b','c','d'),('a','b','c','d')]:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row[0], font_style)
        ws.write(row_num, 1, my_row[1], font_style)
        ws.write(row_num, 2, my_row[2], font_style)
        ws.write(row_num, 3, my_row[3], font_style)

    wb.save(response)
    return response


