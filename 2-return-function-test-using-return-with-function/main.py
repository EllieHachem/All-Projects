# we can add empty return to stop function early or even multiple return using if  and return
#better type string to explain to user what he did but it usually says none if return is empty and return does not need ()
def format_name(f_name, l_name): 
    if f_name == "" or l_name == "":
        return "typing something"
    f_name_edited = f_name.title()
    l_name_edited = l_name.title()
    return f"{f_name_edited} {l_name_edited}"

#return equal end of function even if we put code after return it wont work

print(format_name(input("what is your name\n"), input("what is your last name\n")))

