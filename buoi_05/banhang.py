import os
from lxml import etree

## Lấy đường dẫn đến file XML
currentDirectory = os.path.dirname(os.path.realpath(__file__))
xmlFilePath = os.path.join(currentDirectory, 'banhang.xml')
xmlFile = etree.parse(xmlFilePath).getroot()

print('Lấy tất cả bàn')
# /QUANLY/BANS/BAN
allTables = xmlFile.xpath('/QUANLY/BANS/BAN')
for table in allTables:
    print(etree.tostring(table, pretty_print=True, encoding='unicode').strip())
print('---\n')

print('Lấy tất cả nhân viên')
# /QUANLY/NHANVIENS/NHANVIEN
allEmployees = xmlFile.xpath('/QUANLY/NHANVIENS/NHANVIEN')
for employee in allEmployees:
    print(etree.tostring(employee, pretty_print=True, encoding='unicode').strip())
print('---\n')

print('Lấy tất cả tên món')
# /QUANLY/MONS/MON/TENMON
allDishNames = xmlFile.xpath('/QUANLY/MONS/MON/TENMON/text()')
for dishName in allDishNames:
    print(dishName)
print('---\n')

print("Lấy tên nhân viên có mã 'NV02'")
# /QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']/TENV
employeeName = xmlFile.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']/TENV/text()")
if employeeName:
    print(employeeName[0])
print('---\n')

print("Lấy tên và số điện thoại của nhân viên 'NV03'")
# /QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/TENV | /QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/SDT
employeeInfo = xmlFile.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/TENV | /QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/SDT")
for info in employeeInfo:
     print(etree.tostring(info, pretty_print=True, encoding='unicode').strip())
print('---\n')

print('Lấy tên món có giá > 50,000')
# /QUANLY/MONS/MON[GIA > 50000]/TENMON
expensiveDishes = xmlFile.xpath('/QUANLY/MONS/MON[GIA > 50000]/TENMON/text()')
for dishName in expensiveDishes:
    print(dishName)
print('---\n')

print("Lấy số bàn của hóa đơn 'HD03'")
# /QUANLY/HOADONS/HOADON[SOHD='HD03']/SOBAN
tableNumber = xmlFile.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD03']/SOBAN/text()")
if tableNumber:
    print(tableNumber[0])
print('---\n')

print("Lấy tên món có mã 'M02'")
# /QUANLY/MONS/MON[MAMON='M02']/TENMON
dishName = xmlFile.xpath("/QUANLY/MONS/MON[MAMON='M02']/TENMON/text()")
if dishName:
    print(dishName[0])
print('---\n')

print("Lấy ngày lập của hóa đơn 'HD03'")
# /QUANLY/HOADONS/HOADON[SOHD='HD03']/NGAYLAP
invoiceDate = xmlFile.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD03']/NGAYLAP/text()")
if invoiceDate:
    print(invoiceDate[0])
print('---\n')

print("Lấy tất cả mã món trong hóa đơn 'HD01'")
# /QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON
dishIdsInInvoice = xmlFile.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON/text()")
for dishId in dishIdsInInvoice:
    print(dishId)
print('---\n')

print("Lấy tên món trong hóa đơn 'HD01'")
# /QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON]/TENMON
dishNamesInInvoice = xmlFile.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON]/TENMON/text()")
for dishName in dishNamesInInvoice:
    print(dishName)
print('---\n')

print("Lấy tên nhân viên lập hóa đơn 'HD02'")
# /QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOHD='HD02']/MANV]/TENV
employeeNameForInvoice = xmlFile.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOHD='HD02']/MANV]/TENV/text()")
if employeeNameForInvoice:
    print(employeeNameForInvoice[0])
print('---\n')

print('Đếm số bàn')
# count(/QUANLY/BANS/BAN)
tableCount = xmlFile.xpath('count(/QUANLY/BANS/BAN)')
print(f'Tổng số bàn: {int(tableCount)}')
print('---\n')

print("Đếm số hóa đơn lập bởi 'NV01'")
# count(/QUANLY/HOADONS/HOADON[MANV='NV01'])
invoiceCountByEmployee = xmlFile.xpath("count(/QUANLY/HOADONS/HOADON[MANV='NV01'])")
print(f"Số hóa đơn NV01 đã lập: {int(invoiceCountByEmployee)}")
print('---\n')

print('Lấy tên tất cả món có trong hóa đơn của bàn số 2')
# /QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON
dishesOnTable2 = xmlFile.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON/text()")
for dishName in dishesOnTable2:
    print(dishName)
print('---\n')

print('Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3')
# /QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='3']/MANV]
employeesForTable3 = xmlFile.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='3']/MANV]")
for employee in employeesForTable3:
    print(etree.tostring(employee, pretty_print=True, encoding='unicode').strip())
print('---\n')

print('Lấy tất cả hóa đơn mà nhân viên nữ lập')
# /QUANLY/HOADONS/HOADON[MANV = /QUANLY/NHANVIENS/NHANVIEN[GIOITINH='Nữ']/MANV]
invoicesByFemaleEmployees = xmlFile.xpath("/QUANLY/HOADONS/HOADON[MANV = /QUANLY/NHANVIENS/NHANVIEN[GIOITINH='Nữ']/MANV]")
for invoice in invoicesByFemaleEmployees:
    print(etree.tostring(invoice, pretty_print=True, encoding='unicode').strip())
print('---\n')

print('Lấy tất cả nhân viên từng phục vụ bàn số 1')
# /QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='1']/MANV]
employeesForTable1 = xmlFile.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='1']/MANV]")
for employee in employeesForTable1:
    print(etree.tostring(employee, pretty_print=True, encoding='unicode').strip())
print('---\n')

print('Lấy tất cả món có số lượng gọi > 1 trong một lần gọi')
# /QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON/CTHDS/CTHD[SOLUONG > 1]/MAMON]
dishesOrderedMoreThanOnce = xmlFile.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON/CTHDS/CTHD[SOLUONG > 1]/MAMON]")
for dish in dishesOrderedMoreThanOnce:
    print(etree.tostring(dish, pretty_print=True, encoding='unicode').strip())
print('---\n')

print("Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'")
# /QUANLY/BANS/BAN[SOBAN = /QUANLY/HOADONS/HOADON[SOHD='HD02']/SOBAN]/TENBAN | /QUANLY/HOADONS/HOADON[SOHD='HD02']/NGAYLAP
tableAndDateForInvoice = xmlFile.xpath("/QUANLY/BANS/BAN[SOBAN = /QUANLY/HOADONS/HOADON[SOHD='HD02']/SOBAN]/TENBAN/text() | /QUANLY/HOADONS/HOADON[SOHD='HD02']/NGAYLAP/text()")
for item in tableAndDateForInvoice:
    print(item)
print('---\n')