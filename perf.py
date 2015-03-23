from Way2SMS import *
import random
import time
a = time.ctime()
if '04' <= a[11:13] < '12':
	day = 'Good%20Morning'
elif '12' <= a[11:13] < '20':
	day = 'Inspirational'
else:
	day =  'Good%20Night'
no = random.randint(0,100)
def wilc(token):
	greeturl = 'http://site23.way2sms.com/smsGreets.action?category=%s&Token=%s&pageNo=%d'%(day,token,no)
        file = br.open(greeturl).read()
        msgs = []
        for i in range(0,10):
                if '''<p onclick="javascript:sendgreet('%d');" id='grp%d' style='cursor:pointer;'>'''%(i,i) in file:
                        p = '''<p onclick="javascript:sendgreet('%d');" id='grp%d' style='cursor:pointer;'>'''%(i,i)
                        x = file.index(p)
                        x = x + 104
                        y = x + 145
                        msgs.append(file[x:y])
        return msgs
