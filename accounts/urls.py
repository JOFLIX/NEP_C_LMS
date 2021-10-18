
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.loginuser,name="loginuser"),
    path('loginstaff/',views.loginstaff,name="loginstaff"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('logoutuser/', views.logoutuser,name="logoutuser"),
    path('profile/', views.profile,name="profile"),
    path('news_events/',views.news_events,name="news_events"),


    path('lec_announcement/',views.lec_announcement,name="lec_announcement"),

    path('viewprofile/', views.viewprofile,name="viewprofile"),
    path('updateprofile/<str:pk>/', views.updateprofile,name="updateprofile"),
    path('change_password/', views.change_password,name="change_password"),
    path('register_students_view/', views.register_students_view,name="register_students_view"),
    path('settings/', views.settings_view,name="settings_view"),
    path('update_settings/<str:pk>/', views.update_settings,name="update_settings"),
    path('delete_settings/<str:pk>/', views.delete_settings,name="delete_settings"),
    path('students/', views.View_all_students,name="View_all_students"),
    path('update_students_form/', views.update_students_form,name="update_students_form"),
    path('update_students/<str:pk>/', views.update_students,name="update_students"),
    path('delete_student/<str:pk>/', views.delete_student,name="delete_student"),
    path('add_class/', views.add_class_view,name="add_class"),
    path('view_classes/', views.view_classes,name="view_classes"),
    path('update_class/<str:pk>/', views.update_class,name="update_class"),
    path('delete_class/<str:pk>/', views.delete_class,name="delete_class"),
    path('session/', views.session_view,name="session_view"),
    path('view_session/', views.view_session,name="view_session"),
    path('update_session/<str:pk>/', views.update_session,name="update_session"),
    path('delete_session/<str:pk>/', views.delete_session,name="delete_session"),
    path('add_term/', views.add_term_view,name="add_term"),
    path('view_term/', views.view_term,name="view_term"),
    path('update_term/<str:pk>/', views.update_term_view,name="update_term_view"),
    path('delete_term/<str:pk>/', views.delete_term,name="delete_term"),
    path('add_courses/', views.add_courses_view,name="add_courses"),
    path('view_courses/', views.view_courses_view,name="view_courses"),
    path('update_courses/<str:pk>/', views.update_courses,name="update_courses"),
    path('delete_course/<str:pk>/', views.delete_course,name="delete_course"),
    path('add_department_view/', views.add_department_view,name="add_department_view"),
    path('view_department/', views.view_department,name="view_department"),
    path('update_department_view/<str:pk>/', views.update_department_view,name="update_department_view"),
    path('delete_department/<str:pk>/', views.delete_department,name="delete_department"),
    path('pdf_timetable_export/', views.pdf_timetable_export,name="pdf_timetable_export"),
    path('member_staff/', views.member_staff,name="member_staff"),
    path('register_superuser/', views.register_superuser,name="register_superuser"),
    path('superuser_update_form/', views.superuser_update_form,name="superuser_update_form"),
    path('update_superuser/<str:pk>/', views.update_superuser,name="update_superuser"),
    path('delete_superuser/<str:pk>/', views.delete_superuser,name="delete_superuser"),
    path('add_timetable/', views.add_timetable,name="add_timetable"),
    path('view_timetable/', views.view_timetable,name="view_timetable"),
    path('update_timetable/<str:pk>/', views.update_timetable,name="update_timetable"),
    path('delete_timetable/<str:pk>/', views.delete_timetable,name="delete_timetable"),
    path('add_exam_ressults/', views.add_exam_ressults,name="add_exam_ressults"),
    path('view_results_admin/', views.view_results_admin,name="view_results_admin"),
    path('Update_exam_result/<str:pk>/', views.Update_exam_result,name="Update_exam_result"),
    path('delete_exam_result/<str:pk>/', views.delete_exam_result,name="delete_exam_result"),
    path('view_exam_result_student/', views.view_exam_result_student,name="view_exam_result_student"),
    path('pdf_student_exam_export/', views.pdf_student_exam_export,name="pdf_student_exam_export"),
    path('register_lecturer/',views.register_lecturer,name="register_lecturer"),
    path('lecturers/',views.view_all_lecturers,name="view_all_lecturers"),
    path('update_lecturer_form/',views.update_lecturer_form,name="update_lecturer_form"),
    path('edit_lec/<str:pk>/',views.edit_lec,name="edit_lec"),
    path('delete_lec/<str:pk>/',views.delete_lec,name="delete_lec"),
    path('pdf_all_students_export/',views.pdf_all_students_export,name="pdf_all_students_export"),
    path('add_all_student_announcement/',views.add_all_student_announcement,name="add_all_student_announcement"),
    path('admin_view_all_student_announcement/',views.admin_view_all_student_announcement,name="admin_view_all_student_announcement"),
    path('update_all_student_announcement/<str:pk>/',views.update_all_student_announcement,name="update_all_student_announcement"),
    path('delete_all_student_announcement/<str:pk>/',views.delete_all_student_announcement,name="delete_all_student_announcement"),
    path('pdf_all_lecturers_export/',views.pdf_all_lecturers_export,name="pdf_all_lecturers_export"),
    path('pdf_all_superusers_export/',views.pdf_all_superusers_export,name="pdf_all_superusers_export"),
    path('add_online_class/',views.add_online_class,name="add_online_class"),
    path('view_online_class_adm_lec/',views.view_online_class_adm_lec,name="view_online_class_adm_lec"),
    path('update_online_class/<str:pk>/',views.update_online_class,name="update_online_class"),
    path('delete_online_class/<str:pk>/',views.delete_online_class,name="delete_online_class"),
    path('view_online_class_adm_lec/',views.view_online_class_adm_lec,name="view_online_class_adm_lec"),
    path('add_assignment/',views.add_assignment,name="add_assignment"),
    path('view_assignment_adm_lec/',views.view_assignment_adm_lec,name="view_assignment_adm_lec"),
    path('update_assignment_adm_lec/<str:pk>/',views.update_assignment_adm_lec,name="update_assignment_adm_lec"),
    path('delete_assignment_adm_lec/<str:pk>/',views.delete_assignment_adm_lec,name="delete_assignment_adm_lec"),
    path('student_view_own_online_classes/',views.student_view_own_online_classes,name="student_view_own_online_classes"),
    path('view_announcements_students/',views.view_announcements_students,name="view_announcements_students"),
    path('add_message_lec_std/',views.add_message_lec_std,name="add_message_lec_std"),
    path('admin_reply_message_form/',views.admin_reply_message_form,name="admin_reply_message_form"),
    path('view_all_messages_adm/',views.view_all_messages_adm,name="view_all_messages_adm"),
    path('update_admin_reply_message/<str:pk>/',views.update_admin_reply_message,name="update_admin_reply_message"),
    path('delete_message_adm/<str:pk>/',views.delete_message_adm,name="delete_message_adm"),
    path('view_assignment_student/',views.view_assignment_student,name="view_assignment_student"),
    path('pdf_assignment_export/',views.pdf_assignment_export,name="pdf_assignment_export"),
    path('AddElearningLibraryResouurce/',views.AddElearningLibraryResouurce,name="AddElearningLibraryResouurce"),
    path('ViewElearningLibraryResouurceLec/',views.ViewElearningLibraryResouurceLec,name="ViewElearningLibraryResouurceLec"),
    path('UpdateElearningLibraryResouurce/<str:pk>/',views.UpdateElearningLibraryResouurce,name="UpdateElearningLibraryResouurce"),
    path('delete_elearning_resource/<str:pk>/',views.delete_elearning_resource,name="delete_elearning_resource"),
    path('ViewLibraryStudentLec/',views.ViewLibraryStudentLec,name="ViewLibraryStudentLec"),
    path('pdf_timetable_export_lecturer/',views.pdf_timetable_export_lecturer,name="pdf_timetable_export_lecturer"),
    path('generate_a_printing_notice/',views.generate_a_printing_notice,name="generate_a_printing_notice"),
    path('pdf_notice_admin/',views.pdf_notice_admin,name="pdf_notice_admin"),
    path('update_generate_a_printing_notice/<str:pk>/',views.update_generate_a_printing_notice,name="update_generate_a_printing_notice"),
    path('delete_notice_adm/<str:pk>/',views.delete_notice_adm,name="delete_notice_adm"),
    path('online_applications/',views.online_applications,name="online_applications"),
    path('add_course_unit/',views.add_course_unit,name="add_course_unit"),
    path('view_course_unit_admin/',views.view_course_unit_admin,name="view_course_unit_admin"),
    path('update_course_unit/<str:pk>/',views.update_course_unit,name="update_course_unit"),
    path('delete_course_unit/<str:pk>/',views.delete_course_unit,name="delete_course_unit"),
    path('update_assignment_student/<str:pk>/',views.update_assignment_student,name="update_assignment_student"),
    path('delete_assignment_adm_lec/<str:pk>/',views.delete_assignment_adm_lec,name="delete_assignment_adm_lec"),
    path('uploads/',views.adm_lec_view_std_uploads,name="adm_lec_view_std_uploads"),
    path('uploads_delete/<str:pk>/',views.delete_assignment_adm_lec_std_upload,name="delete_assignment_adm_lec_std_upload"),
    path('register_parent/',views.register_parent,name="register_parent"),
    path('view_parents/',views.view_parents,name="view_parents"),
    path('parent_update_form/',views.parent_update_form,name="parent_update_form"),
    path('update_parent/<str:pk>/',views.update_parent,name="update_parent"),
    path('delete_parent/<str:pk>/',views.delete_parent,name="delete_parent"),
    path('pdf_export_parents/',views.pdf_export_parents,name="pdf_export_parents"),
    path('pdf_export_single_student/<str:pk>/',views.pdf_export_single_student,name="pdf_export_single_student"),
    path('online_application_approval/',views.online_application_approval,name="online_application_approval"),
    path('update_online_application_approval/<str:pk>/',views.update_online_application_approval,name="update_online_application_approval"),
    path('adm_fee/',views.adm_fee,name="adm_fee"),
    path('vw_en_fee/',views.vw_en_fee,name="vw_en_fee"),
    path('pdf_adm_fee/<str:pk>/',views.pdf_adm_fee,name="pdf_adm_fee"),
    path('edt_adm_fee/<str:pk>/',views.edt_adm_fee,name="edt_adm_fee"),


    path('delete_upload_student_own_assignment/<str:pk>/',views.delete_upload_student_own_assignment,name="delete_upload_student_own_assignment"),
    path('admin_view_online_aplications/',views.admin_view_online_aplications,name="admin_view_online_aplications"),
    path('pdf_export_online_application/<str:pk>/',views.pdf_export_online_application,name="pdf_export_online_application"),
    


    



    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "accounts/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"), name ='password_reset_complete')
  
]