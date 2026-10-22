# ⚛️ مختبر الكيمياء الافتراضي – بنية الذرة

مختبر تفاعلي ثلاثي الأبعاد (HTML/JavaScript) لتعلّم بنية الذرة، مُغلَّف بتطبيق **Streamlit** ليسهل نشره على **Streamlit Community Cloud**.

## محتويات المشروع

```
atom-lab/
├── app.py                              # تطبيق ستريملت الذي يعرض المختبر
├── Lap_Atom_Structure_3d_ch-1.html     # ملف المختبر الأصلي
├── requirements.txt                    # المكتبات المطلوبة
└── README.md                           # هذا الملف
```

## التشغيل محلياً

```bash
pip install -r requirements.txt
streamlit run app.py
```

## النشر على Streamlit Community Cloud

1. أنشئ مستودعاً جديداً على **GitHub** (عام Public أو خاص Private).
2. ارفع الملفات الأربعة أعلاه إلى جذر المستودع (Root).
3. ادخل إلى [share.streamlit.io](https://share.streamlit.io) وسجّل الدخول بحساب GitHub.
4. اضغط **Create app** ← **Deploy a public app from GitHub**.
5. اختر:
   - **Repository:** مستودعك
   - **Branch:** `main`
   - **Main file path:** `app.py`
6. اضغط **Deploy** وانتظر دقائق حتى يظهر رابط التطبيق.

## ملاحظات مهمة

- يحتاج المختبر إلى **اتصال بالإنترنت** لأنه يحمّل Tailwind CSS وFont Awesome وخطوط Google (Cairo وTajawal) من CDN.
- يجب أن يبقى اسم ملف HTML في `app.py` مطابقاً تماماً لاسم الملف في المستودع.
- لتغيير ارتفاع نافذة المختبر عدّل قيمة `height` في السطر الأخير من `app.py`.
- أي تعديل على ملف HTML ثم رفعه إلى GitHub يُحدّث التطبيق تلقائياً.
