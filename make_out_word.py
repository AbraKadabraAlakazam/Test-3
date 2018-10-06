
def make_out_word(s,d):
    s1 = s[0:2]
    s2 = s[2:len(s)]
    f=s1+d+s2
    print(f)
    return f

if make_out_word("<<>>", "Yay")=="<<Yay>>":
    print ("correct")
else:
    print("Nope")
