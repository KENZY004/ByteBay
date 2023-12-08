#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     20-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=[1,2,3,5,7,9]
b=[2,3,6,7,9,8]
c_e=list(filter(lambda x: x in a,b))
print(c_e)
c_e=([x for x in a if x in b])
print(c_e)
#no need of two print statements