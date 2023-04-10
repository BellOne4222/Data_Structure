N = int(input())
song = list(map(int, input().split()))
a_song = [1,2,3,4,5,6,7,8]
d_song = sorted(a_song, reverse=True)

if song == a_song:
    print("ascending")
elif song == d_song:
    print("descending")
else:
    print("mixed")