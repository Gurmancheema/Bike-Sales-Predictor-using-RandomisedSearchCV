import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('random_forest_regressor_model.pkl', 'rb'))

def welcome():
	return "Welcome All"

def predict_selling_price(km_Driven,ex_showroom_price,Model_age,seller_type_Individual,owner_2nd_owner,owner_3rd_owner,owner_4th_owner,brand_Hero, brand_Honda, brand_KTM,
       brand_Royal_Enfield, brand_Suzuki, brand_TVS,
       brand_Yamaha,brand_Other):
	prediction = model.predict([[km_Driven, ex_showroom_price, Model_age,
       seller_type_Individual, owner_2nd_owner, owner_3rd_owner,
       owner_4th_owner, brand_Hero, brand_Honda, brand_KTM,
       brand_Other, brand_Royal_Enfield, brand_Suzuki, brand_TVS,
       brand_Yamaha]])
	print(prediction)
	return prediction

def main():
	st.title("Bike Sales Predictor")
	st.write("This Web app is used to predict the reselling price of your Bike. Enter the information about your bike below to get the predicted price.")

    #html_temp = "<div style="background-color:tomato;padding:10px"> <h2 style="color:white;text-align:center;">Streamlit Car Sales Predictor ML App </h2></div>""
    #st.markdown(html_temp, unsafe_allow_html=True)
	km_Driven = st.text_input("Kms Driven","Type Here")
	ex_showroom_price = st.text_input("Purchase Price of bike","Type Here")
	Model_age = st.text_input("Model Age (Years)","Type Here")

	
	#Fuel_Type_Petrol= st.selectbox("Select the Fuel Type of your car",('Petrol','Diesel'))

	owner_2nd_owner = st.text_input("No.of Past Owners of Bike","Type Here")
	#owner_2nd_owner=""
	#owner_3rd_owner=""
	#owner_4th_owner=""
	if (owner_2nd_owner=='0'):
		owner_2nd_owner=0
		owner_3rd_owner=0
		owner_4th_owner=0

	elif (owner_2nd_owner=='1'):
		owner_2nd_owner=1
		owner_3rd_owner=0
		owner_4th_owner=0

	elif (owner_2nd_owner=='2'):
		owner_2nd_owner=0
		owner_3rd_owner=1
		owner_4th_owner=0

	elif (owner_2nd_owner=='3'):
		owner_2nd_owner==0
		owner_3rd_owner==0
		owner_4th_owner==1

	
	seller_type_Individual = st.selectbox("Choose the category of Seller",('Individual','Dealer'))

	if(seller_type_Individual=='Individual'):
		seller_type_Individual=1
	else:
		seller_type_Individual=0

	Brand =  st.selectbox("Select the Type of Brand",('Hero','Honda','KTM','Royal Enfield','Suzuki','TVS','Yamaha','Other'))

	if(Brand=='Hero'):
		brand_Hero=1
		brand_Honda=0
		brand_KTM=0
		brand_Royal_Enfield=0
		brand_Suzuki=0
		brand_TVS=0
		brand_Yamaha=0
		brand_Other=0
	elif(Brand=='Honda'):
		brand_Hero=0
		brand_Honda=1
		brand_KTM=0
		brand_Royal_Enfield=0
		brand_Suzuki=0
		brand_TVS=0
		brand_Yamaha=0
		brand_Other=0
	elif(Brand=='KTM'):
		brand_Hero=0
		brand_Honda=0
		brand_KTM=1
		brand_Royal_Enfield=0
		brand_Suzuki=0
		brand_TVS=0
		brand_Yamaha=0
		brand_Other=0
	elif(Brand=='Royal Enfield'):
		brand_Hero=0
		brand_Honda=0
		brand_KTM=0
		brand_Royal_Enfield=1
		brand_Suzuki=0
		brand_TVS=0
		brand_Yamaha=0
		brand_Other=0
	elif(Brand=='Suzuki'):
		brand_Hero=0
		brand_Honda=0
		brand_KTM=0
		brand_Royal_Enfield=0
		brand_Suzuki=1
		brand_TVS=0
		brand_Yamaha=0
		brand_Other=0
	elif(Brand=='TVS'):
		brand_Hero=0
		brand_Honda=0
		brand_KTM=0
		brand_Royal_Enfield=0
		brand_Suzuki=0
		brand_TVS=1
		brand_Yamaha=0
		brand_Other=0
	elif(Brand=='Yamaha'):
		brand_Hero=0
		brand_Honda=0
		brand_KTM=0
		brand_Royal_Enfield=0
		brand_Suzuki=0
		brand_TVS=0
		brand_Yamaha=1
		brand_Other=0
	elif(Brand=='Other'):
		brand_Hero=0
		brand_Honda=0
		brand_KTM=0
		brand_Royal_Enfield=0
		brand_Suzuki=0
		brand_TVS=0
		brand_Yamaha=0
		brand_Other=1


	result=""

	if st.button("Predict"):

   		result=predict_selling_price(km_Driven,ex_showroom_price,Model_age,seller_type_Individual,owner_2nd_owner,owner_3rd_owner,owner_4th_owner,brand_Hero, brand_Honda, brand_KTM,
       brand_Royal_Enfield, brand_Suzuki, brand_TVS,
       brand_Yamaha,brand_Other)
   		st.success('The predicted price for your bike is {} '.format(result))


if __name__=='__main__':
    main()