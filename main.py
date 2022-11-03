from flask import Flask, request
from datetime import datetime

app = Flask('MY First Application')

@app.route('/')
def index():
  
  return '''
        <h1>Bajo Ngabonziza</h1> 
        <p>
        My name is Bajo and I am christian.
        I like to eat <em>dodo</em> and <strong>yams</strong>.
        </p>

  '''
@app.route('/contact')
def contact_page():

  return 'Contact me at ngabonzizabajo1@gmail.com or 078xxxxx'
@app.route('/date')
def date():   
   date =str(datetime.now())
   return f'Today is {date}'
@app.route('/birthyear', methods=['POST','GET'])
def calc_birthyear():
  if request.method == 'POST': #User is posting or submitting his/her information
    return f"""
          <form action='/birthyear' method='POST'>
            <input type="number" name="birthyear" placeholder="Birthday e.g 2020">
            <input type="submit" name="submit">
         </form> 
          you declared your age as {2022 - int(request.form.get('birthyear'))}"""
  elif request.method == 'GET':  
    
    return '''
         <form action='/birthyear' method='POST'>
            <input type="number" name="birthyear" placeholder="Birthday e.g 2020">
            <button type="submit">submit</button>
         </form>   
    '''
if __name__ == '__main__' :
   app.run()