from asc import *
def myinput(items):
    answer = input(f"{items}: ").lower()
    while answer not in items:
        answer = input(f"{items}: ").lower()
    return answer

def play(a):
    print(pictures.get(a))
    a = myinput(actions.get(a))
    play(a)

pictures = {
    'out': out,
    'house': salon,
    'tv': television,
    'tv1': tv1,
    'tv2': tv2,
    'tv3': tv3,
    'tv4': tv4,
    'tv_off': tv_off,
    'egg': egg,
    'cheese': cheese,
    'chocolate': chocolate,
    'icecream': icecream,
    'drink': drink,
    'apple': apple,
    'cake': cake,
    'pizza': pizza,
    'hotdog': hotdog,
    'hamburger': hamburger,
    'kitchen': kitchen,
    'lamp': l_on,
    'on': l_on,
    'off': l_off,
    'room': room,
    'salon': salon,
    'fridge': refrigerator,
    'macrofer': macrofer,
}
actions = {
    'out': ['house', 'exit'],
    'room': ['salon', 'sleep', 'lamp', 'exit'],
    'tv': ['salon', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'tv1': ['salon', 'tv2', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv2': ['salon', 'tv1', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv3': ['salon', 'tv1', 'tv2', 'tv4', 'tv_off', 'exit'],
    'tv4': ['salon', 'tv1', 'tv2', 'tv3', 'tv_off', 'exit'],
    'tv_off': ['salon', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'house': ['room', 'kitchen', 'tv', 'exit'],
    'kitchen': ['salon', 'fridge', 'macrofer', 'exit'],
    'lamp': ['room', 'off', 'exit'],
    'on': ['room', 'off', 'exit'],
    'off': ['room', 'on', 'exit'],
    'fridge': ['kitchen', 'exit'],
    'macrofer': ['kitchen', 'exit'],
    'salon': ['room', 'kitchen', 'tv', 'exit'],
}
play('out')
