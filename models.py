# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ApartmentsInfocardData(models.Model):
    amenities = models.TextField(blank=True, null=True)
    checkavailabilitytitle = models.TextField(blank=True, null=True)
    includecheckavailability = models.TextField(blank=True, null=True)
    languagesspoken = models.TextField(blank=True, null=True)
    listing_address_city = models.TextField(blank=True, null=True)
    listing_address_country = models.TextField(blank=True, null=True)
    listing_address_deliveryaddress = models.TextField(blank=True, null=True)
    listing_address_location_latitude = models.FloatField(blank=True, null=True)
    listing_address_location_longitude = models.FloatField(blank=True, null=True)
    listing_address_postalcode = models.TextField(blank=True, null=True)
    listing_address_state = models.TextField(blank=True, null=True)
    listing_address_submarket = models.TextField(blank=True, null=True)
    listing_address_unitnumber = models.TextField(blank=True, null=True)
    listing_amenities = models.IntegerField(blank=True, null=True)
    listing_attachment_attachmentid = models.IntegerField(blank=True, null=True)
    listing_attachment_attachmenttype = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_contenttype = models.TextField(blank=True, null=True)
    listing_attachment_description = models.TextField(blank=True, null=True)
    listing_attachment_entitytype = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_height = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_imagesize = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_imagesizerequested = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_isurioptimized = models.NullBooleanField()
    listing_attachment_sortindex = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_uniqueid = models.IntegerField(blank=True, null=True)
    listing_attachment_uri = models.TextField(blank=True, null=True)
    listing_attachment_width = models.SmallIntegerField(blank=True, null=True)
    listing_carouselcount = models.SmallIntegerField(blank=True, null=True)
    listing_certifiedfreshdate = models.TextField(blank=True, null=True)
    listing_externallistingprovider = models.IntegerField(blank=True, null=True)
    listing_hasavailabilities = models.NullBooleanField()
    listing_hasleademail = models.NullBooleanField()
    listing_isfavorite = models.NullBooleanField()
    listing_languagesspoken = models.TextField(blank=True, null=True)
    listing_listhublistingid = models.TextField(blank=True, null=True)
    listing_listingkey = models.CharField(unique=True, max_length=7)
    listing_listingsummarytype = models.SmallIntegerField(blank=True, null=True)
    listing_listingtype = models.SmallIntegerField(blank=True, null=True)
    listing_listingtypeid = models.SmallIntegerField(blank=True, null=True)
    listing_options = models.SmallIntegerField(blank=True, null=True)
    listing_petfriendly = models.SmallIntegerField(blank=True, null=True)
    listing_phones = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_companyid = models.IntegerField(blank=True, null=True)
    listing_propertymanagementcompany_companyname = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_alttext = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_attachmentid = models.IntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_attachmenttype = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_contenttype = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_description = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_entitytype = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_height = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_imagesize = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_imagesizerequested = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_isurioptimized = models.NullBooleanField()
    listing_propertymanagementcompany_logo_sortindex = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_uniqueid = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_uri = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_width = models.SmallIntegerField(blank=True, null=True)
    listing_propertyname = models.TextField(blank=True, null=True)
    listing_propertystyle = models.SmallIntegerField(blank=True, null=True)
    listing_rating = models.FloatField(blank=True, null=True)
    listing_reinforcements = models.TextField(blank=True, null=True)
    listing_rentrollups = models.TextField(blank=True, null=True)
    listing_specialties = models.IntegerField(blank=True, null=True)
    listing_video_attachmenttype = models.SmallIntegerField(blank=True, null=True)
    listing_video_entitytype = models.SmallIntegerField(blank=True, null=True)
    listing_video_isurioptimized = models.NullBooleanField()
    listing_video_sortindex = models.SmallIntegerField(blank=True, null=True)
    listing_video_uniqueid = models.SmallIntegerField(blank=True, null=True)
    listing_video_uri = models.TextField(blank=True, null=True)
    listing_virtualtour_attachmenttype = models.SmallIntegerField(blank=True, null=True)
    listing_virtualtour_entitytype = models.SmallIntegerField(blank=True, null=True)
    listing_virtualtour_isurioptimized = models.NullBooleanField()
    listing_virtualtour_sortindex = models.SmallIntegerField(blank=True, null=True)
    listing_virtualtour_uniqueid = models.SmallIntegerField(blank=True, null=True)
    listing_virtualtour_uri = models.TextField(blank=True, null=True)
    propertyname = models.TextField(blank=True, null=True)
    propertynametitle = models.TextField(blank=True, null=True)
    propertyphotourl = models.TextField(blank=True, null=True)
    propertyurl = models.TextField(blank=True, null=True)
    rentformat_alert = models.TextField(blank=True, null=True)
    rentformat_availability = models.TextField(blank=True, null=True)
    rentformat_beds = models.TextField(blank=True, null=True)
    rentformat_new = models.TextField(blank=True, null=True)
    rentformat_rents = models.TextField(blank=True, null=True)
    searchcriteria_options = models.SmallIntegerField(blank=True, null=True)
    tfnphonelabel = models.TextField(blank=True, null=True)
    videolabel = models.TextField(blank=True, null=True)
    virtualtourlabel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apartments_infocard_data'


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


class ApartmentsPinData(models.Model):
    id = models.CharField(unique=True, max_length=7)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apartments_pin_data'


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


class Apt20170516(models.Model):
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

    class Meta:
        managed = False
        db_table = 'apt_2017_05_16'


class AptActiveIds(models.Model):
    url = models.TextField(unique=True)

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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BnbActiveIds(models.Model):
    url = models.TextField(unique=True)
    id = models.IntegerField(unique=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bnb_active_ids'


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


class CaseStudyDataShortTermRentals(models.Model):
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
    monthly_price_factor = models.FloatField(blank=True, null=True)
    localized_city = models.TextField(blank=True, null=True)
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
    bathrooms = models.FloatField(blank=True, null=True)
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
    security_price_native = models.IntegerField(blank=True, null=True)
    weekly_price_native = models.IntegerField(blank=True, null=True)
    map_image_url = models.TextField(blank=True, null=True)
    max_nights_input_value = models.IntegerField(blank=True, null=True)
    check_in_time = models.IntegerField(blank=True, null=True)
    currency_symbol_left = models.TextField(blank=True, null=True)
    native_currency = models.TextField(blank=True, null=True)
    guest_controls = models.TextField(blank=True, null=True)
    allowed_currencies = models.TextField(blank=True, null=True)
    in_building = models.NullBooleanField()
    picture_captions = models.TextField(blank=True, null=True)
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
    price_native = models.IntegerField(blank=True, null=True)
    bed_type = models.TextField(blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    description_locale = models.TextField(blank=True, null=True)
    amenities_ids = models.TextField(blank=True, null=True)
    room_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_study_data_short_term_rentals'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GarrettInfocardTest(models.Model):
    amenities = models.TextField(blank=True, null=True)
    checkavailabilitytitle = models.TextField(blank=True, null=True)
    includecheckavailability = models.TextField(blank=True, null=True)
    languagesspoken = models.TextField(blank=True, null=True)
    listing_address_city = models.TextField(blank=True, null=True)
    listing_address_country = models.TextField(blank=True, null=True)
    listing_address_deliveryaddress = models.TextField(blank=True, null=True)
    listing_address_location_latitude = models.FloatField(blank=True, null=True)
    listing_address_location_longitude = models.FloatField(blank=True, null=True)
    listing_address_postalcode = models.TextField(blank=True, null=True)
    listing_address_state = models.TextField(blank=True, null=True)
    listing_address_submarket = models.TextField(blank=True, null=True)
    listing_address_unitnumber = models.TextField(blank=True, null=True)
    listing_amenities = models.IntegerField(blank=True, null=True)
    listing_attachment_attachmentid = models.IntegerField(blank=True, null=True)
    listing_attachment_attachmenttype = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_contenttype = models.TextField(blank=True, null=True)
    listing_attachment_description = models.TextField(blank=True, null=True)
    listing_attachment_entitytype = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_height = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_imagesize = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_imagesizerequested = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_isurioptimized = models.NullBooleanField()
    listing_attachment_sortindex = models.SmallIntegerField(blank=True, null=True)
    listing_attachment_uniqueid = models.IntegerField(blank=True, null=True)
    listing_attachment_uri = models.TextField(blank=True, null=True)
    listing_attachment_width = models.SmallIntegerField(blank=True, null=True)
    listing_carouselcount = models.SmallIntegerField(blank=True, null=True)
    listing_certifiedfreshdate = models.TextField(blank=True, null=True)
    listing_externallistingprovider = models.IntegerField(blank=True, null=True)
    listing_hasavailabilities = models.NullBooleanField()
    listing_hasleademail = models.NullBooleanField()
    listing_isfavorite = models.NullBooleanField()
    listing_languagesspoken = models.TextField(blank=True, null=True)
    listing_listhublistingid = models.TextField(blank=True, null=True)
    listing_listingkey = models.TextField(unique=True)
    listing_listingsummarytype = models.SmallIntegerField(blank=True, null=True)
    listing_listingtype = models.SmallIntegerField(blank=True, null=True)
    listing_listingtypeid = models.SmallIntegerField(blank=True, null=True)
    listing_options = models.SmallIntegerField(blank=True, null=True)
    listing_petfriendly = models.SmallIntegerField(blank=True, null=True)
    listing_phones = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_companyid = models.IntegerField(blank=True, null=True)
    listing_propertymanagementcompany_companyname = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_alttext = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_attachmentid = models.IntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_attachmenttype = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_contenttype = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_description = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_entitytype = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_height = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_imagesize = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_imagesizerequested = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_isurioptimized = models.NullBooleanField()
    listing_propertymanagementcompany_logo_sortindex = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_uniqueid = models.SmallIntegerField(blank=True, null=True)
    listing_propertymanagementcompany_logo_uri = models.TextField(blank=True, null=True)
    listing_propertymanagementcompany_logo_width = models.SmallIntegerField(blank=True, null=True)
    listing_propertyname = models.TextField(blank=True, null=True)
    listing_propertystyle = models.SmallIntegerField(blank=True, null=True)
    listing_rating = models.FloatField(blank=True, null=True)
    listing_reinforcements = models.TextField(blank=True, null=True)
    listing_rentrollups = models.TextField(blank=True, null=True)
    listing_specialties = models.IntegerField(blank=True, null=True)
    listing_video_attachmenttype = models.SmallIntegerField(blank=True, null=True)
    listing_video_entitytype = models.SmallIntegerField(blank=True, null=True)
    listing_video_isurioptimized = models.NullBooleanField()
    listing_video_sortindex = models.SmallIntegerField(blank=True, null=True)
    listing_video_uniqueid = models.SmallIntegerField(blank=True, null=True)
    listing_video_uri = models.TextField(blank=True, null=True)
    listing_virtualtour_attachmenttype = models.SmallIntegerField(blank=True, null=True)
    listing_virtualtour_entitytype = models.SmallIntegerField(blank=True, null=True)
    listing_virtualtour_isurioptimized = models.NullBooleanField()
    listing_virtualtour_sortindex = models.SmallIntegerField(blank=True, null=True)
    listing_virtualtour_uniqueid = models.SmallIntegerField(blank=True, null=True)
    listing_virtualtour_uri = models.TextField(blank=True, null=True)
    propertyname = models.TextField(blank=True, null=True)
    propertynametitle = models.TextField(blank=True, null=True)
    propertyphotourl = models.TextField(blank=True, null=True)
    propertyurl = models.TextField(blank=True, null=True)
    rentformat_alert = models.TextField(blank=True, null=True)
    rentformat_availability = models.TextField(blank=True, null=True)
    rentformat_beds = models.TextField(blank=True, null=True)
    rentformat_new = models.TextField(blank=True, null=True)
    rentformat_rents = models.TextField(blank=True, null=True)
    searchcriteria_options = models.SmallIntegerField(blank=True, null=True)
    tfnphonelabel = models.TextField(blank=True, null=True)
    videolabel = models.TextField(blank=True, null=True)
    virtualtourlabel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garrett_infocard_test'


class GarrettPinTest(models.Model):
    id = models.CharField(unique=True, max_length=7, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garrett_pin_test'


class HomeawayActiveIds(models.Model):
    url = models.TextField(unique=True)
    id = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'homeaway_active_ids'


class MinMaxCity(models.Model):
    min_price = models.FloatField(blank=True, null=True)
    max_price = models.FloatField(blank=True, null=True)
    city_state = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'min_max_city'


class PublicCaseStudyDataShortTermRentals(models.Model):
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.FloatField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    is_location_exact = models.NullBooleanField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture_urls = models.TextField(blank=True, null=True)
    picture_captions = models.TextField(blank=True, null=True)
    star_rating = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public.case_study_data_short_term_rentals'


class Str(models.Model):
    instant_book = models.NullBooleanField()
    bathrooms = models.TextField(blank=True, null=True)
    person_capacity = models.IntegerField(blank=True, null=True)
    property_type = models.TextField(blank=True, null=True)
    beds = models.TextField(blank=True, null=True)
    listing_id = models.IntegerField(primary_key=True)
    rating_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    amenities = models.TextField(blank=True, null=True)
    rev_count = models.IntegerField(blank=True, null=True)
    cancel_policy = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image_urls = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    host_id = models.IntegerField(blank=True, null=True)
    bed_type = models.CharField(max_length=50, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    superhost = models.NullBooleanField()
    pic_count = models.IntegerField(blank=True, null=True)
    room_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'str'
