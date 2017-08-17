def RemoveSymbols(X):
    X = X.replace('-', '').replace('(', '').replace(')', '')
    if len(X) > 7:
        return X[-10:]
    else:
        return '495' + X[-7:]
n = 4
notes = []
for i in range(n):
    N = input()
    notes.append(N)
for note in notes[1:]:
    if RemoveSymbols(notes[0]) == RemoveSymbols(note):
        print('YES')
    else:
        print('NO')
