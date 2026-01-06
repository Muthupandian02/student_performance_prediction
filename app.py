from flask import Flask, render_template,request
from src.pipeline.predict_pipeline import predictpipeline, user_input_data

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        data=user_input_data(
            gender=request.form.get('gender'),
            race_or_ethnicity=request.form.get('race_or_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        ) 
        pred_df=data.getting_data()
        predict_line=predictpipeline()
        result=predict_line.predict(pred_df)
        return render_template('home.html', result=result[0])
    
    else:
        return render_template('home.html')
        
if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)

    