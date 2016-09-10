__author__ = 'goldi'
import time
import datetime
tick=time.time()
print tick
localtime = time.localtime(time.time())
print "Local current time :", localtime
print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
print('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
print('Date now: %s' % datetime.datetime.now())
print('Date today: %s' % datetime.date.today())

