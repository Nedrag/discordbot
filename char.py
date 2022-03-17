
int_class_prefix = ['Magister of Magic, ', 'Wizard of ', 'Stupid, '  ]
str_class_prefix = ['Strongman, ', 'Gymrat, ', 'Average Joe, ']
dex_class_prefix = ['Sneaky, Sneaky, Sneaky', 'Stealth Boots Guy', 'Un-Invisible']
def type_cast(intl, str, dex):
    type = 'default'
    intl = int(intl)
    str = int(str)
    dex = int(dex)
    if intl >= 9:
        if str >= 9:
            if dex >= 9:
                type = int_class_prefix[0] + str_class_prefix[0] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[0] + str_class_prefix[0] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[0] + str_class_prefix[0] + dex_class_prefix[2]
        elif str >= 5 and str < 9: 
            if dex >= 9:
                type = int_class_prefix[0] + str_class_prefix[1] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[0] + str_class_prefix[1] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[0] + str_class_prefix[1] + dex_class_prefix[2]
        else:
            
            if dex >= 9:
                type = int_class_prefix[0] + str_class_prefix[2] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[0] + str_class_prefix[2] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[0] + str_class_prefix[2] + dex_class_prefix[2]
    elif intl >= 5 and intl < 9:
        if str >= 9:
            if dex >= 9:
                type = int_class_prefix[1] + str_class_prefix[0] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[1] + str_class_prefix[0] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[1] + str_class_prefix[0] + dex_class_prefix[2]
        elif str >= 5 and str < 9: 
            if dex >= 9:
                type = int_class_prefix[1] + str_class_prefix[1] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[1] + str_class_prefix[1] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[1] + str_class_prefix[1] + dex_class_prefix[2]
        else:
            
            if dex >= 9:
                type = int_class_prefix[1] + str_class_prefix[2] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[1] + str_class_prefix[2] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[1] + str_class_prefix[2] + dex_class_prefix[2]
    else:

        if str >= 9:
            if dex >= 9:
                type = int_class_prefix[2] + str_class_prefix[0] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[2] + str_class_prefix[0] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[2] + str_class_prefix[0] + dex_class_prefix[2]
        elif str >= 5 and str < 9: 
            if dex >= 9:
                type = int_class_prefix[2] + str_class_prefix[1] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[2] + str_class_prefix[1] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[2] + str_class_prefix[1] + dex_class_prefix[2]
        else:
            
            if dex >= 9:
                type = int_class_prefix[2] + str_class_prefix[2] + dex_class_prefix[0] 
            elif dex >= 5 and dex < 9 :
                type = int_class_prefix[2] + str_class_prefix[2] + dex_class_prefix[1] 
            else:
                type = int_class_prefix[2] + str_class_prefix[2] + dex_class_prefix[2]

    return type
class Char:

    def __init__(self, int, dex, str, name):
        self.int = int
        self.dex = dex
        self.str = str
        self.name = name
        self.invenotry = {}

        self.title = type_cast(self.int, self.str, self.dex) 

    
    
        