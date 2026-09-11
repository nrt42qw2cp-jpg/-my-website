import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="بوابة التميز الأكاديمي | جامعة الملك سعود",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تصميم احترافي متجاوب تماماً مع شاشات الجوال والكمبيوتر
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

    html, body, [class*="css"], .stMarkdown {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    /* إصلاح تباعد الصفحة */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 900px !important;
    }

    /* الترويسة الرئيسية بهوية KSU */
    .ksu-banner {
        background: linear-gradient(135deg, #005980 0%, #00364d 100%);
        border-radius: 16px;
        padding: 20px 18px;
        color: #ffffff;
        margin-bottom: 22px;
        box-shadow: 0 4px 15px rgba(0, 89, 128, 0.15);
        border-bottom: 4px solid #C59B27;
        text-align: center;
    }
    .ksu-banner h1 {
        font-size: 20px !important;
        font-weight: 800;
        margin: 0 0 6px 0 !important;
        color: #ffffff !important;
        line-height: 1.4 !important;
    }
    .ksu-banner p {
        font-size: 13px !important;
        margin: 0 !important;
        color: #e2f1f8 !important;
        font-weight: 500;
        line-height: 1.5 !important;
    }

    /* بطاقة المقرر */
    .course-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 18px;
        border: 1px solid #E2E8F0;
        border-right: 5px solid #005980;
        margin-bottom: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .course-card h2 {
        font-size: 18px !important;
        font-weight: 700;
        color: #005980 !important;
        margin: 0 0 8px 0 !important;
        line-height: 1.3 !important;
    }
    .level-badge {
        display: inline-block;
        background-color: #C59B27;
        color: #ffffff;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .course-card p {
        font-size: 13px !important;
        color: #475569 !important;
        margin: 0 !important;
        line-height: 1.6 !important;
    }

    /* تحسين مظهر التبويبات */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        direction: rtl;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Tajawal', sans-serif !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        padding: 8px 12px !important;
        border-radius: 8px 8px 0 0 !important;
        color: #005980 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. بيانات المقررات
COURSES = [
    {
        "id": "LING201",
        "name": "مقدمة في اللغويات (Intro to Linguistics)",
        "code": "201 لغويات",
        "level": "المستوى الثالث",
        "description": "دراسة علمية لبنية اللغة؛ تشمل الصوتيات (Phonetics)، التراكيب (Syntax)، والمعاني (Semantics).",
        "tips": [
            "احفظ جدول الرموز الصوتية (IPA) أولاً بأول؛ تتكرر دائماً في الاختبارات.",
            "تدرب أسبوعياً على رسم شجرة التراكيب (Syntax Trees).",
            "افهم الفرق بين الصرف الاشتقاقي والتصريفي مبكراً."
        ],
        "materials": [
            {"title": "الكتاب المعتمد: The Study of Language (George Yule)", "url": "https://example.com/book1"},
            {"title": "سلايدات وتفريغات المقرر المعتمدة", "url": "https://example.com/slides1"}
        ]
    },
    {
        "id": "TRANS202",
        "name": "الترجمة التحريرية - عامة (Written Translation)",
        "code": "202 ترج",
        "level": "المستوى الرابع",
        "description": "تطوير استراتيجيات النقل والتعريب للنصوص والمقالات الصحفية والإدارية.",
        "tips": [
            "تجنب النقل الحرفي للمصطلحات والمجازات (Idioms) وابحث عن المقابل الثقافي.",
            "انتبه لاختلاف تراكيب الجملة الفعلية في العربية والاسمية في الإنجليزية.",
            "احرص على بناء مسرد شخصي للمفردات المتكررة."
        ],
        "materials": [
            {"title": "كتاب التفكير في الترجمة العربية (Thinking Arabic Translation)", "url": "https://example.com/book2"},
            {"title": "نصوص تدريبية ومسارد مصطلحات", "url": "https://example.com/docs2"}
        ]
    },
    {
        "id": "TRANS311",
        "name": "نظريات الترجمة (Translation Theories)",
        "code": "311 ترج",
        "level": "المستوى الخامس",
        "description": "استعراض أهم نظريات الترجمة من التكافؤ الشكلي والديناميكي إلى نظرية الهدف (Skopos).",
        "tips": [
            "ركز على الفروقات بين التكافؤ الشكلي والديناميكي عند يوجين نيدا.",
            "اربط كل نظرية بمثال تطبيقي يوضح أثرها في النص المترجم.",
            "نظرية الهدف (Skopos Theory) تتكرر دوماً في الأسئلة المقالية."
        ],
        "materials": [
            {"title": "كتاب Introducing Translation Studies (Jeremy Munday)", "url": "https://example.com/book3"},
            {"title": "ملخص نظريات الترجمة وأهم الرواد", "url": "https://example.com/summary3"}
        ]
    }
]

# 4. الترويسة الرئيسية
st.markdown("""
    <div class="ksu-banner">
        <h1>🏛️ بوابة التميز الأكاديمي</h1>
        <p>كلية اللغات والترجمة — جامعة الملك سعود</p>
    </div>
""", unsafe_allow_html=True)

# 5. القائمة المنسدلة لاختيار المقرر
course_labels = [f"{c['code']} - {c['name']}" for c in COURSES]
selected_idx = st.selectbox("📚 اختر المقرر الدراسي لعرض مصادره:", range(len(course_labels)), format_func=lambda x: course_labels[x])

current = COURSES[selected_idx]

# 6. بطاقة المقرر المختارة
st.markdown(f"""
    <div class="course-card">
        <h2>{current['name']}</h2>
        <div class="level-badge">{current['level']}</div>
        <p>{current['description']}</p>
    </div>
""", unsafe_allow_html=True)

# 7. التبويبات التفاعلية
tab_tips, tab_files = st.tabs([
    "💡 نصائح التفوق (A+ Guide)",
    "📂 الحقيبة التعليمية والمراجع"
])

with tab_tips:
    st.write("")
    for idx, tip in enumerate(current["tips"], 1):
        st.success(f"**إضاءة {idx}:** {tip}")

with tab_files:
    st.write("")
    for item in current["materials"]:
        st.markdown(f"🔹 **[{item['title']}]({item['url']})**")
