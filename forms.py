from flask_wtf import FlaskForm
from flask_wtf.file import MultipleFileField, FileAllowed
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    DecimalField,
    BooleanField,
    SelectField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange
)


CATEGORY_CHOICES = [
    ("Electronics", "Electronics"),
    ("building equipments", "building equipments"),
    ("plumbing tools", "plumbing tools"),

    ("Home & Kitchen", "Home & Kitchen"),

    ("Accessories", "Accessories"),
    
    ("Furniture", "Furniture"),
    ("Others", "Others")
]


class LoginForm(FlaskForm):

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    submit = SubmitField("Login")


class ProductForm(FlaskForm):

    name = StringField(
        "Product Name",
        validators=[
            DataRequired(),
            Length(max=200)
        ]
    )

    category = SelectField(
        "Category",
        choices=CATEGORY_CHOICES,
        validators=[
            DataRequired()
        ]
    )

    price = DecimalField(
        "Price",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    short_description = StringField(
        "Short Description",
        validators=[
            DataRequired(),
            Length(max=300)
        ]
    )

    description = TextAreaField(
        "Full Description",
        validators=[
            DataRequired()
        ]
    )

    # Multiple image upload
    images = MultipleFileField(
        "Product Images (Maximum 10)",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png", "gif", "webp"],
                "Only image files are allowed."
            )
        ]
    )

    featured = BooleanField(
        "Featured Product"
    )

    available = BooleanField(
        "Available",
        default=True
    )

    submit = SubmitField(
        "Save Product"
    )