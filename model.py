import keras, pickle
import numpy as np

# global variable
global model, scaler

def load():
    global model, scaler
    model = keras.models.load_model('model/modelds_baru.h5')
    scaler = pickle.load(open('model/le.pkl', 'rb'))

def prediksi(hopen, hclose):

    Tren = 0
    if hclose - hopen > 0:
        Tren = 1
    elif hclose - hopen < 0:
        Tren = -1

    arr = np.array([Tren, hclose])

    data1 = scaler.transform(arr.reshape(1, -1))
    data1 = np.array([data1])
    data1 = np.reshape(data1, (data1.shape[0], data1.shape[1], 2))

    prediksi = model.predict(data1)

    maks = 0
    pred = prediksi.flatten()
    for i in range(len(pred)):
        if pred[i] > pred[maks]:
            maks = i
            if maks == 1:
                maks = 'Naik'
            elif maks == 0:
                maks = 'Tetap'
            elif maks == -1:
                maks = 'Turun'
            return maks