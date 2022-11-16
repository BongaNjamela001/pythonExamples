# Docstring which uses path coverage to test numberutil program
# Bonga Njamela
# 08/06/20

"""
>>> import numberutil
>>> numberutil.aswords(300)
'three hundred'
>>> numberutil.aswords(906)
'nine hundred and six'
>>> numberutil.aswords(729)
'seven hundred and twenty nine'
>>> numberutil.aswords(440)
'four hundred and forty'
>>> numberutil.aswords(55)
'fifty five'
>>> numberutil.aswords(19)
'nineteen'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(100)
'one hundred'

"""
import doctest
doctest.testmod(verbose=True)
