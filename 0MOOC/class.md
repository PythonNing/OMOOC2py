# 有关类(Class)的理解和使用
* https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

# Class是什么
* class是用来定义类的keyword，就像def是用来定义function的。
* class简单来讲是有逻辑关系的data或function的集合。
    * 虽然你可以任意定义这个class里的data或function（class里一般叫method），但一般也会遵循相关的逻辑关系去定义。
    * 经常还是和真实世界的逻辑归类相关，比如“顾客”“动物“之类的。
* class是种建模的技巧，一种程序思考的模式。
* 可以将class理解为制造objects的工厂/蓝图。当你定义class时，你并没有制造出任何产品，只是提供了如何制造产品的manual。

## 举例
```python
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance
```
例如上面这个class定义了customer，但并没有制造出任何一个object。
```python
jeff = Customer('Jeff Knupp', 1000.0)
```
上面这句才是真正使用class的定义制造出一个object，叫jeff。jeff称为一个实例（instance），就是实际产出的一个产品。通过customer()，可以制造出任意数目的实例。

## ```self```是什么

* ```self```在定义class是用到，其实也算一个实例，但是只是一个抽象概念。例如定义```withdraw```这个method的时候，意思是```self```作为一个普遍意义上的customer，它有它的balance，如何如何定义withdraw。
* self在定义method时是一个默认的argument。在call method时例如```jeff.withdraw(100.0)```是等同于```Customer.withdraw(jeff, 100.0)```的。

## ```__init__```是什么

init是initialize的缩写，意思是初始化。例如前面jeff的这个实例。在初始化的时候，定义了```self.name = name```，所以意思就是```jeff.name = 'Jeff Knupp'```, ```jeff.balance = 1000.0```。初始化完成后，```jeff```这个object就可以使用withdraw或者deposit了。
* *完全初始化*：一般情况下，需要在```__init__```里将所有变量初始化，不要在```__init__```外面定义新的变量(attribute)。  

>  object consistency: there shouldn't be any series of method calls that can result in the object entering a state that doesn't make sense

## Instance Methods
* class里定义的function一般叫method，有了一个实例（instance）后，method就可以对实例进行修改等用```self```。
* 需要实例才能使用的叫instance methods

## Static Methods
* 一般attribute都要在```__init__```定义，但也有class-level attribute，是对所有实例都成立的。
* Instance methods仍然可以通过```self.<>```使用或更改class-level attribute。
* static methods就是说不需要通过实例或者说```self```来工作。
```python
class Car(object):
    ...
    @staticmethod
    def make_car_sound():
        print 'VRooooommmm!'
```
```make_car_sound```就是一个static method，不需要self作为参数。

## Class Methods
```python
class Vehicle(object):
    ...
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2
```
class method用class作为参数？

## Inheritance 继承
* inheritance表示子类（child class）表现出父类（parent class）的一些属性的过程。

### Abstract Class
* 例如杯子、碗、筷子分别作为一个class，是real-world object，他们是实际存在的。
* 但是餐具作为一个class的话，是一个抽象概念，但杯子碗筷都属于餐具。餐具是一个abstract class。
* 所以我们可以先定义餐具这个class，然后通过定义杯子是餐具的其中一种来定义杯子class。
* 但是餐具这个class，本身并不希望使用它去制造实例，只是希望借它来定义杯子、碗、筷子的class，那么餐具这个class准确说是Abstract Base Class (ABC)。ABC是单纯用来去继承的。
* python有个module就叫```abc```,其中有一个元类（metaclass）叫```ABCMeta```
* 通过设定元类以及```abstracmethod```，可以将某个class设定为ABC
* 然后定义子类的时候必须要定义```abstractmethod```（？）

### Inheritance and LSP
* Inheritance的关键是abstraction，就是抽象化。
* 如何从真实世界抽象出更高层次，感觉是抓住本质特性是重点，以及即使真实世界看起来make sense，而在coding世界其实并不是这样。
* [Liskov Substitution Principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle)
* [What is LSP - stackoverflow](http://stackoverflow.com/questions/56860/what-is-the-liskov-substitution-principle)

![liskovsubtitutionprinciple_52bb5162](https://cloud.githubusercontent.com/assets/14840170/10790255/3a85753a-7dbd-11e5-8bbf-07005289a162.jpg)

