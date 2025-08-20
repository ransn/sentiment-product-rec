from flask import Flask, request, render_template
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.model import recommend_products, top5_products

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

valid_userid = ['00sab00','1234','zippy','zburt5','joshua','dorothy w','rebecca','walker557','samantha','raeanne','kimmie','cassie','moore222']


#@app.route('/', methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         # Assuming input is a single feature value
#         feature1 = float(request.form['feature1'])
#         result = recommend([feature1])
#         return render_template('index.html', prediction=result)
#     return render_template('index.html')

@app.route('/')
def view():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend_top5():
    print(request.method)
    user_name = request.form['User Name']
    print('User name=',user_name)
    
    if  user_name in valid_userid and request.method == 'POST':
            top20_products = recommend_products(user_name)
            print(top20_products.head())
            get_top5 = top5_products(top20_products)
            #return render_template('index.html',tables=[get_top5.to_html(classes='data',header=False,index=False)],text='Recommended products')
            return render_template('index.html',column_names=get_top5.columns.values, row_data=list(get_top5.values.tolist()), zip=zip,text='Recommended products')
    elif not user_name in  valid_userid:
        return render_template('index.html',text='No Recommendation found for the user')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
