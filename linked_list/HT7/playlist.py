import random

#crear una clase para guardar los detalles de cada cancion.
class Song:
    def __init__(self, song_id, name, artist, album):
        self.song_id = song_id
        self.name = name
        self.artist = artist
        self.album = album

#otra clase con el objeto song y los punteros previous y next
class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None
 
 #la clase donde ya se implementa todo lo de la playlist
class DoublyLinkedList:

   #declarando todas las variables a 0  
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None
        self.current_song = None
        self.length = 0

    # metodo para que pueda iterarse   
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

  #metodo para que imprima la playlist bonito y en orden :)  
    def __repr__(self):
        songs = ["PLAYLIST"]
        current_node = self.head
        while current_node is not None:
            songs.append(current_node.song.name)
            current_node = current_node.next
        
        songs.append('END')
        return  " --> ".join(songs)

    #metodo para agregar las canciones 
    def add_node(self, song):
        new_node = Node(song)
        #ver si no hay nada en la playlist entonces lo pone como la cabeza de la linked list
        if self.head is None:
            #en caso la playlist esta vacia entonces le asigna al head y tail el nuevo nodo
            self.head = self.tail = new_node
        
        # en el caso que ya existan canciones en el playlist entonces la coloca atras haciendo que esa ultima sea la tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        #le agrega al contador para el length de la playlist
        self.length += 1
      
    #metodo para quitar las canciones
    def delete_node(self, node_value):
        current_node = self.head
        #quitar el nodo cuando esta en la cabeza
        #para encontrar el nodo con la cancion dentro de la playlist
        if current_node.song.name == node_value:
            #hace que la cabeza tome el valor de la siguiente cancion
            self.head = self.head.next
            #si es la cabeza entonces hace que el valor de "la cancion anterior" sea none porque no hay canciones antes de head
            if self.head:
                self.head.prev = None
            
            #si no es la cabeza entonces hace que la cola se vuelva none y le quita 1 al length
            else:
                self.tail = None
            self.length -= 1

            #si el current node es current node entonces hace que este y el song se hagan 0 
            if self.current_node == current_node:
                self.current_node = None
                self.current_song = None
            return

        #quitar un nodo que no sea la cabeza
        while current_node:
            #si encuentra el nombre de la cancion y si es igual al valor del nodo
            if current_node.song.name == node_value:
                #si el nodo actual es igual a la cola entonce hace que la cola tome el valor de la cancion anterior
                if current_node == self.tail:
                    self.tail = current_node.prev
                    #hace que despues de tail ya no haya nada 
                    self.tail.next = None

                else:
                    #hace que el puntero next apunte al nodo antes del current node para que apunte al nodo despues de current node
                    current_node.prev.next = current_node.next
                    #hace que el puntero prev del nodo despues del current node apunte al nodo anterior a current node
                    current_node.next.prev = current_node.prev
                #le quita 1 al contador de cuantas canciones hay en la playlist
                self.length -= 1

                #si el nodo actual es igual al nodo que se quiere quitar entonces se resetea a None porque ese nodo ya no existiria
                if self.current_node == current_node:
                    self.current_node = None
                    self.current_song = None
                return
            #hace que el current node se vuelva el siguiente despues haber borrado el nodo 
            current_node = current_node.next


    #metodo para que suene la primera cancion de la playlist
    def play(self):
        #Cuando si hay alguna cancion en la playlist 
        if self.head is not None:
            #asegurarse que no este ya sonando una cancion
            if self.current_song is None:
                #entonces hace que el current node sea la cabeza o la primera cancion
                self.current_node = self.head
            print("La rola que esta sonando es:", self.current_node.song.name, "by", self.current_node.song.artist)
        else:
            print("No hay canciones en esta vaina")
    
    #metodo para que suene la cancion siguiente
    def next(self):
        #asegurarse que este sonando una cancion y que no sea la cola/ la ultima en la playlist
        if self.current_node is not None and self.current_node != self.tail:
            #entonces hace que el current node/song pase al siguiente
            self.current_node = self.current_node.next
            self.current_song = self.current_node.song
            print("La rola que esta sonando es:", self.current_song.name, "by", self.current_song.artist)
        else:
            print("Ya llegaste al final finalito de la playlist como para seguirle dando next.")

    #metodo para regresar una cancion
    def previous(self):
        #asegurarse que si hay alguna cancion sonando y que no sea la cabeza o la primera cancion
        if self.current_node is not None and self.current_node != self.head:
            #entonces se hace que el current node/song sea el anterior
            self.current_node = self.current_node.prev
            self.current_song = self.current_node.song
            print("La rola que esta sonando es:", self.current_song.name, "by", self.current_song.artist)
        else:
            print("Ya no podemos ir pa' tras porque ya estamos en el inicio de la playlist más chevere.")

    #metodo para mostrar los detalles de la cancion 
    def show_details(self):
        #asegurarse que este sonando una cancion.
        if self.current_node is not None and self.current_song is not None:
            print("ID:", self.current_song.song_id)
            print("Name:", self.current_song.name)
            print("Artist:", self.current_song.artist)
            print("Album:", self.current_song.album)
        else:
            print("No esta sonando nada asi que tranqui no se arruino la bocina.")

    #metodo para ver cuantas canciones hay en la playlist 
    def playlist_len(self):
        print('Esta vaina tiene {} canciones'.format(self.length))
        return self.length

    #metodo para que las canciones suenen en aleatorio
    def play_shuffle(self):
        #asegurarse que la playlist no este vacia
        if self.head is not None:
            #se usa random para elegir alguno de los IDs de las canciones
            rand_song = random.choice(list(self))
            #si este numero si existe entonces asigna esa cancion a la current song
            if rand_song is not None:
                self.current_song = rand_song.song
                print("La rola que esta sonando es:", self.current_song.name, "by", self.current_song.artist)
        else:
            print("No hay cancioncitas en esta playlist tan bombaaa como para darle shuffle.")

    #metodo para buscar una cancion por nombre
    def search_by_name(self, song_name):
        current_node = self.head
        while current_node:
            if current_node.song.name == song_name:
                self.current_song = current_node.song
                print("La rola que esta sonando es:", self.current_song.name, "by", self.current_song.artist)
                return
            current_node = current_node.next
        print("Dude no se encontro ninguna cancion con ese nombre...")

    #metodo para buscar una cancion por artista
    def search_by_artist(self, artist_name):
        #hace un array para poder guardar si tiene varias canciones ese artista
        songs_by_artist = []
        #hace que el current node se vuelva la cabeza
        current_node = self.head
        while current_node:
            if current_node.song.artist == artist_name:
                #si la cancion hace match entonces lo mete al array 
                songs_by_artist.append(current_node.song)
            #hace que el current node se vuelva el siguiente
            current_node = current_node.next
        #si el tamaño del array es mayor a 0 es decir que si tiene canciones entonces lo printea
        if len(songs_by_artist) > 0:
            print("Canciones de", artist_name, "en esta vaina:")

            #imprime todas las canciones por su nombre y album
            for song in songs_by_artist:
                print("Name:", song.name)
                print("Album:", song.album)
        else:
            print("No hay cancioncitas de es@ tal", artist_name, "en esta playlist babyyy.")
