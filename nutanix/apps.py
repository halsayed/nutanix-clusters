from django.contrib.admin.apps import AdminConfig

class NutanixAdminConfig(AdminConfig):
    default_site = 'nutanix.admin.NutanixAdminSite'
