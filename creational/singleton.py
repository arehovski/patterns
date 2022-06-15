class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = cls._instances.get(cls)
        if not instance:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return instance


class A(metaclass=SingletonMeta):
    pass


class B(A):
    pass


class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        instance = cls._instances.get(cls)
        if not instance:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances[cls] = instance
        return instance


class C(Singleton):
    pass


class D(C):
    pass


if __name__ == '__main__':
    a1 = A()
    a2 = A()
    assert id(a1) == id(a2)
    b1 = B()
    b2 = B()
    assert id(b1) == id(b2)
    assert id(b1) != id(a1)
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)
    c1 = C()
    c2 = C()
    assert id(c1) == id(c2)
    d1 = D()
    d2 = D()
    assert id(d1) == id(d2)
    assert id(d1) != id(c1)
