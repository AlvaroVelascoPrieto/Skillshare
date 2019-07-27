#dictionary key-value

rooms = {249: "Alvaro Velasco", 258: "Xavi Mendigutxia", 269: "Endika Benito"}
print(rooms)
print("Room 249 is ocupied by: " +  rooms[249])
print("Room 269 is ocupied by: " +  rooms[269])
print("Room 258 is ocupied by: " +  rooms[258])
rooms.update({244: "Iñigo Santurtun", 288: "Asier Moreno"})
print(rooms)
rooms.pop(288)
print(rooms)
rooms.popitem()
print(rooms)
print(len(rooms))

