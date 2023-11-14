import traceback

class AssertionError(Exception):
    def __init__(self):
        pass
    
    def __str__(self):
        return "invalid stack"

def is_valid_card(card):
    if not isinstance(card,str):
        return False
    
    Front = card[0:len(card)-1]
    End = card[-1]
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A','j','q','k','a']
    suits = ['C','D','H','S','c','d','h','s']
    
    if not Front in ranks:
        return False
    if not End in suits:
        return False
    if (Front.islower() and End.isupper()) or (Front.isupper() and End.islower()):
        return False
    
    return True
    
def string_representation(stack):
    ans = ''
    try:
        for card in stack:
            if not is_valid_card(card):
                raise AssertionError
    except AssertionError:
        print(traceback.format_exc())
        return
    
    for card in stack:    
        if card[-1] in ['c','d','h','s']:
            ans += '** '
        else:
            ans += card
            ans += ' '
    ans = ans[0:len(ans)-1]
    return ans

def turn_selection(stack,positions=[1,2,3,4,5,6,7,8,9,10]):
    try:
        for i in range(len(stack)):
            if not is_valid_card(stack[i]):
                raise AssertionError
    except AssertionError:
        print(traceback.format_exc())
        return
    
    for position in positions:
        if stack[position-1][-1].islower():
            stack[position-1] = stack[position-1].upper()
        else:
            stack[position-1] = stack[position-1].lower()
    return stack

def turn_top(stack, num):
    try:
        for i in range(len(stack)):
            if not is_valid_card(stack[i]):
                raise AssertionError
    except AssertionError:
        print(traceback.format_exc())
        return
    
    for i in range(num):
        if stack[i][-1].islower():
            stack[i] = stack[i].upper()
        else:
            stack[i] = stack[i].lower()
    tmp = stack[0:num]
    tmp.reverse()
    for i in range(num):
        stack[i] = tmp[i]
        
    return stack

def cut(stack, num):
    try:
        for i in range(len(stack)):
            if not is_valid_card(stack[i]):
                raise AssertionError
    except AssertionError:
        print(traceback.format_exc())
        return
    
    for i in range(num):
        stack.append(stack[0])
        del stack[0]
    
    return stack

