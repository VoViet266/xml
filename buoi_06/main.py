import mysql.connector
from lxml import etree

def validate_xml(xml_path, xsd_path):
        # Parse tệp XSD
        with open(xsd_path, 'rb') as f:
            xsd_doc = etree.XML(f.read())
        
        # Tạo XMLSchema object từ XSD
        xmlschema = etree.XMLSchema(xsd_doc)
      

        # Parse tệp XML
        with open(xml_path, 'rb') as f:
            xml_doc = etree.XML(f.read())
    

        # Validate XML với XSD
        xmlschema.assertValid(xml_doc)
        print("Tệp XML hợp lệ với XSD.")
        return xml_doc

def get_mysql_connection(host, user, password, database):
 
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Kết nối MySQL thành công.")
            return connection
    except mysql.connector.Error as e:
        print(f"Lỗi kết nối MySQL: {e}")
        return None

def create_tables(cursor):
    
    try:
        ## Lệnh SQL tạo bảng Categories
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Categories (
                id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """)
        # Lệnh SQL tạo bảng Products
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                currency VARCHAR(10) NOT NULL,
                stock INT NOT NULL,
                categoryRef VARCHAR(255),
                FOREIGN KEY (categoryRef) REFERENCES Categories(id)
            )
        """)
    except mysql.connector.Error as e:
        print(f"Lỗi khi tạo bảng: {e}")

def insert_data_from_xml(cursor, xml_doc):
    try:
     
        categories = xml_doc.xpath('//categories/category')
        print(f"Tìm thấy {len(categories)} categories.")
        
        sql_insert_category = """
            INSERT INTO Categories (id, name) 
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE name = VALUES(name)
        """
        for cat in categories:
            cat_id = cat.get('id')
            cat_name = cat.text
            cursor.execute(sql_insert_category, (cat_id, cat_name))
        products = xml_doc.xpath('//products/product')

      
        sql_insert_product = """
            INSERT INTO Products (id, name, price, currency, stock, categoryRef)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                name = VALUES(name), 
                price = VALUES(price), 
                currency = VALUES(currency), 
                stock = VALUES(stock), 
                categoryRef = VALUES(categoryRef)
        """
        for prod in products:
            prod_id = prod.get('id')
            prod_cat_ref = prod.get('categoryRef')
            prod_name = prod.find('name').text
            prod_price = prod.find('price').text
            prod_currency = prod.find('price').get('currency')
            prod_stock = prod.find('stock').text
            cursor.execute(sql_insert_product, (prod_id, prod_name, prod_price, prod_currency, prod_stock, prod_cat_ref))
        print("Chèn/cập nhật dữ liệu vào bảng Products thành công.")

    except Exception as e:
        print(f"Lỗi khi chèn dữ liệu: {e}")


def main():
    xml_file = 'catalog.xml'
    xsd_file = 'catalog.xsd'
    

    xml_tree = validate_xml(xml_file, xsd_file)

    if xml_tree is not None:
       
        db_connection = get_mysql_connection(
            host="localhost",
            user="root",      
            password="",  
            database="catagory"   
        )

        if db_connection:
            cursor = db_connection.cursor()
            create_tables(cursor)
            insert_data_from_xml(cursor, xml_tree)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            print("Hoàn tất quá trình đồng bộ dữ liệu. Đã đóng kết nối MySQL.")

if __name__ == "__main__":
    main()