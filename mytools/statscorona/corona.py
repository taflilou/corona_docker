from flask import Flask
import getcoronastats
app = Flask(__name__)

# TODO
# Make sure when i run getcoronapercountry, i can pass the argument to function too

@app.route('/getcountrylist', methods=["GET"])
def getcountrylist():
    countrylist = getcoronastats.getcountrylist()
    return(countrylist)

@app.route('/getcoronapercountry/<countryname>', methods=["GET"])
def getcoronapercountry(countryname):
    coronatedforcountry = getcoronastats.coronastats(countryname)
    return(coronatedforcountry)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
