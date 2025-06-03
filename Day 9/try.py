

#! and
age = 17 # Example neto False kase yung condition ay 18+ lang ang pwede pumasok
haveId = True # Eto True kase may i.d ka pero hindi eligible yung age mo

if age >= 18 and haveId: # Dapat True etong dalawa para iprint niya
  print("Pwede kana pumasok yah may I.D kanaman at Pasok yung edad mo")
else: # Pero kapag isa lang ang True at false ang isa eto ang ipriprint niya
  print("Bawal pumasok ang bata")


#! or
umuulanBa = True # eto True 
mayPayong = False # pero eto false kaya dalawa na True at False

if umuulanBa or mayPayong: # eto yung i eexecute niya kase pasok yung criteria na dapat yung isa ay True at isa False
  print("Pwede ka parin lumabas pero mababasa ka kase wala kang payung")
else: # pero kapag may payong kanaman so dalawang true na yun hindi niya ieexecute yung una kase ang or ay True at false eto naman same True
  print("Pwede kana lumabas hindi ka mababasa")

#! not
isOnline = False # reverse kapag false i priprint niya pag true yung else ang mag priprint
if not isOnline: # return True if the value is False
  print("Offline")
else:
  print("Online")