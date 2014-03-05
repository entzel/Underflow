#I found this function online already written, to convert float to 
#binary so I could see step by step what is happening as the number gets
#smaller and smaller
def float_to_binary(num):
    exponent=0
    shifted_num=num
    while shifted_num != int(shifted_num):        
        shifted_num*=2
        exponent+=1
    if exponent==0:
        return '{0:0b}'.format(int(shifted_num))
    binary='{0:0{1}b}'.format(int(shifted_num),exponent+1)
    integer_part=binary[:-exponent]
    fractional_part=binary[-exponent:].rstrip('0')
    return '{0}.{1}'.format(integer_part,fractional_part)
    
#Pick a floating point number to start with
under = float(2)

#optionally initialize a counter to count how many divisions we do
#i = 0

print "Starting number is " + str(under)
#We expect with enough divisions graceful underflow will eventually truncate 
#and become zero, losing precision, we want to see that process of gradual precision
#loss. So take the number and divide by 2 over and over

while(under != 0 ):
	under = under/2.0
	print "Number becomes " + str(under)
	num = float_to_binary(under)
	print num
	
	
#The results show the number getting smaller and smaller, and the representation gettting larger and larger as
#each time, another zero is added to the left side of the number. This is losing accuracy as the number gets smaller
#this is how the machine is handling underflow. Eventually, the number the representation is too large, and the number
#gets rounded to zero.
