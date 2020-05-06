# with open("E:\simple.txt",'r') as rf:
#     with open("E:\simple1.txt",'a') as wf:
#         link_exist=True
#         page=rf.read()
#         while link_exist:
#             pos=page.find('<a href=')
#             if pos==-1:
#                 link_exist=False
#             else:
#                 first_quote=page.find('\"',pos)
#                 second_quote=page.find('\"',first_quote+1)
#                 url=page[first_quote+1:second_quote]
#                 wf.write(url+'\n')
#                 page=page[second_quote:]
with open("E:\simple.txt",'r') as file:
    pag = file.read()[0:50]
    pos=file.tell()
    print(pos)
    print(pag)
    while True:
        a=input("Do You Want to stop this loop")
        if a=='s':
            break
        else:
            new=file.read()[pos:pos+50]
            print(new)
            pos=pos+50
            print(pos)
        if pos>644:
           break






