import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root',
                     passwd='1234', db='bestproducts', charset='utf8')
cursor = db.cursor()

sql = '''
CREATE TABLE items (
    item_code VARCHAR(20) NOT NULL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    ori_price INT NOT NULL,
    dis_price INT NOT NULL,
    discount_percent INT NOT NULL,
    provider VARCHAR(100)
);
'''
cursor.execute(sql)

sql = '''
CREATE TABLE ranking (
    num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    main_category VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50) NOT NULL,
    item_ranking TINYINT UNSIGNED NOT NULL,
    item_code VARCHAR(10) NOT NULL,
    FOREIGN KEY (item_code) REFERENCES items(item_code)
);
'''
cursor.execute(sql)

db.commit()
db.close()
