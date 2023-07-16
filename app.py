from flask import Flask, render_template, request
import pickle



app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')



@app.route('/predict', methods = ['POST'])
def predict():
	N_Days = request.form['ndays']
	Drug = request.form['drug']
	Age = request.form['age']
	Sex = request.form['sex']
	Ascites = request.form['ascites']
	Hepatomegaly = request.form['hepatomegaly']
	Spiders = request.form['spiders']
	Bilirubin = request.form['bilirubin']
	Cholesterol = request.form['cholesterol']
	Albumin = request.form['albumin']
	Copper = request.form['copper']
	Alk_Phos = request.form['alkphos']
	SGOT = request.form['sgot']
	Tryglicerides = request.form['triglycerides']
	Platelets = request.form['platelets']
	Prothrombin = request.form['prothrombin']
	Edema = request.form['edema']
	Status = request.form['status']

	EdemaY = 1 if Edema == 'Y' else 0
	EdemaN = 1 if Edema == 'N' else 0
	EdemaS = 1 if Edema == 'S' else 0

	StatusC = 1 if Status == 'C' else 0
	StatusD = 1 if Status == 'D' else 0
	StatusCL = 1 if Status == 'CL' else 0

	Drug = 1 if Drug == 'D-penicillamine' else 0
	Spiders = 1 if Spiders == 'Y' else 0
	Hepatomegaly = 1 if Hepatomegaly == 'Y' else 0
	Ascites = 1 if Ascites == 'Y' else 0
	Sex = 1 if Sex == 'F' else 0


	with open('./model_ada.pkl', 'rb') as file:
		my_model = pickle.load(file)

	prediction = my_model.predict([[N_Days, Drug, Age, Sex, Ascites, Hepatomegaly, Spiders, Bilirubin, Cholesterol, Albumin, Copper, Alk_Phos, SGOT, Tryglicerides, Platelets, Prothrombin, EdemaY, EdemaN, EdemaS, StatusC, StatusD, StatusCL]])

	return render_template('result.html', prediction = prediction)




if __name__  == '__main__':
	app.run(debug = True)