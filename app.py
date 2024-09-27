from flask import Flask, render_template, request
from dadata import Dadata
token = "5d821cbf037e717a89103108de89195b867b0508"


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bic = request.form.get('bic')
        if bic:
            dadata = Dadata(token)
            result = dadata.find_by_id(name="bank", query=bic)
            data = {}
            print(result)
            data["name"] = result[0]["value"]
            data["address"] = result[0]["data"]["address"]["value"]
            data["score"] = result[0]["data"]["correspondent_account"]
            data["bic"] = result[0]["data"]["bic"]
            data["swift"] = result[0]["data"]["swift"]
            return render_template('index.html', data=data)
        else:
            return render_template('index.html', error="Введите БИК")
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/gooodforeal/find-company-app.git
git push -u origin main