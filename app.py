import streamlit as st
import os

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="بوابة النظام الأكاديمي | جامعة الملك سعود",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إنشاء مجلد لحفظ الملفات المرفوعة
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 2. تطبيق استايل وهوية بوابة النظام الأكاديمي (Edugate Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

    html, body, [class*="css"], .stMarkdown {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
        background-color: #f4f6f9 !important;
    }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        max-width: 600px !important;
    }

    /* الهيدر العلوي الأبيض الرسمي للبوابة */
    .edugate-navbar {
        background: #ffffff;
        padding: 10px 14px;
        border-bottom: 2px solid #e2e8f0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .edugate-title-box {
        text-align: right;
    }
    .edugate-sub {
        font-size: 11px;
        color: #0284c7;
        font-weight: 700;
        margin: 0;
    }
    .edugate-main {
        font-size: 13px;
        color: #0284c7;
        font-weight: 800;
        margin: 0;
    }
    .edugate-logo-box img {
        height: 38px;
    }

    /* بطاقة الملف الشخصي الرسمية */
    .student-profile-card {
        background: #ffffff;
        border: 1px solid #dbe2ea;
        border-radius: 8px;
        padding: 16px 14px;
        margin-bottom: 14px;
        position: relative;
    }
    .profile-header-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        border-bottom: 1px dashed #e2e8f0;
        padding-bottom: 12px;
        margin-bottom: 12px;
    }
    .user-avatar-icon {
        width: 44px;
        height: 44px;
        border-radius: 50%;
        border: 2px solid #1e3a8a;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: #1e3a8a;
    }
    .profile-field-title {
        font-size: 13px;
        font-weight: 700;
        color: #1e293b;
        margin: 0 0 2px 0;
    }
    .profile-field-val {
        font-size: 13px;
        color: #0369a1;
        font-weight: 600;
        margin: 0;
    }
    .info-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 10px;
    }
    .info-item {
        display: flex;
        flex-direction: column;
    }
    .info-item-label {
        font-size: 12px;
        font-weight: 700;
        color: #334155;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .info-item-value {
        font-size: 13px;
        color: #0284c7;
        font-weight: 600;
        margin-top: 1px;
    }

    /* بطاقة عنوان الصفحة/القسم */
    .section-title-card {
        background: #ffffff;
        border: 1px solid #dbe2ea;
        border-radius: 8px;
        padding: 12px 14px;
        margin-bottom: 14px;
        text-align: center;
    }
    .term-label {
        font-size: 12px;
        font-weight: 700;
        color: #1e293b;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        margin-bottom: 6px;
    }
    .active-page-tab {
        font-size: 15px;
        font-weight: 800;
        color: #0f172a;
        display: inline-block;
        border-bottom: 3px solid #0284c7;
        padding-bottom: 4px;
    }

    /* بطاقة المقرر الدراسي المختار */
    .course-details-box {
        background: #ffffff;
        border: 1px solid #dbe2ea;
        border-radius: 8px;
        padding: 14px;
        margin-bottom: 14px;
    }

    /* أزرار التبويبات بأسلوب البوابة */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff;
        border-radius: 6px;
        border: 1px solid #dbe2ea;
        padding: 4px;
        gap: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 12px !important;
        font-weight: 700 !important;
        color: #334155 !important;
        border-radius: 4px !important;
        padding: 6px 10px !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0284c7 !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر الرسمي العلوي المطابق للبوابة مع شعار الجامعة
st.markdown("""
    <div class="edugate-navbar">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 20px; color: #1e293b;">☰</span>
            <span style="font-size: 12px; font-weight: bold; color: #1e293b;">خروج</span>
        </div>
        <div class="edugate-title-box">
            <p class="edugate-sub">عمادة شؤون القبول و التسجيل</p>
            <p class="edugate-main">بوابة النظام الأكاديمي</p>
        </div>
        <div class="edugate-logo-box">
            <img src="https://upload.wikimedia.org/wikipedia/ar/thumb/8/87/King_Saud_University_Logo.svg/1200px-King_Saud_University_Logo.svg.png" alt="KSU">
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. بطاقة معلومات الطالب بتنسيق البوابة
st.markdown("""
    <div class="student-profile-card">
        <div class="profile-header-row">
            <div>
                <p class="profile-field-title">اسم الطالب</p>
                <p class="profile-field-val">عبدالعزيز بن عبدالله بن جبران العبدلي</p>
                <p style="font-size: 12px; color: #64748b; margin-top: 4px;">فصل التسجيل</p>
            </div>
            <div class="user-avatar-icon">👤</div>
        </div>
        <div class="info-grid">
            <div class="info-item">
                <div class="info-item-label">🎚️ رقم الطالب</div>
                <div class="info-item-value">445104860</div>
            </div>
            <div class="info-item">
                <div class="info-item-label">🏛️ الكلية</div>
                <div class="info-item-value">اللغات وعلومها</div>
            </div>
            <div class="info-item">
                <div class="info-item-label">🏛️ التخصص</div>
                <div class="info-item-value">اللغة الإنجليزية والترجمة</div>
            </div>
            <div class="info-item">
                <div class="info-item-label">📍 المقر</div>
                <div class="info-item-value">الرياض- طلاب</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. ترويسة الفصل والقسم
st.markdown("""
    <div class="section-title-card">
        <div class="term-label">📅 الفصل الدراسي الحالي 1447/1448هـ</div>
        <div class="active-page-tab">الخطة والمصادر الأكاديمية</div>
    </div>
""", unsafe_allow_html=True)

# 6. الخطة الدراسية الكاملة لبرنامج اللغة الإنجليزية والترجمة[span_0](start_span)[span_0](end_span)
COURSES_DATA = [
    # المستوى 1[span_1](start_span)[span_1](end_span)
    {"id": "انجل-100", "level": 1, "code": "انجل 100", "name": "اللغة الإنجليزية", "hours": 6, "description": "مقرر اللغة الإنجليزية المكثف ضمن البرنامج[span_2](start_span)[span_2](end_span).", "tips": ["الممارسة اليومية وحل التدريبات أولاً بأول."]},
    {"id": "فجب-101", "level": 1, "code": "فجب 101", "name": "اللياقة والثقافة الصحية", "hours": 1, "description": "مقرر اللياقة والثقافة الصحية[span_3](start_span)[span_3](end_span).", "tips": ["الالتزام بالأنشطة البدنية والصحية."]},
    {"id": "نهج-101", "level": 1, "code": "نهج 101", "name": "مهارات جامعية", "hours": 3, "description": "تطوير مهارات التفكير والبحث وإدارة الوقت[span_4](start_span)[span_4](end_span).", "tips": ["تسليم الواجبات في موعدها المحدد."]},
    {"id": "احص-102", "level": 1, "code": "احص 102", "name": "مبادئ في الإحصاء والاحتمالات", "hours": 3, "description": "مبادئ الإحصاء والاحتمالات[span_5](start_span)[span_5](end_span).", "tips": ["التدرب المستمر على الآلة الحاسبة المعتمدة."]},
    {"id": "تقن-102", "level": 1, "code": "تقن 102", "name": "مهارات الحاسب", "hours": 3, "description": "التطبيقات الحاسوبية المكتبية وإدارة البيانات[span_6](start_span)[span_6](end_span).", "tips": ["التركيز في الاختبارات العملية داخل المعمل."]},

    # المستوى 2[span_7](start_span)[span_7](end_span)
    {"id": "عرب-100", "level": 2, "code": "عرب 100", "name": "مهارات الكتابة", "hours": 2, "description": "قواعد الإملاء وصياغة الجمل في العربية[span_8](start_span)[span_8](end_span).", "tips": ["التفريق بين همزتي الوصل والقطع وعلامات الترقيم."]},
    {"id": "ترج-111", "level": 2, "code": "ترج 111", "name": "الكتابة (1)", "hours": 3, "description": "بناء الجملة الإنجليزية والفقرات (Paragraph Writing)[span_9](start_span)[span_9](end_span).", "tips": ["كتابة Topic Sentence واضحة لكل فقرة."]},
    {"id": "ترج-112", "level": 2, "code": "ترج 112", "name": "القراءة (1)", "hours": 3, "description": "استراتيجيات القراءة وتنمية المفردات[span_10](start_span)[span_10](end_span).", "tips": ["التمرن على القراءة السريعة والتقاط الأفكار العامة."]},
    {"id": "ترج-113", "level": 2, "code": "ترج 113", "name": "القواعد (1)", "hours": 3, "description": "أزمنة اللغة الإنجليزية وتراكيب الجمل[span_11](start_span)[span_11](end_span).", "tips": ["حفظ تصاريف الأفعال الشاذة والتدرب عليها."]},
    {"id": "ترج-114", "level": 2, "code": "ترج 114", "name": "الاستماع والحديث (1)", "hours": 3, "description": "فهم المحادثات والتعبير الشفهي بالإنجليزية[span_12](start_span)[span_12](end_span).", "tips": ["الاستماع اليومي للمقاطع الصوتية التعليمية."]},
    {"id": "ترج-115", "level": 2, "code": "ترج 115", "name": "بناء المفردات (1)", "hours": 3, "description": "الجذور واللواحق (Prefixes & Suffixes)[span_13](start_span)[span_13](end_span).", "tips": ["حفظ الكلمات داخل سياقاتها وجملها."]},
    {"id": "عرب-118", "level": 2, "code": "عرب 118", "name": "مهارات القراءة", "hours": 2, "description": "القراءة التحليلية للنصوص العربية[span_14](start_span)[span_14](end_span).", "tips": ["استخراج الأفكار الرئيسة والتسلسل المنطقي."]},

    # المستوى 3[span_15](start_span)[span_15](end_span)
    {"id": "ترج-211", "level": 3, "code": "ترج 211", "name": "الكتابة (2)", "hours": 3, "description": "كتابة المقال متعدد الفقرات (Essay Writing)[span_16](start_span)[span_16](end_span).", "tips": ["صياغة أطروحة المقال (Thesis Statement) بدقة."]},
    {"id": "ترج-212", "level": 3, "code": "ترج 212", "name": "القراءة (2)", "hours": 3, "description": "استيعاب النصوص الطويلة والمعاني الضمنية[span_17](start_span)[span_17](end_span).", "tips": ["التدرب على أسئلة الاستنتاج (Inference)."]},
    {"id": "ترج-213", "level": 3, "code": "ترج 213", "name": "القواعد (2)", "hours": 3, "description": "الجمل المعقدة والمبني للمجهول والشرط[span_18](start_span)[span_18](end_span).", "tips": ["حل تمارين الـ Conditionals والعبارات الموصولة."]},
    {"id": "ترج-214", "level": 3, "code": "ترج 214", "name": "الاستماع والحديث (2)", "hours": 3, "description": "متابعة المحاضرات والعروض التقديمية[span_19](start_span)[span_19](end_span).", "tips": ["التدرب على تدوين الملاحظات السريعة (Note-taking)."]},
    {"id": "ترج-215", "level": 3, "code": "ترج 215", "name": "المفردات (2)", "hours": 3, "description": "المفردات الأكاديمية والتلازمات اللفظية (Collocations)[span_20](start_span)[span_20](end_span).", "tips": ["حفظ الكلمات المتصاحبة لأهميتها في الترجمة."]},
    {"id": "عرب-234", "level": 3, "code": "عرب 234", "name": "النحو (1)", "hours": 3, "description": "الجملة الاسمية والفعلية والمرفوعات والمنصوبات[span_21](start_span)[span_21](end_span).", "tips": ["حل التطبيقات الإعرابية بيدك أسبوعياً."]},
    {"id": "عرب-255", "level": 3, "code": "عرب 255", "name": "الكتابة المتخصصة", "hours": 2, "description": "تحرير التقارير والمراسلات الرسمية والتلخيص[span_22](start_span)[span_22](end_span).", "tips": ["الوضوح والإيجاز وتجنب الحشو اللفظي."]},

    # المستوى 4[span_23](start_span)[span_23](end_span)
    {"id": "ترج-221", "level": 4, "code": "ترج 221", "name": "الكتابة الأكاديمية", "hours": 2, "description": "كتابة الأوراق البحثية والتوثيق الأكاديمي[span_24](start_span)[span_24](end_span).", "tips": ["التدرب على إعادة الصياغة (Paraphrasing) وتجنب الانتحال."]},
    {"id": "ترج-222", "level": 4, "code": "ترج 222", "name": "مدخل إلى علم اللسانيات", "hours": 3, "description": "المدارس اللسانية وفروع اللغويات الأساسية[span_25](start_span)[span_25](end_span).", "tips": ["حفظ جدول الرموز الصوتية (IPA) ومخارج الحروف."]},
    {"id": "ترج-223", "level": 4, "code": "ترج 223", "name": "استخدام المعاجم في الترجمة", "hours": 2, "description": "استخدام القواميس واستخراج المعنى السياقي[span_26](start_span)[span_26](end_span).", "tips": ["قراءة أمثلة الاستخدام داخل المعاجم لا مجرد الكلمة الأولى."]},
    {"id": "ترج-224", "level": 4, "code": "ترج 224", "name": "مدخل إلى دراسات الترجمة", "hours": 2, "description": "تاريخ الترجمة ونظريات التكافؤ اللغوي[span_27](start_span)[span_27](end_span).", "tips": ["ربط المفاهيم النظرية بأمثلة ونصوص واقعية."]},
    {"id": "ترج-225", "level": 4, "code": "ترج 225", "name": "ترجمة عامة (من الإنجليزية إلى العربية)", "hours": 3, "description": "نقل المقالات والنصوص وصياغة الجملة العربية السليمة[span_28](start_span)[span_28](end_span).", "tips": ["تقديم الفعل في الجملة العربية وتجنب الحرفية."]},
    {"id": "عرب-350", "level": 4, "code": "عرب 350", "name": "تطبيقات أسلوبية", "hours": 3, "description": "دراسة الأسلوبية التعبيرية ومباحث التماسك النصي (د. منذر الكفافي / د. محمد الزليطني)[span_29](start_span)[span_29](end_span)[span_30](start_span)[span_30](end_span).", "tips": ["التركيز على أدوات الاتساق الخمسة: الإحالة، الاستبدال، الحذف، الوصل، والتكرار والتضام[span_31](start_span)[span_31](end_span).", "التفريق بين القيم التعبيرية الطبيعية والطارئة عند شارل بالي[span_32](start_span)[span_32](end_span).", "المقارنة بين النص العلمي والنص الأدبي[span_33](start_span)[span_33](end_span)."]},

    # المستوى 5[span_34](start_span)[span_34](end_span)
    {"id": "ترج-312", "level": 5, "code": "ترج 312", "name": "مدخل إلى علم التراكيب والصرف", "hours": 3, "description": "تحليل بنية الكلمة وشجرة الجملة النحوية (Syntax)[span_35](start_span)[span_35](end_span).", "tips": ["رسم شجرة التراكيب بيدك أسبوعياً."]},
    {"id": "ترج-322", "level": 5, "code": "ترج 322", "name": "مدخل إلى علم الدلالة والتداولية", "hours": 3, "description": "المعنى السياقي وأفعال الكلام وقواعد غرايس[span_36](start_span)[span_36](end_span).", "tips": ["حفظ شروط أفعال الكلام ومبادئ غرايس."]},
    {"id": "ترج-323", "level": 5, "code": "ترج 323", "name": "لسانيات النص", "hours": 2, "description": "معايير النصية والترابط المنطقي (Cohesion & Coherence)[span_37](start_span)[span_37](end_span).", "tips": ["المقارنة بين أدوات الربط اللفظية والترابط الدلالي."]},
    {"id": "ترج-324", "level": 5, "code": "ترج 324", "name": "قراءات متقدمة في اللغة والثقافة", "hours": 2, "description": "التفاعل بين اللغة والثقافة وأثر التضمين الثقافي[span_38](start_span)[span_38](end_span).", "tips": ["فهم التحديات الثقافية المصاحبة لكل مصطلح."]},
    {"id": "ترج-326", "level": 5, "code": "ترج 326", "name": "الترجمة المالية والاقتصادية", "hours": 3, "description": "ترجمة القوائم المالية ونشرات الاكتتاب والأسواق[span_39](start_span)[span_39](end_span).", "tips": ["الالتزام بالمسارد المعتمدة؛ فالمصطلح المالي دقيق جداً."]},
    {"id": "ترج-327", "level": 5, "code": "ترج 327", "name": "الترجمة العلمية والتقنية", "hours": 3, "description": "نقل الأبحاث والكتالوجات الهندسية بدقة وموضوعية[span_40](start_span)[span_40](end_span).", "tips": ["الحيادية وتوحيد ترجمة المصطلح المتكرر."]},
    {"id": "ترج-328", "level": 5, "code": "ترج 328", "name": "الترجمة التتبعية والثنائية (2)", "hours": 2, "description": "تدريبات تدوين الملاحظات والمقابلات[span_41](start_span)[span_41](end_span).", "tips": ["تطوير اختصارات شخصية لتدوين الملاحظات."]},

    # المستوى 6[span_42](start_span)[span_42](end_span)
    {"id": "ترج-314", "level": 6, "code": "ترج 314", "name": "قراءات في اللغة والثقافة", "hours": 2, "description": "توسيع المدارك الثقافية والحضارية للنصوص[span_43](start_span)[span_43](end_span).", "tips": ["مناقشة الأبعاد الفكرية خلف النصوص المترجمة."]},
    {"id": "ترج-315", "level": 6, "code": "ترج 315", "name": "ترجمة عامة (من العربية إلى الإنجليزية)", "hours": 3, "description": "إعادة صياغة النصوص بإنجليزية سليمة وطبيعية[span_44](start_span)[span_44](end_span).", "tips": ["تجنب التراكيب الركيكة الناتجة عن النقل الحرفي."]},
    {"id": "ترج-316", "level": 6, "code": "ترج 316", "name": "الترجمة السياسية والإعلامية", "hours": 3, "description": "ترجمة الأخبار والبيانات الصحفية والدبلوماسية[span_45](start_span)[span_45](end_span).", "tips": ["متابعة المصطلحات السياسية المتداولة في الإعلام."]},
    {"id": "ترج-317", "level": 6, "code": "ترج 317", "name": "الترجمة بمساعدة الحاسب", "hours": 2, "description": "أدوات الـ CAT Tools وذاكرات الترجمة والمسارد[span_46](start_span)[span_46](end_span).", "tips": ["التطبيق العملي على أدوات مثل Trados أو Matecat."]},
    {"id": "ترج-318", "level": 6, "code": "ترج 318", "name": "الترجمة التتبعية والثنائية (1)", "hours": 2, "description": "أساسيات الترجمة التتبعية في المعمل وسرعة الاسترجاع[span_47](start_span)[span_47](end_span).", "tips": ["الحفاظ على ثبات الأداء عند مواجهة كلمة صعبة."]},

    # المستوى 7[span_48](start_span)[span_48](end_span)
    {"id": "ترج-411", "level": 7, "code": "ترج 411", "name": "مهارات البحث العلمي", "hours": 2, "description": "منهجيات البحث اللغوي وتصميم الدراسات[span_49](start_span)[span_49](end_span).", "tips": ["تحديد إشكالية بحثية واضحة ومحددة."]},
    {"id": "ترج-412", "level": 7, "code": "ترج 412", "name": "تحليل الخطاب", "hours": 3, "description": "تحليل المعاني المضمرة والأيديولوجيا في النصوص[span_50](start_span)[span_50](end_span).", "tips": ["التركيز على دلالات اختيار المفردات في سياقها."]},
    {"id": "ترج-413", "level": 7, "code": "ترج 413", "name": "التحرير والتنقيح", "hours": 2, "description": "مراجعة النصوص المترجمة وضبط جودتها[span_51](start_span)[span_51](end_span).", "tips": ["التدرب على اكتشاف الأخطاء اللغوية الدقيقة."]},
    {"id": "ترج-416", "level": 7, "code": "ترج 416", "name": "الترجمة الطبية", "hours": 3, "description": "ترجمة التقارير والتحاليل والمصطلحات الطبية[span_52](start_span)[span_52](end_span).", "tips": ["حفظ السوابق واللواحق اللاتينية واليونانية للكلمات."]},
    {"id": "ترج-417", "level": 7, "code": "ترج 417", "name": "الترجمة الإسلامية", "hours": 3, "description": "نقل المصطلحات الفقهية والعقدية بحساسية دلالية[span_53](start_span)[span_53](end_span).", "tips": ["الاستعانة بتراجم القرآن المعتمدة والمعاجم الشرعية."]},
    {"id": "ترج-418", "level": 7, "code": "ترج 418", "name": "الترجمة الفورية (1)", "hours": 2, "description": "التدريب في الكبائن ومواكبة المتحدث وإدارة التأخير[span_54](start_span)[span_54](end_span).", "tips": ["الممارسة اليومية لتقنية الـ Shadowing."]},

    # المستوى 8[span_55](start_span)[span_55](end_span)
    {"id": "ترج-425", "level": 8, "code": "ترج 425", "name": "قضايا الترجمة وإشكالاتها", "hours": 2, "description": "إشكالات الترجمة الآلية، الذكاء الاصطناعي، والأخلاقيات[span_56](start_span)[span_56](end_span).", "tips": ["متابعة أحدث الأبحاث حول الذكاء الاصطناعي والترجمة."]},
    {"id": "ترج-426", "level": 8, "code": "ترج 426", "name": "الترجمة الأدبية", "hours": 3, "description": "ترجمة الرواية والشعر ومراعاة الجماليات والوقع الفني[span_57](start_span)[span_57](end_span).", "tips": ["نقل الأثر الأدبي والجمالي أهم من الترجمة الحرفية."]},
    {"id": "ترج-427", "level": 8, "code": "ترج 427", "name": "الترجمة القانونية", "hours": 3, "description": "ترجمة العقود والاتفاقيات والوثائق القضائية[span_58](start_span)[span_58](end_span).", "tips": ["الالتزام بالصيغ القانونية الثابتة والمصطلحات الملزمة."]},
    {"id": "ترج-428", "level": 8, "code": "ترج 428", "name": "الترجمة الفورية (2)", "hours": 2, "description": "محاكاة المؤتمرات والسرعات العالية في الكابينة[span_59](start_span)[span_59](end_span).", "tips": ["استخدام التجزئة الذكية للجمل الطويلة (Chunking)."]},
    {"id": "ترج-429", "level": 8, "code": "ترج 429", "name": "مشروع الترجمة", "hours": 4, "description": "ترجمة كتاب أو دراسة مع ملحق تحليلي نقدي منهجي[span_60](start_span)[span_60](end_span).", "tips": ["توثيق تحديات الترجمة والحلول المعتمدة في التقرير."]}
]

# 7. اختيار وتصفية المقررات
levels = ["الكل"] + [f"المستوى {i}" for i in range(1, 9)]
selected_lvl_str = st.selectbox("📌 المستوى الأكاديمي:", levels)

if selected_lvl_str == "الكل":
    display_courses = COURSES_DATA
else:
    lvl_num = int(selected_lvl_str.replace("المستوى ", ""))
    display_courses = [c for c in COURSES_DATA if c["level"] == lvl_num]

course_titles = [f"{c['code']} - {c['name']}" for c in display_courses]
selected_idx = st.selectbox("📚 المقرر الدراسي المسجل:", range(len(course_titles)), format_func=lambda x: course_titles[x])
current_course = display_courses[selected_idx]

# بطاقة المقرر المختار
st.markdown(f"""
    <div class="course-details-box">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 14px; font-weight: 800; color: #0f172a;">{current_course['name']}</span>
            <span style="background: #e0f2fe; color: #0369a1; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px;">{current_course['code']}</span>
        </div>
        <p style="font-size: 12px; color: #475569; margin: 0 0 6px 0;">{current_course['description']}</p>
        <span style="font-size: 11px; font-weight: bold; color: #64748b;">الساعات المعتمدة: {current_course['hours']}</span>
    </div>
""", unsafe_allow_html=True)

# مسار مجلد المقرر لحفظ ملفاته
course_folder = os.path.join(UPLOAD_DIR, current_course["id"])
os.makedirs(course_folder, exist_ok=True)

# 8. التبويبات الرسمية
tab_tips, tab_materials, tab_upload = st.tabs([
    "💡 إرشادات المادة",
    "📂 الحقيبة والملفات",
    "🔒 إدارة المقررات"
])

with tab_tips:
    st.write("")
    for idx, tip in enumerate(current_course["tips"], 1):
        st.info(f"**إضاءة أكاديمية {idx}:** {tip}")

with tab_materials:
    st.write("")
    existing_files = os.listdir(course_folder)
    
    if existing_files:
        st.write(f"📁 **الملفات المعتمدة للمقرر ({len(existing_files)}):**")
        for fname in existing_files:
            file_path = os.path.join(course_folder, fname)
            with open(file_path, "rb") as f:
                st.download_button(
                    label=f"📥 تنزيل المستند: {fname}",
                    data=f.read(),
                    file_name=fname,
                    mime="application/pdf",
                    key=f"dl_{current_course['id']}_{fname}"
                )
    else:
        st.warning("📌 يتم تحديده من المحاضِر")

with tab_upload:
    st.write("")
    st.caption(f"إضافة مرفق رسمي لمقرر: {current_course['name']}")
    
    SECRET_CODE = "ksu2026"
    admin_password = st.text_input("رمز الاعتماد الأكاديمي:", type="password", key=f"pwd_{current_course['id']}")
    
    if admin_password:
        if admin_password == SECRET_CODE:
            st.success("تم التحقق من الصلاحية الأكاديمية بنجاح.")
            uploaded_file = st.file_uploader(
                "رفع ملف المادة بصيغة PDF:", 
                type=["pdf"], 
                key=f"uploader_{current_course['id']}"
            )
            
            if uploaded_file is not None:
                save_path = os.path.join(course_folder, uploaded_file.name)
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"✅ تم اعتماد ونشر الملف: {uploaded_file.name}")
        else:
            st.error("الرمز غير صحيح.")
    else:
        st.caption("هذه الخانة مخصصة لمشرف البوابة فقط.")
