### Python Basic

#### String

      "double".find.('s')
      "KasunMAdura".lower

      "test" + "this"
      "Ha" * 4

      print("tab\tDelimited")
      print("new\nline")

      print('"Double" in single')
      print("'Double' in single")

#### Int and Float

      5/3 int
      5.0/3 Float
      5.0//3 int

      int("1")
      float("1.2")
      str(1.2)

#### Boolean
        True,False
        None
        bool("test")

#### Array

        my_list[1,"test",0.2,True]
        my_list[3] 0.2
        my_list[0:3] [1, 'test', True]
        my_list[2:] [True, 0.2]
        my_list[-1] 0.2
        my_list[::2] [1, True]
        my_list[::1] [1, 'test', True, 0.2]

        my_list[0] = "new"
        my_list.append(False)
        my_list + [9.10]
        my_list[1:3]=['a',2]  [1, 'a', 2, 0.2, 'false', False]
        my_list[1:3]=['a',2,3] [1, 'a', 2, 3, 0.2, 'false', False]

        my_list.remove('a')
        my_list.remove('a') [1, 2, 3, 0.2, 'false', False]
        my_list.remove(True) [2, 3, 0.2, 'false', False] Because bool(1) is True


        my_list.pop()
        [2, 3, 0.2, 'false']
        my_list.pop(1)  [2, 0.2, 'false']

        point =(3.0,2.0)

        my_list[2:] [True, 0.2]
        my_list[-1] 0.2
        my_list[::2] [1, True]
        my_list[::1] [1, 'test', True, 0.2]

        my_list[0] = "new"
        my_list.append(False)
        my_list + [9.10]
        my_list[1:3]=['a',2]  [1, 'a', 2, 0.2, 'false', False]
        my_list[1:3]=['a',2,3] [1, 'a', 2, 3, 0.2, 'false', False]

        my_list.remove('a')
        my_list.remove('a') [1, 2, 3, 0.2, 'false', False]
        my_list.remove(True) [2, 3, 0.2, 'false', False] Because bool(1) is True


        my_list.pop()
        [2, 3, 0.2, 'false']
        my_list.pop(1)  [2, 0.2, 'false']

        point =(3.0,2.0)

        "my name is %s" % "kasun"
        'my name is kasun'

        "my name is %s %s" % "kasun","madura"
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: not enough arguments for format string

        "my name is %s %s" % ("kasun","madura")
        'my name is kasun madura'
        "my name is %s %s" % ("kasun","madura")


#### Dictionaries

      ages = {'kasun':59 , 'alex' : 24 , 'sam' : 67}
      {'alex': 24, 'sam': 67, 'kasun': 59}

      ages[kasun] = 21
      {'alex': 24, 'sam': 67, 'kasun': 30}

      del ages['kasun']
      {'alex': 24, 'kasun': 30}

      ages.pop('kasun')
      {'alex': 24}

       ages.keys()
       ['dam', 'madu', 'kasun']

       ages.items()

       [('dam', 31), ('madu', 13), ('kasun', 20)]

       ages.values()
       [31, 13, 20]

       weight=dict(kasun=12,madu=12)
       {'madu': 12, 'kasun': 12}

#### Conditionals

        2 in [1,2,3]
        1 == 1
        1 != 2
        1.0 == 1

        if True:
        ...     print("something is True")
        ...
        something is True

        name="KasunMAdura"
        if len(name) >= 5:
        ...    print ("name is long")
        ...else:
        ...    print ("name is shot")

        if len(name) >= 5:
        ...    print ("name is long")
        ...elif len(name) == 4:
        ...    print ("name is average")
        ...else
        ...    print ("name is True")

#### Loops

        count = 0
        while count < 10:
        ...    print ("ssssss")
        ...    count += 1

        count = 0
        while count < 10:
              if count %2 == 0:
        ...    print ("ssssss")
        ...    count += 1


        while count < 10 :
        ...     if count %2 == 0:
        ...         count +=1
        ...         continue
        ...     print ("we are continuing  odd numbers %s" % count)
        ...     count +=1
        ...
        we are continuing  odd numbers 1
        we are continuing  odd numbers 3
        we are continuing  odd numbers 5
        we are continuing  odd numbers 7
        we are continuing  odd numbers 9

        while count < 10:
        ...     if count % 2 == 0:
        ...        break
        ...     print (" we are contining %s" % count)
        ...     count +=1
        ...


       colors= ['red','green','yellow']
       for x in colors:
       ...    print(x)
       ...


       ages = { 'kasun': 23, 'madu': 45}

       for key in ages:
       ...    print(key)
       ...

       for key, value in ages.items():
       ...    print (key)
       ...    print (value)
       ...

       for key in ages.values():
       ...    print (key)
       ...

#### Logic opertation

      if not len("something") > 10:
      ...    print("it's not")
      ...

      'a' is 'a'
      1 == 1.0
      True
      1 is 1.0
      False

      id(1.0)
      94123033188016
      id(1)
      94123033117032

#### And operator (output is 1st false value or last True value)

      1 and 2
      2
      0 and 1
      0
      bool(0)
      False
      var= None
      var and str(var) ----> no output
      var= 1
      var and str(var) ----> output is 1
      1 and 2 and 0 and 3 ---> output is 0

### OR operator (1st True value)

     1 or 2
     1
     0 or 2
     2
     var = None
     other_var = var or "default"
     other_var --> output is 'default'
     var=1
     other_var = var or "default"
     other_var --> output is 1

     0 or {} or 2 True --> output is 2

### install pip and command

    apt-get install python-pip
    pip install --user package

    pip freeze --user
    pip freeze --user | grep boto3 > requirements.txt
    pip install --user -r requirements.txt

    pip uninstall wheel
    pip freeze --user > requirements.txt
    pip uninstall -r requirements.txt


### Virualenv (Sanbox python enviroment)

    pip install --user Virualenv
    which virtualenv
    ls /.local/bin/virtualenv
    ~/.local/bin/virtualenv venvs/experiment or virtualenv venvs/experiment
    source venvs/experiment/bin/activate
    pip list
    pip install flask
    deactivate

    
