import numpy as np
import pickle
import streamlit as st
import pandas as pd

# loading the saved model
df = pd.read_csv("https://drive.usercontent.google.com/uc?id=1NtaKhQvEOLxN1GS_BTgIPx0U3eO81hSy&export=download")
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def main():
    # HighBP
    diagnosis0 = hypertension_prediction(
        [4.0,1.0,0.0,1.0,26.0,0.0,0.0,1.0,0.0,1.0,0.0,3.0,5.0,30.0,0.0,0.0,0.0]
    )
    if diagnosis0 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis0)
    else:
        st.error(diagnosis0)

    # no HighBP
    diagnosis1 = hypertension_prediction(
        [13.0,1.0,0.0,1.0,26.0,0.0,0.0,1.0,1.0,1.0,0.0,1.0,0.0,10.0,0.0,0.0,0.0]
    )
    if diagnosis1 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis1)
    else:
        st.error(diagnosis1)

    # no HighBP
    diagnosis2 = hypertension_prediction(
        [12.0,0.0,1.0,1.0,37.0,0.0,0.0,1.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0]
    )
    if diagnosis2 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis2)
    else:
        st.error(diagnosis2)

    # HighBP
    diagnosis3 = hypertension_prediction(
        [2.0,0.0,0.0,1.0,26.0,0.0,0.0,1.0,0.0,1.0,1.0,1.0,4.0,0.0,0.0,0.0,0.0]
    )
    if diagnosis3 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis3)
    else:
        st.error(diagnosis3)

    # no HighBP
    diagnosis4 = hypertension_prediction(
        [8.0,1.0,1.0,1.0,39.0,1.0,0.0,1.0,1.0,1.0,0.0,3.0,0.0,10.0,1.0,0.0,0.0]
    )
    if diagnosis4 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis4)
    else:
        st.error(diagnosis4)

    # HighBP
    diagnosis5 = hypertension_prediction(
        [13.0,1.0,1.0,1.0,42.0,0.0,0.0,0.0,0.0,1.0,0.0,4.0,0.0,0.0,1.0,0.0,0.0]
    )
    if diagnosis5 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis5)
    else:
        st.error(diagnosis5)

    # HighBP
    diagnosis6 = hypertension_prediction(
        [4.0,0.0,0.0,1.0,26.0,1.0,0.0,1.0,1.0,1.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0]
    )
    if diagnosis6 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis6)
    else:
        st.error(diagnosis6)

    # no HighBP
    diagnosis7 = hypertension_prediction(
        [2.0,1.0,0.0,1.0,21.0,0.0,0.0,1.0,0.0,1.0,0.0,1.0,0.0,2.0,0.0,0.0,0.0]
    )
    if diagnosis7 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis7)
    else:
        st.error(diagnosis7)

    # no HighBP
    diagnosis8 = hypertension_prediction(
        [6.0,0.0,1.0,1.0,37.0,0.0,0.0,0.0,0.0,1.0,0.0,4.0,0.0,0.0,0.0,0.0,1.0]
    )
    if diagnosis8 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis8)
    else:
        st.error(diagnosis8)

    # HighBP
    diagnosis9 = hypertension_prediction(
        [9.0,0.0,1.0,1.0,25.0,0.0,1.0,1.0,1.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,1.0]
    )
    if diagnosis9 == "Orang ini tidak mengidap penyakit hipertensi":
        st.success(diagnosis9)
    else:
        st.error(diagnosis9)

# creating a function for Prediction
def hypertension_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Orang ini tidak mengidap penyakit hipertensi'
    else:
        return 'Orang ini mengidap penyakit hipertensi'

if __name__ == '__main__':
    main()