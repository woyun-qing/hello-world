import os
import sys
import datetime


head = '#'+'-'*20+'\n'+\
'#Function description:\n'+\
'#'+'-'*20+'\n'+\
'#Author:woyun\n'+\
'#'+'-'*20+'\n'

desFile = sys.argv[1]
if os.path.exists(desFile) or not desFile.endswith('.py'):
	print('% already exitst or is not a Python code file.!'%desFile)
	sys.exit()

fp = open(desFile,'w')
today = str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+\
'-'+str(datetime.date.today().day)
fp.write('#-*-coding:utf-8-*-\n')
fp.write('#Filename:'+desFile+'\n')
fp.write(head)
fp.write('#Date:'+today+'\n')
fp.write('#'+'-'*20+'\n')
fp.close()