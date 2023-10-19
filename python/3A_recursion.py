def countdown(i):

    print(i)
    if i<1:  #BASE CASE
        return
    else:    #RECURSIVE CASE
        countdown(i-1)

countdown(100)