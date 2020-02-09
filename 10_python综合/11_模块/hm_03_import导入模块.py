# import 不能识别自定义包名，该类或者包没有灌入python引入库中
# 解决方案：右击pycharm中项目名-->Mark Directory as -->Resource root，然后重新打开项目红线就消失了
import hm_01_测试模块1
import hm_02_测试模块2

hm_01_测试模块1.say_hello()
hm_02_测试模块2.say_hello()

dog = hm_01_测试模块1.Dog()
print(dog)

cat = hm_02_测试模块2.Cat()
print(cat)
