import src.interpreters.interpreter as interpreter
import src.modelPredictor as modelPredictor


def result(statement):
    # Si hay que hacer alguna limpieza del statement antes de llegar al predictor se hace aca
    # Limpiar tildes
    prediction = modelPredictor.predict(statement)
    print('ya se predijo ')
    equation = interpreter.interpret(prediction, statement)
    result = equation  # result = profebot.resolution(equation) -> TODO Cuando tengamos ProfeBot en el codigo
    return result