from django.db import models

class IcfWheelMeasurement(models.Model):
    form_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    tread_diameter = models.FloatField()
    last_shop_issue_size = models.FloatField()
    condemning_dia = models.FloatField()
    wheel_gauge = models.FloatField()
    permissible_variation_same_axle = models.CharField(max_length=50, default="0.5")
    permissible_variation_same_bogie = models.CharField(max_length=50, default="5")
    permissible_variation_same_coach = models.CharField(max_length=50, default="13")
    wheel_profile = models.CharField(max_length=100, default="29.4 Flange Thickness")
    intermediate_wwp = models.CharField(max_length=100, default="20 TO 28")
    bearing_seat_diameter = models.CharField(max_length=100, default="130.043 TO 130.068")
    roller_bearing_outer_dia = models.CharField(max_length=100)
    roller_bearing_bore_dia = models.CharField(max_length=100)
    roller_bearing_width = models.CharField(max_length=100)
    axle_box_housing_bore_dia = models.CharField(max_length=100)
    wheel_disc_width = models.CharField(max_length=100)

    def __str__(self):
        return f"Form {self.form_number or 'N/A'} by {self.created_by or 'Unknown'}"

class IcfBogieChecksheet(models.Model):
    form_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    tread_diameter_new = models.CharField(max_length=100, blank=True, null=True)
    last_shop_issue_size_dia = models.CharField(max_length=100, blank=True, null=True)
    dia_worn_limit = models.CharField(max_length=100, blank=True, null=True)
    wheel_back_to_back = models.CharField(max_length=100, blank=True, null=True)
    back_to_back_worn_limit = models.CharField(max_length=100, blank=True, null=True)
    flange_thickness = models.CharField(max_length=100, blank=True, null=True)
    flange_thickness_limit = models.CharField(max_length=100, blank=True, null=True)
    flange_height = models.CharField(max_length=100, blank=True, null=True)
    flange_height_limit = models.CharField(max_length=100, blank=True, null=True)
    tread_hollow = models.CharField(max_length=100, blank=True, null=True)
    tread_hollow_limit = models.CharField(max_length=100, blank=True, null=True)
    wheel_profile = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.form_number or 'N/A'} - {self.created_by or 'Unknown'}"