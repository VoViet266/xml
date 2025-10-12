import os
from lxml import etree


# Lấy đường dẫn đến file XML
currentDirectory = os.path.dirname(os.path.realpath(__file__))
xmlFilePath = os.path.join(currentDirectory, 'sinhvien.xml')
xmlFile = etree.parse(xmlFilePath).getroot()

# --- Các câu truy vấn XPath ---

print('Lấy tất cả sinh viên:')
# /school/student
students = xmlFile.xpath('/school/student')
for student in students:
    studentElement = etree.tostring(student, pretty_print=True, encoding='unicode')
    print(studentElement)
print('---\n')

print('Liệt kê tên tất cả sinh viên:')
# /school/student/name
student_names = xmlFile.xpath('/school/student/name/text()')
for name in student_names:
    print(name)
print('---\n')

print('Lấy tất cả id của sinh viên:')
# /school/student/id
student_ids = xmlFile.xpath('/school/student/id/text()')
for id_val in student_ids:
    print(id_val)
print('---\n')

print("Lấy ngày sinh của sinh viên có id = 'SV01':")
# /school/student[id='SV01']/date
dates = xmlFile.xpath("/school/student[id='SV01']/date/text()")
if dates:
    print(dates[0])
print('---\n')

print('Lấy các enrollment (thông tin đăng ký học):')
# /school/enrollment
enrollments = xmlFile.xpath('/school/enrollment')
for enrollment in enrollments:
    enrollmentElement = etree.tostring(enrollment, pretty_print=True, encoding='unicode')
    print(enrollmentElement)
print('---\n')


print('Lấy toàn bộ thông tin của sinh viên đầu tiên:')
# /school/student[1]
first_student = xmlFile.xpath('/school/student[1]')
if first_student:
    studentElement = etree.tostring(first_student[0], pretty_print=True, encoding='unicode')
    print(studentElement)
print('---\n')

print("Lấy mã sinh viên đăng ký khóa học 'Vatly203':")
# /school/enrollment[course='Vatly203']/studentRef
student_refs = xmlFile.xpath("/school/enrollment[course='Vatly203']/studentRef/text()")
for ref in student_refs:
    print(ref)
print('---\n')


print("Lấy tên sinh viên học môn 'Toan101':")
# /school/student[id = /school/enrollment[course='Toan101']/studentRef]/name
student_names_toan = xmlFile.xpath("/school/student[id = /school/enrollment[course='Toan101']/studentRef]/name/text()")
for name in student_names_toan:
    print(name)
print('---\n')


print("Lấy tên sinh viên học môn 'Vatly203':")
# /school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name
student_names_vatly = xmlFile.xpath("/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name/text()")
for name in student_names_vatly:
    print(name)
print('---\n')

print("Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997:")
# /school/student[starts-with(date, '1997')]/name | /school/student[starts-with(date, '1997')]/date
students_1997 = xmlFile.xpath("/school/student[starts-with(date, '1997')]")
for student in students_1997:
    name = student.find('name').text
    date = student.find('date').text
    print(f"- {name}, Ngày sinh: {date}")
print('---\n')


print("Lấy tên của các sinh viên có ngày sinh trước năm 1998:")
# /school/student[substring(date, 1, 4) < '1998']/name
names_before_1998 = xmlFile.xpath("/school/student[substring(date, 1, 4) < '1998']/name/text()")
for name in names_before_1998:
    print(name)
print('---\n')


print('Đếm tổng số sinh viên:')
# count(/school/student)
student_quantity = xmlFile.xpath("count(/school/student)")
print(f"Tổng số sinh viên là: {int(student_quantity)}")
print('---\n')

print('Lấy tất cả sinh viên chưa đăng ký môn nào:')
# /school/student[not(id = /school/enrollment/studentRef)]
unenrolled_students = xmlFile.xpath("/school/student[not(id = /school/enrollment/studentRef)]")
if unenrolled_students:
    for student in unenrolled_students:
        studentElement = etree.tostring(student, pretty_print=True, encoding='unicode')
        print(studentElement)
else:
    print("Tất cả sinh viên đều đã đăng ký ít nhất một môn học.")
print('---\n')

print("Lấy phần tử <date> anh em ngay sau <name> của SV01:")
# /school/student[id='SV01']/name/following-sibling::date
date_sibling = xmlFile.xpath("/school/student[id='SV01']/name/following-sibling::date")
if date_sibling:
    print(etree.tostring(date_sibling[0], pretty_print=True, encoding='unicode'))
print('---\n')

print("Lấy phần tử <id> anh em ngay trước <name> của SV02:")
# /school/student[id='SV02']/name/preceding-sibling::id
id_sibling = xmlFile.xpath("/school/student[id='SV02']/name/preceding-sibling::id")
if id_sibling:
    print(etree.tostring(id_sibling[0], pretty_print=True, encoding='unicode'))
print('---\n')

print("Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03':")
# /school/enrollment[studentRef='SV03']/course
courses_sv03 = xmlFile.xpath("/school/enrollment[studentRef='SV03']/course")
for course in courses_sv03:
    print(etree.tostring(course, pretty_print=True, encoding='unicode'))
print('---\n')


print('Lấy sinh viên có họ là “Trần”:')
# /school/student[starts-with(name, 'Trần')]
students_tran = xmlFile.xpath("/school/student[starts-with(name, 'Trần ')]")
if students_tran:
    for student in students_tran:
        studentElement = etree.tostring(student, pretty_print=True, encoding='unicode')
        print(studentElement)
else:
    print("Không tìm thấy sinh viên nào có họ Trần.")
print('---\n')


print('Lấy năm sinh của sinh viên SV01:')
# substring(/school/student[id='SV01']/date, 1, 4)
birth_year = xmlFile.xpath("substring(/school/student[id='SV01']/date, 1, 4)")
print(f"Năm sinh: {birth_year}")
print('---\n')