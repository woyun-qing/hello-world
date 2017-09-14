# -*- coding:utf-8 -*-
def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

f1(1,2,3,4,5)
