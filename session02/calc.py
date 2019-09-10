import math

#1

r = 5
v = (4/3)*(math.pi)*r**3
v2 = print('The volume of sphere is {:.2f}.'.format(v))

#2
copy = 60
cost = 24.95*0.6*copy+3+(copy-1)*0.75
print('The wholesale cost is {:.2f}.'.format(cost))

#3
start = 6*60+52
easy = 8+15/60
tempo = 7+12/60
time = 1*easy+3*tempo+1*easy
end = start + time

end_hour = math.floor(end/60)
end_min = end%60
print('Time for breakfast is {}:{:.0f}'.format(end_hour, end_min))

#4
grade1=82
grade2=89
percentage=(grade2-grade1)/grade1*100
print('Percentage is {:.1f}'.format(percentage)+'%')