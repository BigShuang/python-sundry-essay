## tkinter Canvas delete 方法详解

### 0 前言
对于用Canvas来实现简单游戏的程序来说，
`delete`方法，是一个很重要的方法。

但是官方文档上好像并没有详细解释该方法，网上搜到的关于这个方法的教程比较零乱。
所以我选择直接去看该方法源码。
```python
def delete(self, *args):
    """Delete items identified by all tag or ids contained in ARGS."""
    self.tk.call((self._w, 'delete') + args)
```

看源码主要看三点
- 参数
- 文档字符串(DocStrings)
- 方法里面的具体代码

1. 这个方法的参数是*args，对新手来说不是很容易看懂（所以到本文第二部分再讲）。
就算看懂了也不明白具体参数的格式和效果。
3. 这个方法里面的代码应该是调用了更底层的代码，很不容易看懂（反正我没看懂）

那么就看第二点，该方法的文档字符串为
> Delete items identified by all tag or ids contained in ARGS.

意思是：删掉所有args参数里面指定的tag和id所标识的项目

结合这个说明和搜到的资料以及一些尝试，
我梳理了下的使用方法，如下：

### 1 `delete`方法的使用

#### 基础使用
简单的来讲，`delete`方法可以清楚canvas画布上已绘制的对象
主要有以下三种使用方法

- `delete(id)`: 通过id来删除。
  id是`canvas.create_something`的返回值
- `delete(tag)`: 通过tag来删除。
  tag通过`canvas.create_something(tag=tag)`来指定
- `delete("all")`: 删除所有已绘制对象

举个例子

```python
import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win)
canvas.pack()

r1 = canvas.create_rectangle(50, 50, 100, 150, fill="red", tag="one")
r2 = canvas.create_rectangle(150, 50, 200, 150, fill="green", tag=("two", "green"))
r3 = canvas.create_oval(250, 50, 300, 150, fill="green", tag=("three", "green"))

win.mainloop()
```

其绘值效果如图
![](imgs\1_1.png)

代码中r1，r2, r3分别为三个绘制对象的id

三个绘制对象的tag通过tag参数指定了。
需要额外注意的是：
多个绘制对象可以使用同一个tag，一个绘制对象也可以使用多个tag

第9行和第11行之间，调用delete方法来清理所有，代码示例如下
- 通过id来删除
```python
canvas.delete(r1)
canvas.delete(r2)
canvas.delete(r3)
```
- 通过tag来删除
```python
canvas.delete("one")
canvas.delete("two")
canvas.delete("three")
```
```python
canvas.delete("one")
canvas.delete("green")  # 会同时删除掉r2和r3
```
- 使用"all"删除所有
```python
canvas.delete("all")  # 会同时所有canvas已绘制的对象，即r1, r2和r3
```

#### 一次删除多个

`delete`方法其实可以一次删除多个项目
- 如
```python
canvas.delete(r1)
canvas.delete(r2)
canvas.delete(r3)
```
可以简写成
```python
canvas.delete(r1, r2, r3)
```
- 再比如
```python
canvas.delete("one")
canvas.delete("two")
canvas.delete("three")
```
可以简写成
```python
canvas.delete("one", "two", "three")
```

#### 混合使用

不仅如此，`delete`里面的参数可以id和tag混搭着使用 ，比如
```python
canvas.delete(r1, "two", "three")
```
等价于
```python
canvas.delete(r1)
canvas.delete("two")
canvas.delete("three")
```

### 2 回头再看*args

看完1之后，*args这样一个参数就好理解了
其代表函数能够接受不定数量个参数，可以接受0个，1个，多个。

### 3 究极探究之current
最好不要用`"current"`作为tag
因为这是一个特殊的内部tag:
鼠标停留在某个绘制对象上的时候，
该绘制对象的tag属性列表会有`"current"`。
