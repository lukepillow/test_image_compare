# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class ImageMatches(models.Model):
    id = models.IntegerField(primary_key=True)
    apartment_url = models.TextField(blank=True, null=True)
    airbnb_url = models.TextField(blank=True, null=True)
    apartment_image_url = models.TextField(blank=True, null=True)
    airbnb_image_url = models.TextField(blank=True, null=True)
    match = models.NullBooleanField()

    class Meta:
        managed = True
        db_table = 'image_matches'

class ImageMatch(models.Model):
    id = models.IntegerField(primary_key=True)
    apt_url = models.TextField(blank=True, null=True)
    bnb_id = models.IntegerField(blank=True, null=True)
    apt_img_url = models.TextField(blank=True, null=True)
    bnb_img_url = models.TextField(blank=True, null=True)
    match = models.NullBooleanField()
    score = models.FloatField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'image_match'


class ImageMatchForm(ModelForm):
    class Meta:
        model = ImageMatch
        fields = ['id', 'apt_img_url', 'bnb_img_url','match']



class ApartmentsPageData(models.Model):
    url = models.TextField(primary_key=True)
    owner = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    unit_type = models.TextField(blank=True, null=True)
    price_type = models.TextField(blank=True, null=True)
    street_address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    neighborhood = models.TextField(blank=True, null=True)
    building_info = models.TextField(blank=True, null=True)
    n_of_unit = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    image_json = models.TextField(blank=True, null=True)
    amenities = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    profiletype = models.TextField(blank=True, null=True)
    mediacollection = models.TextField(blank=True, null=True)
    rentals = models.TextField(blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    costarverified = models.NullBooleanField()
    propertytype = models.TextField(blank=True, null=True)
    listingid = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apartments_page_data'

    def __str__(self):
        return self.url



class Apt(models.Model):
    url = models.TextField(primary_key=True)
    owner = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    unit_type = models.TextField(blank=True, null=True)
    price_type = models.TextField(blank=True, null=True)
    street_address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    neighborhood = models.TextField(blank=True, null=True)
    building_info = models.TextField(blank=True, null=True)
    n_of_unit = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apt'





class AptActiveIds(models.Model):
    url = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'apt_active_ids'


class AptImg(models.Model):
    url = models.TextField(primary_key=True)
    owner = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    unit_type = models.TextField(blank=True, null=True)
    price_type = models.TextField(blank=True, null=True)
    street_address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    neighborhood = models.TextField(blank=True, null=True)
    building_info = models.TextField(blank=True, null=True)
    n_of_unit = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    image_json = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apt_img'

class BookData(models.Model):
    url = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    facilities_list = models.TextField(blank=True, null=True)
    hotelmap = models.TextField(blank=True, null=True)
    hoteltype = models.TextField(blank=True, null=True)
    hotelname = models.TextField(blank=True, null=True)
    description_mini = models.TextField(blank=True, null=True)
    pricerange_text = models.TextField(blank=True, null=True)
    url_again = models.TextField(blank=True, null=True)
    ad_type = models.TextField(blank=True, null=True)
    ad_country = models.TextField(blank=True, null=True)
    ad_locality = models.TextField(blank=True, null=True)
    ad_region = models.TextField(blank=True, null=True)
    ad_postalcode = models.TextField(blank=True, null=True)
    ad_streetadress = models.TextField(blank=True, null=True)
    best_rating = models.FloatField(blank=True, null=True)
    rating_value = models.FloatField(blank=True, null=True)
    reviewcounts = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    review_score_breakdown = models.TextField(blank=True, null=True)
    review_sub_score_breakdown = models.TextField(blank=True, null=True)
    picurl = models.TextField(blank=True, null=True)
    room_types = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_data'



class CrawledBnbListing20170502(models.Model):
    listing_id = models.IntegerField(primary_key=True)
    listing = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crawled_bnb_listing_2017_05_02'


class CrawledBnbListingDetail20170502(models.Model):
    cancel_policy_short_str = models.TextField(blank=True, null=True)
    localized_check_in_time_window = models.TextField(blank=True, null=True)
    medium_url = models.TextField(blank=True, null=True)
    require_guest_profile_picture = models.NullBooleanField()
    country_code = models.TextField(blank=True, null=True)
    property_type = models.TextField(blank=True, null=True)
    recent_review = models.TextField(blank=True, null=True)
    security_deposit_native = models.IntegerField(blank=True, null=True)
    in_landlord_partnership = models.NullBooleanField()
    price_for_extra_person_native = models.IntegerField(blank=True, null=True)
    monthly_price_native = models.IntegerField(blank=True, null=True)
    has_double_blind_reviews = models.NullBooleanField()
    bedrooms = models.IntegerField(blank=True, null=True)
    has_viewed_cleaning = models.NullBooleanField()
    max_nights = models.IntegerField(blank=True, null=True)
    has_viewed_terms = models.NullBooleanField()
    formatted_check_out_time = models.TextField(blank=True, null=True)
    cancellation_policy = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    thumbnail_url = models.TextField(blank=True, null=True)
    hosts = models.TextField(blank=True, null=True)
    min_nights = models.IntegerField(blank=True, null=True)
    has_agreed_to_legal_terms = models.NullBooleanField()
    neighborhood = models.TextField(blank=True, null=True)
    thumbnail_urls = models.TextField(blank=True, null=True)
    locale = models.TextField(blank=True, null=True)
    property_type_id = models.IntegerField(blank=True, null=True)
    primary_host = models.TextField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    neighborhood_overview = models.TextField(blank=True, null=True)
    instant_book_welcome_message = models.TextField(blank=True, null=True)
    picture_urls = models.TextField(blank=True, null=True)
    space = models.TextField(blank=True, null=True)
    require_guest_phone_verification = models.NullBooleanField()
    xl_picture_urls = models.TextField(blank=True, null=True)
    access = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    check_in_time_ends_at = models.IntegerField(blank=True, null=True)
    check_in_time_end = models.TextField(blank=True, null=True)
    public_address = models.TextField(blank=True, null=True)
    price_formatted = models.TextField(blank=True, null=True)
    localized_city = models.TextField(blank=True, null=True)
    monthly_price_factor = models.FloatField(blank=True, null=True)
    check_in_time_start = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    square_feet = models.IntegerField(blank=True, null=True)
    check_out_time = models.IntegerField(blank=True, null=True)
    interaction = models.TextField(blank=True, null=True)
    license = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    requires_license = models.NullBooleanField()
    weekly_price_factor = models.FloatField(blank=True, null=True)
    guests_included = models.IntegerField(blank=True, null=True)
    reviews_count = models.IntegerField(blank=True, null=True)
    transit = models.TextField(blank=True, null=True)
    calendar_updated_at = models.TextField(blank=True, null=True)
    picture_captions = models.TextField(blank=True, null=True)
    market = models.TextField(blank=True, null=True)
    in_toto_area = models.NullBooleanField()
    city = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    room_type_category = models.TextField(blank=True, null=True)
    bed_type_category = models.TextField(blank=True, null=True)
    amenities = models.TextField(blank=True, null=True)
    localized_check_out_time = models.TextField(blank=True, null=True)
    has_license = models.NullBooleanField()
    extras_price_native = models.IntegerField(blank=True, null=True)
    jurisdiction_names = models.TextField(blank=True, null=True)
    instant_bookable = models.NullBooleanField()
    experiences_offered = models.TextField(blank=True, null=True)
    security_deposit_formatted = models.TextField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    force_mobile_legal_modal = models.NullBooleanField()
    picture_count = models.IntegerField(blank=True, null=True)
    cleaning_fee_native = models.IntegerField(blank=True, null=True)
    currency_symbol_right = models.TextField(blank=True, null=True)
    star_rating = models.FloatField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    price_native = models.IntegerField(blank=True, null=True)
    weekly_price_native = models.IntegerField(blank=True, null=True)
    map_image_url = models.TextField(blank=True, null=True)
    max_nights_input_value = models.IntegerField(blank=True, null=True)
    check_in_time = models.IntegerField(blank=True, null=True)
    currency_symbol_left = models.TextField(blank=True, null=True)
    native_currency = models.TextField(blank=True, null=True)
    guest_controls = models.TextField(blank=True, null=True)
    allowed_currencies = models.TextField(blank=True, null=True)
    in_building = models.NullBooleanField()
    bathrooms = models.FloatField(blank=True, null=True)
    person_capacity = models.IntegerField(blank=True, null=True)
    min_nights_input_value = models.IntegerField(blank=True, null=True)
    is_location_exact = models.NullBooleanField()
    id = models.IntegerField(primary_key=True)
    bathroom_type = models.TextField(blank=True, null=True)
    picture_url = models.TextField(blank=True, null=True)
    zipcode = models.TextField(blank=True, null=True)
    cancel_policy = models.IntegerField(blank=True, null=True)
    has_viewed_ib_perf_dashboard_panel = models.NullBooleanField()
    house_rules = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    time_zone_name = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    smart_location = models.TextField(blank=True, null=True)
    jurisdiction_rollout_names = models.TextField(blank=True, null=True)
    xl_picture_url = models.TextField(blank=True, null=True)
    user1 = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    security_price_native = models.IntegerField(blank=True, null=True)
    bed_type = models.TextField(blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    description_locale = models.TextField(blank=True, null=True)
    amenities_ids = models.TextField(blank=True, null=True)
    room_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crawled_bnb_listing_detail_2017_05_02'


