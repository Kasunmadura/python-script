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
