import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="بوابة التميز الأكاديمي | جامعة الملك سعود",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تطبيق هوية جامعة الملك سعود (KSU Theme)
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        text-align: right;
    }
    .ksu-header {
        background: linear-gradient(135deg, #005980 0%, #003a54 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 89, 128, 0.2);
        border-bottom: 4px solid #C59B27;
    }
    .ksu-header h1 {
        color: #ffffff;
        font-size: 26px;
        margin: 0;
        font-weight: 700;
    }
    .ksu-header p {
        color: #e0f2fe;
        font-size: 14px;
        margin-top: 6px;
        margin-bottom: 0;
    }
    .course-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #E2E8F0;
        border-right: 5px solid #005980;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #005980;
    }
    </style>
""", unsafe_allow_html=True)

# 3. بيانات المقررات المدمجة (تستطيع إضافة أي مقرر هنا مباشرة)
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
            {"title": "سلايدات وتفريغات المقرر", "url": "https://example.com/slides1"}
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
            {"title": "نصوص تدريبية ومسارد مصطلحات معتمدة", "url": "https://example.com/docs2"}
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
            "اربط كل نظرية بمثال تطبيقي واقعي يوضح أثرها في النص المترجم.",
            "نظرية الهدف (Skopos Theory) تتكرر دوماً في الأسئلة المقالية."
        ],
        "materials": [
            {"title": "كتاب Introducing Translation Studies (Jeremy Munday)", "url": "https://example.com/book3"},
            {"title": "ملخص نظريات الترجمة وأهم الرواد", "url": "https://example.com/summary3"}
        ]
    }
]

# 4. الترويسة
st.markdown("""
    <div class="ksu-header">
        <h1>🏛️ بوابة التميز الأكاديمي | كلية اللغات والترجمة</h1>
        <p>جامعة الملك سعود — المنصة الطلابية الموحدة للمصادر ونظام التوجيه الدراسي</p>
    </div>
""", unsafe_allow_html=True)

# 5. القائمة الجانبية
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/ar/thumb/8/87/King_Saud_University_Logo.svg/1200px-King_Saud_University_Logo.svg.png", width=170)
    st.markdown("### 📚 المقررات الدراسية")
    course_labels = [f"{c['code']} - {c['name']}" for c in COURSES]
    selected_idx = st.selectbox("حدد المقرر المطلوب:", range(len(course_labels)), format_func=lambda x: course_labels[x])
    
    st.divider()
    st.caption("مشروع مبادرة الابتكار الطلابي © 2026")

current = COURSES[selected_idx]

# بطاقة التوصيف
st.markdown(f"""
    <div class="course-card">
        <h2 style="color: #005980; margin: 0;">{current['name']}</h2>
        <span style="background-color: #C59B27; color: white; padding: 3px 12px; border-radius: 4px; font-size: 13px; font-weight: bold;">{current['level']}</span>
        <p style="margin-top: 12px; color: #475569; line-height: 1.6;">{current['description']}</p>
    </div>
""", unsafe_allow_html=True)

# 6. التبويبات (المصادر + نصائح A+)
tab_tips, tab_files = st.tabs([
    "💡 نصائح وإرشادات التفوق (A+ Guide)",
    "📂 الحقيبة التعليمية والمراجع المعتمدة"
])

with tab_tips:
    st.subheader("🎯 مفاتيح اجتياز المقرر بامتياز مرتفع")
    for idx, tip in enumerate(current["tips"], 1):
        st.info(f"**إضاءة {idx}:** {tip}")

with tab_files:
    st.subheader("📚 الكتب والسلايدات الرسمية")
    for item in current["materials"]:
        st.markdown(f"🔹 **[{item['title']}]({item['url']})**")
