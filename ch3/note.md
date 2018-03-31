3.3 字符和字符串  
python处理字符和字符串的方式是一样的  
python中没有字符数据类型,一个字符的字符串就代表一个字符  
字符串必须被包含在一对单引号或一对双引号中  

python提供ord(ch)函数来返回字符ch的ascii码,用chr(code)返回code所代表的字符  
ch = 'a'
ord(ch)
chr(98)
ord('A')


3.3.5 不换行打印  
print(item, end = "any ending string")  



3.5 对象和方法简介
可以使用id函数和type函数来获取对象的一些信息  
程序执行过程中,对象的id不会变,但每次执行时python都可能会赋予一个不同的id.  
Python按照对象的值决定对象的类型  
Python中class和type意思一样  
python中每个变量实际是一个指向对象的引用  

字符串方法strip()被用来移除一个字符串两端的空格,字符' ', '\t', '\f', '\r', '\n'都是空格符  

Eclipse会自动在input函数输入的字符串后追加\r  