from flask import Flask, render_template, request, flash, redirect, url_for
import openai  # OpenAI 라이브러리를 가져옵니다.

app = Flask(__name__)
app.secret_key = 'hi123'

# OpenAI API 키를 설정합니다.
openai.api_key = "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"  # 여기에 자신의 API 키를 넣어주세요.

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if not user_input:
            flash("입력을 해주세요.")
            return redirect(url_for('index'))

        try:
            # OpenAI GPT-3를 사용하여 사용자 입력에 응답을 생성합니다.
            response = openai.Completion.create(
                engine="text-davinci-002",  # GPT-3 엔진 선택
                prompt=user_input,
                max_tokens=50  # 원하는 답변의 최대 길이를 설정합니다.
            )

            return render_template('index.html', user_input=user_input, response=response.choices[0].text)
        except Exception as e:
            flash(f"오류가 발생했습니다: {e}")
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
