# 基础
- 抽象
- 封装
- 多型
- 继承

# 设计原则
- 封装变化
- 针对接口编程，不针对实现编程
- 多用组合，少用继承
- 对扩展开放，对修改关闭
- 为交互对象之间对松耦合设计而努力
- 依赖抽象，不要依赖具体类（依赖倒置原则）
- 最少知识原则（减少对象对交互）
- 好莱坞原则（超类主控一切）
- 尽量让每个类保持单一责任（高内聚）

# 模式
## 策略模式
> 定义算法族，分别封装起来，让它们之间可以互相替换，此模式让算法的变化独立于使用算法的客户

## 观察者模式
> 在对象之间定义一对多的依赖，这样一来，每当一个对象改变状态，依赖他的对象都会收到通知，并自动更新

观察者模式提供一种对象设计，让主题和观察者之间**松耦合**。

松耦合的设计可以让对象之间的互相依赖降到最低。

## 装饰者模式
> 动态地将责任附加到对象上。想要扩展功能，装饰着提供有别于继承的另一种选择

## 工厂模式
> 定义了一个创建对象的接口，但由子类决定要实例化的类是哪一个。工厂方法让类把实例化推迟到子类。

## 单件模式
> 确保一个类只有一个实例，并提供一个全局访问点

## 命令模式
> 将请求封装成对象，这可以让你使用不同的请求，队列，或者日志请求来参数化其他对象。命令模式也可以支持撤销操作

## 适配器模式
> 将一个类对接口转换成客户期望对另一个接口。适配器让原本不兼容对类可以合作无间

## 外观模式
> 提供类一个统一对接口，用来访问子系统中对一群接口。外观定义类一个高层接口，让子系统更容易使用

## 模板方法模式
> 子一个方法种定义一个算法的骨架，而将一些步骤延迟到子类种。模板方法使得子类可以在不改变算法结构的情况下，重新定义算法中的某些步骤

## 迭代器模式
> 提供一种方法顺序访问一个聚合对象中的各个元素，而又不暴露其内部的表示。

## 组合模式
> 允许你将对象组合属性树形结构来表现 整体/部分 的层次结构。组合能让客户以一致的方式处理个别对象和对象组合。

## 状态模式
> 允许对象在内部状态改变时，改变它的行为，对象看起来好像修改来它的类。