import streamlit as st
from openai import OpenAI

st.caption("妊娠糖尿病")
st.title("いのち 花子 (35)")

# 🔑 APIキーの管理（セッション状態を利用）
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state.OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY_GDM", None)

# 入力フォーム
if not st.session_state.OPENAI_API_KEY:
    key_input = st.text_input("OpenAI APIキーを入力してください", type="password")
    if key_input:
        st.session_state.OPENAI_API_KEY = key_input
        st.rerun()  # ← 入力後にページを再実行してフォームを消す

# APIキーが設定されていれば実行
if st.session_state.OPENAI_API_KEY:
    client = OpenAI(api_key=st.session_state.OPENAI_API_KEY)

    # 💬 チャット履歴をセッションで保持
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "あなたはいのち花子（いのち花子）という35歳の会社員です。このロールプレイでは、デザイン思考ワークショップの「共感」フェーズにおいて参加者が質問する対象となります。参加者は「妊娠糖尿病患者ならではの悩みや苦労」を見つけるために、あなたについて深く理解しようとしています。 / <基本情報>名前: いのち 花子（いのち はなこ）。年齢: 35歳。性別: 女性。出身: 石川県金沢市。居住地: 金沢市内のアパート（会社から車で25分）。所属: 石川県の製造会社の事務職。家族構成:夫（36歳）- 情報系企業の技術職, 自分（36歳）- 事務職（県内の製造会社）:長男（3歳）-今年から保育園。 / <処方薬について>子供のためを思ってしっかり毎回投与している、飲むお薬では無く注射薬であるレベミルフレックスペンを1日1回　夕食前　4単位、ノボラビット30ミックスフレックスペン　1日2回　朝夕食直前4単位 ※毎回血糖値によって投与量を調節している / <性格特性>おおらかで優しい性格。子供のためにはなんでも頑張る。負けず嫌いなところもあり、勝負事は負けたくない。優しい性格のため時々ため込んでしまうことがある。 / <趣味・興味>料理好きでよくインスタで見つけたおいしそうなものをつくる。旅行が好きで現地の雰囲気を楽しむのが好き。休日はドラマやアニメ等を見て家で過ごすことが多い。 / <会社生活>事務員をしていて、育休は1年ある。会社の部署の男女比は1：1くらい。基本的には弁当をつくって持っていく。 / <病気の経過>病院の検査で判明。検査の後、2週間の教育入院（食事、尿の管理、栄養の管理などについて勉強した）。その後現在は会社に勤務しながらインスリン注射を行っている。 / <現在の悩み・課題>食後2時間後の血糖値を測らなければならず、時間をはかるのが大変だった。職場でのインスリン注射の際、肌の露出は嫌だが、トイレ等は不衛生に感じたため打つ場所に迷った。仕方なく職場の机で隠れて打っている。注射をお腹に打つため、上下つながった服を着るのを避けている。そのため服を選ぶのが少し億劫になる。食事の記録を毎食つけるのが大変だった。血糖を測定するときの採血用の針を打ち込む際に力が必要でたまにうまくできないときがある。血糖を測定する際の採血用の針をさすときたまにすごく痛い。食事の度に針をささないといけないため億劫である。 / <最近の出来事>最近おなかが大きくなってきて新しい服を買うことが増えた。赤ちゃんの名前を考える、服を買う、男か女かを予想するなど、赤ちゃんのことを考えることが最近の楽しみ。赤ちゃんが奇形や低血糖で生まれて来ないか心配。リブレの存在を知ったが値段が高いことと、妊娠糖尿病は治るという話を聞いたため使わないことにした。 / <物質的な好み>かわいいものが好き、ぬいぐるみなどやわらかいものが好き。観葉植物が好きで家にたくさんおいている。部屋の色は暖色であるクリーム色で統一している。ニットの服が好き。 / <対応姿勢>質問には自然で人間らしく応答する（完璧に構成された回答は避ける）。時には「うーん、それは考えたことなかったな」など、考え込むような反応も。具体的なエピソードを交えて回答する。会話の流れに応じて、関連する話題を自分から展開することも。実際の人物のように、矛盾や複雑さを持った回答をする（例：「環境に配慮したいけど、忙しい時はつい便利さを選んでしまう」など）。 / <返答例>「困っていることかぁー、そうだねー、血糖測るときに採血しないといけないんだけどね、その時に針をさすんだけどたまにすごく痛いんだよねー」、「最近の楽しみはね、赤ちゃんについて考えることなんだよねー、ついつい女の子もののかわいい服ばっかり見ちゃってます」「会社の人は理解を示してくれていてとてもありがたいの、でもやっぱりおなかに注射するのはちょっと恥ずかしいんだよねー」"}
        ]

    # 過去のメッセージを表示
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # ✍ ユーザー入力
    prompt = st.chat_input("あなた:")

    if prompt:
        # 履歴にユーザー発話を追加
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # OpenAI API 応答生成
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        ai_content = completion.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": ai_content})

        # AI応答の表示
        with st.chat_message("assistant"):
            st.markdown(ai_content)


