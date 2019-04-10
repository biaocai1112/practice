gast_list=['liming','wanghong','xiaogang','xiaodan']
print(gast_list)

#邀请函
print("I would like to invite "+gast_list[0]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[1]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[2]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[3]+" to take part in my birthday party!!")

absent_person='liming'
gast_list.remove(absent_person)
print()
gast_list.insert(0,'xiaonan')

print('\nBecause '+absent_person.title()+' is sick,so i would like to invite '+gast_list[0].title()+' to take part in my birthday party!! ')

print(gast_list)

#新的邀请函
print("I would like to invite "+gast_list[0]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[1]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[2]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[3]+" to take part in my birthday party!!")

print()
print('Because i purchase a new bigger tabble,so i decide to invite three more people!!')
gast_list.insert(0,'Dr.caicheng')
gast_list.insert(3,'Dr.chenyu')
gast_list.append('Dr.liuzheng')

#又一次新的邀请函
print("\nI would like to invite "+gast_list[0]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[1]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[2]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[3]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[4]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[5]+" to take part in my birthday party!!")
print("I would like to invite "+gast_list[6]+" to take part in my birthday party!!")

print("\nI am so sorry for that,my bigger tabble can not be sent in time,therfore i want to reduce the gast number to two person. ")

not_invite0=gast_list.pop(0)
print("\ni am so sorry,that "+not_invite0.title()+" can not take the party.")

not_invite1=gast_list.pop(0)
print("\ni am so sorry,that "+not_invite1.title()+" can not take the party.")

not_invite2=gast_list.pop(0)
print("\ni am so sorry,that "+not_invite2.title()+" can not take the party.")

not_invite3=gast_list.pop(0)
print("\ni am so sorry,that "+not_invite3.title()+" can not take the party.")

not_invite4=gast_list.pop(0)
print("\ni am so sorry,that "+not_invite4.title()+" can not take the party.")

print("\n\n\n")

print(gast_list[0]+":")
print(gast_list[1]+":")
print("\nYou are still in my gast list,welcome to my birthday party!! ")

del gast_list[1]
del gast_list[0]


print(gast_list)
print('the gast list is blank!!')