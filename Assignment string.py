Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str='X-DSPAM-Confidence:0.8475'
str_position=str.find('e,15')
print(str_position)
-1
str='X-DSPAM-Confidence:0.8475'
str_position=str.find('0')
print(str_position)
19
number=str[19:]
print(number)
0.8475
conversion_float=flost(number)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    conversion_float=flost(number)
NameError: name 'flost' is not defined. Did you mean: 'float'?
conversion_float=float(number)
print(conversion_float)
0.8475
