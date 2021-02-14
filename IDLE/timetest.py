from time import *

print('hold on,please wait...'.title())
sleep(1)

print(time()) #现在秒数时间
print(gmtime()) #UTC元组，默认现在秒数时间
print(localtime()) #本地元组，默认现在秒数时间
print(ctime()) #本地字符串，默认现在秒数时间

#元组是time.struct_time对象

print(mktime(localtime())) #元组转【秒数时间】，必有参数
print(asctime()) #元组转【字符串】，默认本地元组
print(strftime('%Y年%m月（%B/%b）%d日%A（%a），%H（%p-%I）点%M分%S秒'))
#元组转【格式化字符串】，二参默认本地元组
