
from survey import AnonymousSurvey

def test_store_single_response():
    question = "que lenguaje aprendiste primero?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    question = "¿que lenguajes aprendistes primero?"
    language_survey = AnonymousSurvey(question)
    responses = ['english','spanish','mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

