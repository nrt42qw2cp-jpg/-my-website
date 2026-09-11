import streamlit as st
import os

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="بوابة التميز الأكاديمي | جامعة الملك سعود",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إنشاء مجلد لحفظ الملفات المرفوعة
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 2. الهوية البصرية لجامعة الملك سعود والتصميم المتجاوب
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

    html, body, [class*="css"], .stMarkdown {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    .block-container {
        padding-top: 1.8rem !important;
        padding-bottom: 3rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 900px !important;
    }
    .ksu-banner {
        background: linear-gradient(135deg, #005980 0%, #00364d 100%);
        border-radius: 16px;
        padding: 20px 16px;
        color: #ffffff;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 89, 128, 0.15);
        border-bottom: 4px solid #C59B27;
        text-align: center;
    }
    .ksu-banner h1 {
        font-size: 21px !important;
        font-weight: 800;
        margin: 0 0 6px 0 !important;
        color: #ffffff !important;
    }
    .ksu-banner p {
        font-size: 13px !important;
        margin: 0 !important;
        color: #e2f1f8 !important;
    }
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
    }
    .badge-gold {
        display: inline-block;
        background-color: #C59B27;
        color: #ffffff;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 10px;
        margin-left: 6px;
    }
    .badge-blue {
        display: inline-block;
        background-color: #005980;
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
    .stTabs [data-baseweb="tab"] {
        font-family: 'Tajawal', sans-serif !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        padding: 8px 12px !important;
        color: #005980 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الخطة الدراسية المعتمدة
COURSES_DATA = [
    # المستوى 1
    {"id": "انجل-100", "level": 1, "code": "انجل 100", "name": "اللغة الإنجليزية", "hours": 6, "description": "مقرر اللغة الإنجليزية المكثف.", "tips": ["الممارسة اليومية وحل التدريبات أولاً بأول."]},
    {"id": "فجب-101", "level": 1, "code": "فجب 101", "name": "اللياقة والثقافة الصحية", "hours": 1, "description": "مقرر اللياقة والثقافة الصحية.", "tips": ["الالتزام بالأنشطة البدنية والصحية."]},
    {"id": "نهج-101", "level": 1, "code": "نهج 101", "name": "مهارات جامعية", "hours": 3, "description": "تطوير مهارات التفكير والبحث وإدارة الوقت.", "tips": ["تسليم الواجبات في موعدها المحدد."]},
    {"id": "احص-102", "level": 1, "code": "احص 102", "name": "مبادئ في الإحصاء والاحتمالات", "hours": 3, "description": "مبادئ الإحصاء والاحتمالات.", "tips": ["التدرب المستمر على الآلة الحاسبة المعتمدة."]},
    {"id": "تقن-102", "level": 1, "code": "تقن 102", "name": "مهارات الحاسب", "hours": 3, "description": "التطبيقات الحاسوبية المكتبية وإدارة البيانات.", "tips": ["التركيز في الاختبارات العملية داخل المعمل."]},

    # المستوى 2
    {"id": "عرب-100", "level": 2, "code": "عرب 100", "name": "مهارات الكتابة", "hours": 2, "description": "قواعد الإملاء وصياغة الجمل في العربية.", "tips": ["التفريق بين همزتي الوصل والقطع وعلامات الترقيم."]},
    {"id": "ترج-111", "level": 2, "code": "ترج 111", "name": "الكتابة (1)", "hours": 3, "description": "بناء الجملة الإنجليزية والفقرات (Paragraph Writing).", "tips": ["كتابة Topic Sentence واضحة لكل فقرة."]},
    {"id": "ترج-112", "level": 2, "code": "ترج 112", "name": "القراءة (1)", "hours": 3, "description": "استراتيجيات القراءة وتنمية المفردات.", "tips": ["التمرن على القراءة السريعة والتقاط الأفكار العامة."]},
    {"id": "ترج-113", "level": 2, "code": "ترج 113", "name": "القواعد (1)", "hours": 3, "description": "أزمنة اللغة الإنجليزية وتراكيب الجمل.", "tips": ["حفظ تصاريف الأفعال الشاذة والتدرب عليها."]},
    {"id": "ترج-114", "level": 2, "code": "ترج 114", "name": "الاستماع والحديث (1)", "hours": 3, "description": "فهم المحادثات والتعبير الشفهي بالإنجليزية.", "tips": ["الاستماع اليومي للمقاطع الصوتية التعليمية."]},
    {"id": "ترج-115", "level": 2, "code": "ترج 115", "name": "بناء المفردات (1)", "hours": 3, "description": "الجذور واللواحق (Prefixes & Suffixes).", "tips": ["حفظ الكلمات داخل سياقاتها وجملها."]},
    {"id": "عرب-118", "level": 2, "code": "عرب 118", "name": "مهارات القراءة", "hours": 2, "description": "القراءة التحليلية للنصوص العربية.", "tips": ["استخراج الأفكار الرئيسة والتسلسل المنطقي."]},

    # المستوى 3
    {"id": "ترج-211", "level": 3, "code": "ترج 211", "name": "الكتابة (2)", "hours": 3, "description": "كتابة المقال متعدد الفقرات (Essay Writing).", "tips": ["صياغة أطروحة المقال (Thesis Statement) بدقة."]},
    {"id": "ترج-212", "level": 3, "code": "ترج 212", "name": "القراءة (2)", "hours": 3, "description": "استيعاب النصوص الطويلة والمعاني الضمنية.", "tips": ["التدرب على أسئلة الاستنتاج (Inference)."]},
    {"id": "ترج-213", "level": 3, "code": "ترج 213", "name": "القواعد (2)", "hours": 3, "description": "الجمل المعقدة والمبني للمجهول والشرط.", "tips": ["حل تمارين الـ Conditionals والعبارات الموصولة."]},
    {"id": "ترج-214", "level": 3, "code": "ترج 214", "name": "الاستماع والحديث (2)", "hours": 3, "description": "متابعة المحاضرات والعروض التقديمية.", "tips": ["التدرب على تدوين الملاحظات السريعة (Note-taking)."]},
    {"id": "ترج-215", "level": 3, "code": "ترج 215", "name": "المفردات (2)", "hours": 3, "description": "المفردات الأكاديمية والتلازمات اللفظية (Collocations).", "tips": ["حفظ الكلمات المتصاحبة لأهميتها في الترجمة."]},
    {"id": "عرب-234", "level": 3, "code": "عرب 234", "name": "النحو (1)", "hours": 3, "description": "الجملة الاسمية والفعلية والمرفوعات والمنصوبات.", "tips": ["حل التطبيقات الإعرابية بيدك أسبوعياً."]},
    {"id": "عرب-255", "level": 3, "code": "عرب 255", "name": "الكتابة المتخصصة", "hours": 2, "description": "تحرير التقارير والمراسلات الرسمية والتلخيص.", "tips": ["الوضوح والإيجاز وتجنب الحشو اللفظي."]},

    # المستوى 4
    {"id": "ترج-221", "level": 4, "code": "ترج 221", "name": "الكتابة الأكاديمية", "hours": 2, "description": "كتابة الأوراق البحثية والتوثيق الأكاديمي.", "tips": ["التدرب على إعادة الصياغة (Paraphrasing) وتجنب الانتحال."]},
    {"id": "ترج-222", "level": 4, "code": "ترج 222", "name": "مدخل إلى علم اللسانيات", "hours": 3, "description": "المدارس اللسانية وفروع اللغويات الأساسية.", "tips": ["حفظ جدول الرموز الصوتية (IPA) ومخارج الحروف."]},
    {"id": "ترج-223", "level": 4, "code": "ترج 223", "name": "استخدام المعاجم في الترجمة", "hours": 2, "description": "استخدام القواميس واستخراج المعنى السياقي.", "tips": ["قراءة أمثلة الاستخدام داخل المعاجم لا مجرد الكلمة الأولى."]},
    {"id": "ترج-224", "level": 4, "code": "ترج 224", "name": "مدخل إلى دراسات الترجمة", "hours": 2, "description": "تاريخ الترجمة ونظريات التكافؤ اللغوي.", "tips": ["ربط المفاهيم النظرية بأمثلة ونصوص واقعية."]},
    {"id": "ترج-225", "level": 4, "code": "ترج 225", "name": "ترجمة عامة (من الإنجليزية إلى العربية)", "hours": 3, "description": "نقل المقالات والنصوص وصياغة الجملة العربية السليمة.", "tips": ["تقديم الفعل في الجملة العربية وتجنب الحرفية."]},
    {"id": "عرب-350", "level": 4, "code": "عرب 350", "name": "تطبيقات أسلوبية", "hours": 3, "description": "دراسة الأسلوبية التعبيرية ومباحث التماسك النصي (د. منذر الكفافي / د. محمد الزليطني)[span_0](start_span)[span_0](end_span).", "tips": ["التركيز على أدوات الاتساق الخمسة: الإحالة، الاستبدال، الحذف، الوصل، والتكرار والتضام[span_1](start_span)[span_1](end_span).", "التفريق بين القيم التعبيرية الطبيعية والطارئة عند شارل بالي[span_2](start_span)[span_2](end_span).", "المقارنة بين النص العلمي (المخاطب للعقل بألفاظ قطعية) والنص الأدبي (المبني على العاطفة والمجاز)[span_3](start_span)[span_3](end_span)."]},

    # المستوى 5
    {"id": "ترج-312", "level": 5, "code": "ترج 312", "name": "مدخل إلى علم التراكيب والصرف", "hours": 3, "description": "تحليل بنية الكلمة وشجرة الجملة النحوية (Syntax).", "tips": ["رسم شجرة التراكيب بيدك أسبوعياً."]},
    {"id": "ترج-322", "level": 5, "code": "ترج 322", "name": "مدخل إلى علم الدلالة والتداولية", "hours": 3, "description": "المعنى السياقي وأفعال الكلام وقواعد غرايس.", "tips": ["حفظ شروط أفعال الكلام (Speech Acts) ومبادئ غرايس."]},
    {"id": "ترج-323", "level": 5, "code": "ترج 323", "name": "لسانيات النص", "hours": 2, "description": "معايير النصية والترابط المنطقي (Cohesion & Coherence).", "tips": ["المقارنة بين أدوات الربط اللفظية والترابط الدلالي."]},
    {"id": "ترج-324", "level": 5, "code": "ترج 324", "name": "قراءات متقدمة في اللغة والثقافة", "hours": 2, "description": "التفاعل بين اللغة والثقافة وأثر التضمين الثقافي.", "tips": ["فهم التحديات الثقافية المصاحبة لكل مصطلح."]},
    {"id": "ترج-326", "level": 5, "code": "ترج 326", "name": "الترجمة المالية والاقتصادية", "hours": 3, "description": "ترجمة القوائم المالية ونشرات الاكتتاب والأسواق.", "tips": ["الالتزام بالمسارد المعتمدة؛ فالمصطلح المالي دقيق جداً."]},
    {"id": "ترج-327", "level": 5, "code": "ترج 327", "name": "الترجمة العلمية والتقنية", "hours": 3, "description": "نقل الأبحاث والكتالوجات الهندسية بدقة وموضوعية.", "tips": ["الحيادية وتوحيد ترجمة المصطلح المتكرر."]},
    {"id": "ترج-328", "level": 5, "code": "ترج 328", "name": "الترجمة التتبعية والثنائية (2)", "hours": 2, "description": "تدريبات تدوين الملاحظات والمقابلات.", "tips": ["تطوير اختصارات شخصية لتدوين الملاحظات."]},

    # المستوى 6
    {"id": "ترج-314", "level": 6, "code": "ترج 314", "name": "قراءات في اللغة والثقافة", "hours": 2, "description": "توسيع المدارك الثقافية والحضارية للنصوص.", "tips": ["مناقشة الأبعاد الفكرية خلف النصوص المترجمة."]},
    {"id": "ترج-315", "level": 6, "code": "ترج 315", "name": "ترجمة عامة (من العربية إلى الإنجليزية)", "hours": 3, "description": "إعادة صياغة النصوص بإنجليزية سليمة وطبيعية.", "tips": ["تجنب التراكيب الركيكة الناتجة عن النقل الحرفي."]},
    {"id": "ترج-316", "level": 6, "code": "ترج 316", "name": "الترجمة السياسية والإعلامية", "hours": 3, "description": "ترجمة الأخبار والبيانات الصحفية والدبلوماسية.", "tips": ["متابعة المصطلحات السياسية المتداولة في الإعلام."]},
    {"id": "ترج-317", "level": 6, "code": "ترج 317", "name": "الترجمة بمساعدة الحاسب", "hours": 2, "description": "أدوات الـ CAT Tools وذاكرات الترجمة والمسارد.", "tips": ["التطبيق العملي على أدوات مثل Trados أو Matecat."]},
    {"id": "ترج-318", "level": 6, "code": "ترج 318", "name": "الترجمة التتبعية والثنائية (1)", "hours": 2, "description": "أساسيات الترجمة التتبعية في المعمل وسرعة الاسترجاع.", "tips": ["الحفاظ على ثبات الأداء عند مواجهة كلمة صعبة."]},

    # المستوى 7
    {"id": "ترج-411", "level": 7, "code": "ترج 411", "name": "مهارات البحث العلمي", "hours": 2, "description": "منهجيات البحث اللغوي وتصميم الدراسات.", "tips": ["تحديد إشكالية بحثية واضحة ومحددة."]},
    {"id": "ترج-412", "level": 7, "code": "ترج 412", "name": "تحليل الخطاب", "hours": 3, "description": "تحليل المعاني المضمرة والأيديولوجيا في النصوص.", "tips": ["التركيز على دلالات اختيار المفردات في سياقها."]},
    {"id": "ترج-413", "level": 7, "code": "ترج 413", "name": "التحرير والتنقيح", "hours": 2, "description": "مراجعة النصوص المترجمة وضبط جودتها.", "tips": ["التدرب على اكتشاف الأخطاء اللغوية الدقيقة."]},
    {"id": "ترج-416", "level": 7, "code": "ترج 416", "name": "الترجمة الطبية", "hours": 3, "description": "ترجمة التقارير والتحاليل والمصطلحات الطبية.", "tips": ["حفظ السوابق واللواحق اللاتينية واليونانية للكلمات."]},
    {"id": "ترج-417", "level": 7, "code": "ترج 417", "name": "الترجمة الإسلامية", "hours": 3, "description": "نقل المصطلحات الفقهية والعقدية بحساسية دلالية.", "tips": ["الاستعانة بتراجم القرآن المعتمدة والمعاجم الشرعية."]},
    {"id": "ترج-418", "level": 7, "code": "ترج 418", "name": "الترجمة الفورية (1)", "hours": 2, "description": "التدريب في الكبائن ومواكبة المتحدث وإدارة التأخير.", "tips": ["الممارسة اليومية لتقنية الـ Shadowing."]},

    # المستوى 8
    {"id": "ترج-425", "level": 8, "code": "ترج 425", "name": "قضايا الترجمة وإشكالاتها", "hours": 2, "description": "إشكالات الترجمة الآلية، الذكاء الاصطناعي، والأخلاقيات.", "tips": ["متابعة أحدث الأبحاث حول الذكاء الاصطناعي والترجمة."]},
    {"id": "ترج-426", "level": 8, "code": "ترج 426", "name": "الترجمة الأدبية", "hours": 3, "description": "ترجمة الرواية والشعر ومراعاة الجماليات والوقع الفني.", "tips": ["نقل الأثر الأدبي والجمالي أهم من الترجمة الحرفية."]},
    {"id": "ترج-427", "level": 8, "code": "ترج 427", "name": "الترجمة القانونية", "hours": 3, "description": "ترجمة العقود والاتفاقيات والوثائق القضائية.", "tips": ["الالتزام بالصيغ القانونية الثابتة والمصطلحات الملزمة."]},
    {"id": "ترج-428", "level": 8, "code": "ترج 428", "name": "الترجمة الفورية (2)", "hours": 2, "description": "محاكاة المؤتمرات والسرعات العالية في الكابينة.", "tips": ["استخدام التجزئة الذكية للجمل الطويلة (Chunking)."]},
    {"id": "ترج-429", "level": 8, "code": "ترج 429", "name": "مشروع الترجمة", "hours": 4, "description": "ترجمة كتاب أو دراسة مع ملحق تحليلي نقدي منهجي.", "tips": ["توثيق تحديات الترجمة والحلول المعتمدة في التقرير."]}
]

# 4. الترويسة الرئيسية
st.markdown("""
    <div class="ksu-banner">
        <h1>🏛️ بوابة التميز الأكاديمي</h1>
        <p>كلية اللغات وعلومها — برنامج بكالوريوس اللغة الإنجليزية والترجمة</p>
    </div>
""", unsafe_allow_html=True)

# 5. التصفية بالمستويات
levels = ["الكل"] + [f"المستوى {i}" for i in range(1, 9)]
selected_lvl_str = st.selectbox("🎯 حدد المستوى الدراسي:", levels)

if selected_lvl_str == "الكل":
    display_courses = COURSES_DATA
else:
    lvl_num = int(selected_lvl_str.replace("المستوى ", ""))
    display_courses = [c for c in COURSES_DATA if c["level"] == lvl_num]

course_titles = [f"{c['code']} - {c['name']}" for c in display_courses]
selected_idx = st.selectbox("📚 اختر المقرر الدراسي:", range(len(course_titles)), format_func=lambda x: course_titles[x])
current_course = display_courses[selected_idx]

# 6. بطاقة بيانات المقرر
st.markdown(f"""
    <div class="course-card">
        <h2>{current_course['name']}</h2>
        <div class="badge-gold">المستوى {current_course['level']}</div>
        <div class="badge-blue">{current_course['hours']} ساعات معتمدة</div>
        <p>{current_course['description']}</p>
    </div>
""", unsafe_allow_html=True)

# مسار مجلد المقرر لحفظ ملفاته
course_folder = os.path.join(UPLOAD_DIR, current_course["id"])
os.makedirs(course_folder, exist_ok=True)

# 7. التبويبات التفاعلية
tab_tips, tab_materials, tab_upload = st.tabs([
    "💡 نصائح التفوق (A+ Guide)",
    "📂 الحقيبة التعليمية والملفات",
    "🔒 إدارة المحتوى (للمشرف)"
])

with tab_tips:
    st.write("")
    for idx, tip in enumerate(current_course["tips"], 1):
        st.success(f"**إضاءة {idx}:** {tip}")

with tab_materials:
    st.write("")
    existing_files = os.listdir(course_folder)
    
    if existing_files:
        st.write(f"📁 **الملفات المتاحة لهذا المقرر ({len(existing_files)}):**")
        for fname in existing_files:
            file_path = os.path.join(course_folder, fname)
            with open(file_path, "rb") as f:
                st.download_button(
                    label=f"📥 تنزيل: {fname}",
                    data=f.read(),
                    file_name=fname,
                    mime="application/pdf",
                    key=f"dl_{current_course['id']}_{fname}"
                )
    else:
        st.info("لم يتم رفع أي ملفات لهذا المقرر حتى الآن.")

with tab_upload:
    st.write("")
    st.markdown("### 🔒 بوابة المشرف لرفع الملفات")
    st.caption(f"إضافة محتوى رسمي لمقرر: **{current_course['name']}**")
    
    # الرمز السري الخاص بك (يمكنك تعديل ksu2026 إلى أي كلمة سر تريدها)
    SECRET_CODE = "ksu2026"
    
    admin_password = st.text_input("أدخل الرمز السري للإدارة:", type="password", key=f"pwd_{current_course['id']}")
    
    if admin_password:
        if admin_password == SECRET_CODE:
            st.success("🔓 تم التحقق بنجاح! الصلاحية مفعلة لرفع الملفات.")
            uploaded_file = st.file_uploader(
                "اختر ملف PDF من جهازك لرفعه:", 
                type=["pdf"], 
                key=f"uploader_{current_course['id']}"
            )
            
            if uploaded_file is not None:
                save_path = os.path.join(course_folder, uploaded_file.name)
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"✅ تم رفع الملف بنجاح: **{uploaded_file.name}**")
                st.info("أصبح الملف متاحاً لجميع الطلاب في تبويب 'الحقيبة التعليمية'.")
        else:
            st.error("❌ الرمز السري غير صحيح. الصلاحية مقتصرة على المشرف فقط.")
    else:
        st.info("⚠️ هذا القسم محمي ومخصص فقط لإدارة المنصة.")
