# http://www.mashup-template.com/ and https://html5up.net/(best) se free template-download- no need to write html css js.many website.
# when extract template-many files-from this we need all html files,one css,one js file wo v uncompressed wali withour zip wali.
# we dun need map file nw-cz it use for debugging, we dun need sample file too.
# html ko templates folder m and css,js and assets ko static folder m patak do.
# iske bad html wali khol kr savi ka sahi path de do,modify kr do,css k v,js ka v ar image ka v wo v sab jgh cz usme puran wala path dala hoga avi wo hmare static folder m hai sab.

from flask import Flask, render_template,url_for
app = Flask(__name__)
"""
@app.route('/index.html')  
def hello_world():
    return render_template('index.html') 

@app.route('/about.html')  
def about():
	print(url_for('static', filename='lightning.ico'))
	return render_template('about.html')
"""
# alag route hr page k liye banane ki wajay single route banake svi html page ko call kr  lo.
# pahle hm specific page k nam route m de rhe the ab variable methode se de like...

@app.route('/index.html')  
def hello_world():
    return render_template('index.html') 


@app.route('/<string:page_name>') # ab index.html page m jo tab hai pages k uspe click krenge to  url m slash k bad wo page.html a jayea jo ki string hai.
def page(page_name): # ab wo page.html ko page func use karega
    return render_template(page_name) 

#ar usi page.html ko call kr dega jo templates m rakha hoga.

# hme component page ki jarurat nhi hai, to ya to pure page ko hata do.
# pr hmne page na hata k, baki k html m nav.bar collaps cls m jo component ki jo line thi ul tag k andar use hata dia.
# navigation bar p hi component page a rha,ar navigation bar har page p hai html q wo to hr page p dikhta hai to hr page se navigation bar se component ko hata rhe.
# ctr+f se find kr skte and crrl+shift+f se find and replace,open wali file m hi karna hai to open file select kr lena.folder m to folder.


# ab page number in navigation bar and page number page ko kholene pe,dono match nahi kar rhe se match them.
# <div class="section-container"> k andar h1 cls m page open krne wale page number milenge,nav.bar wale page number nhi.

# agr works k page p jaye to, to whan discover kren to wahan v 001 to 006 tk link ayenge navig bar ki tarh unhi se alag alag project p ja skte hai.
# pr whan hmare pas ek hi project hai so 001 to chl rha pr 002 or other kam ni kr rhe.hm unhe add v kr skte hai.
# agr add krna hai to ye works.html m nahi balki "work.html" hoga.
# work.html m ja k fir se nav. bar wali script m jake wahan adjustment kr skte hai sath hi jo dikhana hai uski link dal skte hai.
# avi 001 to 006 tk link hai,ar savi jagh index.html hai isliye click krne p pahle page p le ja rha.

#    CONTACT FORM-- GO TO FLASK-QUICK START-Accessing Request Data-request object-copy code n paste--then delete some part of the code.

"""
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'Your form has been submitted sucessfully'
"""
# avi hme data devloper tool m console header m sbse neche mil gya.
#ab hme ise apni memory m v chahte hai mtlb terminal p, dict k form m to--
"""
from flask import request
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		data=request.form.to_dict()
		print(data)
		return 'Your form has been submitted sucessfully'
	else:
		return 'something went wrong, Try Again'
"""

# ab hme thank you ka msg denge ek new html page se.jo contact html ki tarah hoga bs usme form k tag pura hata kar msg type kr dia.
# pr wo page naya jispe navigation bar m koi tab ni hai jo whan le jaye to redirect ko import krna hoga flask se.
"""
from flask import request, redirect
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		data=request.form.to_dict()
		print(data)
		return redirect('thankyou.html')
	else:
		return 'something went wrong, Try Again'
"""
# now we are going to write data into text file and csv file.dabase m rakhna btaya to ni theory screen shots se padho.
# cz data avi memory m hai, server band hote hi ya system band hote hi ye gayab ho jayega.

"""
from flask import request, redirect

def write_to_file(data): # creating new func to write on text and isko hum submit form wale func se cl kr lenge thanku msg dene k pahle hi.
	with open('database.txt', mode='a') as database:
		email=data["email"] # append mode use krke data k email,subject, messagge ko acess kr lia.
		subject=data["Subject"]
		message=data["message"]
		file=database.write(f'\n{email},{subject},{message}') # every entry k pahle new line chahiye. means next entry jb hogi to use pahle new line ban jayegi 2nd wali entry upr rhegi ar pahle wali neeche.
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		data=request.form.to_dict()
		#print(data)
		write_to_file(data) # print ki wjay upr jo naya func banaya use call kr lia data ko pass krke.
		return redirect('thankyou.html')
	else:
		return 'something went wrong, Try Again'

"""
# ab exl or csv file m write krte hai data ko--same process- ek new func banega bs thoda sa csv write krne k tarika alag hai.
# python has built in module--google--python csv--so agn create new file--database.csv

from flask import request, redirect
import csv

def write_to_csv(data): # creating new func to write on csv and isko hum submit form wale func se cl kr lenge thanku msg dene k pahle hi.
	with open('database.csv',newline='', mode='a') as database2: # new line yhi de dia jata hai.
		email=data["email"] # append mode use krke data k email,subject, messagge ko acess kr lia.
		subject=data["Subject"]
		message=data["message"]
		csv_writer=csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL,)
		csv_writer.writerow([email,subject,message]) # simply gave cz these r variable in the form of list. so this row is going to contain these.and iske bad ek new line deni hai jo upr hi file open krte time de di taki ye labels ban jaye,uske bad walin newline default chalegi.header k document section m dekh skte hai but we already have header.
# we r not getting the labels name here.
# text file m comma tha wahan se column seprate honge.ar email,sub.,mess.,labels banege.
# thats y csv is comma separated values.
#csv.writer k andar many parameters de skte hai like delimeter,quote character--par phla parmeter csv file k nam dia jata hai.
# quote char-string used to give quotes.delimiter string used to separate fields.
# quoting=csv.QUOTE_MINIMAL tells the writer object to quote only those fields which contain special character such as limiter,quotechar or ny of the char. in lineterminator.
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		data=request.form.to_dict()
		#print(data)
		write_to_csv(data) # print ki wjay upr jo naya func banaya use call kr lia data ko pass krke.
		return redirect('thankyou.html')
	else:
		return 'something went wrong, Try Again'
