import streamlit as st
import random


# =========================================================
# 페이지 기본 설정
# =========================================================
st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="✨",
    layout="centered"
)


# =========================================================
# 포켓몬 이미지
# PokeAPI Sprites 공식 아트워크 주소 사용
# =========================================================
def get_pokemon_image_url(pokedex_id):
    return (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/other/official-artwork/{pokedex_id}.png"
    )


# =========================================================
# MBTI별 궁합
# 재미를 위한 간단한 매칭
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
    "ESFP": "ISTJ"
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
            "냉철하게 상황을 분석하고 자신만의 전략을 세우는 모습이 "
            "INTJ와 잘 어울려요."
        ),
        (
            "팬텀",
            94,
            "조용히 상황을 관찰하다가 필요한 순간에 움직이는 "
            "영리한 모습이 INTJ와 닮았어요."
        ),
        (
            "나인테일",
            38,
            "신비롭고 지적인 분위기와 독립적인 성향이 "
            "INTJ의 매력과 잘 맞아요."
        )
    ],

    "INTP": [
        (
            "야도킹",
            199,
            "느긋해 보여도 머릿속에서는 끊임없이 생각하는 모습이 "
            "INTP와 닮았어요."
        ),
        (
            "팬텀",
            94,
            "평범한 방식보다 독특한 접근을 즐기는 모습이 "
            "INTP의 자유로운 사고와 잘 어울려요."
        ),
        (
            "이브이",
            133,
            "한 가지 길에 머무르지 않고 다양한 가능성을 가진 모습이 "
            "INTP와 닮았어요."
        )
    ],

    "ENTJ": [
        (
            "리자몽",
            6,
            "강한 자신감과 추진력으로 목표를 향해 나아가는 모습이 "
            "ENTJ와 잘 어울려요."
        ),
        (
            "엠페르트",
            395,
            "당당한 카리스마와 주변을 이끄는 리더의 모습이 "
            "ENTJ를 떠올리게 해요."
        ),
        (
            "루카리오",
            448,
            "목표를 정하면 흔들리지 않고 끝까지 나아가는 강한 의지가 "
            "ENTJ와 닮았어요."
        )
    ],

    "ENTP": [
        (
            "피카츄",
            25,
            "활발하고 재치 있으며 새로운 상황을 즐기는 모습이 "
            "ENTP와 잘 맞아요."
        ),
        (
            "조로아크",
            571,
            "기발한 방법과 뛰어난 임기응변으로 상황을 바꾸는 모습이 "
            "ENTP와 닮았어요."
        ),
        (
            "초염몽",
            392,
            "도전을 즐기고 빠르게 행동하는 강한 에너지가 "
            "ENTP와 잘 어울려요."
        )
    ],

    "INFJ": [
        (
            "뮤",
            151,
            "신비롭고 조용하지만 깊은 가능성을 가지고 있는 모습이 "
            "INFJ와 잘 어울려요."
        ),
        (
            "라프라스",
            131,
            "차분하면서도 주변을 따뜻하게 배려하는 성격이 "
            "INFJ와 닮았어요."
        ),
        (
            "가디안",
            282,
            "다른 사람의 마음을 이해하고 소중한 존재를 지키려는 모습이 "
            "INFJ와 잘 맞아요."
        )
    ],

    "INFP": [
        (
            "가디안",
            282,
            "자신이 중요하게 생각하는 가치와 사람을 지키는 모습이 "
            "INFP와 닮았어요."
        ),
        (
            "푸린",
            39,
            "부드럽고 감성적이며 자신의 마음을 솔직하게 표현하는 모습이 "
            "INFP와 잘 어울려요."
        ),
        (
            "세레비",
            251,
            "따뜻한 이상과 희망을 품은 신비로운 이미지가 "
            "INFP와 닮았어요."
        )
    ],

    "ENFJ": [
        (
            "엠페르트",
            395,
            "주변을 자연스럽게 이끌고 책임감 있게 행동하는 모습이 "
            "ENFJ와 잘 맞아요."
        ),
        (
            "밀로틱",
            350,
            "부드럽고 우아하면서 주변에 긍정적인 영향을 주는 모습이 "
            "ENFJ와 닮았어요."
        ),
        (
            "루카리오",
            448,
            "다른 사람의 마음을 이해하고 함께 성장하려는 모습이 "
            "ENFJ와 잘 어울려요."
        )
    ],

    "ENFP": [
        (
            "피카츄",
            25,
            "밝고 친근하며 어디에서든 새로운 재미를 만들어내는 모습이 "
            "ENFP와 닮았어요."
        ),
        (
            "페라페",
            441,
            "표현력이 풍부하고 활발하게 소통하는 모습이 "
            "ENFP와 잘 맞아요."
        ),
        (
            "치라치노",
            573,
            "호기심이 많고 밝은 에너지로 주변 분위기를 살리는 모습이 "
            "ENFP와 닮았어요."
        )
    ],

    "ISTJ": [
        (
            "메타그로스",
            376,
            "체계적으로 판단하고 맡은 일을 정확하게 해내는 모습이 "
            "ISTJ와 잘 어울려요."
        ),
        (
            "강철톤",
            208,
            "단단하고 쉽게 흔들리지 않으며 원칙을 지키는 모습이 "
            "ISTJ와 닮았어요."
        ),
        (
            "그란돈",
            383,
            "묵직한 존재감과 안정적인 힘이 책임감 강한 "
            "ISTJ를 떠올리게 해요."
        )
    ],

    "ISFJ": [
        (
            "피츄",
            172,
            "다정하고 순수하며 가까운 사람에게 따뜻한 마음을 표현하는 모습이 "
            "ISFJ와 닮았어요."
        ),
        (
            "라프라스",
            131,
            "주변을 편안하게 만들어주고 다른 사람을 배려하는 모습이 "
            "ISFJ와 잘 맞아요."
        ),
        (
            "토게피",
            175,
            "따뜻하고 편안한 분위기와 주변을 챙기는 마음이 "
            "ISFJ와 닮았어요."
        )
    ],

    "ESTJ": [
        (
            "랜드로스",
            645,
            "강한 실행력으로 상황을 정리하고 이끄는 모습이 "
            "ESTJ와 잘 어울려요."
        ),
        (
            "괴력몬",
            68,
            "부지런하고 힘 있게 목표를 수행하는 모습이 "
            "ESTJ의 추진력과 닮았어요."
        ),
        (
            "메타그로스",
            376,
            "효율적이고 체계적으로 판단하는 성격이 "
            "ESTJ와 잘 맞아요."
        )
    ],

    "ESFJ": [
        (
            "이브이",
            133,
            "친근하고 여러 사람들과 자연스럽게 어울리는 모습이 "
            "ESFJ와 닮았어요."
        ),
        (
            "잠만보",
            143,
            "함께 있으면 편안하고 따뜻한 분위기를 만들어주는 모습이 "
            "ESFJ와 잘 어울려요."
        ),
        (
            "럭키",
            113,
            "다른 사람을 돕고 챙기는 다정한 성격이 "
            "ESFJ와 닮았어요."
        )
    ],

    "ISTP": [
        (
            "메타몽",
            132,
            "상황에 따라 빠르고 유연하게 대처하는 모습이 "
            "ISTP와 잘 어울려요."
        ),
        (
            "이상해씨",
            1,
            "차분하면서도 자신의 방식대로 실용적으로 움직이는 모습이 "
            "ISTP와 닮았어요."
        ),
        (
            "리오르",
            447,
            "말보다는 행동으로 보여주며 순간적인 대응력이 뛰어난 모습이 "
            "ISTP와 잘 맞아요."
        )
    ],

    "ISFP": [
        (
            "밀로틱",
            350,
            "부드럽고 감성적이며 자신만의 아름다운 분위기를 가진 모습이 "
            "ISFP와 닮았어요."
        ),
        (
            "이브이",
            133,
            "자신만의 방식과 가능성을 소중하게 여기며 성장하는 모습이 "
            "ISFP와 잘 어울려요."
        ),
        (
            "샤미드",
            134,
            "차분하고 부드러운 분위기 속에 자신만의 감성을 가진 모습이 "
            "ISFP와 닮았어요."
        )
    ],

    "ESTP": [
        (
            "윈디",
            59,
            "빠르고 대담하게 움직이며 새로운 상황을 즐기는 모습이 "
            "ESTP와 닮았어요."
        ),
        (
            "헤라크로스",
            214,
            "활동적이고 도전을 두려워하지 않는 모습이 "
            "ESTP와 잘 맞아요."
        ),
        (
            "파이숭이",
            256,
            "에너지가 넘치고 순간적인 판단으로 행동하는 모습이 "
            "ESTP와 닮았어요."
        )
    ],

    "ESFP": [
        (
            "피츄",
            172,
            "밝고 사랑스러운 에너지로 주변의 관심을 끄는 모습이 "
            "ESFP와 잘 어울려요."
        ),
        (
            "망키",
            56,
            "활발하고 감정 표현이 솔직한 모습이 "
            "ESFP와 닮았어요."
        ),
        (
            "치라미",
            572,
            "사교적이고 귀여운 매력으로 주변 분위기를 즐겁게 만드는 모습이 "
            "ESFP와 잘 맞아요."
        )
    ]
}


# =========================================================
# CSS
# st.html을 사용하므로 HTML이 코드처럼 노출되지 않음
# =========================================================
st.html("""
<style>

.stApp {
    background:
        linear-gradient(
            180deg,
            #FFF2BE 0%,
            #FFF8DF 50%,
            #FFFDF6 100%
        );
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* -------------------------
   첫 화면
------------------------- */

.hero-card {
    background: #FFFDF7;
    border: 3px solid #E9B934;
    border-radius: 30px;
    padding: 34px 24px;
    text-align: center;
    box-shadow: 0 12px 28px rgba(120, 88, 20, 0.12);
    margin-bottom: 24px;
}

.hero-icon {
    font-size: 54px;
    line-height: 1.2;
}

.hero-title {
    color: #503813;
    font-size: 44px;
    font-weight: 900;
    margin-top: 8px;
    letter-spacing: -1.5px;
}

.hero-description {
    color: #806A42;
    font-size: 19px;
    line-height: 1.7;
    margin-top: 12px;
}


/* -------------------------
   MBTI 버튼
------------------------- */

div.stButton > button {
    width: 100%;
    min-height: 56px;

    border: 2px solid #E3BB4D;
    border-radius: 17px;

    background: #FFE58C;
    color: #513A13;

    font-size: 19px;
    font-weight: 800;

    box-shadow: 0 4px 0 #D7AF43;

    transition:
        transform 0.15s ease,
        background 0.15s ease;
}

div.stButton > button:hover {
    background: #FFDA56;
    border-color: #D8A72E;
    color: #44300C;
    transform: translateY(-2px);
}

div.stButton > button:active {
    transform: translateY(1px);
}


/* -------------------------
   포켓몬 카드
------------------------- */

.pokemon-card {
    position: relative;

    background:
        linear-gradient(
            145deg,
            #FFFDF5,
            #FFF0B4
        );

    border: 5px solid #E9B632;
    border-radius: 32px;

    padding: 28px 28px 22px;

    text-align: center;

    box-shadow:
        0 15px 38px rgba(112, 78, 19, 0.16);

    margin-bottom: 20px;
}


/* 카드 상단 작은 원 */
.card-circle {
    width: 15px;
    height: 15px;

    margin: 0 auto 12px;

    border-radius: 50%;

    background: #E24D3E;

    box-shadow:
        22px 0 0 #F5CE4A,
        -22px 0 0 #69A9E8;
}


.mbti-badge {
    display: inline-block;

    background: #F1C645;
    color: #51390F;

    padding: 8px 20px;

    border-radius: 999px;

    font-size: 18px;
    font-weight: 900;
}


.pokemon-name {
    color: #B86C0D;

    font-size: 48px;
    font-weight: 900;

    margin-top: 12px;

    letter-spacing: -1px;
}


.dex-number {
    color: #91733F;

    font-size: 16px;
    font-weight: 700;

    margin-top: 3px;
}


/* -------------------------
   추천 이유
------------------------- */

.reason-box {
    max-width: 690px;

    margin: 20px auto;

    background: #FFF9E8;

    border: 2px solid #EFD785;

    border-radius: 20px;

    padding: 21px 25px;

    color: #59482C;

    font-size: 19px;
    line-height: 1.8;

    text-align: center;

    word-break: keep-all;
}


.reason-title {
    font-size: 17px;
    font-weight: 800;

    color: #8A681F;

    margin-bottom: 9px;
}


/* -------------------------
   궁합
------------------------- */

.match-box {
    max-width: 470px;

    margin: 0 auto 18px;

    background: #FFE99A;

    border: 2px dashed #D4A72D;

    border-radius: 20px;

    padding: 17px;
}


.match-title {
    color: #806329;

    font-size: 16px;
}


.match-type {
    color: #60420B;

    font-size: 30px;
    font-weight: 900;

    margin-top: 2px;
}


/* -------------------------
   포켓몬 이미지
------------------------- */

[data-testid="stImage"] img {
    max-height: 340px;
    object-fit: contain;
}


/* -------------------------
   아래 안내
------------------------- */

.footer {
    margin-top: 25px;

    color: #9A8968;

    font-size: 13px;

    text-align: center;

    line-height: 1.6;
}


/* -------------------------
   모바일
------------------------- */

@media (max-width: 650px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-title {
        font-size: 32px;
    }

    .hero-description {
        font-size: 16px;
    }

    div.stButton > button {
        min-height: 50px;
        font-size: 16px;
    }

    .pokemon-name {
        font-size: 38px;
    }

    .reason-box {
        font-size: 17px;
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
    <div class="hero-icon">✨</div>

    <div class="hero-title">
        MBTI 포켓몬 추천기
    </div>

    <div class="hero-description">
        나의 MBTI를 선택하면<br>
        성격과 잘 어울리는 포켓몬을 찾아드려요!
    </div>
</div>
""")


    mbti_list = [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]


    # 4개씩 4줄
    for start in range(0, 16, 4):

        cols = st.columns(4)

        row = mbti_list[start:start + 4]

        for col, mbti in zip(cols, row):

            with col:

                if st.button(
                    mbti,
                    key=f"mbti_{mbti}",
                    use_container_width=True
                ):

                    st.session_state.selected_mbti = mbti

                    st.session_state.selected_pokemon = random.choice(
                        mbti_pokemon[mbti]
                    )

                    st.rerun()


    st.html("""
<div class="footer">
    MBTI와 포켓몬 매칭은 재미를 위한 콘텐츠입니다 😊
</div>
""")


# =========================================================
# 결과 화면
# =========================================================
else:

    selected_mbti = st.session_state.selected_mbti

    name, dex_id, reason = st.session_state.selected_pokemon

    match = mbti_match[selected_mbti]


    # -----------------------------------------------------
    # 포켓몬 카드 상단
    # -----------------------------------------------------
    st.html(
        f"""
<div class="pokemon-card">

    <div class="card-circle"></div>

    <div class="mbti-badge">
        {selected_mbti} 타입
    </div>

    <div class="pokemon-name">
        {name}
    </div>

    <div class="dex-number">
        Pokédex No. {dex_id}
    </div>

</div>
"""
    )


    # -----------------------------------------------------
    # 포켓몬 이미지
    # -----------------------------------------------------
    left, center, right = st.columns(
        [1, 2.2, 1]
    )

    with center:

        st.image(
            get_pokemon_image_url(dex_id),
            use_container_width=True
        )


    # -----------------------------------------------------
    # 추천 이유
    # -----------------------------------------------------
    st.html(
        f"""
<div class="reason-box">

    <div class="reason-title">
        💬 이 포켓몬을 추천하는 이유
    </div>

    {reason}

</div>
"""
    )


    # -----------------------------------------------------
    # 궁합
    # -----------------------------------------------------
    st.html(
        f"""
<div class="match-box">

    <div class="match-title">
        💛 잘 맞는 MBTI
    </div>

    <div class="match-type">
        {match}
    </div>

</div>
"""
    )


    # 버튼 위 여백
    st.write("")


    # -----------------------------------------------------
    # 버튼
    # -----------------------------------------------------
    col1, col2 = st.columns(2)


    # 같은 MBTI에서 다른 포켓몬 뽑기
    with col1:

        if st.button(
            "🎲 다른 포켓몬 추천",
            use_container_width=True
        ):

            current_pokemon = st.session_state.selected_pokemon

            candidates = [
                pokemon
                for pokemon in mbti_pokemon[selected_mbti]
                if pokemon != current_pokemon
            ]

            st.session_state.selected_pokemon = random.choice(
                candidates
            )

            st.rerun()


    # MBTI 처음부터 고르기
    with col2:

        if st.button(
            "↩ MBTI 다시 고르기",
            use_container_width=True
        ):

            st.session_state.selected_mbti = None
            st.session_state.selected_pokemon = None

            st.rerun()


    # -----------------------------------------------------
    # 출처
    # -----------------------------------------------------
    st.html("""
<div class="footer">
    포켓몬 이미지: PokeAPI Sprites<br>
    MBTI 매칭은 재미를 위한 콘텐츠입니다.
</div>
""")
