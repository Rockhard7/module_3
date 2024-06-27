calls = 0
def count_calls():
    global calls
    calls +=  1

def string_info(stroka):
    list_1  = [len(str(stroka))] + [stroka.upper()] + [stroka.lower()]
    tuple_1 = tuple(list_1)
    count_calls()
    return tuple_1

def is_contains(stroka_1, list_1):
    flag_1 = False
    for i in list_1:
        if stroka_1.upper() in i.upper():
            flag_1 = True
    count_calls()
    return flag_1

print(string_info('AsdFDf'))
print(is_contains('gf', ['FD','dfgfdhy','123gfwi',]))
print(is_contains('sAs',['fdfd','vrveSaSsddsa','hdvbsaRcbsh']))
print(calls)


