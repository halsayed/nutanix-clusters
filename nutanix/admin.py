
from django.contrib import admin


class NutanixAdminSite(admin.AdminSite):
    site_header = "Nutanix Cluster Info"
    site_title = 'Nutanix'

