from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 멤버 정보와 책 상태 정보 추가
members = {
    '강아지': {'전화번호': '1212'},
    '고양이': {'전화번호': '123445'}
}


books = {
    '인공지능': '대출 가능',
    '소프트웨어 공학': '대출 가능',
    '파이썬': '대출 가능',
    'ChatGPT': '대출 가능'
}


@app.route('/')
def index():
    return render_template('index.html', members=members, books=books)

@app.route('/add_member', methods=['POST'])
def add_member():
    member_name = request.form['member_name']
    members[member_name] = {'전화번호': request.form['phone_number']}
    return redirect(url_for('index'))

@app.route('/delete_member', methods=['POST'])
def delete_member():
    member_name = request.form['member_name']
    if member_name in members:
        del members[member_name]
    return redirect(url_for('index'))

@app.route('/add_book', methods=['POST'])
def add_book():
    book_title = request.form['book_title']
    books[book_title] = '대출 가능'
    return redirect(url_for('index'))

@app.route('/delete_book', methods=['POST'])
def delete_book():
    book_title = request.form['book_title']
    if book_title in books:
        del books[book_title]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
