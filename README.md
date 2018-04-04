threading - condition的应用与封装

线程锁在不同类资源较多时，对效率影响很大

所以最好是对实例/行为加锁



对象加锁基本别想了，不容易做到完全保留对象的调用方法

现在能想到的只有将其注册到一个重写过 `__getattr__` 方法的dict中，在调用到这一函数时，做condition检测，选择等待或执行。



那么先考虑对行为加锁的独立性与判定方式

期望用例：

```python
def sec_pack(func):
    ... #checking
    return func

@sec_pack
def func():
    ...
    
func() #内有需要独立的操作
```

类似于java的synchronized代码块

内部行为同时只能由一个线程执行

可以对func做类的二次封装，在内添加标志参数后再返回



但是想保证的是资源的独立性，如果多个代码段都操作同一个资源的的话，意义不大

java中的同步也是要申请资源的锁的，但py中不容易跟踪资源的调用

那么做一点修改，虽然用户操作会多一些，但能够保证资源加锁

类似java对象锁的操作方式

```python

def src_pack(src):
    class mtcls(type):
        def __new__(cls,name,attrs,bases):
            for k,v in dir(src):
                attrs[i]
   	class temp(type(src)):
        ...
    temp()
def func_pack(sec_src):
    def 
   
```

然而出现了一些问题，类重写后不知道怎么将原有属性复制下来

如果是非 built-in/extrnsion 类，可以直接对类的属性进行修改，不必进行复制

现在不知道是否所有内建类都支持接收同种类实例作为构建参数



那么用空间换时间，将正在使用的对象进行记录（除了几种不可变类型外都是引用）





MDZZ劳资不写了

以后有骚操作再说吧

:crab:



---

模仿src manager

```python
src = sec_pack(raw_src)
with src:
    src.entity.do()
```

看起来还行

\__enter__里用event做一层资源占用验证

就这吧，真的难看