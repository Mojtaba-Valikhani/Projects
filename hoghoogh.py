def hoghoogh():
    daramad = int(input('saati chand kar mikoni? '))
    if daramad < 4:
        return ('moft kar mikoni!')
    else:    
        hour = int(input('chand saat kar kardi? ' ))
        if hour > 8:
            return ('ziad kar mikoni!')
        else:    
             pay = daramad * hour
             return 'hoghooghe shoma barabar ast ba:',pay
             
        
print(hoghoogh())
    


