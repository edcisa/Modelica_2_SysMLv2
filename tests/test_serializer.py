from src.serializers.json_serializer import JSONSerializer, ModelicaIR

def test_json_serializer():
    ir = ModelicaIR(components=[], connections=[], parameters=[])
    data = JSONSerializer.serialize(ir)
    ir2 = JSONSerializer.deserialize(data)
    assert ir == ir2
