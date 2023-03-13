from playlist import Node , Song, DoublyLinkedList

# Create a new doubly linked list osea la playlist
playlist = DoublyLinkedList()

# Create some Song objects and add them to the playlist
song1 = Song(1, "Vamonos de Viaje", "Bandalos Chinos", "BACH")
playlist.add_node(song1)
print(playlist)

song2 = Song(2, "I hope that you think of me", "Pity Party (Girls Club)", "Hard Times/Bad Trips")
playlist.add_node(song2)
print(playlist)

song3 = Song(3, "Sweet Child O' Mine", "Guns N' Roses", "Appetite for Destruction")
playlist.add_node(song3)
print(playlist)

song4 = Song(4, "Leave It In My Dreams", "The Voidz", "Virtue")
playlist.add_node(song4)
print(playlist)

song5 = Song(5, "Love Lost", "Mac Miller", "I Love Life, Thank You")
playlist.add_node(song5)
print(playlist)

#borrar la cancion
playlist.delete_node("Sweet Child O' Mine")
print(playlist)
print("----------------------------------------------")
#play
playlist.play()
print("----------------------------------------------")
#next
playlist.next()
print("----------------------------------------------")
#ver detalles de cancion sonando
playlist.show_details()
print("----------------------------------------------")
#prev
playlist.previous()
print("----------------------------------------------")
#when you reach the beginning de la playlist
playlist.previous()

print("----------------------------------------------")
#next song
playlist.next()
playlist.next()

print("----------------------------------------------")
#ver cuantas canciones tiene en su playlist
playlist.playlist_len()

print("----------------------------------------------")
print("Muy pocas rolas para esta vaina asi que vamo a agregarle unas más :)")

song6 = Song(6, "Take Me Out", "Franz Ferdinand", "Franz Ferdinand")
playlist.add_node(song6) 
print(playlist)

song7 = Song(7, "A-Punk", "Vampire Weekend", "Vampire Weekend")
playlist.add_node(song7) 
print(playlist)

song8 = Song(8, "T.N.T", "AC/DC", "High Voltage")
playlist.add_node(song8) 
print(playlist)

song9 = Song(9, "Problem Child", "AC/DC", "Let There Be Rock")
playlist.add_node(song9) 
print(playlist)

print("----------------------------------------------")
playlist.search_by_name("T.N.T")
print("----------------------------------------------")
#cuando no existe
playlist.search_by_name("Hell N Back")

print("----------------------------------------------")
playlist.search_by_artist("AC/DC")
print("----------------------------------------------")
#cuando no existe
playlist.search_by_artist("Rihanna")


print("----------------------------------------------")
#play shuffle
playlist.play_shuffle()
playlist.play_shuffle()
playlist.play_shuffle()

print("----------------------------------------------")
print('Vamo a resetear la playlist')
print(playlist)
playlist.delete_node("I hope that you think of me")
print(playlist) 
playlist.delete_node("Take Me Out")
print(playlist) 
playlist.delete_node("Vamonos de Viaje")
print(playlist) 
playlist.delete_node("A-Punk")
print(playlist) 
playlist.delete_node("T.N.T")
print(playlist) 
playlist.delete_node("Problem Child")
print(playlist) 
playlist.delete_node("Leave It In My Dreams")
print(playlist) 
playlist.delete_node("Love Lost")
print(playlist) 

print("----------------------------------------------")
#probando los metodos cuando ya no hay canciones en la playlist
playlist.play_shuffle()
playlist.show_details()
playlist.next()









