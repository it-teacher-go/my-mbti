import streamlit as st
import random

# =========================================================
# 기본 설정
# =========================================================
st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="✨",
    layout="centered"
)


# =========================================================
# 포켓몬 이미지 주소
# PokeAPI 공개 스프라이트 저장소 사용
# =========================================================
def get_pokemon_image_url(pokedex_id):
    return (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/other/official-artwork/{pokedex_id}.png"
    )


# =========================================================
# MBTI별 궁합 유형
# 재미를 위한 간단한 매칭입니다.
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
# (포켓몬 이름, 도감번호, 추천 이유)
#
# 각 MBTI별로 3마리 중 랜덤으로 1마리를 추천합니다.
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
# 화면 디자인
# =========================================================
st.markdown(
    """
    <style>

    /* 전체 배경 */
    .stApp {
        background:
            linear-gradient(
                180deg,
                #FFF3C4 0%,
                #FFF9E8 55%,
                #FFFDF7 100%
            );
    }

    /* 페이지 너비 */
    .block-container {
        max-width: 900px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }


    /* 상단 제목 카드 */
    .hero-card {
        background: #FFFDF6;
        border: 3px solid #F0C95B;
        border-radius: 30px;
        padding: 32px 25px;
        text-align: center;
        box-shadow:
            0 12px 30px rgba(110, 76, 20, 0.10);
        margin-bottom: 25px;
    }

    .hero-icon {
        font-size: 54px;
        margin-bottom: 5px;
    }

    .hero-title {
        font-size: 44px;
        font-weight: 900;
        color: #523B17;
        letter-spacing: -1.5px;
    }

    .hero-description {
        margin-top: 10px;
        font-size: 19px;
        line-height: 1.7;
        color: #7B6540;
    }


    /* MBTI 선택 버튼 */
    div.stButton > button {

        width: 100%;

        min-height: 55px;

        border-radius: 17px;

        border: 1px solid #E1BC50;

        background: #FFE58C;

        color: #513C17;

        font-size: 19px;

        font-weight: 800;

        box-shadow:
            0 4px 0 #D9B74F;

        transition: 0.15s;
    }


    div.stButton > button:hover {

        background: #FFDA58;

        color: #44300C;

        border-color: #D5AA34;

        transform: translateY(-2px);
    }


    /* 결과 카드 */
    .pokemon-card {

        background:
            linear-gradient(
                145deg,
                #FFFDF4,
                #FFF5CB
            );

        border: 4px solid #E8BC3C;

        border-radius: 30px;

        padding: 28px;

        text-align: center;

        box-shadow:
            0 13px 35px rgba(101, 73, 20, 0.15);

        margin-bottom: 15px;
    }


    /* 카드 상단 MBTI */
    .mbti-badge {

        display: inline-block;

        background: #F2C94C;

        color: #4E3814;

        padding: 8px 20px;

        border-radius: 999px;

        font-size: 18px;

        font-weight: 900;
    }


    /* 포켓몬 이름 */
    .pokemon-name {

        font-size: 46px;

        font-weight: 900;

        color: #C97D12;

        margin-top: 10px;

        margin-bottom: 5px;
    }


    /* 도감 번호 */
    .dex-number {

        color: #967544;

        font-size: 16px;

        font-weight: 700;

        margin-bottom: 5px;
    }


    /* 추천 이유 */
    .reason-box {

        max-width: 680px;

        margin:
            20px auto 20px;

        background: #FFF8DF;

        border: 2px solid #F1D98A;

        border-radius: 18px;

        padding: 20px 24px;

        color: #59492F;

        font-size: 19px;

        line-height: 1.8;

        word-break: keep-all;
    }


    /* 궁합 */
    .match-box {

        max-width: 480px;

        margin: auto;

        background: #FFE898;

        border: 2px dashed #D7AE3D;

        border-radius: 18px;

        padding: 16px;
    }


    .match-title {

        color: #82652F;

        font-size: 16px;
    }


    .match-type {

        color: #60440E;

        font-size: 29px;

        font-weight: 900;

        margin-top: 2px;
    }


    /* 안내 문구 */
    .footer {

        margin-top: 25px;

        text-align: center;

        color: #9B8968;

        font-size: 13px;
    }


    /* 포켓몬 이미지 크기 */
    [data-testid="stImage"] img {

        max-height: 330px;

        object-fit: contain;
    }


    /* 스마트폰 */
    @media (max-width: 650px) {

        .hero-title {
            font-size: 32px;
        }

        .hero-description {
            font-size: 16px;
        }

        div.stButton > button {
            min-height: 49px;
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
    """,
    unsafe_allow_html=True
)


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

    st.markdown(
        """
        <div class="hero-card">

            <div class="hero-icon">
                ✨
            </div>

            <div class="hero-title">
                MBTI 포켓몬 추천기
            </div>

            <div class="hero-description">

                나의 MBTI를 선택하면<br>

                성격과 잘 어울리는 포켓몬을 찾아드려요!

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # MBTI 순서
    mbti_list = [

        "INTJ", "INTP", "ENTJ", "ENTP",

        "INFJ", "INFP", "ENFJ", "ENFP",

        "ISTJ", "ISFJ", "ESTJ", "ESFJ",

        "ISTP", "ISFP", "ESTP", "ESFP"

    ]


    # 4개씩 4줄
    for start in range(0, 16, 4):

        cols = st.columns(4)

        current_row = mbti_list[start:start + 4]

        for col, mbti in zip(cols, current_row):

            with col:

                if st.button(
                    mbti,
                    key=f"mbti_{mbti}",
                    use_container_width=True
                ):

                    st.session_state.selected_mbti = mbti

                    st.session_state.selected_pokemon = (
                        random.choice(
                            mbti_pokemon[mbti]
                        )
                    )

                    st.rerun()


    st.markdown(
        """
        <div class="footer">

        MBTI와 포켓몬 매칭은 재미를 위한 콘텐츠입니다 😊

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 결과 화면
# =========================================================

else:

    selected_mbti = (
        st.session_state.selected_mbti
    )

    name, dex_id, reason = (
        st.session_state.selected_pokemon
    )

    match = mbti_match[selected_mbti]


    # 포켓몬 카드 상단
    st.markdown(
        f"""
        <div class="pokemon-card">

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
        """,
        unsafe_allow_html=True
    )


    # 포켓몬 이미지
    col1, col2, col3 = st.columns(
        [1, 2.2, 1]
    )

    with col2:

        st.image(
            get_pokemon_image_url(
                dex_id
            ),
            use_container_width=True
        )


    # 추천 이유 + 궁합
    st.markdown(
        f"""
        <div class="reason-box">

            <b>💬 이 포켓몬을 추천하는 이유</b>

            <br><br>

            {reason}

        </div>


        <div class="match-box">

            <div class="match-title">
                💛 잘 맞는 MBTI
            </div>

            <div class="match-type">
                {match}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    # 같은 MBTI로 포켓몬 다시 뽑기
    col_left, col_right = st.columns(2)


    with col_left:

        if st.button(
            "🎲 다른 포켓몬 추천",
            use_container_width=True
        ):

            st.session_state.selected_pokemon = (
                random.choice(
                    mbti_pokemon[
                        selected_mbti
                    ]
                )
            )

            st.rerun()


    # MBTI 처음부터 선택
    with col_right:

        if st.button(
            "↩ MBTI 다시 고르기",
            use_container_width=True
        ):

            st.session_state.selected_mbti = None

            st.session_state.selected_pokemon = None

            st.rerun()


    st.markdown(
        """
        <div class="footer">

        포켓몬 이미지: PokeAPI Sprites<br>

        Made with Streamlit

        </div>
        """,
        unsafe_allow_html=True
    )
