from pdfrw import PdfWriter, PdfReader, PageMerge
from pdfrw.objects.pdfname import PdfName
from pdfrw.objects.pdfstring import PdfString
from pdfrw.objects.pdfdict import PdfDict
from pdfrw.objects.pdfarray import PdfArray
from weasyprint import HTML
from django.template.loader import get_template
from django.conf import settings
from generate_components import make_field, make_js_action, make_page
import json
import weasyprint
settings.configure()

#Page positions
PAGE_WIDTH = 612
PAGE_HEIGHT = 792
CANVAS_WIDTH = 612
CANVAS_HEIGHT = 400
CANVAS_BOTTOM = PAGE_HEIGHT - CANVAS_HEIGHT

# Json quote file test
quotesJson = {
    "id" : "001",
    "quote" : "00010",
    "date" : "01-01-2021",
    "quotes":[
        {"id":"1", "productName": "HEXAGONKNOB_V3", "dimensions": "63.500 x 54.993 X 38.100 MM ", "material": "C360 Brass", "parttol":"+/-0.005", "holetol":"+/-0.005", "finish":"Deburr", "coating":"None", "unitPrice":"77.12", "qty":"300","totalPrice":"23,236.00","leadTime":"25"},
        {"id":"2", "productName": "HEXAGONKNOB_V3", "dimensions": "63.500 x 54.993 X 38.100 MM ", "material": "C360 Brass", "parttol":"+/-0.005", "holetol":"+/-0.005", "finish":"Deburr", "coating":"None", "unitPrice":"77.12", "qty":"300","totalPrice":"23,236.00","leadTime":"25"},
        {"id":"3", "productName": "HEXAGONKNOB_V3", "dimensions": "63.500 x 54.993 X 38.100 MM ", "material": "C360 Brass", "parttol":"+/-0.005", "holetol":"+/-0.005", "finish":"Deburr", "coating":"None", "unitPrice":"77.12", "qty":"300","totalPrice":"23,236.00","leadTime":"25"},
        {"id":"4", "productName": "HEXAGONKNOB_V3", "dimensions": "63.500 x 54.993 X 38.100 MM ", "material": "C360 Brass", "parttol":"+/-0.005", "holetol":"+/-0.005", "finish":"Deburr", "coating":"None", "unitPrice":"77.12", "qty":"300","totalPrice":"23,236.00","leadTime":"25"},
        {"id":"5", "productName": "HEXAGONKNOB_V3", "dimensions": "63.500 x 54.993 X 38.100 MM ", "material": "C360 Brass", "parttol":"+/-0.005", "holetol":"+/-0.005", "finish":"Deburr", "coating":"None", "unitPrice":"77.12", "qty":"300","totalPrice":"23,236.00","leadTime":"25"},
    ]
}

fields = []

# Add table headers
productNameHeader = make_field('productNameHeader', x=50, y=PAGE_HEIGHT - 150, width=80, height=20, r=0.9, g=0.9, b=0.9)
fields.append(productNameHeader)
dimensionsHeader = make_field('dimensionsHeader', x=130, y=PAGE_HEIGHT - 150, width=80, height=20, r=0.9, g=0.9, b=0.9)
fields.append(dimensionsHeader)
materialHeader = make_field('materialHeader', x=210, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(materialHeader)
parttolHeader = make_field('parttolHeader', x=250, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(parttolHeader)
holetolHeader = make_field('holetolHeader', x=290, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(holetolHeader)
finishdHeader = make_field('finishHeader', x=330, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(finishdHeader)
coatingHeader = make_field('coatingHeader', x=370, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(coatingHeader)
unitPriceHeader = make_field('unitPriceHeader', x=410, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(unitPriceHeader)
qtyHeader = make_field('qtyHeader', x=450, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(qtyHeader)
totalPriceHeader = make_field('totalPriceHeader', x=490, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(totalPriceHeader)
leadTimeHeader = make_field('leadTimeHeader', x=530, y=PAGE_HEIGHT - 150, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(leadTimeHeader)

#Filling data table
positionY = PAGE_HEIGHT - 170
positionX = 50
for quote in quotesJson['quotes']:
    print (quote['productName'])
    fieldTest = make_field('productName-%s' % (quote['id']), x=50, y=positionY, width=80, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    fieldTest = make_field('dimensions-%s' % (quote['id']), x=130, y=positionY, width=80, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    fieldTest = make_field('material-%s' % (quote['id']), x=210, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    fieldTest = make_field('parttol-%s' % (quote['id']), x=250, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    fieldTest = make_field('holetol-%s' % (quote['id']), x=290, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    fieldTest = make_field('finish-%s' % (quote['id']), x=330, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    fieldTest = make_field('coating-%s' % (quote['id']), x=370, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    fieldTest = make_field('unitPrice-%s' % (quote['id']), x=410, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9,)
    fields.append(fieldTest)
    fieldTest = make_field('qty-%s' % (quote['id']), x=450, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9, typeField=2)
    fields.append(fieldTest)
    fieldTest = make_field('totalPrice-%s' % (quote['id']), x=490, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    fieldTest = make_field('leadTime-%s' % (quote['id']), x=530, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9)
    fields.append(fieldTest)
    positionY = positionY - 20

fieldSubtotal = make_field('subtotal', x=420, y=positionY, width=70, height=20, r=0.9, g=0.9, b=0.9)
fields.append(fieldSubtotal)
fielGrandTotal = make_field('grandTotal', x=410, y=positionY-20, width=80, height=20, r=0.9, g=0.9, b=0.9)
fields.append(fielGrandTotal)
fieldSubtotalRes = make_field('subtotalRes', x=490, y=positionY, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(fieldSubtotalRes)
fieldGRandTotalRes = make_field('grandTotalRes', x=490, y=positionY-20, width=40, height=20, r=0.9, g=0.9, b=0.9)
fields.append(fieldGRandTotalRes)


fields.append(make_field(
    'whole', x=0, y=CANVAS_BOTTOM,
    width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
    r=1, g=1, b=1
))

with open('rules.js', 'r') as js_file:
    script = js_file.read()

# Share our constants with the JS script.
page = make_page(fields, """

var CANVAS_WIDTH = %(CANVAS_WIDTH)s;
var CANVAS_HEIGHT = %(CANVAS_HEIGHT)s;
var CANVAS_BOTTOM = %(CANVAS_BOTTOM)s;
var quotesJson = "%(quotesJson)s";
%(script)s

""" % locals())

out = PdfWriter()
out.addpage(page)
out.write('testPdf.pdf')

pdf = weasyprint.HTML('../core/templates/layout_print.html').write_pdf()
open('head.pdf', 'wb').write(pdf)
base_pdf = PdfReader("testPdf.pdf")
watermark_pdf = PdfReader("head.pdf")
mark = watermark_pdf.pages[0]
    
for page in range(len(base_pdf.pages)):
    merger = PageMerge(base_pdf.pages[page])
    merger.add(mark).render()
  
writer = PdfWriter()
writer.write("final.pdf", base_pdf)
