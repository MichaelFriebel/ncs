from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from datetime import date

# Contains booking status for all booking instances
class BookingStatus(models.Model):
    # :slug: A unique slug identifier.
    slug = models.SlugField(verbose_name=('Slug'))

# Contains each booking's data
class Booking(models.Model):
    """
    On the model itself, most attributes are blank=True to allow the
    creation of empty temporary bookings. Whether a field is required
    is defined in the model's form.

    :user (optional): Connection to Django's User model.
    :session (optional): Stored session to identify anonymous users.
    :forename (optional): User's first name.
    :surname (optional): User's last name.
    :street1 (optional): User's street address.
    :street2 (optional): Additional street address of the user.
    :city (optional): City of the user's address.
    :zip_code (optional): ZIP of the user's address.
    :phone (optional): User's phone number.
    :email: User's email.
    :special_request (optional): User's special request.
    :date_from (optional): Booking start date.
    :date_until (optional): Booking end date.
    :time_period (optional): Booking period.
    :time_unit (optional): Booking unit of time.
    :creation_date: Booking date.
    :booking_id (optional): Custom unique booking identifier.
    :booking_status: Current status of the booking.
    :notes (optional): Staff notes.
    :total (optional): Booking total price.
    """
    user = models.ForeignKey(
        'accounts.User',
        verbose_name=('User'),
        related_name='bookings',
        blank=True, null=True,
        on_delete=models.CASCADE
    )

    session = models.ForeignKey(
        'sessions.Session',
        verbose_name=('Session'),
        blank=True, null=True,
        on_delete=models.CASCADE
    )

    forename = models.CharField(
        verbose_name=('First Name'),
        max_length=20,
        blank=True,
    )

    surname = models.CharField(
        verbose_name=('Last Name'),
        max_length=20,
        blank=True,
    )

    street1 = models.CharField(
        verbose_name=('Street 1'),
        max_length=256,
        blank=True,
    )

    street2 = models.CharField(
        verbose_name=('Street 2'),
        max_length=256,
        blank=True,
    )

    city = models.CharField(
        verbose_name=('City'),
        max_length=256,
        blank=True,
    )

    zip_code = models.CharField(
        verbose_name=('ZIP Code'),
        max_length=256,
        blank=True,
    )

    email = models.EmailField(
        verbose_name=('Email'),
        blank=True,
    )

    phone = models.CharField(
        verbose_name=('Phone'),
        max_length=256,
        blank=True,
    )

    # special_request = models.TextField(
    #     max_length=1024,
    #     verbose_name=('Special Request'),
    #     blank=True,
    # )

    date_from = models.DateTimeField(
        verbose_name=('From'),
        blank=True, null=True,
    )

    date_until = models.DateTimeField(
        verbose_name=('Until'),
        blank=True, null=True,
    )

    creation_date = models.DateTimeField(
        verbose_name=('Creation Date'),
        auto_now_add=True,
    )

    booking_id = models.CharField(
        max_length=100,
        verbose_name=('Booking ID'),
        blank=True,
    )

    booking_status = models.ForeignKey(
        'booking.BookingStatus',
        verbose_name=('Booking Status'),
        blank=True, null=True,
        on_delete=models.CASCADE
    )

    # notes = models.TextField(
    #     max_length=1024,
    #     verbose_name=('Notes'),
    #     blank=True,
    # )

    time_period = models.PositiveIntegerField(
        verbose_name=('Time Period'),
        blank=True, null=True,
    )

    time_unit = models.CharField(
        verbose_name=('Time Unit'),
        default=getattr(settings, 'BOOKING_TIME_INTERVAL', ''),
        max_length=64,
        blank=True,
    )

    total = models.DecimalField(
        max_digits=36,
        decimal_places=2,
        verbose_name=('Total'),
        blank=True, null=True,
    )

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return '#{} ({})'.format(self.booking_id or self.pk, self.creation_date)

# Contain booking process error information
class BookingError(models.Model):
    """
    Particularly useful when a process is automated or reliant 
    on a third party app or API. Returned values can be stored in this model 
    for easy access and reference.

    :booking: The booking during which this error occurred.
    :message: The short error message to store.
    :details: More verbose error or additional information, e.g. a traceback.
    :date: The time and date this error occured.
    """
    booking = models.ForeignKey(
        Booking,
        verbose_name=('Booking'),
        on_delete=models.CASCADE
    )
    message = models.CharField(
        verbose_name=('Message'),
        max_length=1000,
        blank=True,
    )
    details = models.TextField(
        verbose_name=('Details'),
        max_length=4000,
        blank=True,
    )

    date = models.DateTimeField(
        verbose_name=('Date'),
        auto_now_add=True,
    )

    def __str__(self):
        return u'[{0}] {1} - {2}'.format(self.date, self.booking.booking_id, self.message)

# Connects a booking to a related object
class BookingItem(models.Model):
    """
    :quantity: Quantity of booked items.
    :persons (optional): Quantity of persons, who are involved in this booking.
    :subtotal (optional): Field for storing the price of each individual item.
    :booked_item: Connection to related booked item.
    :booking: Connection to related booking.

    properties:
    :price: Returns the full price for subtotal * quantity.
    """
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=('Quantity'),
    )

    # persons = models.PositiveIntegerField(
    #     verbose_name=('Persons'),
    #     blank=True, null=True,
    # )

    subtotal = models.DecimalField(
        max_digits=36,
        decimal_places=2,
        verbose_name=('Subtotal'),
        blank=True, null=True,
    )

    # Generic Foreign Key 'booked_item'
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    booked_item = GenericForeignKey('content_type', 'object_id')

    booking = models.ForeignKey(
        'booking.Booking',
        verbose_name=('Booking'),
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-booking__creation_date']

    def __str__(self):
        return u'{} ({})'.format(self.booking, self.booked_item)

    @property
    def price(self):
        return self.quantity * self.subtotal