from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.user_home, name="profile"),
    path('login.html', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    path("login.html", views.loginpage, name="login.html"),
    path("loginuser/", views.loginuser, name="loginuser"),
    path("logoutuser/", views.logoutuser, name="logoutuser"),
    path("login.html", views.passwordresetpage, name="login.html"),
    path('password_reset_page/', views.passwordresetpage,
         name='password_reset_page'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done,
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm,
         name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete,
         name='password_reset_complete'),
    path("change_password.html", views.changepasswordpage,
         name='change_password.html'),
    path('change_password/', views.change_password, name='change_password'),
    path('create-room/', views.create_room, name='create-room'),
    path("fetch_bill.html", views.fetchBill_page, name='fetch_bill.html'),
    path("read_bills.html", views.readBills_page, name='read_bills.html'),
    path("read_types.html", views.readTypes_page, name='read_types.html'),
    path("add_user.html", views.addUser_page, name='add_user.html'),
    path('add-user/', views.add_user, name='add-user'),
    path("read_users.html", views.read_users, name='read_users'),
    path('update-user/', views.update_user, name='update-user'),
    path("update_user.html/<int:user_id>/",
         views.updateUser_page, name='update_user.html'),

    path('delete-user/<int:user_id>/', views.delete_user, name='delete-user'),


    path("create_room.html", views.createRoom_page, name='create_room.html'),
    path('update-room/', views.update_room, name='update-room'),
    path("read_rooms.html", views.read_rooms, name='read_rooms.html'),
    path('read-rooms/', views.read_rooms, name='read_rooms'),
    path('delete_room/', views.delete_room, name='delete_room'),





    path("set_readings.html", views.setReadings_page, name='set_readings.html'),
    path("manual_set_reading.html", views.manual_set_Reading_page,
         name='manual_set_reading.html'),
    path('update-readings/', views.update_readings, name='update-readings'),
    path('manual-update-readings/', views.manual_update_readings,
         name='manual-update-readings'),

    path('delete_reading/', views.delete_reading, name='delete_reading'),
    path("update_reading.html/<int:reading_id>/",
         views.updateReading_page, name='update_reading.html'),

    path('update-reading/', views.update_reading, name='update-reading'),

    path("bill.html/metered/<int:bill_id>/",
         views.metered_bill_page, name='metered_bill.html'),

    path("bill.html/unmetered/<int:bill_id>/",
         views.unmetered_bill_page, name='unmetered_bill.html'),


    path("get_bulk_bill.html", views.getBulkBill_page, name='get_bulk_bill.html'),
    path("bulk-bill", views.bulk_bill, name='bulk-bill'),

    path("get_bills_pdf.html", views.getBillpdf_page, name='get_bills_pdf.html'),
    path("bills-pdf", views.bills_pdf, name='bills-pdf'),
    path('delete_bill/', views.delete_bill, name='delete_bill'),




    path("update_room.html/<int:room_id>/",
         views.updateRoom_page, name='update_room.html'),

    path("create_meter_rate", views.createMeterRate_page, name='create_meter_rate'),
    path("create_flat_rate", views.createFlatRate_page, name='create_flat_rate'),
    path("read_rates", views.read_rates, name='read_rates'),
    path("user.html", views.userProfile_page, name='user.html'),
    path("tables.html", views.tableList_page, name='tables.html'),
    path("typography.html", views.typography_page, name='typography.html'),
    path("rtl.html", views.rtlSupport_page, name='rtl.html'),
    path("read_readings.html", views.readReadings_page, name='readReadings.html'),
    path('read-rooms/<str:msg>/', views.read_rooms, name='read_rooms'),
    path('calculate-bill/', views.calculate_bill, name='calculate-bill'),

    path('add_department/', views.add_department, name='add_department'),
    path('add_quarter_type/', views.add_quarter_type, name='add_quarter_type'),
    path('add-user/', views.add_user, name='add-user'),
    path('delete_department/', views.delete_department, name='delete_department'),
    path('delete_quarter_type/', views.delete_quarter_type,
         name='delete_quarter_type'),
     path('update-department/', views.update_department, name='update-department'),
     path('update-quarter-type/', views.edit_quarter_type, name='update-quarter-type'),
    # users
    path('user_profile', views.userDetails, name='user_profile'),
    path('user_bills', views.get_user_bills, name='user_bills'),
    # keep this at last because it is for error pages so it should hit at last
    re_path(r'^.*\.*', views.page_not_found, name='page_not_found.html'),
]
