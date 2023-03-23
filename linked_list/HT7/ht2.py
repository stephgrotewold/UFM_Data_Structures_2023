from playlist import Node ,Song, DoublyLinkedList
from memory_profiler import *
# import random
from data_persistence import pickle_object, unpickle_object
import sys

@profile
def insert(playlist):
    for _ in range(1999):
        song1 = Song(1, "Vamonos de Viaje", "Bandalos Chinos", "BACH")
        playlist.add_node(song1)
        song2 = Song(2, "I hope that you think of me", "Pity Party (Girls Club)", "Hard Times/Bad Trips")
        playlist.add_node(song2)
        song3 = Song(3, "Sweet Child O' Mine", "Guns N' Roses", "Appetite for Destruction")
        playlist.add_node(song3)
        song4 = Song(4, "Leave It In My Dreams", "The Voidz", "Virtue")
        playlist.add_node(song4)
    return playlist

@profile 
def traverse_list(playlist):
    for node in playlist:
        pass


@profile
def picklish():
    print(sys.getrecursionlimit())
    pick = unpickle_object('./linked_list/HT7/playlist_save')
    for node in pick:
        pass

    pass


@profile
def main():
    playlist = DoublyLinkedList()
    playlist = insert(playlist)
    traverse_list(playlist)
    print(sys.getrecursionlimit())
    print(sys.setrecursionlimit(1000))
    print(sys.setrecursionlimit(100000))
    pickle_object(playlist, './linked_list/HT7/playlist_save')
    picklish()

main()
