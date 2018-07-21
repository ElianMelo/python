city = str(input('Nome de sua cidade: '))
city = city.lower()
city = city.split()
city = 'santo' in city[0]
print('Possui SANTO no primeiro nome? {}'.format(city))



