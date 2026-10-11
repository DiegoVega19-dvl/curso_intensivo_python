from survey import AnonymousSurvey

question = "¿cual es fue el primer lenguaje que aprendiste?"

language_survey = AnonymousSurvey(question)

language_survey.show_question()

print("ingresa 'q' para quitar: ")
while True:
    response = input("Lenguaje: ")
    if response == 'q':
        break
    else:
        language_survey.store_response(response)

print("Gracias a todos por participar!!!")
language_survey.show_results()