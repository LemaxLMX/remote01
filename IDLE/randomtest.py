from random import *
seed() #默认为当前时间
a=['a','s','d','f','g','h','j','k','l',0,4,2,5]
state=getstate() #获得执行时生成器状态
print(state)

print(randint(1,99)) #整数，包括99
print(randrange(0,99)) #整数，不包括99
print(getrandbits(5)) #生成0到4个比特长度（二进制位数）的整数

print(choice(a)) #返回一个
print(sample(a,3)) #返回多个
shuffle(a) #打乱
print(a)

print(random()) #[0,1.0)小数
print(uniform(1.0,9.0)) #范围内的小数

print(getstate()) #最新状态（随时间变化）
setstate(state) #恢复当时的生成器状态
