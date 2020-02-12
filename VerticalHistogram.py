count=0
count1=0              #defined another counter to print stars
cat1=0                #difined to go through category1 one character at a time
cat2=0                #difined to go through category2 one character at a time
cat3=0                #difined to go through category3 one character at a time
cat4=0                #difined to go through category4 one character at a time
category1=0
category2=0
category3=0
category4=0
marks=int(input("enter your marks:"))

while marks>=0:
    if marks==-99:
        break
    elif marks>=0 and marks<=29:
        category1+=1

    elif marks>=30 and marks<=39:
        category2+=1

    elif marks>=40 and marks<=69:
        category3+=1

    elif marks>=70 and marks<=100:
        category4+=1

    else:
        count-=1
        marks=0


    marks=int(input("enter your marks:"))
    count+=1


print("0-29"," 30-39"," 40-69"," 70-100")  #print the categories
while count1<=count:                       #checking the count1 less than or equal to count so we can print stars line by line

    if cat1<category1:                 #checking how many stars are there in category 1
        a=' *'                         #if there is a star 'a' will be equal to a star
        cat1+=1
    else:                              #if there is no stars 'a' will be equal to a space
        a='  '
    if cat2<category2:                 #checking how many stars are there in category 2
        b='     *'                     #if there is a star 'b' will be equal to a star
        cat2+=1
    else:                              #if there is no stars 'b' will be equal to a space
        b='      '
    if cat3<category3:                 #checking how many stars are there in category 3
        c='     *'                     #if there is a star 'c' will be equal to a star
        cat3+=1
    else:                              #if there is no stars 'c' will be equal to a space
        c='      '
    if cat4<category4:                 #checking how many stars are there in category 4
        d='      *'                    #if there is a star 'd' will be equal to a star
        cat4+=1
    else:                              #if there is no stars 'd' will be equal to a space
        d='       '
    print(a,b,c,d)                     #this will print a star or a space according marks entered line by line
    count1+=1
print(count," students in total")
