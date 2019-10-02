list =  ['a','b','c','d','e']
def rspout(list):
    idx = 0
    def hel():
        nonlocal idx
        if len(list) > idx + 1:
            idx += 1
            return list[idx-1] + hel()
        return list[idx]
    print(hel())

rspout(list)
