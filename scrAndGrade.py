def grdAndScr(num):
    if num >=60 and num<70:
        print "Score:",num,"; Your grade is D"
    elif num >=70 and num<80:
        print "Score:",num,"; Your grade is C"
    elif num >=80 and num< 90:
        print "Score:",num,"; Your grade is B"
    elif num >=90 :
        print "Score:",num,"; Your grade is A"
    else:
        print "Score:",num,"; Your grade is F"

import random
ran=0

for i in range(0,10):
    ran=random.randint(60,100)

    grdAndScr(ran)       

