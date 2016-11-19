--01. SELECT 语句  检索数据
    SELECT prod_name, prod_id, prod_price FROM Products;
    --选择 多列全行 从某表   可以用 table.column 选择列
    SELECT * FROM Products;
    --选择 全列全行 从某表
    SELECT DISTINCT prod_name, prod_id, prod_price FROM Products;
    --选择 多列 DISTINCT：所选的所有列的唯一行 从某表
    SELECT prod_name FROM Products LIMIT 5 offset 5;
    --选择 某列全行 从某表 显示几行 开始行

--02. ORDER BY 语句  排序检索的数据
    SELECT prod_name FROM Products ORDER BY prod_id;
    --按某一列排序
    SELECT prod_name, prod_id, prod_price FROM Products ORDER BY prod_price, prod_id;
    --按某两列排序先后
    SELECT prod_name, prod_id, prod_price FROM Products ORDER BY 2, 3;
    --按 select 的位置排序
    SELECT prod_name, prod_id, prod_price FROM Products ORDER BY prod_price DESC;
    --按某列进行 DESC：反序 排序，不含 desc 不反序

--03. WHERE 过滤语句
    SELECT prod_name, vend_id FROM Products WHERE vend_id != 'DLL01';
    --WHERE限定条件 选取某列的某行 符合条件为某列的某行
    SELECT prod_name, prod_price FROM Products WHERE prod_price BETWEEN 5 AND 10;
    --WHERE限定条件 选取某列的某行 符合条件为某列的某范围行
    SELECT cust_name FROM customers WHERE cust_email is NULL;
    --判断 NULL 用 is

--04. WHERE高级过滤
    --WHERE 后跟 列名 + AND OR IN NOT, 多条件使用 () 来限定顺序，IN 语句后面一定跟 (xx, xx)

--05. 通配符 (LIKE 操作符只能用在字符串)
    -- WHERE + 列名 + LIKE + ‘sample%’， sample%后通配
    -- WHERE + 列名 + LIKE + ‘%sample%’，前通配%sample%后通配
    -- WHERE + 列名 + LIKE + ‘sam%ple’， sam开头ple结尾的通配
    -- WHERE + 列名 + LIKE + ‘_sample’， 匹配一个字符，并且以sample结尾
    -- [fq]%,匹配方括号内某个开始的字符

--06, 嵌套查询
    SELECT cust_name,cust_contact
    FROM Customers
    WHERE cust_id IN ( SELECT cust_id
                       FROM Orders
                       WHERE order_num IN ( SELECT order_num
                                             FROM OrderItems
                                             WHERE prod_id = 'RGAN01'));
    --保证 SELECT 语句具有与 WHERE 子句中相同数目的列

--07, 创建计算字段（结果间的 连接 和 运算）
    SELECT Concat ( vend_name, '(', vend_id, ')' ) AS vend_title FROM vendors;
    --Concat()，选择的结果放进函数里连接
    SELECT Concat vend_num * vend_price AS vend_mon FROM vendors;
    --结果可以四则运算
    --AS 别名列

--08, 汇总数据 (数值计算)
    SELECT COUNT(cust_email) AS num_cust FROM customers;
    --AVG() COUNT() MAX() MIN() SUM()

--09, 分组数据
    SELECT vend_id, COUNT(*) AS num_prods
    FROM products
    WHERE prod_price >= 10
    GROUP BY vend_id HAVING COUNT(*) >=2
    --GROUP BY 创建所选的列和别名列成组
    --HAVING 过滤组用

--10, 联结表（跨表查询）
    SELECT vend_name， prod_name, prod_price
    FORM vendors, products
    WHERE vendors.vend_id = products.vend_id
    --和下面的语句一样 from 后面的是跨表
    SELECT vend_name， prod_name, prod_price
    FORM vendors
    INNER JOIN products
    ON vendors.vend_id = products.vend_id








问题描述：
为管理岗位业务培训信息，建立3个表:
S (S#,SN,SD,SA)
   S#,SN,SD,SA 分别代表学号、学员姓名、所属单位、学员年龄
C (C#,CN )
   C#,CN 分别代表课程编号、课程名称
SC ( S#,C#,G )
     S#,C#,G 分别代表学号、所选修的课程编号、学习成绩

要求实现如下5个处理：
1. 使用标准SQL嵌套语句查询选修课程名称为’税收基础’的学员学号和姓名
    SELECT
2. 使用标准SQL嵌套语句查询选修课程编号为’C2’的学员姓名和所属单位
3. 使用标准SQL嵌套语句查询不选修课程编号为’C5’的学员姓名和所属单位
4. 使用标准SQL嵌套语句查询选修全部课程的学员姓名和所属单位
5. 查询选修了课程的学员人数
6. 查询选修课程超过5门的学员学号和所属单位