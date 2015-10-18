# 1w task
# dairy system

print 'Here is the previous dairy.'
f = open('new dairy.txt','r')
print f.read()

print 'Let\'s write the new dairy.'
f = open('new dairy.txt','a')
line = raw_input(' >')
f.write(line)
f.write('\n')
f.close()
