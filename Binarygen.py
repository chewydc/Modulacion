def binary(sym, sym_len):
    import numpy as np
    rand_n = np.random.rand(sym)
    rand_n[np.where(rand_n >= 0.5)] = 1
    rand_n[np.where(rand_n <= 0.5)] = 0
    sig = np.zeros(int(sym*sym_len)) # generating symbols
    id1 = np.where(rand_n == 1)
    for i in id1[0]:
        temp = int(i*sym_len)
        sig[temp:temp+sym_len] = 1
    return sig