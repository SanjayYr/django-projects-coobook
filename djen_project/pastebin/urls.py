from django.urls import path
from .views import PasteCreate, PasteDetail, PasteList, PasteUpdate, PasteDelete

urlpatterns = [
	path(r'', PasteCreate.as_view(), name='pastebin_paste_create'),
	path('paste/<int:pk>', PasteDetail.as_view(), name='pastebin_paste_detail'),
	path('pastes/', PasteList.as_view(), name='pastebin_paste_list'),
	path('paste/edit/<int:pk>', PasteUpdate.as_view(), name='pastebin_paste_edit'),
	path('paste/delete/<int:pk>', PasteDelete.as_view(), name='pastebin_paste_delete'),
]