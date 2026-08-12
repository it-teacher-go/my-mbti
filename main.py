import random
import streamlit as st


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="✨",
    layout="centered"
)


# =========================================================
# 포켓몬 이미지 URL
# =========================================================
def get_pokemon_image_url(pokedex_id: int) -> str:
    return (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/other/official-artwork/{pokedex_id}.png"
    )


# =========================================================
# MBTI별 궁합
# =========================================================
mbti_match = {
    "INTJ": "ENFP",
    "INTP": "ENTJ",
    "ENTJ": "INTP",
    "ENTP": "INFJ",
    "INFJ": "ENTP",
    "INFP": "ENFJ",
    "ENFJ": "INFP",
    "ENFP": "INTJ",
    "ISTJ": "ESFP",
    "ISFJ": "ESTP",
    "ESTJ": "ISFP",
    "ESFJ": "ISTP",
    "ISTP": "ESFJ",
    "ISFP": "ESTJ",
    "ESTP": "ISFJ",
    "ESFP": "ISTJ",
}


# =========================================================
# MBTI별 추천 포켓몬
# (이름, 도감번호, 추천 이유)
# =========================================================
mbti_pokemon = {
    "INTJ": [
        (
            "뮤츠",
            150,
            "혼자 깊이 생각하고 자신만의 전략을 세우는 모습이 닮았어요.<br>"
            "목표가 정해지면 흔들리지 않고 끝까지 밀고 나가는 힘이 있어요."
        ),
        (
            "팬텀",
            94,
            "조용히 상황을 살피다가 필요한 순간에 움직이는 영리함이 닮았어요.<br>"
            "남들과 다른 방식으로 문제를 바라보는 점도 잘 어울려요."
        ),
        (
            "나인테일",
            38,
            "신비롭고 지적인 분위기와 독립적인 성향이 잘 맞아요.<br>"
            "쉽게 속을 드러내지 않지만 자신만의 기준은 분명해요."
        ),
    ],

    "INTP": [
        (
            "야도킹",
            199,
            "느긋해 보여도 머릿속에서는 계속 생각이 이어지는 모습이 닮았어요.<br>"
            "새로운 가능성을 탐구하고 자기만의 답을 찾아가는 성향과 잘 맞아요."
        ),
        (
            "메타몽",
            132,
            "정해진 틀보다 상황에 따라 자유롭게 변하는 모습이 닮았어요.<br>"
            "한 가지 방식에 갇히지 않고 색다른 해결책을 찾아내요."
        ),
        (
            "이브이",
            133,
            "여러 가능성을 품고 있다는 점이 INTP와 잘 어울려요.<br>"
            "아직 정해지지 않은 길을 탐색하며 자신만의 방향을 찾아가요."
        ),
    ],

    "ENTJ": [
        (
            "리자몽",
            6,
            "강한 추진력과 자신감으로 목표를 향해 나아가는 모습이 닮았어요.<br>"
            "어려운 상황에서도 중심을 잡고 앞으로 밀고 나가는 힘이 있어요."
        ),
        (
            "엠페르트",
            395,
            "당당한 카리스마와 리더십이 돋보이는 포켓몬이에요.<br>"
            "목표를 정하면 체계적으로 움직이며 주변을 이끄는 모습이 잘 맞아요."
        ),
        (
            "루카리오",
            448,
            "목표가 생기면 흔들리지 않고 끝까지 나아가는 의지가 닮았어요.<br>"
            "강한 집중력과 판단력으로 상황을 주도하는 모습이 잘 어울려요."
        ),
    ],

    "ENTP": [
        (
            "피카츄",
            25,
            "활발하고 재치 있으며 새로운 상황을 즐기는 모습이 닮았어요.<br>"
            "빠르게 반응하고 예상 밖의 재미를 만들어내는 매력이 있어요."
        ),
        (
            "조로아크",
            571,
            "기발한 방식으로 상황을 바꾸는 모습이 ENTP와 닮았어요.<br>"
            "임기응변과 창의적인 아이디어로 상대를 놀라게 해요."
        ),
        (
            "초염몽",
            392,
            "도전을 즐기고 빠르게 행동하는 강한 에너지가 잘 어울려요.<br>"
            "새로운 승부와 자극을 두려워하지 않는 모습이 닮았어요."
        ),
    ],

    "INFJ": [
        (
            "뮤",
            151,
            "조용하면서도 신비롭고 깊은 가능성을 품고 있는 모습이 닮았어요.<br>"
            "겉으로 드러나지 않아도 따뜻한 마음과 자신만의 세계가 있어요."
        ),
        (
            "라프라스",
            131,
            "차분하고 따뜻하며 주변을 배려하는 모습이 잘 어울려요.<br>"
            "부드러운 분위기 속에서도 자신만의 중심을 잃지 않아요."
        ),
        (
            "가디안",
            282,
            "다른 사람의 마음을 이해하고 소중한 존재를 지키려는 모습이 닮았어요.<br>"
            "조용하지만 깊은 신념을 가진 점이 잘 맞아요."
        ),
    ],

    "INFP": [
        (
            "치코리타",
            152,
            "따뜻한 마음과 풍부한 감성을 가진 모습이 잘 어울려요.<br>"
            "자신이 중요하게 생각하는 가치에는 누구보다 진심이에요."
        ),
        (
            "푸린",
            39,
            "부드럽고 감성적이며 자신의 마음을 표현하는 모습이 닮았어요.<br>"
            "순수하고 따뜻한 분위기가 INFP의 매력과 잘 맞아요."
        ),
        (
            "세레비",
            251,
            "희망과 이상을 소중하게 여기는 모습이 잘 어울려요.<br>"
            "자신만의 세계와 따뜻한 상상력을 가진 점이 닮았어요."
        ),
    ],

    "ENFJ": [
        (
            "루카리오",
            448,
            "다른 사람의 마음을 이해하고 함께 성장하려는 모습이 닮았어요.<br>"
            "강한 신념을 가지면서도 동료를 중요하게 생각해요."
        ),
        (
            "밀로틱",
            350,
            "부드럽고 우아하면서 주변에 긍정적인 영향을 주는 모습이 잘 맞아요.<br>"
            "사람들을 편안하게 만드는 따뜻한 분위기가 닮았어요."
        ),
        (
            "엠페르트",
            395,
            "주변을 자연스럽게 이끄는 리더십이 잘 어울려요.<br>"
            "책임감 있게 행동하며 모두를 함께 끌고 가는 힘이 있어요."
        ),
    ],

    "ENFP": [
        (
            "피카츄",
            25,
            "밝고 친근하며 새로운 사람과 경험을 즐기는 모습이 닮았어요.<br>"
            "긍정적인 에너지로 주변 분위기를 자연스럽게 살려줘요."
        ),
        (
            "페라페",
            441,
            "표현력이 풍부하고 활발하게 소통하는 모습이 닮았어요.<br>"
            "자유로운 분위기와 재치 있는 매력이 ENFP와 잘 맞아요."
        ),
        (
            "치라치노",
            573,
            "호기심이 많고 밝은 에너지로 주변을 즐겁게 만드는 모습이 닮았어요.<br>"
            "새로운 것을 반갑게 받아들이는 태도가 잘 어울려요."
        ),
    ],

    "ISTJ": [
        (
            "메타그로스",
            376,
            "체계적으로 판단하고 맡은 일을 정확하게 해내는 모습이 닮았어요.<br>"
            "꾸준하고 믿음직스러워 함께할수록 든든한 매력을 보여줘요."
        ),
        (
            "강철톤",
            208,
            "단단하고 쉽게 흔들리지 않으며 원칙을 지키는 모습이 잘 맞아요.<br>"
            "묵묵하게 자신의 역할을 수행하는 점이 ISTJ와 닮았어요."
        ),
        (
            "거북왕",
            9,
            "차분하고 안정적으로 자신의 역할을 해내는 모습이 닮았어요.<br>"
            "겉으로 요란하지 않아도 책임감 있게 끝까지 버텨내요."
        ),
    ],

    "ISFJ": [
        (
            "이브이",
            133,
            "주변을 세심하게 살피고 소중한 사람을 챙기는 모습이 닮았어요.<br>"
            "부드럽고 따뜻하면서도 상황에 맞게 유연하게 적응해요."
        ),
        (
            "라프라스",
            131,
            "주변을 편안하게 만들고 다른 사람을 배려하는 모습이 잘 맞아요.<br>"
            "차분하고 따뜻한 분위기가 ISFJ와 닮았어요."
        ),
        (
            "토게피",
            175,
            "따뜻하고 순수한 분위기와 주변을 챙기는 마음이 닮았어요.<br>"
            "함께 있는 사람에게 편안함을 주는 점이 잘 어울려요."
        ),
    ],

    "ESTJ": [
        (
            "망나뇽",
            149,
            "목표가 정해지면 힘 있게 실행으로 옮기는 모습이 닮았어요.<br>"
            "책임감 있게 주변을 챙기며 든든하게 중심을 잡아줘요."
        ),
        (
            "메타그로스",
            376,
            "효율적이고 체계적으로 판단하는 모습이 ESTJ와 잘 맞아요.<br>"
            "계획한 일을 정확하게 실행하는 힘이 돋보여요."
        ),
        (
            "괴력몬",
            68,
            "부지런하고 힘 있게 목표를 수행하는 모습이 닮았어요.<br>"
            "해야 할 일이 생기면 망설이지 않고 바로 움직이는 타입이에요."
        ),
    ],

    "ESFJ": [
        (
            "럭키",
            113,
            "다른 사람을 잘 챙기고 따뜻한 분위기를 만드는 모습이 닮았어요.<br>"
            "함께 있는 사람들에게 편안함과 긍정적인 에너지를 전해줘요."
        ),
        (
            "이브이",
            133,
            "친근하고 여러 사람들과 자연스럽게 어울리는 모습이 잘 맞아요.<br>"
            "상대에게 맞춰 따뜻하게 관계를 이어가는 점이 닮았어요."
        ),
        (
            "푸크린",
            40,
            "밝고 포근한 분위기로 주변 사람을 편안하게 해줘요.<br>"
            "사람들과 함께할 때 매력이 더 살아나는 점이 ESFJ와 잘 맞아요."
        ),
    ],

    "ISTP": [
        (
            "개굴닌자",
            658,
            "말보다 행동으로 보여주고 상황을 빠르게 파악하는 모습이 닮았어요.<br>"
            "침착하고 독립적이면서 필요한 순간에는 놀라운 실력을 보여줘요."
        ),
        (
            "리오르",
            447,
            "빠르게 상황을 읽고 직접 행동으로 해결하는 모습이 잘 맞아요.<br>"
            "말보다 실력으로 보여주는 점이 ISTP와 닮았어요."
        ),
        (
            "메타몽",
            132,
            "상황에 따라 빠르고 유연하게 대처하는 모습이 닮았어요.<br>"
            "필요할 때 가장 적절한 방식으로 바뀌는 실용적인 면이 있어요."
        ),
    ],

    "ISFP": [
        (
            "님피아",
            700,
            "자신만의 감성과 취향을 소중하게 생각하는 모습이 닮았어요.<br>"
            "부드럽고 다정하지만 좋아하는 것을 지킬 때는 누구보다 단단해요."
        ),
        (
            "밀로틱",
            350,
            "부드럽고 감성적이며 자신만의 아름다운 분위기를 가진 모습이 잘 맞아요.<br>"
            "조용하지만 분명한 매력을 가진 점이 ISFP와 닮았어요."
        ),
        (
            "샤미드",
            134,
            "차분하고 부드러운 분위기 속에 자신만의 감성을 가지고 있어요.<br>"
            "자연스럽고 편안한 매력이 ISFP와 잘 어울려요."
        ),
    ],

    "ESTP": [
        (
            "윈디",
            59,
            "빠르게 움직이고 새로운 상황에 뛰어드는 모습이 닮았어요.<br>"
            "대담하고 활동적이며 순간의 기회를 놓치지 않는 힘이 있어요."
        ),
        (
            "헤라크로스",
            214,
            "활동적이고 도전을 두려워하지 않는 모습이 잘 맞아요.<br>"
            "몸으로 부딪히며 해결하는 에너지가 ESTP와 닮았어요."
        ),
        (
            "초염몽",
            392,
            "강한 에너지와 빠른 행동력이 ESTP와 잘 어울려요.<br>"
            "새로운 승부와 자극을 즐기는 모습이 닮았어요."
        ),
    ],

    "ESFP": [
        (
            "파이리",
            4,
            "밝고 적극적이며 주변 사람에게 활기를 주는 모습이 닮았어요.<br>"
            "감정을 솔직하게 표현하고 즐거운 경험을 누구보다 잘 즐겨요."
        ),
        (
            "피츄",
            172,
            "밝고 사랑스러운 에너지로 주변의 관심을 끄는 모습이 잘 맞아요.<br>"
            "함께 있을 때 분위기를 즐겁게 만드는 점이 닮았어요."
        ),
        (
            "치라미",
            572,
            "사교적이고 귀여운 매력으로 주변 분위기를 즐겁게 만들어요.<br>"
            "활발하게 사람들과 어울리는 모습이 ESFP와 잘 맞아요."
        ),
    ],
}


# =========================================================
# 디자인
# =========================================================
st.html("""
<style>

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

#MainMenu,
footer {
    visibility: hidden;
}

.stApp {
    background:
        radial-gradient(
            circle at 18% 8%,
            rgba(255, 221, 94, 0.26),
            transparent 28%
        ),
        linear-gradient(
            180deg,
            #FFF4C7 0%,
            #FFF9E6 48%,
            #FFFDF7 100%
        );
}

.block-container {
    max-width: 940px;
    padding-top: 0.55rem;
    padding-bottom: 0.55rem;
}


/* 시작 화면 */
.hero-card {
    background: #FFFDF7;
    border: 4px solid #E3B32B;
    border-radius: 26px;
    padding: 18px 22px 16px;
    text-align: center;

    box-shadow:
        0 10px 26px rgba(100, 69, 14, 0.12);

    margin-bottom: 12px;
}

.hero-ball {
    width: 42px;
    height: 42px;

    margin: 0 auto 6px;

    border: 4px solid #49351B;
    border-radius: 50%;

    position: relative;

    background:
        linear-gradient(
            180deg,
            #E85B4D 0%,
            #E85B4D 43%,
            #49351B 43%,
            #49351B 57%,
            #FFFFFF 57%,
            #FFFFFF 100%
        );
}

.hero-ball::after {
    content: "";

    position: absolute;

    width: 11px;
    height: 11px;

    background: white;

    border: 3px solid #49351B;
    border-radius: 50%;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%);
}

.hero-title {
    font-size: 34px;
    font-weight: 900;

    color: #4B3513;

    letter-spacing: -1.2px;
}

.hero-description {
    margin-top: 5px;

    font-size: 15px;

    color: #816A42;
}


/* 버튼 */
div.stButton > button {
    width: 100%;

    min-height: 43px;

    border:
        2px solid #DCAA31;

    border-radius: 13px;

    background: #FFE58A;

    color: #503914;

    font-size: 16px;
    font-weight: 800;

    box-shadow:
        0 3px 0 #C79728;

    transition: 0.12s;
}

div.stButton > button:hover {
    background: #FFD64F;

    color: #412D0B;

    border-color: #CE981C;

    transform: translateY(-2px);
}


/* 포켓몬 카드 */
.pokemon-card {
    background:
        linear-gradient(
            145deg,
            #FFF6C9 0%,
            #FFE8A0 100%
        );

    border:
        6px solid #DCA923;

    border-radius: 28px;

    box-shadow:
        0 14px 32px rgba(99, 68, 12, 0.18),
        inset 0 0 0 2px rgba(255, 255, 255, 0.72);

    overflow: hidden;
}

.card-top {
    padding: 10px 18px 8px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    border-bottom:
        2px solid rgba(120, 85, 20, 0.14);
}

.mbti-badge {
    background: #E6B629;

    color: #473107;

    border-radius: 999px;

    padding: 6px 14px;

    font-size: 15px;
    font-weight: 900;
}

.dex-number {
    color: #806329;

    font-size: 13px;
    font-weight: 800;
}

.card-body {
    display: grid;

    grid-template-columns:
        0.95fr 1.05fr;

    min-height: 315px;
}


/* 왼쪽 */
.visual-area {
    padding: 10px 16px;

    display: flex;

    flex-direction: column;

    align-items: center;
    justify-content: center;

    border-right:
        2px solid rgba(120, 85, 20, 0.13);

    background:
        radial-gradient(
            circle,
            rgba(255,255,255,.82) 0%,
            rgba(255,255,255,.18) 60%,
            transparent 61%
        );
}

.pokemon-image {
    width: 100%;

    max-width: 245px;
    max-height: 215px;

    object-fit: contain;

    filter:
        drop-shadow(
            0 9px 8px rgba(88,57,8,.12)
        );
}

.pokemon-name {
    color: #B66807;

    font-size: 38px;

    font-weight: 900;

    line-height: 1.05;
}

.small-label {
    margin-top: 3px;

    color: #937131;

    font-size: 12px;

    font-weight: 700;
}


/* 오른쪽 */
.info-area {
    padding: 17px 20px;

    display: flex;

    flex-direction: column;

    justify-content: center;
}

.info-title {
    color: #75551C;

    font-size: 14px;

    font-weight: 900;

    margin-bottom: 6px;
}

.reason-box {
    padding: 14px 16px;

    border:
        2px solid #E1C576;

    border-radius: 15px;

    background:
        rgba(255, 253, 243, 0.9);

    color: #54432A;

    font-size: 16px;

    line-height: 1.62;

    word-break: keep-all;
}

.match-box {
    margin-top: 10px;

    padding: 9px 13px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    border:
        2px dashed #C79621;

    border-radius: 14px;

    background: #FFE178;
}

.match-label {
    color: #73571E;

    font-size: 13px;

    font-weight: 800;
}

.match-type {
    color: #553A04;

    font-size: 24px;

    font-weight: 900;
}

.footer-note {
    margin-top: 5px;

    text-align: center;

    color: #9A8967;

    font-size: 11px;
}


/* 모바일 */
@media (max-width: 700px) {

    .block-container {
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }

    .hero-title {
        font-size: 28px;
    }

    .hero-description {
        font-size: 14px;
    }

    div.stButton > button {
        min-height: 41px;
        font-size: 14px;
    }

    .card-body {
        grid-template-columns: 1fr;
    }

    .visual-area {
        border-right: 0;

        border-bottom:
            2px solid rgba(120,85,20,.13);
    }

    .pokemon-image {
        max-width: 190px;
        max-height: 165px;
    }

    .pokemon-name {
        font-size: 31px;
    }

    .info-area {
        padding: 13px;
    }

    .reason-box {
        font-size: 14px;
    }

}

</style>
""")


# =========================================================
# 세션 상태
# =========================================================
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

if "selected_pokemon" not in st.session_state:
    st.session_state.selected_pokemon = None


# =========================================================
# MBTI 선택 화면
# =========================================================
if st.session_state.selected_mbti is None:

    st.html("""
<div class="hero-card">

    <div class="hero-ball"></div>

    <div class="hero-title">
        MBTI 포켓몬 추천기
    </div>

    <div class="hero-description">
        나의 MBTI를 선택하고 나와 닮은 포켓몬을 랜덤으로 만나보세요!
    </div>

</div>
""")


    mbti_list = [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP",
    ]


    for start in range(0, 16, 4):

        cols = st.columns(
            4,
            gap="small"
        )

        row = mbti_list[
            start:start + 4
        ]


        for col, mbti in zip(
            cols,
            row
        ):

            with col:

                if st.button(
                    mbti,
                    key=f"mbti_{mbti}",
                    use_container_width=True
                ):

                    st.session_state.selected_mbti = (
                        mbti
                    )

                    st.session_state.selected_pokemon = (
                        random.choice(
                            mbti_pokemon[mbti]
                        )
                    )

                    st.rerun()


    st.html("""
<div class="footer-note">
    MBTI와 포켓몬 매칭은 재미를 위한 콘텐츠입니다 😊
</div>
""")


# =========================================================
# 결과 화면
# =========================================================
else:

    mbti = (
        st.session_state.selected_mbti
    )

    name, dex_id, reason = (
        st.session_state.selected_pokemon
    )

    match = (
        mbti_match[mbti]
    )


    st.html(
        f"""
<div class="pokemon-card">

    <div class="card-top">

        <div class="mbti-badge">
            {mbti} 타입
        </div>

        <div class="dex-number">
            Pokédex No. {dex_id}
        </div>

    </div>


    <div class="card-body">

        <div class="visual-area">

            <img
                class="pokemon-image"
                src="{get_pokemon_image_url(dex_id)}"
                alt="{name}"
            >

            <div class="pokemon-name">
                {name}
            </div>

            <div class="small-label">
                이번에 만난 포켓몬
            </div>

        </div>


        <div class="info-area">

            <div class="info-title">
                💬 이 포켓몬이 어울리는 이유
            </div>

            <div class="reason-box">
                {reason}
            </div>


            <div class="match-box">

                <div class="match-label">
                    💛 잘 맞는 MBTI
                </div>

                <div class="match-type">
                    {match}
                </div>

            </div>

        </div>

    </div>

</div>
"""
    )


    # =====================================================
    # 결과 버튼
    # =====================================================
    col1, col2 = st.columns(
        2,
        gap="small"
    )


    # 같은 MBTI의 다른 포켓몬 추천
    with col1:

        if st.button(
            "🎲 같은 MBTI로 다시 추천",
            use_container_width=True
        ):

            current = (
                st.session_state.selected_pokemon
            )

            candidates = [
                pokemon
                for pokemon
                in mbti_pokemon[mbti]
                if pokemon != current
            ]

            st.session_state.selected_pokemon = (
                random.choice(
                    candidates
                )
            )

            st.rerun()


    # 처음 화면으로 돌아가기
    with col2:

        if st.button(
            "↩ MBTI 다시 고르기",
            use_container_width=True
        ):

            st.session_state.selected_mbti = (
                None
            )

            st.session_state.selected_pokemon = (
                None
            )

            st.rerun()


    st.html("""
<div class="footer-note">
    포켓몬 이미지: PokeAPI Sprites · MBTI 매칭은 재미를 위한 콘텐츠입니다.
</div>
""")
