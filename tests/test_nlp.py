import json
import pytest

from core.nlp_engine import NLPEngine


def parse_output(output):
    """
    Intenta convertir la salida del LLM en JSON válido.
    Maneja casos donde el modelo agrega texto extra.
    """
    try:
        return json.loads(output)
    except:
        start = output.find("[")
        end = output.rfind("]")
        if start != -1 and end != -1:
            return json.loads(output[start:end+1])
        raise ValueError("Output is not valid JSON")


def test_nlp_output_structure():
    """
    Test principal:
    Verifica que el NLP devuelve una lista válida de conceptos
    """

    nlp = NLPEngine()
    text = "human in a savanna with drought"

    result = nlp.extract(text)

    assert result is not None

    parsed = parse_output(result)

    assert isinstance(parsed, list)
    assert len(parsed) > 0


def test_nlp_semantic_basic():
    """
    Test semántico suave:
    Verifica que al menos detecta conceptos relevantes
    """

    nlp = NLPEngine()
    text = "human in a savanna"

    result = nlp.extract(text)
    parsed = parse_output(result)

    parsed_lower = [str(x).lower() for x in parsed]

    # No exigimos exactitud, solo presencia lógica
    assert any("human" in x for x in parsed_lower)
    assert any("savanna" in x or "environment" in x for x in parsed_lower)


@pytest.mark.skip(reason="Requiere API real, usar solo en validación final")
def test_nlp_real_call_stability():
    """
    Test opcional:
    Solo para correr manualmente (no en CI)
    """

    nlp = NLPEngine()
    text = "ecosystem collapse with human survival pressure"

    result = nlp.extract(text)
    parsed = parse_output(result)

    assert isinstance(parsed, list)
