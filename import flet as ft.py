import flet as ft
from flet import (
    Page,
    AppBar,
    Icon,
    IconButton,
    Text,
    colors,
    ListView,
    ListTile,
    CircleAvatar,
    Container,
    padding,
    margin,
    Column,
    Row,
    MainAxisAlignment,
    ScrollMode,
    ThemeMode,
)

def main(page: Page):
    # إعدادات الصفحة الرئيسية
    page.title = "تطبيقاتي"
    page.rtl = True
    page.theme_mode = ThemeMode.SYSTEM
    page.padding = 0
    page.window_bgcolor = colors.TRANSPARENT
    page.bgcolor = colors.TRANSPARENT
    
    # قائمة التطبيقات للعرض
    APPS = [
        {"name": "واتساب", "package": "com.whatsapp", "category": "تواصل اجتماعي", "color": colors.GREEN},
        {"name": "يوتيوب", "package": "com.google.android.youtube", "category": "وسائط", "color": colors.RED},
        {"name": "جوجل كروم", "package": "com.android.chrome", "category": "متصفح", "color": colors.BLUE},
        {"name": "جيميل", "package": "com.google.android.gm", "category": "بريد إلكتروني", "color": colors.RED_700},
        {"name": "خرائط جوجل", "package": "com.google.android.maps", "category": "خرائط", "color": colors.GREEN_700},
        {"name": "إنستجرام", "package": "com.instagram.android", "category": "تواصل اجتماعي", "color": colors.PURPLE},
        {"name": "تويتر", "package": "com.twitter.android", "category": "تواصل اجتماعي", "color": colors.BLUE_500},
        {"name": "تيك توك", "package": "com.zhiliaoapp.musically", "category": "تواصل اجتماعي", "color": colors.BLACK},
    ]

    def create_app_tile(app):
        return Container(
            content=ListTile(
                leading=CircleAvatar(
                    content=Text(app["name"][0], size=20, weight="bold"),
                    bgcolor=app["color"],
                ),
                title=Text(
                    app["name"],
                    size=16,
                    weight="bold",
                ),
                subtitle=Column(
                    controls=[
                        Text(app["category"], size=12, color=colors.GREY_500),
                        Text(app["package"], size=11, color=colors.GREY_400),
                    ],
                    spacing=2,
                ),
                trailing=IconButton(icon=ft.icons.LAUNCH, icon_size=20),
            ),
            bgcolor=colors.SURFACE_VARIANT,
            border_radius=10,
            margin=margin.symmetric(horizontal=10, vertical=5),
            padding=padding.all(5),
        )

    def toggle_theme():
        page.theme_mode = ThemeMode.LIGHT if page.theme_mode == ThemeMode.DARK else ThemeMode.DARK
        page.appbar.actions[-1].icon = ft.icons.DARK_MODE if page.theme_mode == ThemeMode.LIGHT else ft.icons.LIGHT_MODE
        page.update()

    # شريط التطبيق العلوي
    page.appbar = AppBar(
        leading=Icon(ft.icons.APPS_ROUNDED),
        leading_width=40,
        title=Text("تطبيقاتي", weight="bold"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            IconButton(ft.icons.SEARCH),
            IconButton(ft.icons.FILTER_LIST),
            IconButton(
                icon=ft.icons.DARK_MODE if page.theme_mode == ThemeMode.LIGHT else ft.icons.LIGHT_MODE,
                on_click=lambda _: toggle_theme(),
            ),
        ],
    )

    # إحصائيات التطبيقات
    stats_row = Row(
        controls=[
            Container(
                content=Column(
                    controls=[
                        Text("إجمالي التطبيقات", size=14, color=colors.GREY_500),
                        Text(str(len(APPS)), size=24, weight="bold"),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                bgcolor=colors.SURFACE_VARIANT,
                padding=15,
                border_radius=10,
                expand=True,
                margin=margin.symmetric(horizontal=5),
            ),
            Container(
                content=Column(
                    controls=[
                        Text("التطبيقات النشطة", size=14, color=colors.GREY_500),
                        Text(str(len(APPS)), size=24, weight="bold"),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                bgcolor=colors.SURFACE_VARIANT,
                padding=15,
                border_radius=10,
                expand=True,
                margin=margin.symmetric(horizontal=5),
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
    )

    # قسم الفئات
    categories = list(set(app["category"] for app in APPS))
    category_chips = Row(
        controls=[
            Container(
                content=Text(category, size=12, color=colors.WHITE),
                bgcolor=colors.BLUE,
                padding=padding.symmetric(horizontal=10, vertical=5),
                border_radius=15,
                margin=margin.only(right=5),
            ) for category in categories
        ],
        scroll=ScrollMode.AUTO,
    )

    # قائمة التطبيقات
    apps_list = ListView(
        controls=[create_app_tile(app) for app in APPS],
        spacing=0,
        padding=padding.only(top=10, bottom=20),
    )

    # الحاوية الرئيسية
    main_container = Container(
        content=Column(
            controls=[
                Container(
                    content=stats_row,
                    margin=margin.only(top=10, left=10, right=10),
                ),
                Container(
                    content=Column(
                        controls=[
                            Text(
                                "الفئات",
                                size=18,
                                weight="bold",
                            ),
                            category_chips,
                        ],
                    ),
                    margin=margin.only(top=20, left=15, right=15, bottom=5),
                ),
                Container(
                    content=Text(
                        "التطبيقات المثبتة",
                        size=18,
                        weight="bold",
                    ),
                    margin=margin.only(top=20, left=15, bottom=5),
                ),
                apps_list,
            ],
            scroll=ScrollMode.AUTO,
        ),
        margin=margin.only(top=10),
    )

    page.add(main_container)

# تشغيل التطبيق
ft.app(target=main, view=ft.AppView.FLET_APP)
