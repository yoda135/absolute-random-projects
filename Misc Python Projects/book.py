

    book = [
    
    [("hello"),                             ("how are you")                 ],
    [("what is your name"),                 ("my name is brian")            ],
    [("how old are you"),                   ("mind your own bussiness")     ],
    [("what is your favourite colour"),     ("red")                         ],
        ]
for j in range (0,5):
    
    q = input("say something ")


    for i in book:
        if i[0] == q:
            print (i[1])
