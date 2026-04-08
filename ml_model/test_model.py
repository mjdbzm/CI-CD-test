from model import predict

def test_predict():
    assert predict(1) == 3
    assert predict(2) == 5
    assert predict(3) == 7

if __name__ == "__main__":
    test_predict()
    print("All tests passed ✅")

