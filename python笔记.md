### Python小坑记录  
* 布尔值首字母大写 True False
* dict类型默认是无序的，需要用
* collections.OrderedDict()
* dict key为空时不能进行+=操作,必须先has_key('key_name') 或者 if key_name in dict.keys()
* 查找字符串最后一次出现的位置,rfind
* 判断子字符串是否存在, 
    * for 'word' in string
    * string.find('word')
    * string.index('word') > -1 (不存在会返回-1,在字符串截取的时候需要注意下)
* python的抬头编码声明, #coding = utf-8

![Alt text](test.png)