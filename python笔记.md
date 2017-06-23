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
* python没有switch语法
* 逻辑运算符是 and or 而不是 ||之类的，看来是崇尚自然的表达
* python没有自增只有 i += 1
* r'字符串'的作用是 取消字符串里面特殊转义，比如\n。' " ''' 三种引号没有根本区别，都会直接执行转义字符，只是为了彼此包含更方便。变量都不能在引号中输出值，只能使用占位符的方式
* re.match 是全局匹配，re.search是局部查找，compile正则式应该是为了复用，一次性的话可直接match/search， str.find()找不到返回-1，str.find()找不到就抛异常
* 用%占位符来代替 + 拼接字符串， '%s and %d' % ('aa', 12)
* python整型有两种int 和 长整型，长整型不需要声明，两者会直接转换，可保存超长的基于操作系统的整型
* [python中没有switch](https://www.pydanny.com/why-doesnt-python-have-switch-case.html)
```python
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")
```
* py自带chm在win2安装目录下