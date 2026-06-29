import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from predict import predict_news

def test_fake_news():
    result = predict_news("Breaking: Scientists discover moon is made of cheese!")
    # result is a dict: {'result': 'FAKE NEWS', 'confidence': '...', 'emoji': '...'}
    assert isinstance(result, dict), "Result should be a dict"
    assert 'result' in result, "Dict should have 'result' key"
    assert result['result'] in ["FAKE NEWS", "REAL NEWS"], f"Unexpected: {result}"
    print(f"✅ Test passed! Result: {result['result']}")

def test_real_news():
    result = predict_news("The government announced new economic policies today.")
    assert isinstance(result, dict), "Result should be a dict"
    assert 'result' in result, "Dict should have 'result' key"
    assert result['result'] in ["FAKE NEWS", "REAL NEWS"], f"Unexpected: {result}"
    print(f"✅ Test passed! Result: {result['result']}")

if __name__ == "__main__":
    test_fake_news()
    test_real_news()
    print("✅ All tests passed!")