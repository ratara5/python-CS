import facebook
graph=facebook.GraphAPI(access_token="EAALEZBRxoZCuwBACK2DyZApOJptJP8hurKWNBMevV2kdZBHh2zfQb2Ae1O7FnULtvXZB7jFh4miz2Wltzb4ZAPKj4VZAPNXedX7G8WBlAALUdPFZA9uc8c0VZAEuYkkiCodxEo0vpc5NeTvk2hDI013mzRfpFNwnsslDSkVBa3jL87pmOFZAklG2M0ZA6V3ZAtbaVb4AsqeQDdvIYBr3lC6oZCqsys5ZBZC0hZAjvS9SMVptCX6BBQZDZD")
f=graph.get_connections(id='147567027115848', connection_name='friends')
print (f)
