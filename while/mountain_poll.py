responses = {}

polling_activate = True
while polling_activate:
    name = input("cual es tu nombre?: ")
    response = input("que montaña te gustaria escalar algun dia?: ")

    responses[name] = response

    repeat = input("quieres que otra persona responda? (y/n): ")

    if repeat == 'n':
        polling_activate = False


for name, response in responses.items():
    print(f"a {name} le gustaria escalar: {response}")
