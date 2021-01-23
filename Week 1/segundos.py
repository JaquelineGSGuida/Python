segundos=input("Por favor, entre com o número de segundos que deseja converter: ")
temp=int(segundos)

dias=temp//86400

horas=(temp%86400)//3600

minutos=((temp%86400)%3600)//60

segundos=((temp%86400)%3600)%60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")

