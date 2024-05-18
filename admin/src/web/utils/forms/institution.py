from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, FieldList, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Regexp, url


class InstitutionCreateForm(FlaskForm):
    name = StringField(
        "Nombre",
        validators=[
            DataRequired(),
            Length(max=100, message="Máximo 100 caracteres"),
            Regexp(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ ]*$", message="Solo letras y números"),
        ],
    )
    address = StringField(
        "Dirección",
        validators=[
            DataRequired(),
            Length(max=100, message="Máximo 100 caracteres"),
            Regexp(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ ]*$", message="Solo letras y números"),
        ],
    )
    location = FieldList(
        StringField(
            "Dirección",
            validators=[
                Regexp(r"^(-?\d+(\.\d+)?)$", message="Solo menos numeros y coma"),
                DataRequired(),
                Length(max=100, message="Máximo 100 caracteres"),
            ],
        ),
        min_entries=2,
        max_entries=2,
    )
    web = StringField(
        "URL",
        validators=[
            url(message="Dirección de URL invalida"),
            DataRequired(),
            Length(max=100, message="Máximo 100 caracteres"),
        ],
    )

    days_and_opening_hours = StringField(
        "Cronograma",
        validators=[
            DataRequired(),
            Length(max=100, message="Máximo 100 caracteres"),
            Regexp(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ ]*$", message="Solo letras y números"),
        ],
    )
    information = TextAreaField(
        "Información",
        validators=[DataRequired(), Length(max=1000, message="Máximo 1000 caracteres")],
    )
    keywords = StringField(
        "Palabras clave",
        validators=[
            DataRequired("Campo requerido"),
            Length(max=100, message="Máximo 100 caracteres"),
            Regexp(
                r"^([a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ]+)(,\s*[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ]+)*$",
                message="Solo letras y números separados por coma",
            ),
        ],
    )
    email = EmailField(
        "Correo",
        validators=[
            Email("Correo invalido"),
            DataRequired(),
            Length(max=100, message="Máximo 100 caracteres"),
        ],
    )


class InstitutionUpdateForm(InstitutionCreateForm):
    enabled = BooleanField("Habilitado")


class InstitutionAddOwnerForm(FlaskForm):
    email = EmailField("Correo", validators=[Email("Correo invalido")])
