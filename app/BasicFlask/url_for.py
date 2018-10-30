from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index1():
    user={'username':'Dhiraj'}
    posts=[
        {
            'author':{'username':'Daneil'},
            'body': 'Beautiful day in srilanka!'
            },
        {
            'author':{'username':'Daneil'},
            'body':'Tiger Zinda hey movie was so cool!'
            }
        ]
    return render_template('tmp.html', user=user, posts=posts)


if __name__=='__main__':
    app.run(debug=True)

