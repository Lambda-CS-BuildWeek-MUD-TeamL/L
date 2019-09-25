from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_34 = Room(title="Room 34", description="")
r_35 = Room(title="Room 35", description="")
r_36 = Room(title="Room 36", description="")
r_37 = Room(title="Room 37", description="")
r_38 = Room(title="Room 38", description="")
r_39 = Room(title="Room 39", description="")
r_40 = Room(title="Room 40", description="")
r_41 = Room(title="Room 41", description="")
r_42 = Room(title="Room 42", description="")
r_43 = Room(title="Room 43", description="")
r_44 = Room(title="Room 44", description="")
r_45 = Room(title="Room 45", description="")
r_46 = Room(title="Room 46", description="")
r_47 = Room(title="Room 47", description="")
r_48 = Room(title="Room 48", description="")
r_49 = Room(title="Room 49", description="")
r_50 = Room(title="Room 50", description="")
r_51 = Room(title="Room 51", description="")
r_52 = Room(title="Room 52", description="")
r_53 = Room(title="Room 53", description="")
r_54 = Room(title="Room 54", description="")
r_55 = Room(title="Room 55", description="")
r_56 = Room(title="Room 56", description="")
r_57 = Room(title="Room 57", description="")
r_58 = Room(title="Room 58", description="")
r_59 = Room(title="Room 59", description="")
r_60 = Room(title="Room 60", description="")
r_61 = Room(title="Room 61", description="")
r_62 = Room(title="Room 62", description="")
r_63 = Room(title="Room 63", description="")
r_64 = Room(title="Room 64", description="")
r_65 = Room(title="Room 65", description="")
r_66 = Room(title="Room 66", description="")
r_67 = Room(title="Room 67", description="")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()

r_34.save()
r_35.save()
r_36.save()
r_37.save()
r_38.save()
r_39.save()
r_40.save()
r_41.save()
r_42.save()
r_43.save()
r_44.save()
r_45.save()
r_46.save()
r_47.save()
r_48.save()
r_49.save()
r_50.save()
r_51.save()
r_52.save()
r_53.save()
r_54.save()
r_55.save()
r_56.save()
r_57.save()
r_58.save()
r_59.save()
r_60.save()
r_61.save()
r_62.save()
r_63.save()
r_64.save()
r_65.save()
r_66.save()
r_67.save()

# Link rooms together
r_34.connectRooms(r_33, "w")
r_34.connectRooms(r_35, "e")

r_35.connectRooms(r_34, "w")
r_35.connectRooms(r_25, "n")
r_35.connectRooms(r_36, "e")

r_36.connectRooms(r_35, "w")
r_36.connectRooms(r_37, "e")

r_37.connectRooms(r_36, "w")
r_37.connectRooms(r_38, "e")
r_37.connectRooms(r_47, "s")

r_38.connectRooms(r_37, "w")
r_38.connectRooms(r_39, "e")

r_39.connectRooms(r_38, "w")
r_39.connectRooms(r_29, "n")
r_39.connectRooms(r_40, "e")

r_40.connectRooms(r_39, "w")
r_40.connectRooms(r_50, "s")

r_41.connectRooms(r_31, "n")
r_41.connectRooms(r_42, "e")

r_42.connectRooms(r_41, "w")
r_42.connectRooms(r_52, "s")

r_43.connectRooms(r_33, "n")
r_43.connectRooms(r_53, "s")

r_44.connectRooms(r_45, "e")
r_44.connectRooms(r_54, "s")

r_45.connectRooms(r_44, "w")
r_45.connectRooms(r_46, "e")

r_46.connectRooms(r_45, "w")

r_47.connectRooms(r_37, "n")
r_47.connectRooms(r_57, "s")

r_48.connectRooms(r_49, "e")
r_48.connectRooms(r_58, "s")

r_49.connectRooms(r_48, "w")
r_49.connectRooms(r_59, "s")

r_50.connectRooms(r_40, "n")

r_51.connectRooms(r_52, "e")
r_51.connectRooms(r_61, "s")

r_52.connectRooms(r_51, "w")
r_52.connectRooms(r_42, "n")
r_52.connectRooms(r_62, "s")

r_53.connectRooms(r_43, "n")
r_53.connectRooms(r_54, "e")

r_54.connectRooms(r_53, "w")
r_54.connectRooms(r_44, "n")
r_54.connectRooms(r_64, "s")

r_55.connectRooms(r_56, "e")
r_55.connectRooms(r_65, "s")

r_56.connectRooms(r_55, "w")
r_56.connectRooms(r_66, "s")

r_57.connectRooms(r_47, "n")
r_57.connectRooms(r_58, "e")

r_58.connectRooms(r_57, "w")
r_58.connectRooms(r_48, "n")
r_58.connectRooms(r_68, "s")

r_59.connectRooms(r_49, "n")
r_59.connectRooms(r_60, "e")
r_59.connectRooms(r_69, "s")

r_60.connectRooms(r_59, "w")

r_61.connectRooms(r_51, "n")
r_61.connectRooms(r_71, "s")

r_62.connectRooms(r_52, "n")
r_62.connectRooms(r_63, "e")
r_62.connectRooms(r_72, "s")

r_63.connectRooms(r_62, "w")
r_63.connectRooms(r_73, "s")

r_64.connectRooms(r_54, "n")

r_65.connectRooms(r_55, "n")
r_65.connectRooms(r_75, "s")

r_66.connectRooms(r_56, "n")
r_66.connectRooms(r_76, "s")

r_67.connectRooms(r_68, "e")
r_67.connectRooms(r_77, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

