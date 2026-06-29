import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from predict import predict_news

def test_fake_news():
    result = predict_news("Breaking: Scientists discover moon is made of cheese!")
    assert result in ["FAKE", "REAL"], f"Unexpected result: {result}"
    print(f"✅ Test passed! Result: {result}")

def test_real_news():
    result = predict_news("The government announced new economic policies today.")
    assert result in ["FAKE", "REAL"], f"Unexpected result: {result}"
    print(f"✅ Test passed! Result: {result}")

if __name__ == "__main__":
    test_fake_news()
    test_real_news()
    print("✅ All tests passed!")