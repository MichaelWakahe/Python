
## <pre>Examples of **args and **kwargs</pre>


```python
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
```


```python
# test first with *args
args = ("two", 3, 5)
test_args_kwargs(*args)
```

    arg1: two
    arg2: 3
    arg3: 5



```python
# now test with **kwargs
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
```

    arg1: 5
    arg2: two
    arg3: 3



```python
def test_kwargs(arg1, **kwargs):
    print("A normal arg1:", arg1)
    if 'myKey' in kwargs:
        print("Found myKey, value is: {}".format(kwargs.get("myKey")))
    else:
        print("myKey not found")
        
    if 'myKey2' not in kwargs:
        print("myKey2 not found")
```


```python
test_kwargs("Michael")
```

    A normal arg1: Michael
    myKey not found
    myKey2 not found



```python
test_kwargs("Michael", myKey='myValue')
```

    A normal arg1: Michael
    Found myKey, value is: myValue
    myKey2 not found

