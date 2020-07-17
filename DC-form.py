import tkinter as tk
import xlsxwriter
import inflect
from openpyxl import Workbook
from functools import partial

root=tk.Tk()
root.title("DC")
sln=[]
hsn=[]
desc=[]
qty=[]
uom=[]
rate=[]


def add(e1):
    n=e1.get()
    x=int(n)
    i=1
    #master=tk.Toplevel(root)
    tk.Label(root,text="S.N.").grid(row=1,column=0)
    tk.Label(root,text="HSN Code").grid(row=1,column=1)
    tk.Label(root,text="Goods/ Services Description").grid(row=1,column=2)
    tk.Label(root,text="Qty").grid(row=1,column=3)
    tk.Label(root,text="UOM").grid(row=1,column=4)
    tk.Label(root,text="Unit Rate (INR)").grid(row=1,column=5)
    while(i<=x):
            sln.append(i)
            tk.Label(root,text=i).grid(row=i+1,column=0)
            e2=tk.Entry(root)
            e2.grid(row=i+1,column=1)
            hsn.append(e2)
            e3=tk.Entry(root)
            e3.grid(row=i+1,column=2)
            desc.append(e3)
            e4=tk.Entry(root)
            e4.grid(row=i+1,column=3)
            qty.append(e4)
            e5=tk.Entry(root)
            e5.grid(row=i+1,column=4)
            uom.append(e5)
            e6=tk.Entry(root)
            e6.grid(row=i+1,column=5)
            rate.append(e6)
            i+=1
    tk.Button(root,text='Next',command=wb).grid(row=0,column=3)
def wb():
    cnt=len(sln)
    wb=Workbook()
    ws=wb.active
    workbook = xlsxwriter.Workbook('C:\\Users\\20031748\\Desktop\\DC1.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 11.57)
    worksheet.set_column('B:B', 19.29)
    worksheet.set_column('C:C', 8.29)
    worksheet.set_column('D:D', 35.57)
    worksheet.set_column('E:E', 6.29)
    worksheet.set_column('F:F', 5.71)
    worksheet.set_column('G:G', 12.14)
    worksheet.set_column('H:H', 30.86)
                                                            

    merge_frm1= workbook.add_format({'bold': 1,'border': 1,'align': 'center','valign': 'vcenter'})
    merge_frm2= workbook.add_format({'bold': 1,'border': 1,'align': 'right','valign': 'vcenter'})
    merge_frm3= workbook.add_format({'bold': 1,'border': 1,'align': 'left','valign': 'vcenter'})
    merge_frm4= workbook.add_format({'bold': 1,'border': 1,'align': 'left','valign': 'top'})
    merge_frm4.set_text_wrap()
    brdr_frm=workbook.add_format()
    brdr_frm.set_border(1)
    bold=workbook.add_format()
    bold.set_bold()
    worksheet.merge_range('A1:H1','Delivery Challan',merge_frm1)
    worksheet.merge_range('A2:H2','Original/Duplicate/Triplicate',merge_frm2)
    worksheet.merge_range('B11:C11','State:Karnataka',merge_frm3)
    worksheet.merge_range('E11:G11','State:Karnataka',merge_frm3)
    From=["Shipper / Exporters:","L&T Technology Services Limited - SEZ Unit II.,","“Hazel-Block L3”, Ground to 3rd Floors,","Manyata Embassy Business Park,","Nagawara Hobli, Outer Ring Road,","Bangalore - 560045","GST # 29AACCL4310P1Z9"]
    cl_H=["DC No.:LTTS/SEZ-II/024/2018","DC Date: 23.04.2019","Client Code:","Job Code:","Sales Order No.:","Place of Supply: Bangalore"]
    TnC="Other Terms & Conditions:The Above Items are sent for repeir & return purpose on Returnable basis and these items are not for Sale."
    bom=["S.N.","HSN Code","Goods/ Services Description","Qty","UOM","Unit Rate (INR)","Taxable Value(INR)"]
    po=['PO No.:','PO Date:']
    pay="Payment/Delivery Terms:"
    #payment
    ws.insert_rows(15,amount=cnt)
                                                            

    worksheet.write_column('A3',From)
    worksheet.write_column('H3',cl_H)
    
    worksheet.write('A11','SC: 29')
    worksheet.write('D11','SC: 29')
    worksheet.merge_range('A13:A14','S.N',merge_frm1)
    worksheet.merge_range('B13:B14','HSN Code',merge_frm1)
    worksheet.merge_range('C13:D14','Goods/ Services Description',merge_frm1)
    worksheet.merge_range('E13:E14','Qty',merge_frm1)
    worksheet.merge_range('F13:F14','UOM',merge_frm1)
    worksheet.merge_range('G13:G14','Unit Rate (INR)',merge_frm1)
    worksheet.merge_range('H13:H14','Taxable Value(INR)',merge_frm1)
    worksheet.merge_range('A15:G15','Total Amount of Taxable Value',merge_frm1)
    worksheet.merge_range('A26:E32',TnC,merge_frm4)
    i=26
    #worksheet.write_formula('Hi', '=SUM(H15:H26)')
    worksheet.write_column('H11',po)


    c=0
    r=12
    #while (c<=7):
        #if (c==2 or c==3):
         #   worksheet.merge_range('C13:D14','',merge_frm1)
        #else:
        #    worksheet.merge_range(r,c,r+1,c,'',merge_frm1)
        #c+=1
    #worksheet.merge_range('C13:D13','temp',merge_frm1)
    #worksheet.write_row('A13',bom)
    worksheet.conditional_format( 'H3:H10' , { 'type' : 'no_blanks' , 'format' : merge_frm1} )
    worksheet.conditional_format( 'A3:C10' , { 'type' : 'no_blanks' , 'format' : brdr_frm} )
    worksheet.conditional_format( 'D3:G10' , { 'type' : 'no_blanks' , 'format' : brdr_frm} )
    worksheet.conditional_format( 'H3:H10' , { 'type' : 'no_blanks' , 'format' : merge_frm3} )
    worksheet.conditional_format( 'H3:H10' , { 'type' : 'no_blanks' , 'format' : bold} )


    workbook.close()


tk.Label(root,text="Number of Parts").grid(row=0,column=0)
e1=tk.Entry(root)
e1.grid(row=0,column=1)
tk.Button(root,text='Add',command=partial(add,e1)).grid(row=0,column=2)
tk.Button(root,text="Close",command=root.destroy).grid(row=0, column=4)
root.mainloop()
