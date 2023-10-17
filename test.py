# def display_message():
#     print("I'm learning functions")
#
#
# def favorite_book(title):
#     print(f"My favorite book is: {title}")
#
#
# def make_tshirt(print_text="I love Python", size="Large"):
#     print(f"I want the size: {size}, with the text: '{print_text}'")
#
# make_tshirt()
# make_tshirt(size="Medium", print_text="I love Java")
# make_tshirt(size="Large", print_text="C++ rocks!")
#
# def describe_city(city, country="Portugal"):
#     print(f"{city} is in {country}")
#
# describe_city(city="Lisbon")
# describe_city(city="Santorini", country="Greece")

# def city_country(city, country):
#     print(f'"{city.title()}, {country.title()}"')
#
# city_country("lisbon", "portugal")
# city_country("paris", "france")
# city_country("washington", "usa")
#
# def make_album(artist_name, album_title, number_of_tracks=''):
#     if number_of_tracks:
#         album = {'name': artist_name, 'title': album_title, 'tracks': number_of_tracks}
#     else:
#         album = {'name': artist_name, 'title': album_title}
#     return album
#
# # new_album1 = make_album("jimi", "hendrix")
# # new_album2 = make_album("jimi", "hendrix", 20)
# # print(new_album2)
# # print(new_album1)
#
# is_on = True
# while is_on:
#     name_artist = input("Artist: ")
#     name_title = input("Title: ")
#     number_tracks = input("Number of tracks: ")
#     if name_artist == "q" or name_title == "q" or number_tracks == "q":
#         break
#     album = make_album(album_title=name_title, artist_name=name_artist, number_of_tracks=number_tracks)
#     print(album)
#





