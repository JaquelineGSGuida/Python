seconds=input("Please, enter the number of seconds you wish to convert: ")
temp=int(seconds)

days=temp//86400

hours=(temp%86400)//3600

minutes=((temp%86400)%3600)//60

seconds=((temp%86400)%3600)%60

print(days,"days,",hours,"hours,",minutes,"minutes and",seconds,"seconds.")

