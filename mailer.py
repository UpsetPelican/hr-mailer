import yagmail
import datetime
import pyexcel as pe

# Puts template in email_template var
with open("mail-template.txt") as mt:
    email_template = mt.read()

# Puts database in sheet
sheet = pe.get_sheet(file_name="database.xlsx")

# Start yagmail instance
yag = yagmail.SMTP("ucoria@itexico.net")

# Parse the document, if [item,3] empty: send mail; else: skip.
for index, item in enumerate(sheet):
    if sheet[index,3] == "":
        txt = email_template.format(name=sheet[index,1],position=sheet[index,2])
        contents = [txt]
        timestamp = datetime.datetime.now().strftime("%d/%b/%y, %H:%M")
        sheet[index,3] = timestamp
        yag.send(sheet[index,0],"{} position available!".format(sheet[index,2]),contents)

sheet.save_as("database.xlsx")
print "Success!"
raw_input("Press enter to continue...")
