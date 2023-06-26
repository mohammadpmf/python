import requests
url = 'https://opengameart.org/sites/default/files/dance_field_2.mp3'
# chand ta ahang e dg
# url = 'https://opengameart.org/sites/default/files/audio_preview/33_-_adventure_cats_pirate_radio.ogg.mp3'
# url = 'https://opengameart.org/sites/default/files/audio_preview/34_-_dad_got_me_a_new_nes_game_but_it_sucks.ogg.mp3'
url = 'https://www.hitstreet.net/wp-content/uploads/filebase/Gwen_Stefani_ft_Akon_-_The_Sweet_Escape.mp3'
r = requests.get(url, allow_redirects=True)
f = open('downloaded.mp3', 'wb')
f.write(r.content)
f.close()